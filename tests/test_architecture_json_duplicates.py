"""Real API/CLI controls for the common architecture JSON loader."""
from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from tools.architecture_conformance import _load_json, check_workspace

REPOS = ['Math-', 'google-drive', 'governance-', 'main', 'meta-framework',
         'query-', 'sandbox', 'trial']
SCRIPT = Path(__file__).resolve().parents[1] / 'tools/architecture_conformance.py'
ROUTES = {
    'registry': ('meta-framework/registry.json', 'scientific_status_authority', False, True,
                 'registry parse error: ', 'registry cannot be scientific-status authority'),
    'manifest': ('Math-/SOURCE_MANIFEST.json', 'scientific_status_authority', False, True,
                 'Math-/SOURCE_MANIFEST.json: ',
                 'Math-/SOURCE_MANIFEST.json: source manifest cannot be scientific-status authority'),
    'snapshot': ('meta-framework/WORKSPACE_SNAPSHOT.json', 'commit', '1' * 40, 'main',
                 'workspace snapshot: ', 'workspace snapshot: exact commit required'),
    'generated': ('meta-framework/generated/probe.json', 'scientific_status_authority', False, True,
                  'generated JSON parse error: meta-framework/generated/probe.json: ',
                  'generated scientific-status authority: meta-framework/generated/probe.json'),
    'authority': ('main/architecture/scientific_state/v1/AUTHORITY_MAP.json',
                  'owns', ['schema_contract'], ['status'],
                  'authority map validation error: ', 'architecture authority overreach: status'),
}


