"""Compatibility pins for the source contracts: producer form versus reader acceptance.

Decision record: issue 15 (finding 6129626684; decision 6133399141 as corrected by
6133564511). These tests pin both sides of that decision with the standard library only:

* the validators' two compatibility allowances (major-1 version spellings, omitted
  ``runtime_package``) and the refusals that hold under them;
* the canonical form of the published examples;
* the literal schema facets the decision relies on, read with ``json`` alone.

No schema engine is implemented here; every schema assertion names a literal facet.
Scientific effect NONE.
"""
from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path

from tools.contract_validation import (
    VER,
    ContractError,
    parse_major,
    validate_repository_role,
    validate_source_manifest,
    validate_source_ref,
    validate_workspace_snapshot,
)

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / 'schemas'
EXAMPLES = ROOT / 'examples'
SANDBOX = 'd6g8k5htny-coder/sandbox'

EXAMPLE_VALIDATORS = {
    'repository_role.json': validate_repository_role,
    'source_ref.git.json': validate_source_ref,
    'source_ref.drive.json': validate_source_ref,
    'source_manifest.json': validate_source_manifest,
    'workspace_snapshot.json': validate_workspace_snapshot,
}
ACCEPTED_MINOR_SPELLINGS = ('1.1', '1.10', '01.0', '1.00')
REFUSED_VERSIONS = {
    '1': 'invalid schema_version',
    '1.0.0': 'invalid schema_version',
    '2.0': 'unsupported schema major',
    '1.0\n': 'invalid schema_version',
    ' 1.0': 'invalid schema_version',
    1: 'schema_version must be a string',
    1.0: 'schema_version must be a string',
    None: 'schema_version must be a string',
    True: 'schema_version must be a string',
}
# Literal JSON Schema type names mapped to the Python types a parsed document carries.
JSON_TYPES = {'string': (str,), 'integer': (int,), 'array': (list,), 'object': (dict,), 'boolean': (bool,), 'null': (type(None),)}


def load(path: Path):
    return json.loads(path.read_text(encoding='utf-8'))


def example(name: str) -> dict:
    return load(EXAMPLES / name)


def schema_profile(name: str) -> dict:
    """The schema object that governs the named example (the matching oneOf branch for source refs)."""
    if name.startswith('source_ref.'):
        kind = example(name)['kind']
        branches = [b for b in load(SCHEMAS / 'source_ref.schema.json')['oneOf'] if b['properties']['kind'] == {'const': kind}]
        if len(branches) != 1:
            raise AssertionError('expected exactly one source_ref branch for kind ' + kind)
        return branches[0]
    return load(SCHEMAS / name.replace('.json', '.schema.json'))


def has_declared_type(value, prop: dict) -> bool:
    """Literal facet check: const, enum, or type (integer excludes bool, as the validators do)."""
    if 'const' in prop:
        return value == prop['const'] and type(value) is type(prop['const'])
    if 'enum' in prop:
        return value in prop['enum']
    names = prop['type'] if isinstance(prop['type'], list) else [prop['type']]
    if isinstance(value, bool):
        return 'boolean' in names
    return any(isinstance(value, JSON_TYPES[n]) for n in names)


