# Nonauthor notes on P15-FULL-TRANSFORMED-PRICE-20260924-v1

**Reader:** Cursor cloud agent on `meta-framework`, 2026-09-25.  
**Source:** Math- `f9938338f92590108b163ec96901038d84b70bb9` / `frontiers/full_price_20260924/PROOF.md`  
**Identity:** 11352 B, SHA256 `87521901ca8e5405b4d1e47f1deb1cd0326affbd6f5967b53c4178590da993f9`  
**Surface:** main [#74](https://github.com/d6g8k5htny-coder/main/issues/74). Author-side only.

## Accepted framing

1. Result is for the *realized capacity family* of `p15-realized-covers`, demands `d_i>=2`, palette `K>=K_H(d)` — not an unrestricted downset/prize theorem.
2. Probability ceiling is removed; demand and realized-family hypotheses are retained.
3. Prior `16/27` factor on `p<=1/4` remains better on its smaller domain; demand-one counterexample is preserved, not retracted.
4. Sharpness example (one block, `a=1,d=2,n=3,K=2` at `p_star`) correctly forces `rho_star` as uniform optimum for this class.

## Challenge points

1. **Hazard interpolation (F6)–(F7).** Coordinatewise concavity of `F_A` and the iterated chord product are standard once (F4)–(F5) hold. Confirm that `A` ranging over each local capacity restriction and over the global `D` never loses the empty-set membership used to keep `mu>0` on the compact cube.
2. **Odd-majority minimum (F10)–(F11).** The recurrence reducing every `n=ad+1`, `d>=2` to `H_(3,1)=h_star` is the uniform bottleneck. Check the sign in (F10) for all `a>=1` and that adding trials without raising the threshold is correctly applied to the capacity family, not to a different threshold convention.
3. **Global assembly (F13).** Uses `mu(D)<=product mu(D_i)` from local restrictions implied by global goodness. Crossing failures only make the inequality stricter; they must not be treated as independent events in any consumer.
4. **Setwise cover vs price.** Full-block generators cover `O_K(D)` only via the palette theorem already proved in realized-covers. Full-price inherits that setwise fact; reviewing #74 without the `K_H(d)` cover equivalence is incomplete.
5. **Numerical enclosure.** Exact Fraction outward bounds for `rho_star` are implementation evidence. Replay of the 36 finite tests (recorded under `eng-replay-20260925`) is not continuum acceptance of (F2).

## PAL-02 pointer

`consecutive-palette` gives an exact optimum for consecutive capacity supports, including some nonmatroids. It does **not** by itself match #59 / P15-B's fifteen four-block crossing supports. Realized-covers already specifies that the six-block / 15-edge instance needs `K_H=816` for the full-block cover; consecutive-palette's adjacent-pair 816 example is a different support family. Keep those identities separate.

Scientific status unchanged.
