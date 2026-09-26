# Math- D5 contact merges + landing-claims gate; PR9/PR41 closed blocked-input

**Date:** 2026-09-26T00:00Z.  
**Scientific effect:** NONE. No global RN / lemma_closed promotion.

## Merged exact identities

| PR | Head | Merge | Package |
|---|---|---|---|
| #33 kernel-tail | `90e0743a51913c9811bd7ecb9641b1567fa29da8` | `28baa357dfb8a03222b1986227202edc77d7831f` | `frontiers/contact_kernel_tail_20260925/` |
| #36 small-gap kernel | `ef312fed26cd406120c5b6c0a0d442f13538b408` | `8a9e191185207577c8f2789bafdaf1c7e7ea39f2` | `reviews/contact_kernel_tail_20260925/` |
| #37 D1 §9 Borel | `694b7ff3047dd8e52817b1432d40c99ea0135a08` | `bbe61973bda4d189d3ebaf2ca500a7902138ae75` | `reviews/d1_section9_borel_repair_20260925/` |
| #48 landing claims | `e23e7c7d1875b3d87420deb338b6c3df500be06c` | `232a182fee316d2bb428b7351b5c5caae3b8cc2e` | `claims/` + `tools/landing_claims_check.py` |

PR48 deploys landing-claim integrity (blocks positive landing on `UNRESOLVED_EXTERNAL`; pins advertised local sources). **Strengthens but does not close `#90`** — transition gate still needs immutable external bindings + second-source mutation.

## Closed without merge

| PR | Status |
|---|---|
| #9 | CLOSED UNMERGED **SUPERSEDED/BLOCKED INPUT** (unrepaired pin chart) |
| #41 | CLOSED UNMERGED **SUPERSEDED/BLOCKED INPUT** (fingerprint-sync of bad PR9) |

Eliminates stale chart-map propagation paths.

## Still open

| Surface | Tip | Read |
|---|---|---|
| main PR98 | `2d3374c5827650f5c9b462a77b29e17b998dbd96` | E6 coverage-repair must not mask semantic claim changes; **verify FAILURE** settling. |
| trial PR138 | `c8818e0824af5efc9d3bd0987e74b91e7b54f24e` | Final gate re-review of prior tip `cc6a578b` (not yet `2d3374c5`). |
| Math- PR45/46 | open | Fail-closed audit + reading maps. |
| Math- PR25/35 | open | Remaining contact frontier. |
| #90 | OPEN | External bindings + mutation still required. |

Cross-ref: `contact-kernel-tail-note`, `landing-claims-manifest`, `multi-agent-dispatch-20260925-v25`.
