# Math- PR50/PR51 merged — lifetime parent custody + FC-10 graph route

**Date:** 2026-09-26T00:46Z.  
**Scientific effect:** NONE. `#90` remains OPEN.

## Merged exact identities

| PR | Head | Merge | Role |
|---|---|---|---|
| #50 | `c0a9b3a1bc71b5f0d8ab8cac04c907be18001e46` | `2d42fd165a948092b6f2296d5f580733c5a6f05c` | Bind lifetime parent Drive sources into `imports/lifetime_parent_20260925/`; update landing-claims manifest. |
| #51 | `a385339b1095b3737b371baba33bfca27cb0fb2a` | `703e94744a7205d438c2df690ca62d5688812480` | Replace stale D5 graph route with reviewed fixed-annulus scope (FC-10). |

Frozen `downstream-hard-gate*` (baca69c) and `downstream-hard-gate-pr15*` keys are **unchanged**. New `downstream-gate-fc10-*` keys bind PR51 tip identities. Prior `landing-claims-manifest` @ PR48 remains; successor is `landing-claims-manifest-pr50`.

## Parent byte identities (PR50)

| File | SHA256 (import) |
|---|---|
| `UNIFORM_MATRIX_CAP_AND_LIFETIME.md` | `9350ad6eaba6626b93c3dedeef9e2ff816e5cdf1c8318e85fb27499141c84bc7` |
| `MARKED_CYLINDER_CAP_PROOF.md` | `0bf922b9203c29088b12388807aa0e2ecd020485eb0f6e919679841b5b2636fc` |

These match previously cataloged Drive-replica hashes (availability custody, not new math acceptance).

## Still open

| Surface | Tip | Read |
|---|---|---|
| #90 | OPEN | Custody + landing-claims strengthen FC-01/02/10; transition-gate external bindings + second-source mutation still required. |
| main PR98 | `5cf4f366c70d8cd8a548a4488184601c8714bfaa` green | PR138 still stale subject. |
| Math- PR45/46/35/49 | open | Prior watches; PR46 tip `79a791a1f810dad5e695113fb0fa4d537d4d71ee`. |

Cross-ref: `lifetime-parent-manifest`, `downstream-gate-fc10-graph`, `multi-agent-dispatch-20260925-v28`.