class ReaderVersionAllowance(unittest.TestCase):
    def test_examples_accepted_under_every_major1_spelling(self):
        for name, validator in EXAMPLE_VALIDATORS.items():
            for version in ('1.0',) + ACCEPTED_MINOR_SPELLINGS:
                with self.subTest(example=name, version=version):
                    doc = example(name)
                    doc['schema_version'] = version
                    self.assertEqual(validator(doc)['schema_version'], version)

    def test_refused_versions_keep_their_messages_on_every_example(self):
        for name, validator in EXAMPLE_VALIDATORS.items():
            for version, message in REFUSED_VERSIONS.items():
                with self.subTest(example=name, version=repr(version)):
                    doc = example(name)
                    doc['schema_version'] = version
                    with self.assertRaisesRegex(ContractError, message):
                        validator(doc)

    def test_version_grammar_is_pinned(self):
        self.assertEqual(VER.pattern, r'^([0-9]+)\.([0-9]+)$')
        for version in ('1.0',) + ACCEPTED_MINOR_SPELLINGS:
            with self.subTest(version=version):
                self.assertEqual(parse_major(version), 1)
        self.assertIsNone(VER.fullmatch('1.0\n'))
        with self.assertRaisesRegex(ContractError, 'unsupported schema major'):
            parse_major('02.0')

    def test_semantic_refusals_hold_under_accepted_minor_spellings(self):
        git = example('source_ref.git.json')
        drive = example('source_ref.drive.json')
        role = example('repository_role.json')
        manifest = example('source_manifest.json')
        manifest['schema_version'] = '1.10'
        manifest['files'].append(dict(manifest['files'][0]))
        snapshot = example('workspace_snapshot.json')
        snapshot['schema_version'] = '1.00'
        snapshot['repositories'][7] = dict(snapshot['repositories'][0])
        cases = [
            ('git sandbox path', validate_source_ref, dict(git, schema_version='1.1', path='sandbox/x.md'), 'sandbox'),
            ('git parent path', validate_source_ref, dict(git, schema_version='1.10', path='../x.md'), 'unsafe path'),
            ('git padded role', validate_source_ref, dict(git, schema_version='1.10', role=' proof '), 'role required'),
            ('git float size', validate_source_ref, dict(git, schema_version='01.0', size_bytes=1.0), 'invalid size_bytes'),
            ('git mutable commit', validate_source_ref, dict(git, schema_version='1.00', commit='main'), 'exact commit'),
            ('external private in public mode', validate_source_ref, dict(drive, schema_version='1.1', visibility='private'), 'public visibility'),
            ('role bad runtime_package type', validate_repository_role, dict(role, schema_version='1.00', runtime_package=1), 'runtime_package must be string or null'),
            ('role status authority', validate_repository_role, dict(role, schema_version='1.1', scientific_status_authority=True), 'scientific-status'),
            ('role empty list member', validate_repository_role, dict(role, schema_version='01.0', canonical_authority_for=['']), 'unique string list'),
            ('manifest duplicate path', validate_source_manifest, manifest, 'duplicate manifest path'),
            ('manifest sandbox repository', validate_source_manifest, dict(example('source_manifest.json'), schema_version='1.1', repository=SANDBOX), 'sandbox'),
            ('snapshot duplicate repository', validate_workspace_snapshot, snapshot, 'duplicate repository'),
        ]
        for label, validator, doc, message in cases:
            with self.subTest(case=label):
                with self.assertRaisesRegex(ContractError, message):
                    validator(doc)


class RuntimePackageOmissionAllowance(unittest.TestCase):
    def setUp(self):
        self.role = example('repository_role.json')

    def test_omitted_key_is_accepted_and_never_synthesized(self):
        doc = dict(self.role)
        del doc['runtime_package']
        before = copy.deepcopy(doc)
        out = validate_repository_role(doc)
        self.assertNotIn('runtime_package', out)
        self.assertIsNone(out.get('runtime_package'))
        self.assertEqual(doc, before)
        self.assertIsNot(out, doc)
        self.assertEqual(out, doc)

    def test_explicit_null_is_accepted_and_preserved_as_present(self):
        doc = dict(self.role, runtime_package=None)
        before = copy.deepcopy(doc)
        out = validate_repository_role(doc)
        self.assertIn('runtime_package', out)
        self.assertIsNone(out['runtime_package'])
        self.assertEqual(doc, before)
        self.assertIsNot(out, doc)

    def test_string_accepted_and_other_types_refused(self):
        self.assertEqual(validate_repository_role(dict(self.role, runtime_package='pkg'))['runtime_package'], 'pkg')
        self.assertEqual(validate_repository_role(dict(self.role, runtime_package=''))['runtime_package'], '')
        for bad in (1, 1.5, True, ['a'], {'a': 1}):
            with self.subTest(value=repr(bad)):
                with self.assertRaisesRegex(ContractError, 'runtime_package must be string or null'):
                    validate_repository_role(dict(self.role, runtime_package=bad))

    def test_returned_object_is_a_distinct_shallow_copy(self):
        out = validate_repository_role(self.role)
        self.assertIsNot(out, self.role)
        self.assertEqual(out, self.role)
        self.assertIs(out['canonical_authority_for'], self.role['canonical_authority_for'])


