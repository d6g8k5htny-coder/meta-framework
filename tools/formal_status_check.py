"""Fail-closed check of the Layer 1 formalization metadata in registry.json.

Usage:
  python -B -S tools/formal_status_check.py --registry registry.json
  python -B -S tools/formal_status_check.py --registry registry.json --lean-root formal/lean \
      --axiom-report /tmp/axioms.txt

Standard library only; no network; nothing is executed. A passing run means the recorded
formalization statuses are supported by the recorded evidence and byte identities. It is not
theorem acceptance and moves no scientific status (see docs/FORMAL_VERIFICATION.md).
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import sys

STATUS_ORDER = ('none', 'specified', 'proved', 'kernel-checked')
ALIGNMENT_ORDER = ('none', 'open', 'accepted', 'amend_required')
CORE_AXIOMS = ('propext', 'Classical.choice', 'Quot.sound')
SORRY_AXIOM = 'sorryAx'
ASSUMPTIONS_ROOT = 'Side24.Assumptions.'
LEAN_NAME = re.compile(r"[^\s\[\],]+")
EVIDENCE_PREFIX = 'https://github.com/d6g8k5htny-coder/'
THIS_REPOSITORY = 'meta-framework'


class FormalError(ValueError):
    pass


def unique(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            raise FormalError('duplicate JSON key: ' + key)
        out[key] = value
    return out


def load_json(path):
    file = Path(path)
    if file.stat().st_size > 1000000:
        raise FormalError('file exceeds size bound: ' + str(path))
    return json.loads(file.read_text(encoding='utf-8'), object_pairs_hook=unique)


def relative_file(root, text, what):
    if not isinstance(text, str) or not text or '\\' in text or ':' in text:
        raise FormalError(what + ': unsafe path')
    pure = PurePosixPath(text)
    if pure.is_absolute() or '..' in pure.parts or str(pure) != text:
        raise FormalError(what + ': unsafe path')
    path = Path(root)
    for part in pure.parts:
        path = path / part
        if path.is_symlink():
            raise FormalError(what + ': symlink refused: ' + text)
    if not path.is_file():
        raise FormalError(what + ': missing file: ' + text)
    return path


def string_list(value, what, allow_empty=True):
    if not isinstance(value, list) or (not allow_empty and not value):
        raise FormalError(what + ': nonempty list of strings required')
    for item in value:
        if not isinstance(item, str) or not item or not LEAN_NAME.fullmatch(item):
            raise FormalError(what + ': invalid entry')
    if len(set(value)) != len(value):
        raise FormalError(what + ': duplicate entry')
    return value


def check_block(data, root):
    block = data.get('formal_verification')
    if not isinstance(block, dict):
        raise FormalError('formal_verification block required')
    if block.get('scientific_status_authority') is not False:
        raise FormalError('formal_verification must declare scientific_status_authority false')
    vocab = block.get('status_vocabulary')
    if not isinstance(vocab, dict) or set(vocab) != set(STATUS_ORDER):
        raise FormalError('status_vocabulary must describe exactly ' + ', '.join(STATUS_ORDER))
    alignment = block.get('alignment_vocabulary')
    if not isinstance(alignment, dict) or set(alignment) != set(ALIGNMENT_ORDER):
        raise FormalError('alignment_vocabulary must describe exactly ' + ', '.join(ALIGNMENT_ORDER))
    for name, text in list(vocab.items()) + list(alignment.items()):
        if not isinstance(text, str) or not text:
            raise FormalError('vocabulary entry needs a description: ' + name)
    if block.get('allowed_axioms') != list(CORE_AXIOMS):
        raise FormalError('allowed_axioms must be exactly the three core axioms')
    backend = block.get('backend')
    if not isinstance(backend, dict):
        raise FormalError('backend required')
    if backend.get('prover') != 'Lean 4':
        raise FormalError('backend.prover must be Lean 4')
    toolchain = backend.get('toolchain')
    if not isinstance(toolchain, str) or not re.fullmatch(r'leanprover/lean4:v[0-9]+\.[0-9]+\.[0-9]+(-rc[0-9]+)?', toolchain):
        raise FormalError('backend.toolchain must be an exact leanprover/lean4 version')
    rev = backend.get('mathlib_rev')
    if not isinstance(rev, str) or not re.fullmatch('[0-9a-f]{40}', rev):
        raise FormalError('backend.mathlib_rev must be a full commit')
    for key in ('spec', 'glossary', 'alignment_ledger'):
        relative_file(root, block.get(key), 'formal_verification.' + key)
    lean_root = block.get('lean_root')
    if not isinstance(lean_root, str) or not lean_root:
        raise FormalError('formal_verification.lean_root required')
    return block


def check_lean_root(root, lean_root, backend):
    base = Path(root) / lean_root
    if not base.is_dir():
        raise FormalError('lean root missing: ' + lean_root)
    toolchain = relative_file(base, 'lean-toolchain', 'lean root').read_text(encoding='utf-8').strip()
    if toolchain != backend['toolchain']:
        raise FormalError('lean-toolchain differs from catalog backend.toolchain')
    manifest = load_json(relative_file(base, 'lake-manifest.json', 'lean root'))
    packages = manifest.get('packages')
    if not isinstance(packages, list):
        raise FormalError('lake-manifest packages missing')
    mathlib = [row for row in packages if isinstance(row, dict) and row.get('name') == 'mathlib']
    if len(mathlib) != 1 or mathlib[0].get('rev') != backend['mathlib_rev']:
        raise FormalError('lake-manifest mathlib rev differs from catalog backend.mathlib_rev')
    relative_file(base, 'lakefile.toml', 'lean root')
    relative_file(base, 'scripts/AxiomAudit.lean', 'lean root')
    sources = []
    for path in sorted(base.rglob('*.lean')):
        if '.lake' in path.relative_to(base).parts:
            continue
        sources.append(path.relative_to(root).as_posix())
    if not sources:
        raise FormalError('lean root contains no sources')
    return sources


def parse_axiom_report(path):
    text = Path(path).read_text(encoding='utf-8')
    theorems = {}
    declared = []
    totals = {}
    for line in text.splitlines():
        line = line.strip()
        if line.startswith('AXIOMS '):
            match = re.fullmatch(r'AXIOMS (\S+) \[(.*)\]', line)
            if not match:
                raise FormalError('malformed axiom report line: ' + line)
            name = match.group(1)
            if name in theorems:
                raise FormalError('duplicate theorem in axiom report: ' + name)
            axioms = [a.strip() for a in match.group(2).split(',') if a.strip()]
            theorems[name] = axioms
        elif line.startswith('DECLARED_AXIOM '):
            declared.append(line.split(' ', 1)[1].strip())
        elif line.startswith('AUDIT_THEOREMS ') or line.startswith('AUDIT_SORRY '):
            key, value = line.split(' ', 1)
            if not value.strip().isdigit():
                raise FormalError('malformed audit total: ' + line)
            totals[key] = int(value)
        elif 'error' in line.lower():
            raise FormalError('axiom report contains an error line: ' + line)
    if totals.get('AUDIT_THEOREMS') != len(theorems) or 'AUDIT_SORRY' not in totals:
        raise FormalError('axiom report totals missing or inconsistent')
    if totals['AUDIT_SORRY'] != sum(1 for a in theorems.values() if SORRY_AXIOM in a):
        raise FormalError('axiom report sorry total inconsistent')
    return theorems, declared


def status_rank(value, what):
    if value not in STATUS_ORDER:
        raise FormalError(what + ': unknown formalization status')
    return STATUS_ORDER.index(value)


def check_artifacts(data, root, block, report):
    by_key = {}
    for row in data['artifacts']:
        by_key[row['key']] = row
    lean_root = block['lean_root'].rstrip('/') + '/'
    lean_keys = {k for k, row in by_key.items() if row['path'].endswith('.lean')}
    claims = []
    theorem_owner = {}
    specified = set()
    assumed_all = set()
    for key, row in by_key.items():
        is_claim = row['path'].endswith('.md')
        formal = row.get('formalization')
        if key in lean_keys:
            if row['repository'] != THIS_REPOSITORY or not row['path'].startswith(lean_root):
                raise FormalError(key + ': lean sources must live under the catalog lean_root of this repository')
            if formal is not None:
                raise FormalError(key + ': lean source artifacts carry no formalization record')
            continue
        if formal is None:
            if is_claim:
                raise FormalError(key + ': claim documents require a formalization record')
            continue
        if not isinstance(formal, dict):
            raise FormalError(key + ': formalization must be an object')
        if not is_claim:
            if formal.get('status') != 'none' or len(formal) != 1:
                raise FormalError(key + ': non-claim artifacts may only record status none')
            continue
        status = formal.get('status')
        rank = status_rank(status, key)
        lemma_status = formal.get('lemma_status', 'none')
        lemma_rank = status_rank(lemma_status, key + '.lemma_status')
        effective = max(rank, lemma_rank)
        for field in formal:
            if field not in ('status', 'lemma_status', 'lean_artifact', 'theorems', 'assumed_axioms',
                             'alignment_review', 'alignment_reviewer', 'alignment_ledger', 'authorship',
                             'evidence', 'note'):
                raise FormalError(key + ': unknown formalization field ' + field)
        if effective == 0:
            for field in ('lean_artifact', 'theorems', 'evidence', 'alignment_reviewer'):
                if field in formal:
                    raise FormalError(key + ': ' + field + ' requires a status above none')
            if formal.get('alignment_review', 'none') != 'none':
                raise FormalError(key + ': alignment_review requires a status above none')
            continue
        lean_artifact = formal.get('lean_artifact')
        if lean_artifact not in lean_keys:
            raise FormalError(key + ': lean_artifact must name a catalogued .lean artifact')
        theorems = string_list(formal.get('theorems'), key + '.theorems', allow_empty=False)
        assumed = string_list(formal.get('assumed_axioms', []), key + '.assumed_axioms')
        for axiom in assumed:
            if not axiom.startswith(ASSUMPTIONS_ROOT):
                raise FormalError(key + ': assumed axioms must be declared under ' + ASSUMPTIONS_ROOT)
        assumed_all.update(assumed)
        if assumed and effective == 3:
            raise FormalError(key + ': kernel-checked is capped at proved while assumed_axioms is nonempty')
        authorship = formal.get('authorship')
        if not isinstance(authorship, str) or not authorship:
            raise FormalError(key + ': authorship required above none')
        alignment = formal.get('alignment_review')
        if alignment not in ALIGNMENT_ORDER:
            raise FormalError(key + ': alignment_review required above none')
        relative_file(root, formal.get('alignment_ledger'), key + '.alignment_ledger')
        reviewer = formal.get('alignment_reviewer')
        if alignment == 'accepted':
            if not isinstance(reviewer, str) or not reviewer or reviewer == authorship:
                raise FormalError(key + ': accepted alignment requires a distinct nonauthor alignment_reviewer')
        evidence = formal.get('evidence', [])
        if not isinstance(evidence, list) or any(not isinstance(u, str) or not u.startswith(EVIDENCE_PREFIX) for u in evidence):
            raise FormalError(key + ': evidence must be a list of project GitHub URLs')
        if effective == 3 and not evidence:
            raise FormalError(key + ': kernel-checked requires CI evidence')
        for theorem in theorems:
            if theorem in theorem_owner:
                raise FormalError(key + ': theorem already claimed by ' + theorem_owner[theorem] + ': ' + theorem)
            theorem_owner[theorem] = key
            if effective == 1:
                specified.add(theorem)
        if report is not None:
            reported, declared = report
            for theorem in theorems:
                if theorem not in reported:
                    raise FormalError(key + ': theorem absent from axiom report: ' + theorem)
                axioms = set(reported[theorem])
                extra = axioms - set(CORE_AXIOMS) - set(assumed)
                if effective == 1:
                    extra.discard(SORRY_AXIOM)
                if extra:
                    raise FormalError(key + ': ' + theorem + ' depends on unrecorded axioms ' + ','.join(sorted(extra)))
        claims.append({'key': key, 'status': status, 'lemma_status': lemma_status,
                       'alignment_review': alignment, 'theorems': len(theorems)})
    if report is not None:
        reported, declared = report
        for theorem, axioms in reported.items():
            if SORRY_AXIOM in axioms and theorem not in specified:
                raise FormalError('sorry outside a specified catalog theorem: ' + theorem)
        for axiom in declared:
            if axiom not in assumed_all:
                raise FormalError('declared Lean axiom not recorded in any assumed_axioms: ' + axiom)
    return claims


def check_local_identities(data, root):
    checked = []
    for row in data['artifacts']:
        if row['repository'] != THIS_REPOSITORY:
            continue
        path = relative_file(root, row['path'], row['key'])
        raw = path.read_bytes()
        if len(raw) != row['bytes'] or hashlib.sha256(raw).hexdigest() != row['sha256']:
            raise FormalError('local bytes differ from catalog identity; re-index: ' + row['key'])
        checked.append(row['key'])
    return checked


def basic_catalog(data):
    if not isinstance(data, dict) or data.get('schema_version') != 1 or data.get('scientific_status_authority') is not False:
        raise FormalError('unsupported catalog or false status authority')
    rows = data.get('artifacts')
    if not isinstance(rows, list) or not rows:
        raise FormalError('artifact list required')
    keys = set()
    for row in rows:
        if not isinstance(row, dict):
            raise FormalError('artifact must be an object')
        for field in ('key', 'repository', 'path', 'sha256'):
            if not isinstance(row.get(field), str) or not row[field]:
                raise FormalError('artifact missing ' + field)
        if type(row.get('bytes')) is not int:
            raise FormalError(row['key'] + ': bytes must be an integer')
        if row['key'] in keys:
            raise FormalError('duplicate artifact key: ' + row['key'])
        keys.add(row['key'])
    return data


def run(registry, root, lean_root=None, axiom_report=None):
    data = basic_catalog(load_json(registry))
    block = check_block(data, root)
    sources = None
    if lean_root is not None:
        if lean_root.rstrip('/') != block['lean_root'].rstrip('/'):
            raise FormalError('--lean-root differs from catalog lean_root')
        sources = check_lean_root(root, block['lean_root'], block['backend'])
    report = parse_axiom_report(axiom_report) if axiom_report is not None else None
    claims = check_artifacts(data, root, block, report)
    identities = check_local_identities(data, root)
    return {'formal_claims': claims,
            'local_identities_verified': identities,
            'lean_sources': sources,
            'axiom_report_theorems': None if report is None else len(report[0]),
            'meaning': 'recorded formalization statuses are supported by recorded evidence and bytes; not theorem acceptance'}


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('--registry', required=True, type=Path)
    p.add_argument('--root', type=Path, default=None, help='repository root (default: registry directory)')
    p.add_argument('--lean-root', default=None, help='Lake project directory relative to root')
    p.add_argument('--axiom-report', type=Path, default=None, help='output of lake env lean scripts/AxiomAudit.lean')
    args = p.parse_args()
    root = args.root if args.root is not None else args.registry.resolve().parent
    try:
        output = run(args.registry, root, args.lean_root, args.axiom_report)
        print(json.dumps(output, indent=2, sort_keys=True))
    except (OSError, ValueError, KeyError, TypeError) as error:
        print('REFUSED: ' + str(error), file=sys.stderr)
        return 2
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
