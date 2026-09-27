# Statement alignment ledger — SIDE24 image ledger pilot

Object: FORMAL-ALIGNMENT-SIDE24-IMAGE-LEDGER-20260927-v1. Author: Cursor (AI, author-side).
Disposition: author-side alignment record; nonauthor formalization review OPEN.
Scientific effect: NONE. This ledger does not accept, promote or reinterpret any theorem.

## Purpose

The Lean kernel checks that each declaration in
[`lean/Side24Formal/ImageLedger.lean`](lean/Side24Formal/ImageLedger.lean) is a proof of the
statement written in that file. It does not check that the Lean statement is the statement the
informal proof meant. That alignment is a separate review obligation (see
[`docs/FORMAL_VERIFICATION.md`](../docs/FORMAL_VERIFICATION.md), lane F2). This ledger is the
author-side half of that obligation: one row per Lean declaration, quoting the informal source
it is meant to capture and listing every hypothesis added, dropped or reinterpreted.

Until a Lean Blueprint toolchain is adopted, this Markdown ledger is the alignment artifact.
Reviewers should treat a missing or vague row as a defect of the formalization, not of the
informal proof.

## Informal source (Layer 0 identity)

| Field | Value |
|---|---|
| Repository | `d6g8k5htny-coder/Math-` |
| Commit | `e329fba1e927a12dbb4f0d1556f85f39284d17a9` |
| Path | `coefficients/side24_v1/PROOF.md` |
| SHA256 | `c06daccc4ba4b9168522b9888b76a7d599934fc3b91bd753ee5d492262917769` |
| Catalog key | `side24-coefficient` |
| Companion code | `coefficients/side24_v1/coefficient.py`, SHA256 `03ae6d0f15160cb681f9bbb19a84dc861c3a0db3e881291ea621061cc90c86ab`, function `image_ledger` (catalog key `side24-coefficient-code`) |

## Formal source (Layer 1 identity)

| Field | Value |
|---|---|
| Path | `formal/lean/Side24Formal/ImageLedger.lean` (this repository) |
| Toolchain | `leanprover/lean4:v4.35.0-rc3` ([`lean/lean-toolchain`](lean/lean-toolchain)) |
| Mathlib | tag `v4.35.0-rc3`, commit `c55e6e786f49471c72fbddbec5415808896aec1e` ([`lean/lake-manifest.json`](lean/lake-manifest.json)) |
| Axioms | `propext`, `Classical.choice`, `Quot.sound` only ([`lean/scripts/AxiomAudit.lean`](lean/scripts/AxiomAudit.lean)) |
| Exact bytes | see the `side24-image-ledger-lean` entry of [`registry.json`](../registry.json) |

## Rows

Alignment review column: `OPEN` until a nonauthor reviewer binds a verdict to the exact Lean
file identity above. The author cannot fill it in.