class ArchitectureJSONDuplicates(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        for name in REPOS:
            (self.root / name).mkdir()
        self.write('meta-framework/registry.json', {
            'schema_version': 1, 'scientific_status_authority': False,
            'repositories': {name: {'full_name': 'd6g8k5htny-coder/' + name,
                                   'visibility': 'private' if name == 'sandbox' else 'public'}
                             for name in REPOS}, 'artifacts': []})
        self.write('Math-/SOURCE_MANIFEST.json', {
            'schema_version': '1.0', 'distribution': 'test', 'version': '0.1.0',
            'repository': 'd6g8k5htny-coder/Math-', 'commit': 'a' * 40,
            'scientific_status_authority': False,
            'files': [{'path': 'test.txt', 'sha256': 'b' * 64, 'bytes': 1}]})
        self.write('meta-framework/WORKSPACE_SNAPSHOT.json', {
            'schema_version': '1.0', 'snapshot': 'synthetic',
            'repositories': [{'repository': 'd6g8k5htny-coder/' + name,
                              'commit': format(i, 'x') * 40}
                             for i, name in enumerate(REPOS, 1)]})
        self.write('meta-framework/generated/probe.json', {
            'layers': [{'scientific_status_authority': False}]})
        self.write('main/architecture/scientific_state/v1/AUTHORITY_MAP.json', {
            'required_authority_ids': ['claims', 'architecture'],
            'authorities': {'claims': {'id': 'claims', 'owns': ['grade']}},
            'this_package': {'id': 'architecture', 'owns': ['schema_contract'],
                             'never_writes': ['status', 'grade', 'classification', 'controlling',
                                              'lemma_closed', 'prizes_solved', 'independence_credit']}})
        self.originals = self.inventory()

    def write(self, name, value):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value), encoding='utf-8')

    def inventory(self):
        return {p.relative_to(self.root).as_posix(): p.read_bytes()
                for p in self.root.rglob('*') if p.is_file()}

    def restore(self):
        for name, data in self.originals.items():
            (self.root / name).write_bytes(data)

    def assert_report(self, expected):
        before = self.inventory()
        flags = ['-B', '-S'] + (['-O'] if sys.flags.optimize else [])
        # The exact child mode is explicit; inherited optimization cannot select it.
        env = dict(os.environ)
        env.pop('PYTHONOPTIMIZE', None)
        actual = check_workspace(self.root)
        child = subprocess.run([sys.executable, *flags, str(SCRIPT), '--workspace', str(self.root)],
                               capture_output=True, text=True, encoding='utf-8', env=env, timeout=10)
        self.assertEqual(self.inventory(), before)
        self.assertEqual(child.stderr, '')
        self.assertEqual(actual, expected)
        self.assertEqual(child.returncode, 0 if expected['ok'] else 2, child.stdout)
        self.assertEqual(child.stdout, json.dumps(expected, indent=2, sort_keys=True) + '\n')

    @staticmethod
    def report(violations=(), checked=REPOS):
        return {'ok': not violations, 'repositories_checked': sorted(checked),
                'violations': list(violations), 'scientific_effect': 'NONE'}

    def replace_member(self, route, replacement):
        name, key, good, _, _, _ = ROUTES[route]
        text = self.originals[name].decode('utf-8')
        needle = json.dumps(key) + ': ' + json.dumps(good)
        self.assertEqual(text.count(needle), 1, (route, needle))
        (self.root / name).write_text(text.replace(needle, replacement), encoding='utf-8')

    def test_unique_inputs_pass(self):
        self.assert_report(self.report())

    def test_duplicate_orders_equal_values_and_escaped_keys_are_refused_on_all_routes(self):
        for route, (_, key, good, bad, prefix, _) in ROUTES.items():
            quoted = json.dumps(key)
            escaped = '"\\u%04x%s"' % (ord(key[0]), key[1:])
            variants = (
                quoted + ': ' + json.dumps(bad) + ', ' + quoted + ': ' + json.dumps(good),
                quoted + ': ' + json.dumps(good) + ', ' + quoted + ': ' + json.dumps(bad),
                quoted + ': ' + json.dumps(good) + ', ' + quoted + ': ' + json.dumps(good),
                quoted + ': ' + json.dumps(bad) + ', ' + escaped + ': ' + json.dumps(good),
            )
            for variant in variants:
                with self.subTest(route=route, variant=variant):
                    self.restore()
                    self.replace_member(route, variant)
                    error = prefix + 'duplicate JSON member: ' + quoted
                    errors = [error]
                    checked = REPOS
                    if route == 'registry':
                        checked = []
                        errors += ['registry schema_version must equal integer 1',
                                   'repository map required']
                        errors += ['missing repository role: ' + name for name in sorted(REPOS)]
                        errors += ['registry cannot be scientific-status authority',
                                   'registry artifacts must be a list']
                    self.assert_report(self.report(errors, checked))

    def test_single_prohibited_values_keep_original_refusals(self):
        for route, (_, key, _, bad, _, refusal) in ROUTES.items():
            with self.subTest(route=route):
                self.restore()
                self.replace_member(route, json.dumps(key) + ': ' + json.dumps(bad))
                self.assert_report(self.report([refusal]))

    def test_nested_duplicate_diagnostics_are_quoted_and_ascii_safe(self):
        name = 'meta-framework/generated/probe.json'
        path = self.root / name
        for key in ('', 'x', 'quote"', 'line\nbreak', '\u00e9', '\ud800'):
            quoted = json.dumps(key, ensure_ascii=True)
            expected = 'duplicate JSON member: ' + quoted
            with self.subTest(key=quoted):
                # Unknown fields still need duplicate refusal, including inside arrays.
                path.write_text('{"layer":[{"deeper":{' + quoted + ':1,' + quoted + ':1}}]}',
                                encoding='utf-8')
                before = path.read_bytes()
                with self.assertRaises(ValueError) as caught:
                    _load_json(path)
                self.assertEqual(str(caught.exception), expected)
                self.assertTrue(str(caught.exception).isascii())
                self.assertEqual(path.read_bytes(), before)
                self.assert_report(self.report(['generated JSON parse error: ' + name + ': ' + expected]))

    def test_names_in_distinct_objects_and_distinct_unicode_spellings_are_allowed(self):
        value = {'objects': [{'same': 1}, {'same': 2}],
                 'text': '"same": 1, "same": 2',
                 'a': 1, 'A': 2, '\u00e9': 3, 'e\u0301': 4}
        name = 'meta-framework/generated/probe.json'
        self.write(name, value)
        self.assertEqual(_load_json(self.root / name), value)
        self.assert_report(self.report())

    def test_unique_nonobject_roots_and_malformed_syntax_keep_loader_contract(self):
        path = self.root / 'scratch.json'
        for value in (None, True, False, 0, 1.5, '', 'text', [], [1, {'x': 2}]):
            with self.subTest(value=value):
                data = json.dumps(value).encode('utf-8')
                path.write_bytes(data)
                self.assertEqual(_load_json(path), value)
                self.assertEqual(path.read_bytes(), data)
        path.write_bytes(b'{')
        with self.assertRaises(json.JSONDecodeError):
            _load_json(path)
        self.assertEqual(path.read_bytes(), b'{')


if __name__ == '__main__':
    unittest.main()
