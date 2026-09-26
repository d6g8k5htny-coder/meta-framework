from __future__ import annotations
import json,tempfile,unittest
from pathlib import Path
from tools.architecture_conformance import check_workspace
REPOS=['Math-','google-drive','governance-','main','meta-framework','query-','sandbox','trial']

class ArchitectureConformance(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.root=Path(self.tmp.name)
        for name in REPOS:(self.root/name).mkdir(parents=True)
        registry={'schema_version':1,'scientific_status_authority':False,'repositories':{name:{'full_name':'d6g8k5htny-coder/'+name,'role':name,'visibility':'private' if name=='sandbox' else 'public'} for name in REPOS},'artifacts':[]}
        (self.root/'meta-framework/registry.json').write_text(json.dumps(registry))
    def run_check(self):return check_workspace(self.root)
    def test_valid_legacy_workspace_does_not_require_src_yet(self):
        report=self.run_check();self.assertTrue(report['ok'],report);self.assertEqual(set(report['repositories_checked']),set(REPOS));self.assertEqual(report['scientific_effect'],'NONE')
    def test_wrong_owner_is_violation(self):
        p=self.root/'meta-framework/registry.json';data=json.loads(p.read_text());data['repositories']['Math-']['full_name']='other/Math-';p.write_text(json.dumps(data))
        report=self.run_check();self.assertFalse(report['ok']);self.assertTrue(any('unexpected owner' in x for x in report['violations']))
    def test_registry_scientific_status_fields_are_refused(self):
        p=self.root/'meta-framework/registry.json';data=json.loads(p.read_text());data['artifacts']=[{'key':'x','repository':'Math-','path':'x','commit':'1'*40,'sha256':'2'*64,'bytes':1,'scope':'x','visibility':'public','status':'ACCEPT'}];p.write_text(json.dumps(data))
        report=self.run_check();self.assertFalse(report['ok']);self.assertTrue(any('forbidden scientific field' in x for x in report['violations']))
    def test_public_source_manifest_sandbox_path_is_violation(self):
        manifest={'schema_version':'1.0','distribution':'x','version':'0.1.0','repository':'d6g8k5htny-coder/Math-','commit':'1'*40,'scientific_status_authority':False,'files':[{'path':'sandbox/private.py','sha256':'2'*64,'bytes':1}]}
        (self.root/'Math-/SOURCE_MANIFEST.json').write_text(json.dumps(manifest));report=self.run_check();self.assertFalse(report['ok']);self.assertTrue(any('sandbox' in x for x in report['violations']))
    def test_mutable_workspace_snapshot_is_violation(self):
        snap={'schema_version':'1.0','snapshot':'x','repositories':[{'repository':'d6g8k5htny-coder/main','commit':'main'}]}
        (self.root/'meta-framework/WORKSPACE_SNAPSHOT.json').write_text(json.dumps(snap));report=self.run_check();self.assertFalse(report['ok']);self.assertTrue(any('exact commit' in x for x in report['violations']))
    def test_generated_status_authority_is_violation(self):
        g=self.root/'meta-framework/generated';g.mkdir();(g/'X.json').write_text(json.dumps({'scientific_status_authority':True}))
        report=self.run_check();self.assertFalse(report['ok']);self.assertTrue(any('generated scientific-status authority' in x for x in report['violations']))
    def test_authority_map_cannot_give_architecture_promotion_fields(self):
        p=self.root/'main/architecture/scientific_state/v1';p.mkdir(parents=True);(p/'AUTHORITY_MAP.json').write_text(json.dumps({'this_package':{'owns':['schema_contract','classification']}}))
        report=self.run_check();self.assertFalse(report['ok']);self.assertTrue(any('architecture authority overreach' in x for x in report['violations']))
if __name__=='__main__':unittest.main()
