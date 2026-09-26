from __future__ import annotations
import json,unittest
from pathlib import Path
from tools.contract_validation import ContractError,parse_major,validate_repository_role,validate_source_manifest,validate_source_ref,validate_workspace_snapshot
ROOT=Path(__file__).resolve().parents[1]
REPOS=['Math-','google-drive','governance-','main','meta-framework','query-','sandbox','trial']

def git_ref(**changes):
    row={'schema_version':'1.0','kind':'git','repository':'d6g8k5htny-coder/Math-','commit':'1'*40,'path':'frontiers/x/PROOF.md','git_blob_sha1':'2'*40,'sha256':'3'*64,'size_bytes':10,'role':'proof','visibility':'public'}
    row.update(changes);return row

class SourceContracts(unittest.TestCase):
    def test_version_1_0_and_unknown_major(self):
        self.assertEqual(parse_major('1.0'),1)
        with self.assertRaisesRegex(ContractError,'unsupported schema major'): parse_major('2.0')
    def test_git_source_ref_requires_immutable_identity(self):
        self.assertEqual(validate_source_ref(git_ref())['repository'],'d6g8k5htny-coder/Math-')
        with self.assertRaisesRegex(ContractError,'exact commit'): validate_source_ref(git_ref(commit='main'))
    def test_public_git_source_ref_rejects_sandbox_and_noncanonical_repo(self):
        for repo in ['d6g8k5htny-coder/sandbox','d6g8k5htny-coder/sandbox ','d6g8k5htny-coder/Sandbox','d6g8k5htny-coder/sandbox.git','d6g8k5htny-coder/../evil/Math-']:
            with self.subTest(repo=repo):
                with self.assertRaises(ContractError): validate_source_ref(git_ref(repository=repo))
    def test_source_ref_rejects_case_variant_sandbox_path(self):
        with self.assertRaisesRegex(ContractError,'sandbox'): validate_source_ref(git_ref(path='Sandbox/private.txt'))
    def test_external_frozen_source_ref(self):
        row={'schema_version':'1.0','kind':'external','provider':'google-drive','source_id':'abc','sha256':'4'*64,'size_bytes':12,'monitorability':'external-frozen','role':'historical-source','visibility':'public'}
        self.assertEqual(validate_source_ref(row)['provider'],'google-drive')
    def test_repository_role_is_routing_not_scientific_status(self):
        row={'schema_version':'1.0','repository':'d6g8k5htny-coder/Math-','role_id':'math','canonical_authority_for':['proofs'],'derived_consumers':['main','meta-framework'],'visibility':'public','runtime_package':'universal-law-math','scientific_status_authority':False}
        self.assertEqual(validate_repository_role(row)['role_id'],'math')
        with self.assertRaisesRegex(ContractError,'scientific-status'): validate_repository_role(dict(row,scientific_status_authority=True))
    def test_source_manifest_rejects_private_path_and_status_authority(self):
        base={'schema_version':'1.0','distribution':'universal-law-query','version':'0.1.0','repository':'d6g8k5htny-coder/query-','commit':'a'*40,'scientific_status_authority':False,'files':[{'path':'src/universal_law_query/__init__.py','sha256':'b'*64,'bytes':1}]}
        self.assertEqual(validate_source_manifest(base)['distribution'],'universal-law-query')
        bad=json.loads(json.dumps(base));bad['files'][0]['path']='sandbox/private.py'
        with self.assertRaises(ContractError): validate_source_manifest(bad)
        with self.assertRaises(ContractError): validate_source_manifest(dict(base,scientific_status_authority=True))
        with self.assertRaises(ContractError): validate_source_manifest(dict(base,repository='d6g8k5htny-coder/sandbox '))
    def test_workspace_snapshot_requires_exact_eight_repositories(self):
        base={'schema_version':'1.0','snapshot':'workspace-snapshot-1','repositories':[{'repository':'d6g8k5htny-coder/'+name,'commit':f'{i:x}'*40} for i,name in enumerate(REPOS,1)]}
        self.assertEqual(len(validate_workspace_snapshot(base)['repositories']),8)
        with self.assertRaises(ContractError): validate_workspace_snapshot(dict(base,repositories=base['repositories'][:-1]))
        dup=json.loads(json.dumps(base));dup['repositories'][-1]=dict(dup['repositories'][0])
        with self.assertRaises(ContractError): validate_workspace_snapshot(dup)
        mutable=json.loads(json.dumps(base));mutable['repositories'][0]['ref']='main'
        with self.assertRaisesRegex(ContractError,'mutable'): validate_workspace_snapshot(mutable)
        mutable=json.loads(json.dumps(base));mutable['repositories'][0]['commit']='main'
        with self.assertRaisesRegex(ContractError,'exact commit'): validate_workspace_snapshot(mutable)
    def test_schema_documents_and_examples_validate(self):
        validators={'source_ref.git.json':lambda d:validate_source_ref(d),'source_ref.drive.json':lambda d:validate_source_ref(d),'repository_role.json':validate_repository_role,'source_manifest.json':validate_source_manifest,'workspace_snapshot.json':validate_workspace_snapshot}
        for name in ('source_ref.schema.json','repository_role.schema.json','source_manifest.schema.json','workspace_snapshot.schema.json'): self.assertIsInstance(json.loads((ROOT/'schemas'/name).read_text()),dict)
        for name,validator in validators.items():
            with self.subTest(example=name): validator(json.loads((ROOT/'examples'/name).read_text()))
if __name__=='__main__':unittest.main()