class CanonicalProducerExamples(unittest.TestCase):
    def test_every_example_declares_the_literal_string_1_0(self):
        for name in EXAMPLE_VALIDATORS:
            with self.subTest(example=name):
                doc = example(name)
                self.assertIs(type(doc['schema_version']), str)
                self.assertEqual(doc['schema_version'], '1.0')

    def test_every_example_carries_each_required_key_with_its_declared_facet(self):
        for name in EXAMPLE_VALIDATORS:
            doc = example(name)
            profile = schema_profile(name)
            for key in profile['required']:
                with self.subTest(example=name, key=key):
                    self.assertIn(key, doc)
                    self.assertTrue(has_declared_type(doc[key], profile['properties'][key]), key)

    def test_repository_role_example_writes_runtime_package_explicitly(self):
        doc = example('repository_role.json')
        self.assertIn('runtime_package', doc)
        self.assertIs(type(doc['runtime_package']), str)
        self.assertTrue(doc['runtime_package'])

    def test_every_example_passes_its_validator_in_default_mode(self):
        for name, validator in EXAMPLE_VALIDATORS.items():
            with self.subTest(example=name):
                doc = example(name)
                before = copy.deepcopy(doc)
                self.assertEqual(validator(doc), doc)
                self.assertEqual(doc, before)


class SchemaFacetsPinned(unittest.TestCase):
    def test_all_five_schema_version_declarations_are_const_1_0(self):
        declarations = [load(SCHEMAS / (name + '.schema.json'))['properties']['schema_version'] for name in ('repository_role', 'source_manifest', 'workspace_snapshot')]
        declarations += [branch['properties']['schema_version'] for branch in load(SCHEMAS / 'source_ref.schema.json')['oneOf']]
        self.assertEqual(len(declarations), 5)
        for declaration in declarations:
            self.assertEqual(declaration, {'const': '1.0'})
        self.assertEqual(parse_major('1.0'), 1)

    def test_repository_role_runtime_package_is_required_string_or_null(self):
        schema = load(SCHEMAS / 'repository_role.schema.json')
        self.assertIn('runtime_package', schema['required'])
        self.assertEqual(schema['properties']['runtime_package'], {'type': ['string', 'null']})
        nullable = [key for key, prop in schema['properties'].items() if isinstance(prop.get('type'), list) and 'null' in prop['type']]
        self.assertEqual(nullable, ['runtime_package'])

    def test_required_lists_are_pinned(self):
        expected = {
            'repository_role': ['schema_version', 'repository', 'role_id', 'canonical_authority_for', 'derived_consumers', 'visibility', 'runtime_package', 'scientific_status_authority'],
            'source_manifest': ['schema_version', 'distribution', 'version', 'repository', 'commit', 'scientific_status_authority', 'files'],
            'workspace_snapshot': ['schema_version', 'snapshot', 'repositories'],
        }
        for name, required in expected.items():
            with self.subTest(schema=name):
                self.assertEqual(load(SCHEMAS / (name + '.schema.json'))['required'], required)
        branches = load(SCHEMAS / 'source_ref.schema.json')['oneOf']
        self.assertEqual([b['properties']['kind']['const'] for b in branches], ['git', 'external'])
        self.assertEqual(branches[0]['required'], ['schema_version', 'kind', 'repository', 'commit', 'path', 'git_blob_sha1', 'sha256', 'size_bytes', 'role', 'visibility'])
        self.assertEqual(branches[1]['required'], ['schema_version', 'kind', 'provider', 'source_id', 'sha256', 'size_bytes', 'monitorability', 'role', 'visibility'])

    def test_sandbox_membership_of_repository_enums_is_pinned(self):
        git_branch = load(SCHEMAS / 'source_ref.schema.json')['oneOf'][0]
        self.assertNotIn(SANDBOX, git_branch['properties']['repository']['enum'])
        self.assertNotIn(SANDBOX, load(SCHEMAS / 'source_manifest.schema.json')['properties']['repository']['enum'])
        self.assertIn(SANDBOX, load(SCHEMAS / 'workspace_snapshot.schema.json')['properties']['repositories']['items']['properties']['repository']['enum'])
        self.assertIn(SANDBOX, load(SCHEMAS / 'repository_role.schema.json')['properties']['repository']['enum'])


if __name__ == '__main__':
    unittest.main()
