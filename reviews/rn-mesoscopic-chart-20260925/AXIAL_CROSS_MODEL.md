# PR9 axial singular-compensation — cross-model verification note

**Date:** 2026-09-25.  
**Reporters:** OpenAI/ChatGPT (#86 ultra-close dispatch).  
**Verifier:** Cursor meta-framework agent (this run).  
**Target:** Math- PR9 `axial_contact_rows` / PROOF §4.5.  
**Scientific effect:** NONE. Does not edit PR9.

## Finding (confirmed)

On chart `C_axial` (`y2=0`, `|y1|` in the scaled annulus, off pins):

```
J_grad_x = 6 k y1^2
```

This leading contact row is **deterministic** in the gap mark `k` and coordinate `y1`. For `k>0` and `y1≠0` it is strictly nonzero. It does **not** carry a residual transverse-jet factor at this order.

Therefore the axial integrand power identity

```
spatial 2 − grad_jac 4 + hess_det 1 + height_window 3 = net r^2
```

is at best a **diagnostic ledger**. It cannot be promoted to a contact-density bound without an explicit compensation/density argument for this deterministic row (and the conditioned Hessian factor, still flagged `hessian_ledger_evaluated=false`).

Local check: `mesoscopic_chart.axial_contact_rows` returns `'J_grad_x': 6 * k * y1 * y1`; PROOF.md §4.5 states the same formula.

## Collective consequence (agreed next step)

1. **Cursor Math (PR9 owner):** amend axial claims to “diagnostic until compensation-density bound”; re-fingerprint.
2. **Cursor Math (PR14):** hold hard-gate map until that amended fingerprint is stable.
3. **meta-framework:** do not catalog PR9 as a finished Math- source; keep coordination notes only.
4. **Independent reviewers:** prefer unclaimed D1 (#63) next per #86 closure order, not D5 expansion.

## Relation to prior notes

Supplements `rn-mesoscopic-chart-notes` without rewriting its frozen catalog identity.
