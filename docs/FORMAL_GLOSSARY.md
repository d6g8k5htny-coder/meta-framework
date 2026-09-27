# Formal glossary — project terms to standard mathematics and Lean/Mathlib

Object: FORMAL-GLOSSARY-20260927-v1. Author: Cursor (AI), author-side. Scientific effect: NONE.

Purpose: every non-standard term used in the project's proofs must map to a standard
mathematical object before a theorem using it may be labelled `specified` or higher in
[`registry.json`](../registry.json). Where a Mathlib object exists it is named. Where it does not,
the row says what must be defined in Lean first. A term that resists mapping is either ill-defined
or novel; novelty needs a literature comparison (see `main/docs/RECON_NOVELTY_20260925.md`) and a
Lean definition before any theorem about it is formalized.

Mapping status: `mapped` (standard object identified, Mathlib name known or definable in a few
lines), `partial` (standard reading clear but a project-specific convention must be fixed in Lean
before use), `pending` (the project source must supply a precise definition first).

Row sources are the exact catalog artifacts (`registry.json` keys); quoted definitions come from
those bytes. Extend this file in the same PR as any new Lean theorem.

## A. Gaussian field and Kac–Rice objects

| Project term | Standard meaning | Lean / Mathlib target | Status | Source key |
|---|---|---|---|---|
| Universal Law field; "the parent's exact centered variance-one Gaussian field on the fixed torus" | Stationary centered Gaussian random field `f : ℝ^d/(Lℤ^d) → ℝ` with covariance `K_L(z) = Σ_n e^{-|z+Ln|²/2} / Σ_n e^{-|Ln|²/2}` (periodized heat kernel, normalized to variance one) | Gaussian measures exist (`ProbabilityTheory.gaussianReal`, `ProbabilityTheory.IsGaussian`), but a Gaussian *process/field* on a torus with a given covariance kernel is not in Mathlib. Define `K_L` as a function first (`tsum` over `ℤ^d`); the field itself requires a construction (projective families/limits exist as `MeasureTheory.IsProjectiveLimit`; continuity/regularity of sample paths does not). | `partial` | `lifetime-remainder`, `side24-coefficient` |
| `K_24`, `K_infty` | The covariance above with `L = 24`; `K_infty(z) = e^{-|z|²/2}` is the nonperiodic reference | `K_infty` is definable directly. `K_24` is a `tsum` over `Fin d → ℤ`. Summability must be proved (Gaussian decay). | `mapped` | `side24-coefficient` |
| pins `M = -ru/2`, `S = ru/2` with heights `b`, `b - k r³` and zero gradients | Conditioning event: prescribed values and vanishing gradient of `f` at two points at distance `r` along unit vector `u` | Linear observations of the field; conditional law is Gaussian regression. Needs the field construction above. | `partial` | `lifetime-remainder` |
| Gaussian regression law `Q` | Conditional distribution of a Gaussian vector given linear observations (Schur complement covariance) | Finite-dimensional conditional Gaussian: definable from `Matrix` Schur complements; `Matrix.schur_complement` lemmas exist (`Matrix.det_fromBlocks₁₁` etc.). No packaged "conditional Gaussian" yet. | `partial` | `lifetime-remainder` |
| marked Kac–Rice identity; full-pin Kac–Rice expression | Expected number of critical points (with marks/weights) as an integral of a conditional determinant expectation times a density (Kac–Rice / Rice formula) | Not in Mathlib. Formalization target of its own; the SIDE24 pilot does **not** touch it. | `pending` | `lifetime-remainder`, `rn-count-interface` |
| full normalizer `Z = E_Q W`, `W = |det H_M det H_S| · 1{max/index-(d−1) saddle}` | Normalizing constant of a weighted conditional law | Expectation of a measurable weight under a Gaussian measure; definable once `Q` exists. | `partial` | `lifetime-remainder` |
| elder rule / elder pairing / elder selection | Standard persistence pairing rule: when two components merge, the younger (later-born) dies (elder survives). "Elder-selected pair" = the (max, saddle) pair recorded by persistent homology of superlevel sets | Persistent homology is not in Mathlib. For finite point clouds a combinatorial definition is possible; for smooth fields it needs Morse theory (absent). | `pending` | `lifetime-remainder` |
| candidate density `nu_cand(ell)`; elder density `nu_eld(ell)` | Expected per-unit-volume density of ordered (maximum, index-(d−1) saddle) pairs with height gap `ell` (all pairs), respectively only the pairs realized as finite superlevel H₀ bars | Ratio of an expected count to volume; needs Kac–Rice + elder selection. | `pending` | `lifetime-remainder` |
| finite bar / essential bar; superlevel H₀ bars | Persistence intervals of `H₀` of the superlevel filtration; the essential bar is the one that never dies (global maximum class) | As for elder rule. | `pending` | `lifetime-remainder` |
| lifetime coefficient `c = c_{d,L}`, "equation (15.2)" | Leading constant in `nu(ell) ~ c · ell^{-1/3}`, expressed as a ratio of Gaussian moments: `c_{d,ref} = Γ(7/6)(3/2)^{1/3} D_{d−1} / [2√3 π^{d−1} √π]` | `Real.Gamma`, `Real.pi`, `Real.rpow`, and the cone moments `D_m` below. Definable as a real number once `D_m` is. | `partial` | `side24-coefficient` |
| SIDE24 | Project label for "the coefficient evaluated for the torus side length `L = 24`, dimensions `d ∈ {2,3}`" | Not a mathematical object; naming only. | `mapped` | `side24-coefficient` |
| cone moment `D_m = E[det(A)² 1{A < 0}]` | Second moment of the determinant of an `m×m` GOE-like Gaussian symmetric matrix restricted to the negative-definite cone | `Matrix.det`, negative-definite cone as `(-A).PosDef` (`Matrix.PosDef`); a Gaussian law on symmetric matrices must be defined (product of independent normals on upper-triangular coordinates). `D_1 = 4/3` reduces to one-dimensional Gaussian moments (`ProbabilityTheory.gaussianReal`, `integral_gaussian`). | `partial` | `side24-coefficient` |
| transverse Hessian `A = Q + √(2/3) Z I_m` | Conditional Hessian block after conditioning on `V = Hu = 0`; decomposition into a traceless-like part and a scalar shift | Finite-dimensional linear algebra; definable. | `mapped` | `side24-coefficient` |
| image (periodic image), image constant `E`, image ledger | Terms `n ≠ 0` of the lattice sum defining `K_24`; `E = 1458·(76·24⁶+15)·10⁻¹²⁵` bounds their total contribution to derivatives through order 6 at 0 | `E : ℚ` and its inequalities are formalized (`Side24.ImageLedger`). The lattice-counting step is not. | `mapped` (constants) / `pending` (lattice bound) | `side24-coefficient`, `side24-image-ledger-lean` |
| covariance allowance `epsilon = 10⁻¹⁰⁸`; "(1−ε)C_ref ≤ C_24 ≤ (1+ε)C_ref" | Loewner-order (positive-semidefinite) two-sided comparison of covariance matrices | `Matrix.PosSemidef`; the scoped `MatrixOrder` partial order `x ≤ y := (y - x).PosSemidef` (`Mathlib/Analysis/Matrix/Order.lean`). | `mapped` | `side24-coefficient` |
| outward rounding on the grid `10⁻⁸⁰`; outward rational bounds | Interval arithmetic with directed rounding to a fixed rational grid | Not needed in Lean: state the final inequality with exact rational endpoints and prove by `norm_num`/exact arithmetic. The Python code remains replay evidence. | `mapped` | `side24-coefficient-code` |
| Stirling remainder (DLMF 5.11(ii)) | Bound on the error of the Stirling series for `log Γ` at positive real argument | `Real.Gamma` exists; `Stirling` in Mathlib covers `n!` asymptotics (`Stirling.stirlingSeq`), not the `log Γ` series remainder. Needs proof. | `pending` | `side24-coefficient` |
| contact kernel `Lambda_j`; contact observations; observation transform `U_r = T_r O_r` | Explicit positive continuous function of the conditioning parameters arising from the divided-difference frame of two nearby critical points | Definable as an explicit function once the divided-difference linear map is written in `Matrix`. | `partial` | `rn-fixed-remote-window`, `lifetime-remainder` |
| RN, RN counting, RN-04 | Project lane: expected number of *remote* critical points ("remote neighbour") beyond the two pinned points; task RN-04 = derive an expected-count estimate from a pairing-failure probability bound | Expected count of critical points in a region: Kac–Rice (pending). The probability-to-count *implications* (Markov, Hölder, `E[N 1_E] = q E[N|E]`) are standard and formalizable now (`MeasureTheory.mul_meas_ge_le_integral`, `ENNReal.lintegral_mul_le_Lp_mul_Lq`). | `mapped` (interface) / `pending` (count) | `rn-count-interface` |
| 24-jet, 24-jet certificate, JETMOD | Legacy numerical route: Taylor jet of order 24 of the covariance with a certified enclosure; "JETMOD" is its module in the hardening branch | Historical numerical obligation, not a theorem to formalize here; if formalized, it is a certified Taylor-remainder bound (`taylor_mean_remainder` family). | `pending` | `rn-count-interface` |
| fixed remote window; between-pin height window; fixed annulus; thin tube; inner belt | Regions of the torus (fixed distance from the pins; scaled annulus; tube around the pin axis) and height intervals used to localize counts | Sets in `EuclideanSpace ℝ (Fin d)` / the torus; definable. | `mapped` | `rn-fixed-remote-window` |
| witness, witness-pair, witness collision | A remote critical point that "witnesses" a pairing failure; collision = two witnesses approaching each other | Needs the count objects above. | `pending` | `rn-fixed-remote-window` |

