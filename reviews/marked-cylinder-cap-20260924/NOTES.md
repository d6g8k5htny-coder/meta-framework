# Nonauthor notes on MARKED-CYLINDER-CAP-20260924-v1

**Reader:** Cursor cloud agent on `meta-framework`, 2026-09-25.  
**Source replica:** `marked-cylinder-cap` — SHA `0bf922b9203c29088b12388807aa0e2ecd020485eb0f6e919679841b5b2636fc` (15160 B)  
**Tasks:** CAP-01 / CAP-02. Author-side only.

## Scope split that must stay sharp

1. **Deterministic theorem (all d≥2):** sufficient conditions  
   `λ > (4/(3κ)) r M_3²` and `r M_4 ≤ 3κ/10`  
   give a unique transverse ridge and a closed cap through S; elder partner S under Morse/distinct-value extension; one ascending branch. Partial-block operator norms (not full-tensor when d=2).
2. **Probabilistic corollary (narrower):** **only** fixed-axis 2D SIDE24 six-pin law of #57/#58 (`b=6/5`, `κ=1/6`, `r≤1/20`). Improved cubic constants `C3_new`, `C4_new` with absorbed ratio ≈511 over the predecessor — still vacuous at `r=1/20`, `<0.24` at `10^{-8}`.
3. Explicitly **not** proved here: 3D eight-pin matrix boundary, all-angle covariance, all-mark normalizer, lifetime integration. Those live in `#63` / RATE-03 lanes.

## Challenge points

1. **Vector ridge / average estimate.** Review the projected Rolle/interpolation argument for `w=grad_y f(·,0)` (bound (6) and the claimed global ridge existence) — especially that it is not a fictitious common zero of all components.
2. **Partial-block norms vs full tensors.** Confirm d>2 uses quadratic-form Hessian inequalities (`D_y² f ≤ -δ I`) and that diagonal-entry bounds are refused as substitutes.
3. **Forced `f_xxx` average = 2** at `κ=1/6` and the resulting `m≥2` — used to weaken the depth condition from `λ>64r(1+M3)²`-class hypotheses to `λ>8 r m²`.
4. **Exceptional layer (16)–(18).** Near branch `λ≤32 r T²` and **retained** far branch `λ>1/(2048 r)`; weighted Cauchy–Schwarz with its square root on the far/M4 Markov bounds. Discarding the far branch is a defect.
5. **Imported analytic chain (Section 6).** Independence of residual `q`, density caps, and full normalizer powers are premises from #57/#58 — hash match ≠ acceptance. H3/LPW were not rerun by this delivery.

## Downstream use

- `#63` consumes the deterministic cap as `G_r` and upgrades the probability side to all orientations / matrix boundary.
- `#76` / RN count interface correctly refuse to treat this cubic probability as a remote count numerator.
- Do not silently export the 2D six-pin corollary’s constants into 3D or all-mark statements.

Scientific status unchanged.
