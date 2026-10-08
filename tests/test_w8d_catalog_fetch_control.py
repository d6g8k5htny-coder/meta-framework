"""Proposed control (W8d, group C): the inline fetch() identity gate in
meta-framework .github/workflows/catalog.yml (L28-36 at 75685db7).

The job's only exercise of fetch() is the real registry, where every row is
legitimate, so no refusal branch is ever executed by CI. This control extracts
fetch() verbatim from the workflow text (no copy of the logic lives here),
binds it to a fake urllib and a temporary root, and checks each predicate in
isolation. Offline: no network.

Positive: each of the six approved repositories at a 40-hex commit, safe path,
exact size+sha256 -> returns root/<repo>/<path>, writes exactly the served
bytes, requests exactly the pinned raw URL once.
Negatives: ValueError with the exact message ('unapproved source',
'unsafe path', 'invalid identity', 'source mismatch: <repo>/<path>'), and
nothing written under root; the first three also make NO request.
"""
from __future__ import annotations

import hashlib
import os
import pathlib
import re
import tempfile
import textwrap
import types
import unittest
from pathlib import Path

WORKFLOW = Path(os.environ.get('W8D_CATALOG_YML') or
                Path(__file__).resolve().parents[1] / '.github' / 'workflows' / 'catalog.yml')
APPROVED = ('Math-', 'meta-framework', 'query-', 'google-drive', 'trial', 'governance-')
COMMIT = '1' * 40
PAYLOAD = b'alpha\n'
DIGEST = hashlib.sha256(PAYLOAD).hexdigest()


def extract_fetch_source(text):
    lines = text.splitlines()
    starts = [i for i, l in enumerate(lines) if l.rstrip().endswith("<<'PY'")]
    if len(starts) != 1:
        raise AssertionError('expected exactly one <<\'PY\' heredoc, found %d' % len(starts))
    body = []
    for l in lines[starts[0] + 1:]:
        if l.strip() == 'PY':
            break
        body.append(l)
    else:
        raise AssertionError('unterminated heredoc')
    script = textwrap.dedent('\n'.join(body))
    out, inside = [], False
    for l in script.splitlines():
        if l.startswith('def fetch('):
            if inside or out:
                raise AssertionError('more than one def fetch')
            inside = True
        elif inside and l and not l[0].isspace():
            break
        if inside:
            out.append(l)
    if not out:
        raise AssertionError('def fetch not found')
    return '\n'.join(out) + '\n'


FETCH_SOURCE = extract_fetch_source(WORKFLOW.read_text(encoding='utf-8'))


class _Response:
    def __init__(self, data):
        self._data = data

    def read(self, n=-1):
        return self._data if n is None or n < 0 else self._data[:n]

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


class CatalogFetchControl(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name).resolve() / 'workspace'
        self.root.mkdir()
        self.requests = []
        self.served = {}

        def urlopen(url, timeout=None):
            self.requests.append(url)
            return _Response(self.served.get(url, PAYLOAD))

        fake = types.SimpleNamespace(request=types.SimpleNamespace(urlopen=urlopen))
        ns = {'hashlib': hashlib, 'pathlib': pathlib, 're': re, 'urllib': fake, 'root': self.root}
        exec(compile(FETCH_SOURCE, str(WORKFLOW) + ':fetch', 'exec'), ns)
        self.fetch = ns['fetch']

    def url(self, repo, commit, path):
        return f'https://raw.githubusercontent.com/d6g8k5htny-coder/{repo}/{commit}/{path}'

    def written(self):
        return sorted(str(p.relative_to(self.root)) for p in self.root.rglob('*') if p.is_file())

    def assert_refused(self, message, args, fetched):
        with self.assertRaises(ValueError) as cm:
            self.fetch(*args)
        self.assertEqual(str(cm.exception), message)
        self.assertEqual(self.written(), [], 'a refused fetch must not write a payload')
        if not fetched:
            self.assertEqual(self.requests, [], 'a pre-fetch refusal must not open a URL')

    # positive ------------------------------------------------------------
    def test_approved_exact_source_is_fetched_and_written(self):
        for repo in APPROVED:
            with self.subTest(repo=repo):
                self.requests.clear()
                dest = self.fetch(repo, COMMIT, 'dir/a.txt', len(PAYLOAD), DIGEST)
                self.assertEqual(dest, self.root / repo / 'dir/a.txt')
                self.assertEqual(dest.read_bytes(), PAYLOAD)
                self.assertEqual(self.requests, [self.url(repo, COMMIT, 'dir/a.txt')])

    # C-ALLOW (L29) --------------------------------------------------------
    def test_unapproved_repository_is_refused(self):
        for repo in ('sandbox', 'Sandbox', 'main', 'evil', 'Math-/../sandbox'):
            with self.subTest(repo=repo):
                self.assert_refused('unapproved source',
                                    (repo, COMMIT, 'dir/a.txt', len(PAYLOAD), DIGEST), False)

    def test_non_exact_commit_is_refused(self):
        for commit in ('main', 'abcdef1', '1' * 41, 'A' * 40, 'refs/' + '1' * 40, '1' * 40 + '\n'):
            with self.subTest(commit=commit):
                self.assert_refused('unapproved source',
                                    ('Math-', commit, 'dir/a.txt', len(PAYLOAD), DIGEST), False)

    # C-PATH (L30-31) ------------------------------------------------------
    def test_unsafe_path_is_refused(self):
        for path in ('/abs.txt', '../a.txt', 'dir/../a.txt', './a.txt', 'dir//a.txt',
                     'dir\\a.txt', 'dir:a.txt', ''):
            with self.subTest(path=path):
                self.assert_refused('unsafe path',
                                    ('Math-', COMMIT, path, len(PAYLOAD), DIGEST), False)

    # C-IDENT (L32) --------------------------------------------------------
    def test_invalid_declared_identity_is_refused(self):
        for size, digest in ((True, DIGEST), (-1, DIGEST), (1000001, DIGEST), (6.0, DIGEST),
                             ('6', DIGEST), (6, DIGEST[:63]), (6, DIGEST + '0'),
                             (6, DIGEST.upper()), (6, 'x' + DIGEST[1:])):
            with self.subTest(size=size, digest=digest):
                self.assert_refused('invalid identity',
                                    ('Math-', COMMIT, 'dir/a.txt', size, digest), False)

    # C-MATCH (L33-34) -----------------------------------------------------
    def test_served_bytes_must_match_declared_size_and_digest(self):
        url = self.url('Math-', COMMIT, 'dir/a.txt')
        for served in (b'ALPHA\n', PAYLOAD + b'EXTRA', PAYLOAD[:-1], b''):
            with self.subTest(served=served):
                self.requests.clear()
                self.served[url] = served
                self.assert_refused('source mismatch: Math-/dir/a.txt',
                                    ('Math-', COMMIT, 'dir/a.txt', len(PAYLOAD), DIGEST), True)
                self.assertEqual(self.requests, [url])


if __name__ == '__main__':
    unittest.main()
