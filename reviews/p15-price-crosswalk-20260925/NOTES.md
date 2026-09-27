# P15 price crosswalk: boundary counterexample → restricted budget → full-price

**Reader:** Cursor cloud agent on `meta-framework`, 2026-09-25.  
**Sources (exact identities):**
- `p15-price-boundary` — SHA `498af650ef7139c39d2630561dbfd0822c495ce6308a6cac8b767aefe0c2a40b` (2266 B)
- `p15-price-budget` — SHA `3b79d2de60d77df9dd0d81cea60935d3dbceeb26fcf2d38d62667a425180a535` (7935 B)
- `p15-full-price` — SHA `87521901ca8e5405b4d1e47f1deb1cd0326affbd6f5967b53c4178590da993f9` (already noted under `p15-full-price-notes`)

**Disposition:** dependency crosswalk, not acceptance.

## What each source settles

| Source | Claim | What it does **not** do |
|---|---|---|
| Realized covers | `c<=p`, palette `K_H(d)`, full-block cover | Transformed prices |
| Price boundary | Same palette + `c<=phi(p)` is **false** in general (exact `4/9 > log(4/3)` on two coords, `d=1`) | Refute P15-B (local `phi(q_i)` fails here); refute larger-palette theorems |
| Price budget | Restore `c<=phi(p)` under **`d_i>=2` and `p_v<=1/4`**, factor **16/27** | Retract the counterexample; claim sharpness of `1/4` |
| Full price | Remove probability ceiling for realized family with **`d_i>=2`**, sharp factor `rho_star=1/h_star` | Unrestricted downset/prize; demand-one cases |

## Challenge points on the restricted budget (T1)–(T6)

1. **Ratio (T3).** Verify exponents `n-a-1` vs `n` with `n=ad+1`, `d>=2`, and the chain `<=(4/3)(4/9)^a<=16/27` for all `a>=1`.
2. **Demand load-bearing.** When `a=d=1`, `n=2`, (T3) fails and the boundary counterexample applies — keep that as a hard gate, not a special case to paper over.
3. **Global assembly (T6).** Same direction as full-price: `mu(D)<=product(1-q_i)`; crossing failures only help the inequality.
4. **Sufficient checker `rho(a,d,p_*)`.** `rho>1` is not a counterexample; do not treat inconclusive software output as impossibility.
5. **816 example at tiny p.** Extending to `c<=log(40900/40899)` at the same 816 palette is a realized-family consequence, not a new support theorem.

## Ordering for reviewers / reverse impact (#90)

```
realized-covers  →  price-boundary (negative control)
                 →  price-budget (p<=1/4, d>=2, 16/27)
                 →  full-price (all p, d>=2, rho_star)
```

If realized-covers’ `K_H` cover equivalence fails, both budget theorems HOLD. If only the `p<=1/4` ratio fails, full-price may still stand on its odd-majority route. The boundary counterexample must remain published under any promotion of either positive theorem.

Scientific status unchanged.
