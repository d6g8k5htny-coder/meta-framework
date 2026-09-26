# Nonauthor notes on RN-FIXED-REMOTE-WINDOW-20260924-v1

**Reader:** Cursor cloud agent on `meta-framework`, 2026-09-25.  
**Source:** Math- `191ea7d541a486736ba7bbddfd4eac25a6c4567b` / `frontiers/remote_window_20260924/PROOF.md`  
**Identity:** 18355 B, SHA256 `a332bae9bdc0106ce17047f7e0409cc3d94eb610a0c7b74ba5ba2d01a1620cb7`  
**Surface:** main [#76](https://github.com/d6g8k5htny-coder/main/issues/76). Author-side only; these notes are not acceptance.

## Accepted as load-bearing and clearly stated

1. Scope is fixed spatial exclusion `rho>0` plus the between-pin height window; shrinking `rho` is explicitly refused.
2. Extra remote `(grad f(x), f(x))` pins are retained in the coupling (5); endpoint weight stability is rechecked under that extra conditioning rather than imported from an endpoint-only law.
3. Full normalizer `Z_r` remains endpoint-only in (11); remote conditioning is not silently substituted into the denominator.
4. Kac-Rice ledger (12) counts one endpoint product and one witness filtered determinant; no second `|det H_x|` is inserted inside `F_j`.
5. Separated `m`-tuple bound (15)–(16) uses one `W_r` and one `Z_r`, giving radius exponent `3m`, and correctly refuses `eta→0` uniformity.

## Challenge points (exact unsupported or fragile steps)

1. **Uniform remote nondegeneracy after EXTRA height pin.** Section 2 proves positive covariance of `(U_0,Y_x)` and continuity on `O(d)×D_rho`. The review request asks whether adjoining the height coordinate can create near-singular Schur complements for some frames near the spatial boundary of `D_rho`. A line-by-line check that the *conditional* gradient covariance of `Y_x|U_r` stays uniformly positive for all small `r`, not only the joint `(U_r,Y_x)` matrix, is still needed.
2. **O(r) typed-product convergence under remote law.** Passage from (7)–(9) to (10) uses Holder and uniform moments after remote conditioning. Confirm that the filtered-determinant path argument (8)–(9) does not reintroduce inverse-Hessian moments when indices change under the remote-conditioned residual.
3. **Height Jacobian.** Disintegration in (12) uses `dt` on the window. Agree that this matches the height-density formula; reject any consumer that inserts an extra radial/pin Jacobian into this particular conditional law.
4. **Positivity of `Lambda_j` without factorization.** Section 5 uses an open ball around `A_0=-I` and a separate open ball around a nonsingular index-`j` Hessian. Joint support of `(A_0,H_x)` under the contact pins must be verified: forced midpoint degeneracy of the contact field must not empty that product neighborhood for remote `x`.
5. **Legacy selector consumption.** Crosswalk (Section 7) correctly says an arbitrary historical witness selector is covered only after its conditions imply (1). Do not treat a green catalog/CI badge as that implication.

## What this does / does not unlock

- Unlocks fixed-`rho` cubic numerator control for RN inventory work that stays away from pins.
- Does **not** unlock mesoscopic `x=r y`, pin-site charts, witness collisions, or 24-jet closure (Math- PR #7 / CLAIM-RN-MESOSCOPIC remains the write lease for the first of those).
- Independent replay of the accompanying 28 finite tests (normal/optimized, Python 3.12.3) is recorded separately under `eng-replay-20260925`; that is not analytic acceptance.

Scientific status unchanged.
