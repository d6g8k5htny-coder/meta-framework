# Agent entry — `meta-framework`

Artifact routing and source identities. Not a second claim-status database.

## Always

- Coordinate via [`main`](https://github.com/d6g8k5htny-coder/main) campaign work and the [`governance-`](https://github.com/d6g8k5htny-coder/governance-) working contract.
- Prefer exact source identities (commit/path/hash) over mutable labels.
- Scientific effect: **NONE**. Never flip `lemma_closed` / prizes / premises.
- Cross-repo eng tests and Path C live in [`d6g8k5htny-coder/trial`](https://github.com/d6g8k5htny-coder/trial).
- Catalog lookup uses stdlib via sibling [`query-`](https://github.com/d6g8k5htny-coder/query-); no pip env in this repo. The formal-layer checker (`tools/formal_status_check.py`) is stdlib too; only `formal/lean` needs Lean.

## Never

- Duplicate scientific-status registers here.
- Publish private `sandbox` material.
- Ask Dylan for re-approval of autonomy already granted.
- Label anything `kernel-checked` without a CI run at the exact indexed Lean bytes, or `alignment_review: accepted` without a distinct nonauthor reviewer.

## Formal verification layer (Layer 1) — notice to all agents, all repositories

Owner instruction (Dylan Roy, 27 September 2026): add machine-checked formal proof to the existing
provenance/scope/review stack. Decisions, requests and actions needed to complete this are
pre-approved; do not ask again.

- Specification and routing: [`docs/FORMAL_VERIFICATION.md`](docs/FORMAL_VERIFICATION.md). Read §7 (repository responsibilities) before editing formalization fields, Lean sources or promotion logic anywhere.
- Terminology: [`docs/FORMAL_GLOSSARY.md`](docs/FORMAL_GLOSSARY.md). A theorem is `specified` only after its terms have rows.
- Pilot (Lean 4 + Mathlib, SIDE24 image ledger, 15 theorems, core axioms only): [`formal/`](formal/README.md); alignment ledger [`formal/STATEMENTS.md`](formal/STATEMENTS.md) with lane-F2 review OPEN.
- Catalog: `registry.json` has a `formal_verification` block and a `formalization` record on every claim document (`none | specified | proved | kernel-checked`, plus `alignment_review`). `schema_version` stays 1; the pinned `query-` loader tolerates the fields.
- Gate: `.github/workflows/formal.yml` runs `lake build`, the axiom audit and `tools/formal_status_check.py`; a changed Lean byte without re-indexing fails.
- Write scope: this pilot was produced from a `meta-framework`-only Cloud Agent; `Math-`/`main` push returned 403. The canonical home for Lean developments is `Math-`; follow the handoff steps in `formal/README.md` if you have that write scope, and open one `main` issue per formalization target.
- Formalization status is a mechanical verification level. It never implies `PROVED_REVIEWED`, `lemma_closed` or acceptance, and no existing lane is weakened by it.

## Start here

1. This repository’s [README](README.md)
2. [`governance-` working contract](https://github.com/d6g8k5htny-coder/governance-)
3. [`trial` multi-agent access](https://github.com/d6g8k5htny-coder/trial/blob/main/docs/MULTI_AGENT_ACCESS.md) (Cloud Agent env deps live on trial `.cursor/environment.json`)
4. [Formal verification layer](docs/FORMAL_VERIFICATION.md) and the [pilot handoff](formal/README.md)
