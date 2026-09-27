"""Engineering controls for tools/formal_status_check.py. Software behavior only; no theorem acceptance."""
import copy
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / 'tools'))
import formal_status_check as f

TOOLCHAIN = 'leanprover/lean4:v4.35.0-rc3'
MATHLIB = 'c' * 40
CORE = '[Classical.choice, Quot.sound, propext]'


class Fixture(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        for rel in ('docs/FORMAL_VERIFICATION.md', 'docs/FORMAL_GLOSSARY.md', 'formal/STATEMENTS.md',
                    'formal/lean/lakefile.toml', 'formal/lean/scripts/AxiomAudit.lean'):
            self.write(rel, rel + '\n')
        self.write('formal/lean/lean-toolchain', TOOLCHAIN + '\n')
        self.write('formal/lean/lake-manifest.json', json.dumps({'packages': [{'name': 'mathlib', 'rev': MATHLIB}]}))
        self.lean_bytes = b'theorem Side24.Pilot.t : True := trivial\n'
        self.write('formal/lean/Side24Formal/Pilot.lean', self.lean_bytes)
        self.data = {
            'schema_version': 1, 'scientific_status_authority': False,
            'repositories': {'Math-': {'full_name': 'd6g8k5htny-coder/Math-', 'visibility': 'public'},
                             'meta-framework': {'full_name': 'd6g8k5htny-coder/meta-framework', 'visibility': 'public'}},
            'formal_verification': {
                'scientific_status_authority': False, 'spec': 'docs/FORMAL_VERIFICATION.md',
                'glossary': 'docs/FORMAL_GLOSSARY.md', 'alignment_ledger': 'formal/STATEMENTS.md',
                'lean_root': 'formal/lean', 'allowed_axioms': ['propext', 'Classical.choice', 'Quot.sound'],
                'backend': {'prover': 'Lean 4', 'toolchain': TOOLCHAIN, 'mathlib_rev': MATHLIB},
                'status_vocabulary': {k: 'd' for k in f.STATUS_ORDER},
                'alignment_vocabulary': {k: 'd' for k in f.ALIGNMENT_ORDER}},
            'artifacts': [
                {'key': 'claim', 'repository': 'Math-', 'path': 'x/PROOF.md', 'commit': '0' * 40, 'visibility': 'public',
                 'bytes': 1, 'sha256': '0' * 64, 'scope': 's', 'formalization': {'status': 'none'}},
                {'key': 'code', 'repository': 'Math-', 'path': 'x/code.py', 'commit': '0' * 40, 'visibility': 'public',
                 'bytes': 1, 'sha256': '0' * 64, 'scope': 's'}]}
        self.report = self.root / 'axioms.txt'
        self.write_report(['AXIOMS Side24.Pilot.t ' + CORE], sorry=0)

    def write(self, rel, content):
        path = self.root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        if isinstance(content, bytes):
            path.write_bytes(content)
        else:
            path.write_text(content, encoding='utf-8')

    def write_report(self, lines, sorry, declared=()):
        body = list(lines) + ['DECLARED_AXIOM ' + d for d in declared]
        body += ['AUDIT_THEOREMS %d' % len(lines), 'AUDIT_SORRY %d' % sorry]
        self.report.write_text('\n'.join(body) + '\n')

    def registry(self, data=None):
        path = self.root / 'registry.json'
        path.write_text(json.dumps(self.data if data is None else data))
        return path

    def run_check(self, lean_root='formal/lean', report=True):
        return f.run(self.registry(), self.root, lean_root, self.report if report else None)

    def refuse(self, pattern, **kw):
        with self.assertRaisesRegex(f.FormalError, pattern):
            self.run_check(**kw)

    def add_lean_artifact(self):
        self.data['artifacts'].append({
            'key': 'pilot-lean', 'repository': 'meta-framework', 'path': 'formal/lean/Side24Formal/Pilot.lean',
            'commit': '1' * 40, 'visibility': 'public', 'bytes': len(self.lean_bytes),
            'sha256': hashlib.sha256(self.lean_bytes).hexdigest(), 'scope': 'lean source'})

    def proved_claim(self, **extra):
        self.add_lean_artifact()
        self.data['artifacts'][0]['formalization'] = dict({
            'status': 'none', 'lemma_status': 'proved', 'lean_artifact': 'pilot-lean',
            'theorems': ['Side24.Pilot.t'], 'authorship': 'Cursor (AI)', 'alignment_review': 'open',
            'alignment_ledger': 'formal/STATEMENTS.md'}, **extra)


class StatusRules(Fixture):
    def test_none_only_passes(self):
        out = self.run_check()
        self.assertEqual(out['formal_claims'], [])
        self.assertEqual(out['axiom_report_theorems'], 1)

    def test_proved_claim_passes_and_binds_local_bytes(self):
        self.proved_claim()
        out = self.run_check()
        self.assertEqual(out['formal_claims'][0]['lemma_status'], 'proved')
        self.assertEqual(out['local_identities_verified'], ['pilot-lean'])

    def test_changed_lean_bytes_require_reindex(self):
        self.proved_claim()
        self.write('formal/lean/Side24Formal/Pilot.lean', b'theorem Side24.Pilot.t : True := by trivial\n')
        self.refuse('re-index')

    def test_kernel_checked_requires_evidence(self):
        self.proved_claim(lemma_status='kernel-checked')
        self.refuse('requires CI evidence')
        self.data['artifacts'][0]['formalization']['evidence'] = ['https://github.com/d6g8k5htny-coder/meta-framework/actions/runs/1']
        self.assertEqual(self.run_check()['formal_claims'][0]['lemma_status'], 'kernel-checked')

    def test_foreign_evidence_refused(self):
        self.proved_claim(evidence=['https://example.com/run'])
        self.refuse('project GitHub URLs')

    def test_accepted_alignment_needs_distinct_reviewer(self):
        self.proved_claim(alignment_review='accepted')
        self.refuse('distinct nonauthor')
        self.data['artifacts'][0]['formalization']['alignment_reviewer'] = 'Cursor (AI)'
        self.refuse('distinct nonauthor')
        self.data['artifacts'][0]['formalization']['alignment_reviewer'] = 'OpenAI / ChatGPT'
        self.run_check()

    def test_status_none_cannot_carry_lean_fields(self):
        self.add_lean_artifact()
        self.data['artifacts'][0]['formalization'] = {'status': 'none', 'lean_artifact': 'pilot-lean'}
        self.refuse('requires a status above none')

    def test_claim_without_record_refused(self):
        del self.data['artifacts'][0]['formalization']
        self.refuse('claim documents require')

    def test_non_claim_only_none(self):
        self.data['artifacts'][1]['formalization'] = {'status': 'proved'}
        self.refuse('non-claim artifacts may only record status none')

    def test_unknown_status_and_field(self):
        self.data['artifacts'][0]['formalization'] = {'status': 'verified'}
        self.refuse('unknown formalization status')
        self.proved_claim(extra_field='x')
        self.refuse('unknown formalization field')

    def test_lean_artifact_must_be_lean_under_root(self):
        self.proved_claim()
        self.data['artifacts'][0]['formalization']['lean_artifact'] = 'code'
        self.refuse('catalogued .lean artifact')
        self.data['artifacts'][0]['formalization']['lean_artifact'] = 'pilot-lean'
        self.data['artifacts'][2]['path'] = 'elsewhere/Pilot.lean'
        self.refuse('lean_root')

    def test_lean_source_carries_no_record(self):
        self.proved_claim()
        self.data['artifacts'][2]['formalization'] = {'status': 'none'}
        self.refuse('carry no formalization record')

    def test_theorem_absent_from_report(self):
        self.proved_claim(theorems=['Side24.Pilot.missing'])
        self.refuse('absent from axiom report')

    def test_theorem_claimed_twice(self):
        self.proved_claim()
        self.data['artifacts'].append(dict(copy.deepcopy(self.data['artifacts'][0]), key='claim2', path='y/PROOF.md'))
        self.refuse('already claimed')

    def test_sorry_policy(self):
        self.proved_claim()
        self.write_report(['AXIOMS Side24.Pilot.t [sorryAx, propext]'], sorry=1)
        self.refuse('unrecorded axioms sorryAx')
        self.data['artifacts'][0]['formalization']['lemma_status'] = 'specified'
        self.run_check()
        self.write_report(['AXIOMS Side24.Pilot.t [propext]', 'AXIOMS Side24.Other.u [sorryAx]'], sorry=1)
        self.refuse('sorry outside a specified catalog theorem')

    def test_assumed_axioms(self):
        self.proved_claim()
        self.write_report(['AXIOMS Side24.Pilot.t [Side24.Assumptions.parent, propext]'], sorry=0,
                          declared=['Side24.Assumptions.parent'])
        self.refuse('unrecorded axioms Side24.Assumptions.parent')
        self.data['artifacts'][0]['formalization']['assumed_axioms'] = ['Side24.Assumptions.parent']
        self.run_check()
        self.data['artifacts'][0]['formalization']['lemma_status'] = 'kernel-checked'
        self.data['artifacts'][0]['formalization']['evidence'] = ['https://github.com/d6g8k5htny-coder/meta-framework/actions/runs/1']
        self.refuse('capped at proved')

    def test_declared_axiom_must_be_recorded(self):
        self.proved_claim()
        self.write_report(['AXIOMS Side24.Pilot.t ' + CORE], sorry=0, declared=['Side24.Assumptions.unused'])
        self.refuse('declared Lean axiom not recorded')

    def test_rogue_assumption_namespace(self):
        self.proved_claim(assumed_axioms=['Side24.Rogue.ax'])
        self.refuse('declared under Side24.Assumptions')


class BlockAndToolchain(Fixture):
    def test_block_required_and_authority_false(self):
        self.data['formal_verification']['scientific_status_authority'] = True
        self.refuse('scientific_status_authority false')
        del self.data['formal_verification']
        self.refuse('formal_verification block required')

    def test_vocabulary_closed(self):
        self.data['formal_verification']['status_vocabulary']['verified'] = 'd'
        self.refuse('status_vocabulary')

    def test_allowed_axioms_fixed(self):
        self.data['formal_verification']['allowed_axioms'].append('sorryAx')
        self.refuse('three core axioms')

    def test_toolchain_pins(self):
        self.write('formal/lean/lean-toolchain', 'leanprover/lean4:v4.34.0\n')
        self.refuse('lean-toolchain differs')
        self.write('formal/lean/lean-toolchain', TOOLCHAIN + '\n')
        self.write('formal/lean/lake-manifest.json', json.dumps({'packages': [{'name': 'mathlib', 'rev': 'd' * 40}]}))
        self.refuse('mathlib rev differs')

    def test_lean_root_argument_must_match(self):
        self.refuse('differs from catalog lean_root', lean_root='other')

    def test_without_lean_root_or_report(self):
        out = f.run(self.registry(), self.root, None, None)
        self.assertIsNone(out['lean_sources'])
        self.assertIsNone(out['axiom_report_theorems'])

    def test_duplicate_json_key(self):
        path = self.root / 'registry.json'
        path.write_text('{"schema_version":1,"schema_version":1}')
        with self.assertRaisesRegex(f.FormalError, 'duplicate JSON'):
            f.run(path, self.root, None, None)

    def test_malformed_report(self):
        self.report.write_text('AXIOMS bad\nAUDIT_THEOREMS 1\nAUDIT_SORRY 0\n')
        self.refuse('malformed axiom report')
        self.report.write_text('AXIOMS Side24.Pilot.t [propext]\nAUDIT_THEOREMS 2\nAUDIT_SORRY 0\n')
        self.refuse('totals missing or inconsistent')
        self.report.write_text('AXIOMS Side24.Pilot.t [propext]\nerror: disallowed axioms\nAUDIT_THEOREMS 1\nAUDIT_SORRY 0\n')
        self.refuse('error line')


class RealCatalog(unittest.TestCase):
    def test_actual_catalog_passes_without_report(self):
        out = f.run(REPO / 'registry.json', REPO, 'formal/lean', None)
        self.assertTrue(out['lean_sources'])
        for claim in out['formal_claims']:
            self.assertIn(claim['status'], f.STATUS_ORDER)

    def test_cli_refusal_is_clean(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'registry.json'
            path.write_text('[]')
            p = subprocess.run([sys.executable, '-B', '-S', str(REPO / 'tools/formal_status_check.py'), '--registry', str(path)],
                               capture_output=True, text=True, timeout=30)
        self.assertEqual(p.returncode, 2)
        self.assertIn('REFUSED', p.stderr)
        self.assertNotIn('Traceback', p.stderr)


if __name__ == '__main__':
    unittest.main()
