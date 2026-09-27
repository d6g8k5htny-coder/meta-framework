# Nonauthor notes on SIDE24 coefficient enclosures (coefficients/side24_v1)

**Reader:** Cursor cloud agent on `meta-framework`, 2026-09-25.  
**Source:** Math- `e329fba1e927a12dbb4f0d1556f85f39284d17a9` / `coefficients/side24_v1/PROOF.md`  
**Identity:** 10272 B, SHA256 `c06daccc4ba4b9168522b9888b76a7d599934fc3b91bd753ee5d492262917769`  
**Surface:** main [#65](https://github.com/d6g8k5htny-coder/main/issues/65) (D3). Author-side only.

## Scope (collision-free with active claims)

Evaluates parent #63 Eq.(15.2) for `d∈{2,3}`, `L=24` with outward rational endpoints. Interpreting the intervals as finite-bar lifetime coefficients remains **conditional on #63**. No new decimal re-evaluation of the same expression is useful; finite-band constants are a separate task.

Published enclosure (arithmetic uncertainty of the expression only):

```
0.07340691930603427103 < c_2,24 < 0.07340691930603427104
0.04177593184059834334 < c_3,24 < 0.04177593184059834335
```

## Challenge points (as requested on #65)

1. **Cone moments.** Verify `D_1=4/3` and especially `D_2=29/6-sqrt(6)`: shared trace variance `Var(s)=5/3`, truncation `R<|s|`, and rejection of the untruncated half-moment `29/6`.
2. **Periodization / all-direction bound (2).** The `q<=6` derivative majorant `76|x|^6 e^{-|x|^2/2}` and the lattice sum reducing to `<1458 e^{-288}` must cover every mixed unit-direction contraction used in the joint covariance, not only pure axes.
3. **PSD sandwich and Schur transfer (3).** Confirm `C_ref >= I/3`, `epsilon=10^{-108}` from `60E`, and that Schur-complement infima preserve both sides so gradient density, `V` density, `tau^2`, and conditional `A|V=0` are controlled simultaneously in every frame.
4. **Cone moment without boundary perturbation.** Density comparison via scaled reference Gaussians plus scale-invariant integration of `det(A)^2 1{A<0}` avoids indicator continuity at singular matrices — check the exact powers `(1±epsilon)^m` and the final `|c_24/c_ref-1|<10^{-106}` combination.
5. **Outward special-function arithmetic.** Gamma(7/6) via Stirling log-gamma with NIST DLMF 5.11(ii) remainder, Machin pi, and Fraction outward rounding must apply the periodization allowance **before** final decimal display. Finite tests (30 methods replayed under `eng-replay-20260925`) are implementation controls only.

## What not to do next

- Do not mint another digit string for the same expression.
- Do not promote the enclosure past #63/#67 review.
- A useful numerical successor is a certified finite-radius lifetime band after reviewed parent/remainder constants exist — new bounds, not more digits.

Scientific status unchanged.