| ID | Informal statement (PROOF.md) | Lean declaration | Added / dropped hypotheses | Alignment review |
|---|---|---|---|---|
| A1 | §2 eq. (2): `E := 1458*(76*24^6+15)*10^(-125) = 21175738586478*10^(-125)` | `image_constant_eq`, `E` | None. Stated over `ℕ` and `ℚ`. | OPEN |
| A2 | §3 eq. (3): `epsilon = 10^(-108)`, "since 60E < epsilon" | `eps`, `sixty_E_lt_eps` | None. Exact rational inequality. | OPEN |
| A3 | §4: "safely between 1-32epsilon and 1+32epsilon … `|c_d,24/c_d,ref - 1| < 10^(-106)`" — the arithmetic step `32·epsilon < 10^(-106)` only | `relativeBound`, `thirty_two_eps_lt_relativeBound` | Captures only the numeric comparison, not the ratio bound (4) itself. | OPEN |
| A4 | §4: "Since epsilon is far below 1/28" | `eps_lt_one_div_28` | None. | OPEN |
| A5 | §2: "The code proves e^(288/125) > 10 using the positive rational Taylor sum through 20" | `ten_lt_exp_288_div_125` | Proved from `Real.sum_le_exp_of_nonneg` with 21 terms (orders 0–20), matching `coefficient.py` `range(21)`. | OPEN |
| A6 | §2: "hence e^(-288) < 10^(-125)" | `ten_pow_125_lt_exp_288`, `exp_neg_288_lt` | None. | OPEN |
| A7 | §2: "successive terms have ratio at most 512e^(-864) < 1/2" | `five_twelve_exp_neg_864_lt_half`, `tailTerm_succ_le_half` | Terms are `tailTerm j = j^9 e^(-288 j^2)` for natural `j ≥ 1`; the ratio bound is stated as `tailTerm (j+1) ≤ (1/2) tailTerm j`. | OPEN |
| A8 | §2: "`729 sum_{j>=1} j^9 e^(-288j^2) <= 1458 e^(-288)`", i.e. `sum_{j>=1} j^9 e^(-288 j^2) <= 2 e^(-288)` | `tailTerm_le_geometric`, `tsum_tailTerm_le`, `tsum_tailTerm_lt` | Sum indexed as `∑' k : ℕ, tailTerm (k+1)`. Summability is proved, not assumed. The factor 729 is not carried. | OPEN |
| A9 | §1: "For a>=0, elementary integration gives `integral_0^a (a-z)^2 e^(-z/2) dz/2 = a^2-4a+8-8e^(-a/2)`" | `cone_integral` | Hypothesis `0 ≤ a` kept to match the prose; the identity holds for all real `a`. Interval integral in the Bochner/Lebesgue sense of Mathlib. | OPEN |

## Explicitly NOT formalized

The following remain informal. No Lean object stands for them and nothing above may be cited
as machine-checked evidence for them.

1. The Gaussian field, its covariance `K_24`, and the coefficient `c_{d,24}` of parent
   equation (15.2). The pilot does not define these objects.
2. §2 lattice counting: "at most `27 j^3` possibilities for `d <= 3`, `|n|^6 <= 27 j^6`,
   `|n|^2 >= j^2`", the derivative-bound `76|x|^6 e^(-|x|^2/2)` for `q <= 6`, and the
   normalization step `S >= 1`. Hence inequality (2) itself is not formalized; only its numeric
   constant (A1) and the tail sum it relies on (A8).
3. §3 covariance comparison, spectral bounds and Schur-complement argument (inequality (3)).
   Only the arithmetic `60E < epsilon` (A2) is formalized.
4. §4 density comparison, cone-moment scaling and the ratio bound (4).
5. §1 Gaussian moment computations (`D_1 = 4/3`, `D_2 = 29/6 - sqrt 6`) and formula (1).
6. §5 special-function enclosures (pi, log, exp intervals, Gamma(7/6) via Stirling/DLMF).
7. The interval-arithmetic implementation in `coefficient.py` and the reported decimal bounds
   on `c_{2,24}`, `c_{3,24}`.
8. The parent theorem UNIFORM-MATRIX-CAP-LIFETIME-20260924-v1 (main issue 63), which remains
   unreviewed and is neither imported nor axiomatized here.

## Reviewer checklist (lane F2)

- Bind the review to the exact Lean file SHA256 and the Mathlib commit above.
- For each row: does the Lean statement say what the quoted prose says, with the same
  quantifiers, domains and constants? Record any mismatch as `AMEND_REQUIRED` for that row.
- Confirm `lake build` and `lake env lean scripts/AxiomAudit.lean` were reproduced, or cite
  the CI run that did.
- Do not re-prove the theorems; the kernel already did. Do not grade the informal proof; that
  is the existing nonauthor analytic review (main issue 63 / SIDE24 review), a different lane.
- Return the verdict in a writable repository with this ledger's identity; do not edit this
  file to record acceptance.
