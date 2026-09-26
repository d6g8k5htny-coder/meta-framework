from __future__ import annotations
import re
from pathlib import PurePosixPath
from typing import Any

class ContractError(ValueError):
    pass

HEX40=re.compile(r'^[0-9a-f]{40}$')
HEX64=re.compile(r'^[0-9a-f]{64}$')
VER=re.compile(r'^([0-9]+)\\.([0-9]+)$')

def parse_major(version: str) -> int:
    if not isinstance(version,str):
        raise ContractError('schema_version must be a string')
    m=VER.fullmatch(version)
    if not m:
        raise ContractError('invalid schema_version')
    major=int(m.group(1))
    if major!=1:
        raise ContractError('unsupported schema major')
    return major

def _copy(data: Any) -> dict:
    if not isinstance(data,dict):
        raise ContractError('contract object required')
    return dict(data)

def _safe_path(text: Any) -> str:
    if not isinstance(text,str) or not text or '\\\\' in text or ':' in text:
        raise ContractError('unsafe path')
    p=PurePosixPath(text)
    if p.is_absolute() or '..' in p.parts or str(p)!=text:
        raise ContractError('unsafe path')
    if 'sandbox' in p.parts:
        raise ContractError('private sandbox path refused')
    return text

def _nonempty(value: Any, field: str) -> str:
    if not isinstance(value,str) or not value.strip():
        raise ContractError(field+' required')
    return value

def _size(value: Any) -> int:
    if type(value) is not int or value < 0:
        raise ContractError('invalid size_bytes')
    return value

def _visibility(value: Any) -> str:
    if value not in {'public','private'}:
        raise ContractError('invalid visibility')
    return value

def validate_source_ref(data: dict, *, public: bool=True) -> dict:
    row=_copy(data); parse_major(row.get('schema_version'))
    kind=row.get('kind'); _nonempty(row.get('role'),'role'); vis=_visibility(row.get('visibility'))
    if public and vis!='public': raise ContractError('public contract requires public visibility')
    if kind=='git':
        repo=_nonempty(row.get('repository'),'repository')
        if not repo.startswith('d6g8k5htny-coder/'):
            raise ContractError('unexpected repository owner')
        if public and repo=='d6g8k5htny-coder/sandbox':
            raise ContractError('private sandbox source refused')
        if not HEX40.fullmatch(str(row.get('commit',''))): raise ContractError('exact commit required')
        _safe_path(row.get('path'))
        if not HEX40.fullmatch(str(row.get('git_blob_sha1',''))): raise ContractError('exact blob required')
        if not HEX64.fullmatch(str(row.get('sha256',''))): raise ContractError('exact sha256 required')
        _size(row.get('size_bytes'))
    elif kind=='external':
        _nonempty(row.get('provider'),'provider'); _nonempty(row.get('source_id'),'source_id')
        if not HEX64.fullmatch(str(row.get('sha256',''))): raise ContractError('exact sha256 required')
        _size(row.get('size_bytes'))
        if row.get('monitorability') not in {'external-frozen','external-live'}:
            raise ContractError('invalid monitorability')
    else:
        raise ContractError('unknown source kind')
    return row

def _string_list(value: Any, field: str) -> list[str]:
    if not isinstance(value,list) or any(not isinstance(x,str) or not x for x in value) or len(value)!=len(set(value)):
        raise ContractError(field+' must be a unique string list')
    return list(value)

def validate_repository_role(data: dict) -> dict:
    row=_copy(data); parse_major(row.get('schema_version'))
    repo=_nonempty(row.get('repository'),'repository')
    if not repo.startswith('d6g8k5htny-coder/'): raise ContractError('unexpected repository owner')
    _nonempty(row.get('role_id'),'role_id')
    _string_list(row.get('canonical_authority_for'),'canonical_authority_for')
    _string_list(row.get('derived_consumers'),'derived_consumers')
    _visibility(row.get('visibility'))
    if row.get('runtime_package') is not None and not isinstance(row.get('runtime_package'),str):
        raise ContractError('runtime_package must be string or null')
    if type(row.get('scientific_status_authority')) is not bool:
        raise ContractError('scientific_status_authority must be boolean')
    return row

def validate_source_manifest(data: dict) -> dict:
    row=_copy(data); parse_major(row.get('schema_version'))
    _nonempty(row.get('distribution'),'distribution'); _nonempty(row.get('version'),'version')
    repo=_nonempty(row.get('repository'),'repository')
    if not repo.startswith('d6g8k5htny-coder/') or repo=='d6g8k5htny-coder/sandbox':
        raise ContractError('public source manifest repository refused')
    if not HEX40.fullmatch(str(row.get('commit',''))): raise ContractError('exact commit required')
    if row.get('scientific_status_authority') is not False:
        raise ContractError('source manifest cannot be scientific-status authority')
    files=row.get('files')
    if not isinstance(files,list): raise ContractError('files list required')
    seen=set()
    for item in files:
        if not isinstance(item,dict): raise ContractError('file entry must be object')
        path=_safe_path(item.get('path'))
        if path in seen: raise ContractError('duplicate manifest path')
        seen.add(path)
        if not HEX64.fullmatch(str(item.get('sha256',''))): raise ContractError('exact sha256 required')
        value=item.get('bytes')
        if type(value) is not int or value<0: raise ContractError('invalid bytes')
    return row

def validate_workspace_snapshot(data: dict) -> dict:
    row=_copy(data); parse_major(row.get('schema_version')); _nonempty(row.get('snapshot'),'snapshot')
    repos=row.get('repositories')
    if not isinstance(repos,list) or not repos: raise ContractError('repositories list required')
    seen=set()
    for item in repos:
        if not isinstance(item,dict): raise ContractError('repository snapshot entry must be object')
        repo=_nonempty(item.get('repository'),'repository')
        if not repo.startswith('d6g8k5htny-coder/'): raise ContractError('unexpected repository owner')
        if repo in seen: raise ContractError('duplicate repository')
        seen.add(repo)
        if not HEX40.fullmatch(str(item.get('commit',''))): raise ContractError('exact commit required')
    return row