## B. P15 combinatorics (Talagrand-type discrete problem)

| Project term | Standard meaning | Lean / Mathlib target | Status | Source key |
|---|---|---|---|---|
| P15 | Project label for the discrete prize problem on decreasing families and cover costs (Talagrand-style selector/price conjecture) | Naming only. | `mapped` | `p15-realized-covers` |
| decreasing family `D` (downset) | Family of subsets of a finite ground set `X` closed under taking subsets | `Finset (Finset X)` with `IsLowerSet` (Mathlib `IsLowerSet`, `Finset.powerset`), or `Set (Finset X)` lower set. | `mapped` | `p15-realized-covers`, `p15-full-price` |
| original coordinate blocks `X_i`, `|X_i| = a_i d_i + 1` | A partition of the ground set into disjoint blocks of prescribed sizes | `Finpartition` or an indexed family of disjoint `Finset`s. | `mapped` | `p15-full-price` |
| demand `d_i`, capacity `a_i` | Integer parameters of the realized family: `U ∈ D` iff `|U ∩ X_i| ≤ a_i` for all `i` and the occupied-block support contains no `H`-edge | Direct predicate on `Finset X`. | `mapped` | `p15-full-price` |
| clutter `H` of block supports; `H`-edge | Antichain (Sperner family) of subsets of the block index set | `Finset (Finset ι)` with `IsAntichain (· ⊆ ·)`. | `mapped` | `p15-full-price` |
| `O_K(D)`: sets not partitionable into at most `K` members of `D` | Complement of the `K`-fold "union closure" of `D` | Definable: `¬ ∃ parts : Fin K → Finset X, (∀ j, parts j ∈ D) ∧ ⋃ parts = S`. | `mapped` | `p15-full-price` |
| palette `P_i`, palette size `K_H(d)` | Assignment of colour sets to blocks with `|P_i| ≥ d_i` and empty intersection over every `H`-edge; `K_H(d)` the least number of colours | Finite combinatorial minimum: `Finset.min'` over a decidable predicate, or `Nat.find`. | `mapped` | `p15-full-price` |
| generator `g`, cost `Π_{v∈g} c_v`; cover cost `covercost_c(F)` | Weighted set cover: a family of generators whose union-closure contains `F`; cost is the sum of products of prices | `Finset.prod`, `Finset.sum`; the infimum over covers is `sInf` on `ℝ≥0∞` or a finite minimum. | `mapped` | `p15-full-price`, `p15-price-budget` |
| price `c_v`, transformed price `c_v ≤ φ(p_v)`, `φ(p) = min(1, −log(1−p))` | Weight per coordinate bounded by a hazard-type transform of its probability | `Real.log`, `min`; extended value at `p = 1` handled by the `min`. | `mapped` | `p15-full-price` |
| global hazard `−log μ_p(D)`; hazard transfer / hazard interpolation lemma | `μ_p` = product Bernoulli measure; hazard = negative log probability of `D`; the lemma transfers hazard from coordinates to the family | `PMF.bernoulli`, product measures on `Finset X → Bool` (`MeasureTheory.Measure.pi`); `μ_p(D)` as a finite sum. | `mapped` | `p15-full-price` |
| sharp uniform factor `rho_star = 1/(3 − log(3e−2))`, bounds (F3) | Explicit real constant with decimal enclosure | `Real.exp`, `Real.log`; enclosure `0.845… < ρ* < 0.845… < 6/7` provable with `Real.exp_bound`/`Real.log` inequalities — a natural next `norm_num`-style target. | `mapped` | `p15-full-price`, `p15-full-price-output` |
| realized covers, cover threshold 816 / 818 | Specific finite instance: minimal cover size for the realized family vs. whole ground set | Finite decidable statement; `decide` may be too slow, use explicit witness + verification. | `mapped` | `p15-realized-covers` |
| demand-one counterexample (price boundary) | Explicit finite instance falsifying the unrestricted transformed-price extension | Finite computation; `decide`/`norm_num` on explicit data. | `mapped` | `p15-price-boundary` |

