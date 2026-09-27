from __future__ import annotations
import argparse,json,sys
from pathlib import Path,PurePosixPath
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from tools.contract_validation import ContractError, HEX40, HEX64, REPO_NAMES, validate_source_manifest, validate_workspace_snapshot

REQUIRED_REPOS=set(REPO_NAMES)
FORBIDDEN_ARTIFACT_FIELDS={'status','grade','classification','disposition','lemma_closed','controlling','prizes_solved','independence_credit','scientific_status','promotion_permission'}
FORBIDDEN_ARCH_OWNS={'status','grade','classification','controlling','terminality','reverse_impact_revalidation','promotion_permission','lemma_closed','prizes_solved','independence_credit'}

def _load_json(path:Path): return json.loads(path.read_text(encoding='utf-8'))
def _safe_registry_path(text):
    if not isinstance(text,str) or not text or '\\' in text or ':' in text: return False
    p=PurePosixPath(text)
    return not p.is_absolute() and '..' not in p.parts and str(p)==text and all(x.casefold()!='sandbox' for x in p.parts)
def _contains_status_authority(value):
    if isinstance(value,dict):
        if value.get('scientific_status_authority') is True: return True
        return any(_contains_status_authority(v) for v in value.values())
    if isinstance(value,list): return any(_contains_status_authority(v) for v in value)
    return False

def _check_authority_map(data,violations):
    if not isinstance(data,dict): violations.append('authority map must be an object');return
    authorities=data.get('authorities');required=data.get('required_authority_ids');pkg=data.get('this_package')
    if not isinstance(authorities,dict) or not isinstance(required,list) or not isinstance(pkg,dict): violations.append('authority map structure invalid');return
    pkg_id=pkg.get('id');known=set(authorities)
    if isinstance(pkg_id,str) and pkg_id: known.add(pkg_id)
    if any(not isinstance(x,str) or x not in known for x in required): violations.append('authority map required_authority_ids unresolved')
    for aid,row in authorities.items():
        if not isinstance(row,dict) or row.get('id')!=aid or not isinstance(row.get('owns'),list) or any(not isinstance(x,str) for x in row.get('owns',[])): violations.append('authority record invalid: '+str(aid))
    owns=pkg.get('owns');never=pkg.get('never_writes')
    if not isinstance(owns,list) or any(not isinstance(x,str) for x in owns): violations.append('architecture authority owns must be a string list');owns=[]
    if not isinstance(never,list) or any(not isinstance(x,str) for x in never): violations.append('architecture never_writes must be a string list');never=[]
    bad=set(owns)&FORBIDDEN_ARCH_OWNS
    if bad: violations.append('architecture authority overreach: '+','.join(sorted(bad)))
    required_never={'status','grade','classification','controlling','lemma_closed','prizes_solved','independence_credit'}
    missing=required_never-set(never)
    if missing: violations.append('architecture never_writes missing: '+','.join(sorted(missing)))

def check_workspace(root:Path)->dict:
    root=Path(root).resolve();violations=[];checked=[];regpath=root/'meta-framework/registry.json'
    if not regpath.is_file(): return {'ok':False,'repositories_checked':checked,'violations':['missing meta-framework/registry.json'],'scientific_effect':'NONE'}
    try:registry=_load_json(regpath)
    except Exception as exc: violations.append('registry parse error: '+str(exc));registry={}
    if type(registry.get('schema_version')) is not int or registry.get('schema_version')!=1: violations.append('registry schema_version must equal integer 1')
    repos=registry.get('repositories') if isinstance(registry,dict) else None
    if not isinstance(repos,dict): violations.append('repository map required');repos={}
    for name,row in repos.items():
        checked.append(name)
        if name not in REQUIRED_REPOS: violations.append('unexpected repository key: '+str(name))
        if not isinstance(row,dict) or row.get('full_name')!='d6g8k5htny-coder/'+name: violations.append('unexpected owner for repository: '+str(name))
        expected='private' if name=='sandbox' else 'public'
        if not isinstance(row,dict) or row.get('visibility')!=expected: violations.append('visibility mismatch for repository: '+str(name))
        if not (root/name).is_dir(): violations.append('missing sibling repository directory: '+str(name))
    for name in sorted(REQUIRED_REPOS-set(repos)): violations.append('missing repository role: '+name)
    if registry.get('scientific_status_authority') is not False: violations.append('registry cannot be scientific-status authority')
    artifacts=registry.get('artifacts')
    if not isinstance(artifacts,list): violations.append('registry artifacts must be a list');artifacts=[]
    for idx,row in enumerate(artifacts):
        if not isinstance(row,dict): violations.append(f'artifact {idx} must be an object');continue
        bad=FORBIDDEN_ARTIFACT_FIELDS & set(row)
        if bad: violations.append('forbidden scientific field in registry artifact: '+','.join(sorted(bad)))
        repo=row.get('repository')
        if repo not in repos: violations.append('artifact repository unknown: '+str(repo))
        elif repo=='sandbox' or (isinstance(repos.get(repo),dict) and repos[repo].get('visibility')!='public') or row.get('visibility')!='public': violations.append('artifact sandbox/private visibility refused: '+str(repo))
        if not HEX40.fullmatch(str(row.get('commit',''))): violations.append('artifact exact commit required: '+str(row.get('key')))
        if not _safe_registry_path(row.get('path')): violations.append('artifact unsafe/sandbox path: '+str(row.get('key')))
        if not HEX64.fullmatch(str(row.get('sha256',''))): violations.append('artifact exact sha256 required: '+str(row.get('key')))
        if type(row.get('bytes')) is not int or row.get('bytes',-1)<0: violations.append('artifact bytes invalid: '+str(row.get('key')))
    for name in REQUIRED_REPOS:
        manifest=root/name/'SOURCE_MANIFEST.json'
        if manifest.is_file():
            try: validate_source_manifest(_load_json(manifest))
            except (ContractError,ValueError,TypeError,KeyError) as exc: violations.append(f'{name}/SOURCE_MANIFEST.json: {exc}')
    snapshot=root/'meta-framework/WORKSPACE_SNAPSHOT.json'
    if snapshot.is_file():
        try: validate_workspace_snapshot(_load_json(snapshot))
        except (ContractError,ValueError,TypeError,KeyError) as exc: violations.append('workspace snapshot: '+str(exc))
    generated=root/'meta-framework/generated'
    if generated.is_dir():
        for path in generated.glob('**/*.json'):
            try:data=_load_json(path)
            except Exception as exc: violations.append('generated JSON parse error: '+str(path.relative_to(root))+': '+str(exc));continue
            if _contains_status_authority(data): violations.append('generated scientific-status authority: '+str(path.relative_to(root)))
    authority=root/'main/architecture/scientific_state/v1/AUTHORITY_MAP.json'
    if not authority.is_file(): violations.append('missing main authority map')
    else:
        try:_check_authority_map(_load_json(authority),violations)
        except Exception as exc: violations.append('authority map validation error: '+str(exc))
    return {'ok':not violations,'repositories_checked':sorted(set(checked)),'violations':violations,'scientific_effect':'NONE'}

def main(argv=None)->int:
    p=argparse.ArgumentParser(description='Read-only cross-repository architecture conformance checker');p.add_argument('--workspace',required=True,type=Path);args=p.parse_args(argv);report=check_workspace(args.workspace);print(json.dumps(report,indent=2,sort_keys=True));return 0 if report['ok'] else 2
if __name__=='__main__':raise SystemExit(main())
