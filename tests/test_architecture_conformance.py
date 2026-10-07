from __future__ import annotations
import json,subprocess,sys,tempfile,unittest
from pathlib import Path
from tools.architecture_conformance import check_workspace
REPOS=['Math-','google-drive','governance-','main','meta-framework','query-','sandbox','trial']

def valid_authority():
    return {'required_authority_ids':['claims_firewall','scientific_state_architecture'],'authorities':{'claims_firewall':{'id':'claims_firewall','owns':['grade']}},'this_package':{'id':'scientific_state_architecture','owns':['schema_contract'],'never_writes':['status','grade','classification','controlling','lemma_closed','prizes_solved','independence_credit']}}
class ArchitectureConformance(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.root=Path(self.tmp.name)
        for name in REPOS:(self.root/name).mkdir(parents=True)
        registry={'schema_version':1,'scientific_status_authority':False,'repositories':{name:{'full_name':'d6g8k5htny-coder/'+name,'role':name,'visibility':'private' if name=='sandbox' else 'public'} for name in REPOS},'artifacts':[]}
        (self.root/'meta-framework/registry.json').write_text(json.dumps(registry))
        a=self.root/'main/architecture/scientific_state/v1';a.mkdir(parents=True);(a/'AUTHORITY_MAP.json').write_text(json.dumps(valid_authority()))
    def run_check(self):return check_workspace(self.root)
    def mutate_registry(self,fn):
        p=self.root/'meta-framework/registry.json';d=json.loads(p.read_text());fn(d);p.write_text(json.dumps(d))
    def test_valid_legacy_workspace_does_not_require_src_yet(self):
        report=self.run_check();self.assertTrue(report['ok'],report);self.assertEqual(set(report['repositories_checked']),set(REPOS));self.assertEqual(report['scientific_effect'],'NONE')
    def test_wrong_owner_is_violation(self):
        self.mutate_registry(lambda d:d['repositories']['Math-'].__setitem__('full_name','other/Math-'));self.assertFalse(self.run_check()['ok'])
    def test_registry_scientific_status_fields_and_private_artifacts_are_refused(self):
        def mutate(d):d['artifacts']=[None,{'key':'x','repository':'sandbox','path':'secret/experiment.py','commit':'main','sha256':'2'*64,'bytes':1,'scope':'x','visibility':'private','status':'ACCEPT','lemma_closed':True,'controlling':True,'prizes_solved':True}]
        self.mutate_registry(mutate);r=self.run_check();self.assertFalse(r['ok']);joined='\n'.join(r['violations'])
        for term in ('artifact','sandbox','commit','status','lemma_closed','controlling','prizes_solved'):self.assertIn(term,joined)
    def test_registry_schema_version_is_checked(self):
        self.mutate_registry(lambda d:d.__setitem__('schema_version',99));r=self.run_check();self.assertFalse(r['ok']);self.assertTrue(any('schema_version' in x for x in r['violations']))
    def test_public_source_manifest_sandbox_path_is_violation(self):
        manifest={'schema_version':'1.0','distribution':'x','version':'0.1.0','repository':'d6g8k5htny-coder/Math-','commit':'1'*40,'scientific_status_authority':False,'files':[{'path':'Sandbox/private.py','sha256':'2'*64,'bytes':1}]}
        (self.root/'Math-/SOURCE_MANIFEST.json').write_text(json.dumps(manifest));r=self.run_check();self.assertFalse(r['ok']);self.assertTrue(any('sandbox' in x.lower() for x in r['violations']))
    def test_mutable_workspace_snapshot_is_violation(self):
        rows=[{'repository':'d6g8k5htny-coder/'+name,'commit':f'{i:x}'*40} for i,name in enumerate(REPOS,1)];rows[0]['ref']='main'
        (self.root/'meta-framework/WORKSPACE_SNAPSHOT.json').write_text(json.dumps({'schema_version':'1.0','snapshot':'x','repositories':rows}));r=self.run_check();self.assertFalse(r['ok']);self.assertTrue(any('snapshot' in x for x in r['violations']))
    def test_nested_generated_status_authority_is_violation(self):
        g=self.root/'meta-framework/generated';g.mkdir();(g/'X.json').write_text(json.dumps({'nested':{'scientific_status_authority':True}}));r=self.run_check();self.assertFalse(r['ok']);self.assertTrue(any('generated scientific-status authority' in x for x in r['violations']))
    def test_authority_map_cannot_give_architecture_promotion_fields_or_be_malformed(self):
        p=self.root/'main/architecture/scientific_state/v1/AUTHORITY_MAP.json';d=valid_authority();d['this_package']['owns'].append('classification');p.write_text(json.dumps(d));r=self.run_check();self.assertFalse(r['ok']);self.assertTrue(any('overreach' in x for x in r['violations']))
        d=valid_authority();d['this_package']['owns']='classification';p.write_text(json.dumps(d));r=self.run_check();self.assertFalse(r['ok']);self.assertTrue(any('authority' in x for x in r['violations']))
    def test_missing_or_unresolved_authority_map_is_violation(self):
        p=self.root/'main/architecture/scientific_state/v1/AUTHORITY_MAP.json';p.unlink();self.assertFalse(self.run_check()['ok'])
        p.parent.mkdir(parents=True,exist_ok=True);d=valid_authority();d['required_authority_ids'].append('missing');p.write_text(json.dumps(d));self.assertFalse(self.run_check()['ok'])
    def test_direct_cli_invocation_works_with_dash_s(self):
        script=Path(__file__).resolve().parents[1]/'tools/architecture_conformance.py';p=subprocess.run([sys.executable,'-B','-S',str(script),'--workspace',str(self.root)],capture_output=True,text=True,timeout=10);self.assertEqual(p.returncode,0,p.stderr);self.assertTrue(json.loads(p.stdout)['ok'])

    def _input_files(self):
        return {str(p.relative_to(self.root)): p.read_bytes()
                for p in self.root.rglob('*') if p.is_file()}

    def _registry_cli(self):
        script = Path(__file__).resolve().parents[1] / 'tools/architecture_conformance.py'
        flags = ['-B', '-S'] + (['-O'] if sys.flags.optimize else [])
        return subprocess.run([sys.executable, *flags, str(script), '--workspace', str(self.root)],
                              capture_output=True, text=True, timeout=10)

    def _assert_registry_cli_report(self, expected):
        result = self._registry_cli()
        self.assertEqual(result.returncode, 0 if expected['ok'] else 2, result.stderr)
        self.assertEqual(result.stderr, '')
        self.assertEqual(result.stdout, json.dumps(expected, indent=2, sort_keys=True) + '\n')

    def test_nonobject_registry_api_is_handled(self):
        expected = {'ok': False, 'repositories_checked': [],
                    'violations': ['registry must be an object'], 'scientific_effect': 'NONE'}
        path = self.root / 'meta-framework/registry.json'
        for raw in (b'[]\n', b'[{"schema_version":1}]\n', b'null\n', b'false\n', b'true\n',
                    b'0\n', b'1.5\n', b'""\n', b'"registry"\n'):
            with self.subTest(raw=raw):
                path.write_bytes(raw)
                before = self._input_files()
                try:
                    report = self.run_check()
                except Exception as exc:
                    self.fail('registry refusal escaped as ' + type(exc).__name__ + ': ' + str(exc))
                self.assertEqual(report, expected)
                self.assertEqual(self._input_files(), before)

    def test_nonobject_registry_cli_is_handled(self):
        expected = {'ok': False, 'repositories_checked': [],
                    'violations': ['registry must be an object'], 'scientific_effect': 'NONE'}
        path = self.root / 'meta-framework/registry.json'
        for raw in (b'[]\n', b'[{"schema_version":1}]\n', b'null\n', b'false\n', b'true\n',
                    b'0\n', b'1.5\n', b'""\n', b'"registry"\n'):
            with self.subTest(raw=raw):
                path.write_bytes(raw)
                before = self._input_files()
                self._assert_registry_cli_report(expected)
                self.assertEqual(self._input_files(), before)

    def test_registry_object_and_parse_boundaries_keep_reports(self):
        path = self.root / 'meta-framework/registry.json'
        valid = path.read_bytes()
        missing_fields = ['registry schema_version must equal integer 1', 'repository map required']
        missing_fields += ['missing repository role: ' + name for name in sorted(REPOS)]
        missing_fields += ['registry cannot be scientific-status authority', 'registry artifacts must be a list']
        try:
            json.loads('{')
        except ValueError as exc:
            parse_error = 'registry parse error: ' + str(exc)
        cases = (
            (valid, {'ok': True, 'repositories_checked': sorted(REPOS),
                     'violations': [], 'scientific_effect': 'NONE'}),
            (b'{}\n', {'ok': False, 'repositories_checked': [],
                       'violations': missing_fields, 'scientific_effect': 'NONE'}),
            (b'{', {'ok': False, 'repositories_checked': [],
                    'violations': [parse_error] + missing_fields, 'scientific_effect': 'NONE'}),
        )
        for raw, expected in cases:
            with self.subTest(raw=raw):
                path.write_bytes(raw)
                before = self._input_files()
                self.assertEqual(self.run_check(), expected)
                self._assert_registry_cli_report(expected)
                self.assertEqual(self._input_files(), before)

    def test_missing_registry_keeps_report(self):
        (self.root / 'meta-framework/registry.json').unlink()
        before = self._input_files()
        expected = {'ok': False, 'repositories_checked': [],
                    'violations': ['missing meta-framework/registry.json'], 'scientific_effect': 'NONE'}
        self.assertEqual(self.run_check(), expected)
        self._assert_registry_cli_report(expected)
        self.assertEqual(self._input_files(), before)

if __name__=='__main__':unittest.main()