## C. Process terms (not mathematical objects)

| Term | Meaning | Formal counterpart |
|---|---|---|
| author-side | Written by the author (human or AI) without a qualifying nonauthor review | `authorship` field; never a Lean object |
| same-author replay | Tests/mutants/`run_validation` rerun by the author's tooling | Layer 0 evidence; not a proof |
| nonauthor analytic review | Independent reading of the informal proof | Distinct from lane F2 (statement alignment) |
| reconnaissance memo | Literature/novelty comparison | Cited in glossary rows for `pending` terms |
| `PROVED_REVIEWED`, `CONTROLLING_ELIGIBLE`, `REQUIRED_SATISFIED` | Math- hard-gate scientific-status labels | Never implied by `kernel-checked`; see `FORMAL_VERIFICATION.md` §4 |
| `lemma_closed` | Campaign Boolean for closed obligations | Never written by formal tooling |

## D. Rules for extending this glossary

1. One row per term, quoting the defining bytes' catalog key. Do not paraphrase a definition
   from memory; read the exact artifact.
2. A theorem may be labelled `specified` only if every term in its Lean statement has a row with
   status `mapped` or `partial` **and** the `partial` convention is fixed in the Lean file's
   docstring.
3. Changing a row's standard meaning is a semantic change: it stales any `alignment_review:
   accepted` that relied on it (record the row ID in the review).
4. Do not remove rows; mark superseded meanings and point to the successor.
