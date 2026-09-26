from __future__ import annotations
import json
import unittest
from pathlib import Path
from tools.contract_validation import ContractError, validate_repository_role, validate_source_manifest, validate_source_ref, validate_workspace_snapshot
ROOT=Path(__file__).resolve().parents[1]

class SourceContracts(unittest.TestCase):
    def test_git_source_ref_requires_immutable_identity(self):
        row={'schema_version':'1.0','kind':'git','repository':'d6g8k5htny-coder/Math-','commit':'1'*40,'path':'frontiers/x/PROOF.md','git_blob_sha1':'2'*40,'sha256':'3'*64,'size_bytes':10,'role':'proof','visibility':'public'}
        self.assertEqual(validate_source_ref(row)['repository'],row['repository'])
        with self.assertRaises(ContractError): validate_source_ref(dict(row,commit='main'))
    def test_public_git_source_ref_rejects_sandbox(self):
        row={'schema_version':'1.0','kind':'git','repository':'d6g8k5htny-coder/sandbox','commit':'1'*40,'path':'private.txt','git_blob_sha1':'2'*40,'sha256':'3'*64,'size_bytes':1,'role':'proof','visibility':'public'}
        with self.assertRaises(ContractError): validate_source_ref(row)
    def test_external_frozen_source_ref(self):
        row={'schema_version':'1.0','kind':'external','provider':'google-drive','source_id':'abc','sha256':'4'*64,'size_bytes':12,'monitorability':'external-frozen','role':'historical-source','visibility':'public'}
        self.assertEqual(validate_source_ref(row)['provider'],'google-drive')
    def test_unknown_major_version_fails_closed(self):
        row={'schema_version':'2.0','kind':'external','provider':'google-drive','source_id':'abc','sha256':'4'*64,'size_bytes':12,'monitorability':'external-frozen','role':'historical-source','visibility':'public'}
        with self.assertRaises(ContractError): validate_source_ref(row)
    def test_repository_role_has_single_machine_shape(self):
        row={'schema_version':'1.0','repository':'d6g8k5htny-coder/Math-','role_id':'math','canonical_authority_for':['proofs'],'derived_consumers':['main','meta-framework'],'visibility':'public','runtime_package':'universal-law-math','scientific_status_authority':True}
        self.assertEqual(validate_repository_role(row)['role_id'],'math')
    def test_source_manifest_rejects_private_path_and_status_authority(self):
        base={'schema_version':'1.0','distribution':'universal-law-query','version':'0.1.0','repository':'d6g8k5htny-coder/query-','commit':'a'*40,'scientific_status_authority':False,'files':[{'path':'src/universal_law_query/__init__.py','sha256':'b'*64,'bytes':1}]}
        self.assertEqual(validate_source_manifest(base)['distribution'],'universal-law-query')
        bad=json.loads(json.dumps(base));bad['files'][0]['path']='sandbox/private.py'
        with self.assertRaises(ContractError): validate_source_manifest(bad)
        with self.assertRaises(ContractError): validate_source_manifest(dict(base,scientific_status_authority=True))
    def test_workspace_snapshot_rejects_duplicate_repo_and_mutable_ref(self):
        base={'schema_version':'1.0','snapshot':'workspace-snapshot-1','repositories':[{'repository':'d6g8k5htny-coder/main','commit':'1'*40},{'repository':'d6g8k5htny-coder/Math-','commit':'2'*40}]}
        self.assertEqual(len(validate_workspace_snapshot(base)['repositories']),2)
        dup=json.loads(json.dumps(base));dup['repositories'].append(dict(dup['repositories'][0]))
        with self.assertRaises(ContractError): validate_workspace_snapshot(dup)
        mutable=json.loads(json.dumps(base));mutable['repositories'][0]['commit']='main'
        with self.assertRaises(ContractError): validate_workspace_snapshot(mutable)
    def test_schema_documents_exist_and_are_json(self):
        for name in ('source_ref.schema.json','repository_role.schema.json','source_manifest.schema.json','workspace_snapshot.schema.json'):
            path=ROOT/'schemas'/name;self.assertTrue(path.is_file(),name);self.assertIsInstance(json.loads(path.read_text()),dict)
if __name__=='__main__':unittest.main()
