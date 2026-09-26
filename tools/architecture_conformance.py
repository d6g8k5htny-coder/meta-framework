from __future__ import annotations
import argparse
import json
from pathlib import Path
from tools.contract_validation import ContractError, validate_source_manifest, validate_workspace_snapshot

REQUIRED_REPOS={'Math-','google-drive','governance-','main','meta-framework','query-','sandbox','trial'}
FORBIDDEN_ARTIFACT_FIELDS={'status','grade','classification','disposition'}
FORBIDDEN_ARCH_OWNS={'classification','controlling','terminality','reverse_impact_revalidation','promotion_permission'}

def _load_json(path: Path):
    return json.loads(path.read_text(encoding='utf-8'))

def check_workspace(root: Path) -> dict:
    root=Path(root).resolve(); violations=[]; checked=[]
    regpath=root/'meta-framework/registry.json'
    if not regpath.is_file():
        violations.append('missing meta-framework/registry.json')
        return {'ok':False,'repositories_checked':checked,'violations':violations,'scientific_effect':'NONE'}
    try: registry=_load_json(regpath)
    except Exception as exc:
        violations.append('registry parse error: '+str(exc)); registry={}
    repos=registry.get('repositories') if isinstance(registry,dict) else None
    if not isinstance(repos,dict):
        violations.append('repository map required'); repos={}
    for name,row in repos.items():
        checked.append(name)
        if name not in REQUIRED_REPOS: violations.append('unexpected repository key: '+name)
        if not isinstance(row,dict) or row.get('full_name')!='d6g8k5htny-coder/'+name:
            violations.append('unexpected owner for repository: '+name)
        expected='private' if name=='sandbox' else 'public'
        if not isinstance(row,dict) or row.get('visibility')!=expected:
            violations.append('visibility mismatch for repository: '+name)
        if not (root/name).is_dir(): violations.append('missing sibling repository directory: '+name)
    for name in sorted(REQUIRED_REPOS-set(repos)): violations.append('missing repository role: '+name)
    if registry.get('scientific_status_authority') is not False:
        violations.append('registry cannot be scientific-status authority')
    for row in registry.get('artifacts') or []:
        if isinstance(row,dict):
            bad=FORBIDDEN_ARTIFACT_FIELDS & set(row)
            if bad: violations.append('forbidden scientific field in registry artifact: '+','.join(sorted(bad)))
    for name in REQUIRED_REPOS:
        manifest=root/name/'SOURCE_MANIFEST.json'
        if manifest.is_file():
            try: validate_source_manifest(_load_json(manifest))
            except (ContractError,ValueError,TypeError,KeyError) as exc:
                violations.append(f'{name}/SOURCE_MANIFEST.json: {exc}')
    snapshot=root/'meta-framework/WORKSPACE_SNAPSHOT.json'
    if snapshot.is_file():
        try: validate_workspace_snapshot(_load_json(snapshot))
        except (ContractError,ValueError,TypeError,KeyError) as exc:
            violations.append('workspace snapshot: '+str(exc))
    generated=root/'meta-framework/generated'
    if generated.is_dir():
        for path in generated.glob('**/*.json'):
            try: data=_load_json(path)
            except Exception as exc:
                violations.append('generated JSON parse error: '+str(path.relative_to(root))+': '+str(exc)); continue
            if isinstance(data,dict) and data.get('scientific_status_authority') is True:
                violations.append('generated scientific-status authority: '+str(path.relative_to(root)))
    authority=root/'main/architecture/scientific_state/v1/AUTHORITY_MAP.json'
    if authority.is_file():
        try: data=_load_json(authority)
        except Exception as exc: violations.append('authority map parse error: '+str(exc)); data={}
        owns=((data.get('this_package') or {}).get('owns') or []) if isinstance(data,dict) else []
        bad=set(owns)&FORBIDDEN_ARCH_OWNS
        if bad: violations.append('architecture authority overreach: '+','.join(sorted(bad)))
    return {'ok':not violations,'repositories_checked':sorted(set(checked)),'violations':violations,'scientific_effect':'NONE'}

def main(argv=None) -> int:
    p=argparse.ArgumentParser(description='Read-only cross-repository architecture conformance checker')
    p.add_argument('--workspace',required=True,type=Path)
    args=p.parse_args(argv); report=check_workspace(args.workspace)
    print(json.dumps(report,indent=2,sort_keys=True))
    return 0 if report['ok'] else 2

if __name__=='__main__': raise SystemExit(main())
