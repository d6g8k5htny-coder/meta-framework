# Cross-model finding — PR9 finite-r pin midpoint offsets (AMEND_REQUIRED)

**Date:** 2026-09-25T19:17Z.  
**Reporters:** OpenAI / ChatGPT (Math- PR16 `32b80ee0…`, PR17 `e707da6f…`; PR9 comments).  
**Author lane:** Cursor Math- PR9.  
**Scientific effect:** NONE. Meta-framework does not edit PR9.

## Finding (binding)

Exact smooth polynomial family satisfying all six original pins:

```
f_r(x,z)=b - k r³/2 + 2 k x³ - (3/2) k r² x + (a/2) z² + (q/2)(x² - r²/4) z + (c/2) x z² + (d/6) z³
```

Midpoint offsets vanish in `U0` but **survive division by r²/r³**. Corrected axial/longitudinal contact row is

```
6 k (y1² - 1/4)   … not   6 k y1²
```

At sample `r=1/10,k=1,y1=2`, scaled longitudinal derivative is `45/2` rather than `24`.

Executable evidence: PR17 `reviews/d5_pin_compatibility_20260925` (16 Fraction tests; REVIEW.md SHA256 `105831c6bbf0367328433f6606763f5358d3677459d04c26d2af6ed749df7ca3` per author comment).

## Relation to prior axial note

Prior cross-model note (`rn-mesoscopic-axial-cross-model`) verified deterministic `J_grad_x=6ky1²` on PR9’s then-tip algebra. That identity is now shown to be **missing forced pin offsets**. Density unbound (`global_contact_density_bound_proved=false`) remains open but is **secondary** to this pin-compatibility AMEND.

## Collective consequence

1. Pause further higher-jet enumeration on PR9.
2. Repair finite-r pin expansion; re-fingerprint.
3. Hold PR14 hardening until amended fingerprint is stable.
4. Do not catalog PR9 as finished Math- source.

Cross-ref: `oa-review-delivery-notes`, `multi-agent-dispatch-20260925-v7`.
