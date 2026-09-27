# PAL-02 matching notes: consecutive palette vs realized P15 covers

**Reader:** Cursor cloud agent on `meta-framework`, 2026-09-25.  
**Sources:**
- `consecutive-palette` — Drive replica SHA `6abcc0607e7b4b3cfdcecec854aa2920bb3f830a238ac12e27d18babf64707eb`
- `p15-realized-covers` — Math- `9b5fb7fa0ce3271afb4168dbada4893a53eaf307`, SHA `c0dbb821fb57b685a20cc321e4074456f39a9697f3104afd1f728e4732179bb9`
- P15-B cited in realized-covers: Drive `19D-eHQAIXMGGy2ThZUfZ0GGjIKWm5C2j`, SHA `9b18b6e9abc90d18deef06ab12e3aa7794dad40e1618d99daa88e369c300e8c3` (not re-downloaded in this pass)

**Disposition:** application-matching review notes, not palette or prize acceptance.

## Exact comparison of the two “816” examples

| | Realized covers (§6) | Consecutive palette (§4) |
|---|---|---|
| Blocks / demands | 6 blocks, `a_i=1`, `d_i=408` | 6 blocks, demand 408 each |
| Crossing supports | **All 15 four-block subsets** | **Five adjacent pairs** `{i,i+1}` |
| Structural method | Uniform matroid / `K_H` via (P9) with `s=3` | Consecutive capacity formula (1) |
| Palette optimum | `K_H=816` | Optimum `816` |
| Whole-ground chromatic | `818` (`2454/3`) | Not the same obstruction family |
| Displayed coloring | e.g. paired independent sets of size ≤3 | 408 on `{0,2,4}` + 408 on `{1,3,5}` |

**Verdict:** Coincident `816` and similar bipartite-looking colorings do **not** identify the support families. Consecutive-palette explicitly states the adjacent-pair instance is not #59’s fifteen four-block supports. Realized-covers likewise says consecutive-palette may be consumed only when its complete-support hypotheses hold.

## What PAL-02 still requires for P15-B application

1. Prove that every **actual** P15-B crossing minimal original forbidden set (complete crossing supports) is consecutive in one supplied block order — or reject that route for that instance.
2. Match local demands / capacities to the consecutive theorem’s `d_i`, `A_j`, `c_j` — not to an abstract hypergraph drawing.
3. For the six-block / 15-edge benchmark, the consecutive route is **blocked** unless a different consecutive presentation of those 15 edges exists (the triangle refusal shows not every pair system is consecutive). Matroid / `K_H` remains the realized-covers path for that H.
4. Price/cover theorems (`p15-price-budget`, `p15-full-price`) inherit realized-covers’ setwise `K>=K_H(d)` fact; they do not become consecutive-palette theorems by citation.

## Minimal separators already recorded by the authors

- Path constraints `{0,1},{1,2}`: nonmatroid but consecutive — consecutive theorem applies; matroid route fails.
- Triangle `{0,1},{1,2},{0,2}`: formula (1) alone would give 2; true optimum 3; code must reject nonconsecutive input.
- These separate arbitrary / matroid / consecutive / circular support classes as PAL-04 requested; they are not yet a full P15-B cover match.

Scientific status unchanged. No claim that consecutive-palette discharges P15-B.
