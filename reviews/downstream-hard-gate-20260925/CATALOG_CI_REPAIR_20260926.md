# Catalog CI repair — path collisions + governance allowlist

**Date:** 2026-09-26T00:53Z.  
**Scientific effect:** NONE.

## Failures observed

| Tip | Error | Cause |
|---|---|---|
| `d94d447` | `byte count mismatch: downstream-hard-gate-graph` | Successor Math- keys shared paths with frozen baca69c / PR48 keys; CI workspace overwrite |
| `23b56f7` / tip | `unapproved source` | `review-topology-merged` uses repository `governance-`, absent from catalog.yml fetch allowlist |

## Repair

1. Relocate `downstream-gate-fc10-*` and `landing-claims-manifest-pr50` to meta-framework replicas (same bytes/SHA256 as Math- merges; SOURCE.json binds exact Math- commits). Frozen Math- keys unchanged.
2. Add `governance-` to catalog.yml public fetch allowlist (already a registered public federation role).

Cross-ref: `downstream-gate-fc10-graph`, `landing-claims-manifest-pr50`, `review-topology-merged`.
