"""Proposed control (W8d, group A): registry artifact-row identity predicates in
meta-framework tools/architecture_conformance.py (L70-73, helper
_safe_registry_path L13-16, at 75685db7).

The existing suite has one artifact fixture whose sha256 and bytes are valid,
whose path is not a sandbox/unsafe path, and whose commit is 'main'; it only
checks that some violation text contains a term. Here each predicate is
isolated: one field of one otherwise-valid row is changed, and the report must
contain EXACTLY that one violation.

Positive: a valid public row -> ok True, no violations; CLI exit 0, empty
stderr, exact JSON stdout.
Negatives: violations == ['<exact message>: k']; CLI exit 2, empty stderr,
stdout exactly the JSON report. Offline: no network. Duplicate-member JSON
parsing, non-object roots, manifests, snapshots and the authority map are
out of scope (other owners).
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.architecture_conformance import check_workspace

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'tools' / 'architecture_conformance.py'
REPOS = ['Math-', 'google-drive', 'governance-', 'main', 'meta-framework', 'query-', 'sandbox', 'trial']


def valid_authority():
    return {'required_authority_ids': ['claims_firewall', 'scientific_state_architecture'],
            'authorities': {'claims_firewall': {'id': 'claims_firewall', 'owns': ['grade']}},
            'this_package': {'id': 'scientific_state_architecture', 'owns': ['schema_contract'],
                             'never_writes': ['status', 'grade', 'classification', 'controlling',
                                              'lemma_closed', 'prizes_solved', 'independence_credit']}}


def valid_row(**over):
    row = {'key': 'k', 'repository': 'Math-', 'visibility': 'public', 'commit': '1' * 40,
           'path': 'frontiers/a.txt', 'sha256': 'a' * 64, 'bytes': 6,
           'scope': 'synthetic W8d control row, not acceptance'}
    row.update(over)
    return row


class RegistryRowIdentityControl(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        for name in REPOS:
            (self.root / name).mkdir(parents=True)
        a = self.root / 'main/architecture/scientific_state/v1'
        a.mkdir(parents=True)
        (a / 'AUTHORITY_MAP.json').write_text(json.dumps(valid_authority()))

    def write_registry(self, row):
        registry = {'schema_version': 1, 'scientific_status_authority': False,
                    'repositories': {n: {'full_name': 'd6g8k5htny-coder/' + n, 'role': n,
                                         'visibility': 'private' if n == 'sandbox' else 'public'}
                                     for n in REPOS},
                    'artifacts': [row]}
        (self.root / 'meta-framework/registry.json').write_text(json.dumps(registry))

    def cli(self):
        flags = ['-B', '-S'] + (['-O'] if sys.flags.optimize else [])
        p = subprocess.run([sys.executable, *flags, str(SCRIPT), '--workspace', str(self.root)],
                           capture_output=True, text=True, timeout=20)
        return p.returncode, p.stdout, p.stderr

    def expected(self, violations):
        return {'ok': not violations, 'repositories_checked': sorted(REPOS),
                'violations': violations, 'scientific_effect': 'NONE'}

    def assert_report(self, row, violations):
        self.write_registry(row)
        exp = self.expected(violations)
        self.assertEqual(check_workspace(self.root), exp)
        code, out, err = self.cli()
        self.assertEqual(err, '')
        self.assertEqual(code, 0 if not violations else 2)
        self.assertEqual(out, json.dumps(exp, indent=2, sort_keys=True) + '\n')

    # positive ------------------------------------------------------------
    def test_valid_public_row_is_accepted(self):
        self.assert_report(valid_row(), [])

    # A-COMMIT (L70) ------------------------------------------------------
    def test_non_exact_commit_is_refused(self):
        for bad in ('A' * 40, '1' * 40 + 'x', 'abc1234', 'main', ''):
            with self.subTest(commit=bad):
                self.assert_report(valid_row(commit=bad), ['artifact exact commit required: k'])

    # A-PATH (L71, L13-16) ------------------------------------------------
    def test_unsafe_or_sandbox_path_is_refused(self):
        for bad in ('sandbox/x.txt', 'Sandbox/x.txt', 'a/SANDBOX/x.txt', '../x.txt', 'a/../x.txt',
                    'a\\b.txt', 'a:b.txt', '/abs.txt', './a.txt', ''):
            with self.subTest(path=bad):
                self.assert_report(valid_row(path=bad), ['artifact unsafe/sandbox path: k'])

    # A-SHA (L72) ---------------------------------------------------------
    def test_non_exact_sha256_is_refused(self):
        for bad in ('A' * 64, 'a' * 63, 'a' * 64 + '0', 'not-a-hash', ''):
            with self.subTest(sha256=bad):
                self.assert_report(valid_row(sha256=bad), ['artifact exact sha256 required: k'])

    # A-BYTES (L73) -------------------------------------------------------
    def test_invalid_bytes_is_refused(self):
        for bad in (True, -1, 6.0, '6', None):
            with self.subTest(bytes=bad):
                self.assert_report(valid_row(bytes=bad), ['artifact bytes invalid: k'])


if __name__ == '__main__':
    unittest.main()
