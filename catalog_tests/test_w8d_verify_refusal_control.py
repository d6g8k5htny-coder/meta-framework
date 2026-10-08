"""Proposed control (W8d, group V): the catalog `--verify` refusal contract of the
query- lookup tool that meta-framework's catalog.yml pins and executes
(query- 8e201316d17cf4ff3c679e1e9906d4b016ac6730 research_query.py, blob c2dd46a2,
sha256 54105dcd...; catalog.yml L38/L40/L42/L46).

Positive: exact bytes for two rows in two repositories -> exit 0, empty stderr,
stdout is exactly the verified JSON report.
Negatives (one predicate per test, always on the SECOND row 'b' in
'google-drive', so first-row-only or one-repository exemptions cannot pass):
exit 2, stderr exactly 'REFUSED: <message>\n', EMPTY stdout, and the API raises
CatalogError with the exact message. Offline: no network.

Source location (first that exists): $W8D_QUERY_SOURCE, then
$FEDERATION_WORKSPACE/query-/research_query.py, then ../query-/research_query.py
beside this repository. If $W8D_QUERY_SOURCE is set but missing the module fails
closed; if nothing is found the module is SKIPPED (a skip is not protection).

W8-F (meta-framework catalog_tests/, run by catalog.yml): with W8D_REQUIRE_SOURCE=1 the
ONLY accepted source is $W8D_QUERY_SOURCE (no FEDERATION_WORKSPACE or sibling fallback,
never a skip); unset or missing -> the module fails closed. test_mode_receipt spawns a
child through the same child_flags() helper that cli() uses and checks that the child's
actual sys.flags.optimize equals the parent's; with W8D_MODE_RECEIPT=<file> it also writes
that observation as JSON (the optimized-coverage receipt).
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


def _locate():
    env = os.environ.get('W8D_QUERY_SOURCE')
    if os.environ.get('W8D_REQUIRE_SOURCE') == '1' and not env:
        raise RuntimeError('W8D_REQUIRE_SOURCE=1 requires W8D_QUERY_SOURCE (no fallback)')
    if env:
        p = Path(env)
        if not p.is_file():
            raise RuntimeError('W8D_QUERY_SOURCE does not name a file: ' + env)
        return p.resolve()
    cands = []
    if os.environ.get('FEDERATION_WORKSPACE'):
        cands.append(Path(os.environ['FEDERATION_WORKSPACE']) / 'query-' / 'research_query.py')
    cands.append(Path(__file__).resolve().parents[2] / 'query-' / 'research_query.py')
    for p in cands:
        if p.is_file():
            return p.resolve()
    raise unittest.SkipTest('query- research_query.py not found; set W8D_QUERY_SOURCE')


QUERY = _locate()
_SPEC = importlib.util.spec_from_file_location('w8d_checked_query', QUERY)
q = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(q)

A_BYTES = b'alpha\n'
B_BYTES = b'beta\n'
MEANING = 'exact bytes only; not currentness or theorem acceptance'


def child_flags():
    # forward the parent's optimization to every child (M292-OPT-01)
    return ['-B', '-S'] + (['-O'] if sys.flags.optimize else [])


def child_env():
    # C164-OPT-01: drop ambient PYTHONOPTIMIZE. One -O cannot express a
    # parent level above 1, so pin that observed level after the pop.
    env = dict(os.environ)
    env.pop('PYTHONOPTIMIZE', None)
    if sys.flags.optimize > 1:
        env['PYTHONOPTIMIZE'] = str(sys.flags.optimize)
    return env


def row(key, repo, path, payload, **over):
    r = {'key': key, 'repository': repo, 'path': path, 'commit': '1' * 40,
         'visibility': 'public', 'bytes': len(payload),
         'sha256': hashlib.sha256(payload).hexdigest(),
         'scope': 'synthetic W8d control row, not acceptance'}
    r.update(over)
    return r


class VerifyRefusalControl(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.base = Path(tmp.name).resolve()
        self.ws = self.base / 'ws'
        (self.ws / 'Math-').mkdir(parents=True)
        (self.ws / 'google-drive' / 'r').mkdir(parents=True)
        (self.ws / 'Math-' / 'a.txt').write_bytes(A_BYTES)
        (self.ws / 'google-drive' / 'r' / 'b.txt').write_bytes(B_BYTES)
        self.catalog = {
            'schema_version': 1, 'scientific_status_authority': False,
            'repositories': {
                'Math-': {'full_name': 'd6g8k5htny-coder/Math-', 'visibility': 'public'},
                'google-drive': {'full_name': 'd6g8k5htny-coder/google-drive', 'visibility': 'public'},
                'sandbox': {'full_name': 'd6g8k5htny-coder/sandbox', 'visibility': 'private'}},
            'artifacts': [row('a', 'Math-', 'a.txt', A_BYTES),
                          row('b', 'google-drive', 'r/b.txt', B_BYTES)]}
        self.catpath = self.base / 'catalog.json'

    # helpers -------------------------------------------------------------
    def write_catalog(self):
        self.catpath.write_text(json.dumps(self.catalog), encoding='utf-8')

    def cli(self, *extra, cwd=None, workspace=True):
        self.write_catalog()
        args = [sys.executable, *child_flags(), str(QUERY), '--registry', str(self.catpath), '--verify']
        if workspace:
            args += ['--workspace', str(self.ws)]
        p = subprocess.run(args + list(extra), cwd=cwd or self.base,
                           capture_output=True, text=True, timeout=20, env=child_env())
        return p.returncode, p.stdout, p.stderr

    def assert_refused(self, message):
        code, out, err = self.cli()
        self.assertEqual(err, 'REFUSED: ' + message + '\n')
        self.assertEqual(code, 2)
        self.assertEqual(out, '', 'a refused run must not print a report')

    def assert_api_refused(self, message):
        self.write_catalog()
        data = q.load_catalog(self.catpath)
        with self.assertRaises(q.CatalogError) as cm:
            q.verify(data, self.ws)
        self.assertEqual(str(cm.exception), message)

    def assert_load_refused(self, message):
        self.write_catalog()
        with self.assertRaises(q.CatalogError) as cm:
            q.load_catalog(self.catpath)
        self.assertEqual(str(cm.exception), message)
        self.assert_refused(message)

    def set_b(self, **over):
        self.catalog['artifacts'][1].update(over)

    # mode receipt ----------------------------------------------------------
    def test_mode_receipt(self):
        p = subprocess.run([sys.executable, *child_flags(), '-c', 'import sys; print(sys.flags.optimize)'],
                           capture_output=True, text=True, timeout=20, env=child_env())
        self.assertEqual((p.returncode, p.stderr), (0, ''))
        receipt = {'parent_optimize': sys.flags.optimize, 'child_optimize': int(p.stdout.strip()),
                   'child_flags': child_flags(), 'query_source': str(QUERY),
                   'query_sha256': hashlib.sha256(QUERY.read_bytes()).hexdigest()}
        if os.environ.get('W8D_MODE_RECEIPT'):
            Path(os.environ['W8D_MODE_RECEIPT']).write_text(json.dumps(receipt, sort_keys=True) + '\n')
        self.assertEqual(receipt['child_optimize'], receipt['parent_optimize'])

    # positive ------------------------------------------------------------
    def test_exact_bytes_are_verified_with_exact_report(self):
        code, out, err = self.cli()
        self.assertEqual((code, err), (0, ''))
        self.assertEqual(out, json.dumps({'meaning': MEANING, 'verified': ['a', 'b']},
                                         indent=2, sort_keys=True) + '\n')
        self.write_catalog()
        self.assertEqual(q.verify(q.load_catalog(self.catpath), self.ws)['verified'], ['a', 'b'])

    # V-BYTES (L101-102) --------------------------------------------------
    def test_longer_payload_is_byte_count_refusal(self):
        (self.ws / 'google-drive/r/b.txt').write_bytes(B_BYTES + b'\n')
        self.assert_api_refused('byte count mismatch: b')
        self.assert_refused('byte count mismatch: b')

    def test_shorter_payload_is_byte_count_refusal(self):
        (self.ws / 'google-drive/r/b.txt').write_bytes(B_BYTES[:-1])
        self.assert_api_refused('byte count mismatch: b')
        self.assert_refused('byte count mismatch: b')

    # V-HASH (L103-105) ---------------------------------------------------
    def test_same_length_substitution_is_hash_refusal(self):
        (self.ws / 'google-drive/r/b.txt').write_bytes(b'BETA\n')
        self.assert_api_refused('hash mismatch: b')
        self.assert_refused('hash mismatch: b')

    # V-PAYLOAD (L95-100) -------------------------------------------------
    def test_symlinked_final_component_is_refused(self):
        target = self.base / 'elsewhere.txt'
        target.write_bytes(B_BYTES)
        p = self.ws / 'google-drive/r/b.txt'
        p.unlink()
        p.symlink_to(target)
        self.assert_api_refused('symlink payload refused: b')
        self.assert_refused('symlink payload refused: b')

    def test_symlinked_intermediate_directory_is_refused(self):
        real = self.ws / 'real-gd'
        (self.ws / 'google-drive').rename(real)
        (self.ws / 'google-drive').symlink_to(real, target_is_directory=True)
        self.assert_api_refused('symlink payload refused: b')
        self.assert_refused('symlink payload refused: b')

    def test_missing_payload_names_the_key(self):
        (self.ws / 'google-drive/r/b.txt').unlink()
        self.assert_api_refused('missing/outside payload: b')
        self.assert_refused('missing/outside payload: b')

    # V-COMMIT (L71-72) ---------------------------------------------------
    def test_non_exact_commit_is_refused(self):
        for bad in ('abcdef1', 'A' * 40, '0' * 40 + 'x', 'refs/' + '0' * 40, 'main'):
            with self.subTest(commit=bad):
                self.set_b(commit=bad)
                self.assert_load_refused('exact commit required')

    # V-SHAFMT (L73-74) ---------------------------------------------------
    def test_non_exact_sha256_is_refused(self):
        for bad in ('a' * 40, 'a' * 63, 'a' * 64 + '0', 'A' * 64):
            with self.subTest(sha256=bad):
                self.set_b(sha256=bad)
                self.assert_load_refused('exact SHA256 required')

    # V-BYTESFMT (L75-76) -------------------------------------------------
    def test_invalid_byte_count_is_refused(self):
        for bad in (True, -1, 10000001, 5.0, '5'):
            with self.subTest(bytes=bad):
                self.set_b(bytes=bad)
                self.assert_load_refused('invalid byte count')

    # V-PATH (valid_path L29-35) ------------------------------------------
    def test_unsafe_paths_are_refused(self):
        for bad in ('r\\b.txt', 'r:b.txt', './r/b.txt', 'r//b.txt', '/r/b.txt',
                    '../r/b.txt', 'r/../b.txt', ''):
            with self.subTest(path=bad):
                self.set_b(path=bad)
                self.assert_load_refused('unsafe path')

    # V-CLI (L118-133) ----------------------------------------------------
    def test_verify_without_workspace_is_refused_even_in_a_valid_cwd(self):
        code, out, err = self.cli(cwd=self.ws, workspace=False)
        self.assertEqual(err, 'REFUSED: --verify requires --workspace\n')
        self.assertEqual(code, 2)
        self.assertEqual(out, '')


if __name__ == '__main__':
    unittest.main()
