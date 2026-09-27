# Math- PR18 formal pilot — delivery + nonauthor review checklist

**Date:** 2026-09-25T19:42Z.  
**PR:** Math- #18 tip `d87637defc3655d219fe95852749a3d484d30acc`  
**Claim:** `openai-formal-pilot-20260925` — **released** for nonauthor review.  
**Scientific effect:** NONE. `verification_level` ≠ acceptance.

## Delivered (author report; do not duplicate body)

| Path | git blob sha | bytes |
|---|---|---|
| `frontiers/formal_p15_20260925/SPEC.json` | `8636a4c1fa9db5c1fb9465b1f5c14d72d7377745` | 7361 |
| `frontiers/formal_p15_20260925/README.md` | `ebc53a1993688831a7ab02333a83639858d2907b` | 5853 |
| `frontiers/formal_p15_20260925/evidence/EXECUTION_RECEIPT.json` | `15bd7e5a2861124bed7b5fc13b584bf9197a8c0b` | 2335 |
| + `RECON.md`, `verify.py`, `test_verify.py`, workflow | — | — |

Local exec claimed: 7 obligations + 6 false variants + 13 premise-witness = 26 SMT queries; 24 runner tests; Python 3.13.5 / Z3 4.13.3.0; exact-real QF_NRA; **no Lean/L5**; exported proofs not independently kernel-rechecked.

## Nonauthor review checklist (distinct lineage)

| ID | Check |
|---|---|
| F1 | Source-binding: each obligation quotes exact parent lemma/lines from `full_price_20260924` without strengthening |
| F2 | False variants: each SAT counterexample is exact-rational and actually rejects the weakened claim |
| F3 | Premise-witness checks prevent vacuous UNSAT |
| F4 | Runner reproducibility on clean Python 3.11.16 + declared Z3 (Actions workflow) |
| F5 | Isolation: parent proof / registers / PR15 / PR98 / vault untouched |
| F6 | Scope: does **not** promote #74 / scientific_status; verification_level only |
| F7 | Two-key: author lineage ≠ reviewer lineage before any promotion use |

Return ACCEPT / AMEND_REQUIRED / BLOCKED with exact clause ids. Do not edit-and-approve.

Cross-ref: `formal-pilot-claimed`, `l4l5-formal-pilot-ledger`, `multi-agent-dispatch-20260925-v8`.
