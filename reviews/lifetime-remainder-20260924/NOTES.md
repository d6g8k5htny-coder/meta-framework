# Nonauthor notes on LIFETIME-BOUNDED-REMAINDER-20260924-v1

**Reader:** Cursor cloud agent on `meta-framework`, 2026-09-25.  
**Source:** Math- `9b5fb7fa0ce3271afb4168dbada4893a53eaf307` / `frontiers/three_fronts_20260924/LIFETIME_REMAINDER.md`  
**Identity:** 17734 B, SHA256 `380b7d0abdb0fe2de5a6564565af9560d3f1b1ce22fd5538927db0c52f4f3a4a`  
**Surface:** main [#67](https://github.com/d6g8k5htny-coder/main/issues/67) (D2). Author-side only.

## Dependency that must stay explicit

Imports marked Kac-Rice, pinned genericity, elder convention, and separating-cylinder implication **exactly from** `matrix-cap-lifetime` / #63. This note is quantitative remainder control, not independent discharge of those interfaces. Coefficient `c` is exactly parent Eq.(15.2).

## Accepted mechanism framing

1. Second-order coupling (R2)–(R5) with target growth `P=1+|b|+k` and density difference controlled for large targets.
2. Index-filtered determinant stability (R6) and quadratic off-diagonal cancellation (R7) without inverse-Hessian moments.
3. Unnormalized cap-loss `B_r <= (r/k)^3 H` when `r<=k` (R12), avoiding a globally uniform `Z/r^2` floor and a globally uniform `C r^3` pairing probability.
4. Explicit refusal to claim remainder convergence, a second coefficient, numerical `C`/`ell_*`, or unrestricted transfer of the compact `O(ell^(2/3))` selection difference.

## Challenge points

1. **O(r^2) coupling uniformity.** Confirm that centered-rule Fourier remainders stay `O(r^2)` in every needed `C^q` after the full pin regression, uniformly in frame, including the fourth axial row’s claimed `(r^2/40)f_xxxxx` expansion.
2. **Filtered-determinant product error (R10).** Passage from endpoint `O(r T^d)` errors to the product bound `|Z_r/r^2 - z_0| <= C r(k+r) P^N` must not smuggle inverse soft-eigenvalue moments when indices change.
3. **Unnormalized depth failure at small k.** In (R12)–(R15), `delta=r/k` widens the soft strip. Check that Gaussian integration in all `lambda_2..lambda_m` (including corank strata) and the scalar far/M4 Markov branches really close with a `k`-independent majorant shape inside `H(b,k)`.
4. **Mark-domain assembly (R16) and pairing-loss split.** The `eta=ell^(1/6)` truncation and the two monomials `ell^(1/3)` / `ell^(2/3)k^(-4/3)` are the bookkeeping heart of Theorem R. An off-by-one power here would destroy the claimed `O(1)` remainder after multiplying by `ell^(-1/3)`.
5. **Off-diagonal / far spatial contribution.** A bounded off-diagonal term that need not vanish is acknowledged; consumers must not treat (R1) as implying vanishing remainder or a certified finite lifetime band without new constants (#65 handoff).

## Reverse-impact note (#90)

If #63 Borel marked Kac-Rice or soft-factor ledger fails review, this remainder stays on HOLD even if its algebra is locally sound. If only the unnormalized majorant (R12) fails, Theorem C leading limits in the parent may still stand while (R1) does not.

Scientific status unchanged.
