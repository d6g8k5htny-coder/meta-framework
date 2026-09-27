import Mathlib

/-!
# SIDE24 image ledger — Layer 1 formal pilot

Informal source (Layer 0 identity, not modified here):

* repository `d6g8k5htny-coder/Math-`, commit `e329fba1e927a12dbb4f0d1556f85f39284d17a9`
* `coefficients/side24_v1/PROOF.md`, SHA256
  `c06daccc4ba4b9168522b9888b76a7d599934fc3b91bd753ee5d492262917769`, section 2 and the
  numerical constants of sections 3–4
* `coefficients/side24_v1/coefficient.py`, SHA256
  `03ae6d0f15160cb681f9bbb19a84dc861c3a0db3e881291ea621061cc90c86ab`, function `image_ledger`

Every theorem below is a self-contained statement about real or rational numbers. The
kernel checks exactly these statements. Nothing here formalizes the Gaussian field, the
covariance `K_24`, the coefficient `c_{d,24}`, the parent Kac–Rice argument, or the
identification of the ledger constants with those objects; that alignment is recorded in
`formal/STATEMENTS.md` and remains subject to nonauthor formalization review.

Disposition: author-side (Cursor) formalization; scientific effect NONE.
-/

namespace Side24.ImageLedger

open Real Finset

/-! ### Exact integer and rational ledger constants -/

/-- PROOF.md eq. (2): the image constant `1458·(76·24⁶ + 15)`. -/
theorem image_constant_eq : (1458 : ℕ) * (76 * 24 ^ 6 + 15) = 21175738586478 := by
  norm_num

/-- `E := image_constant · 10⁻¹²⁵` as an exact rational. -/
def E : ℚ := 21175738586478 / 10 ^ 125

/-- `ε := 10⁻¹⁰⁸`, the multiplicative covariance allowance of PROOF.md eq. (3). -/
def eps : ℚ := 1 / 10 ^ 108

/-- `10⁻¹⁰⁶`, the reported relative bound of PROOF.md eq. (4). -/
def relativeBound : ℚ := 1 / 10 ^ 106

/-- PROOF.md eq. (3): `60·E < ε`. -/
theorem sixty_E_lt_eps : 60 * E < eps := by
  unfold E eps; norm_num

/-- PROOF.md §4: `32·ε < 10⁻¹⁰⁶`. -/
theorem thirty_two_eps_lt_relativeBound : 32 * eps < relativeBound := by
  unfold eps relativeBound; norm_num

/-- PROOF.md §4: `ε < 1/28`, the smallness hypothesis used for the log/exp bounds. -/
theorem eps_lt_one_div_28 : eps < 1 / 28 := by
  unfold eps; norm_num

/-! ### `e^(288/125) > 10` and `e^(-288) < 10^(-125)` -/

/-- PROOF.md §2 / `coefficient.py` `image_ledger`: `e^(288/125) > 10`, proved from the
positive Taylor partial sum through order 20 (`Real.sum_le_exp_of_nonneg`). -/
theorem ten_lt_exp_288_div_125 : (10 : ℝ) < Real.exp (288 / 125) := by
  have h := Real.sum_le_exp_of_nonneg (x := (288 / 125 : ℝ)) (by norm_num) 21
  refine lt_of_lt_of_le ?_ h
  simp only [Finset.sum_range_succ, Finset.sum_range_zero, Nat.factorial]
  norm_num

/-- `10¹²⁵ < e^288`, since `e^288 = (e^(288/125))^125`. -/
theorem ten_pow_125_lt_exp_288 : (10 : ℝ) ^ 125 < Real.exp 288 := by
  have h : Real.exp 288 = Real.exp (288 / 125) ^ 125 := by
    rw [← Real.exp_nat_mul]; norm_num
  rw [h]
  exact pow_lt_pow_left₀ ten_lt_exp_288_div_125 (by norm_num) (by norm_num)

/-- PROOF.md §2: `e^(-288) < 10^(-125)`. -/
theorem exp_neg_288_lt : Real.exp (-288) < 1 / 10 ^ 125 := by
  rw [Real.exp_neg, inv_eq_one_div]
  exact one_div_lt_one_div_of_lt (by positivity) ten_pow_125_lt_exp_288

/-! ### Geometric decay of the image tail terms -/

/-- The `j`-th image tail term `j⁹ e^(-288 j²)` of PROOF.md §2, indexed by `j ≥ 1`. -/
noncomputable def tailTerm (j : ℕ) : ℝ := (j : ℝ) ^ 9 * Real.exp (-288 * (j : ℝ) ^ 2)

theorem tailTerm_nonneg (j : ℕ) : 0 ≤ tailTerm j := by
  unfold tailTerm; positivity

/-- `512 · e^(-864) < 1/2`, via `e^864 = (e^432)² ≥ 433² > 1024`. -/
theorem five_twelve_exp_neg_864_lt_half : 512 * Real.exp (-864) < 1 / 2 := by
  have h432 : (433 : ℝ) ≤ Real.exp 432 := by
    have := Real.add_one_le_exp (432 : ℝ); linarith
  have h864 : (1024 : ℝ) < Real.exp 864 := by
    have h : Real.exp 864 = Real.exp 432 ^ 2 := by
      rw [← Real.exp_nat_mul]; norm_num
    rw [h]
    nlinarith [h432]
  rw [Real.exp_neg]
  have hpos : 0 < Real.exp 864 := Real.exp_pos _
  rw [mul_inv_lt_iff₀ hpos]
  linarith

/-- PROOF.md §2: successive image tail terms have ratio at most `512 e^(-864) < 1/2`. -/
theorem tailTerm_succ_le_half (j : ℕ) (hj : 1 ≤ j) :
    tailTerm (j + 1) ≤ (1 / 2) * tailTerm j := by
  unfold tailTerm
  have hj' : (1 : ℝ) ≤ j := by exact_mod_cast hj
  push_cast
  have hpow : ((j : ℝ) + 1) ^ 9 ≤ 512 * (j : ℝ) ^ 9 := by
    have h2 : (j : ℝ) + 1 ≤ 2 * j := by linarith
    calc ((j : ℝ) + 1) ^ 9 ≤ (2 * (j : ℝ)) ^ 9 := by gcongr
      _ = 512 * (j : ℝ) ^ 9 := by ring
  have hexp : Real.exp (-288 * ((j : ℝ) + 1) ^ 2)
      ≤ Real.exp (-864) * Real.exp (-288 * (j : ℝ) ^ 2) := by
    rw [← Real.exp_add]
    apply Real.exp_le_exp.mpr
    nlinarith
  have hE : 0 ≤ Real.exp (-288 * (j : ℝ) ^ 2) := (Real.exp_pos _).le
  have hj9 : 0 ≤ (j : ℝ) ^ 9 := by positivity
  calc ((j : ℝ) + 1) ^ 9 * Real.exp (-288 * ((j : ℝ) + 1) ^ 2)
      ≤ (512 * (j : ℝ) ^ 9) * (Real.exp (-864) * Real.exp (-288 * (j : ℝ) ^ 2)) := by
        apply mul_le_mul hpow hexp (Real.exp_pos _).le (by positivity)
    _ = (512 * Real.exp (-864)) * ((j : ℝ) ^ 9 * Real.exp (-288 * (j : ℝ) ^ 2)) := by ring
    _ ≤ (1 / 2) * ((j : ℝ) ^ 9 * Real.exp (-288 * (j : ℝ) ^ 2)) := by
        apply mul_le_mul_of_nonneg_right five_twelve_exp_neg_864_lt_half.le
        positivity

/-- Each tail term is dominated by the geometric envelope `e^(-288) (1/2)^k`. -/
theorem tailTerm_le_geometric (k : ℕ) :
    tailTerm (k + 1) ≤ Real.exp (-288) * (1 / 2) ^ k := by
  induction k with
  | zero => simp [tailTerm]
  | succ n ih =>
    calc tailTerm (n + 1 + 1) ≤ (1 / 2) * tailTerm (n + 1) :=
          tailTerm_succ_le_half (n + 1) (Nat.le_add_left 1 n)
      _ ≤ (1 / 2) * (Real.exp (-288) * (1 / 2) ^ n) := by gcongr
      _ = Real.exp (-288) * (1 / 2) ^ (n + 1) := by ring

/-- PROOF.md §2: `∑_{j ≥ 1} j⁹ e^(-288 j²) ≤ 2 e^(-288)`. -/
theorem tsum_tailTerm_le : ∑' k : ℕ, tailTerm (k + 1) ≤ 2 * Real.exp (-288) := by
  have hg : Summable fun k : ℕ => Real.exp (-288) * (1 / 2 : ℝ) ^ k :=
    summable_geometric_two.mul_left _
  have hf : Summable fun k : ℕ => tailTerm (k + 1) :=
    Summable.of_nonneg_of_le (fun k => tailTerm_nonneg _) tailTerm_le_geometric hg
  calc ∑' k : ℕ, tailTerm (k + 1)
      ≤ ∑' k : ℕ, Real.exp (-288) * (1 / 2 : ℝ) ^ k :=
        hf.tsum_le_tsum tailTerm_le_geometric hg
    _ = Real.exp (-288) * ∑' k : ℕ, (1 / 2 : ℝ) ^ k := tsum_mul_left
    _ = 2 * Real.exp (-288) := by rw [tsum_geometric_two]; ring

/-- Consequently the tail is below `2 · 10^(-125)`, the form used in PROOF.md eq. (2). -/
theorem tsum_tailTerm_lt : ∑' k : ℕ, tailTerm (k + 1) < 2 / 10 ^ 125 := by
  have h := tsum_tailTerm_le
  have h2 := exp_neg_288_lt
  calc ∑' k : ℕ, tailTerm (k + 1) ≤ 2 * Real.exp (-288) := h
    _ < 2 * (1 / 10 ^ 125) := by linarith
    _ = 2 / 10 ^ 125 := by ring

/-! ### The elementary cone integral of PROOF.md §1 -/

/-- PROOF.md §1: `∫₀ᵃ (a - z)² e^(-z/2) dz / 2 = a² - 4a + 8 - 8 e^(-a/2)` for `a ≥ 0`.
The hypothesis `0 ≤ a` is not needed for the identity but matches the informal statement. -/
theorem cone_integral (a : ℝ) (_ha : 0 ≤ a) :
    ∫ z in (0 : ℝ)..a, (a - z) ^ 2 * Real.exp (-z / 2) / 2
      = a ^ 2 - 4 * a + 8 - 8 * Real.exp (-a / 2) := by
  have hderiv : ∀ z ∈ Set.uIcc (0 : ℝ) a,
      HasDerivAt (fun z : ℝ => -(Real.exp (-z / 2) * ((a - z) ^ 2 - 4 * (a - z) + 8)))
        ((a - z) ^ 2 * Real.exp (-z / 2) / 2) z := by
    intro z _
    have h1 : HasDerivAt (fun z : ℝ => -z / 2) (-1 / 2) z := by
      simpa using ((hasDerivAt_id z).neg).div_const 2
    have h2 : HasDerivAt (fun z : ℝ => Real.exp (-z / 2)) (Real.exp (-z / 2) * (-1 / 2)) z :=
      h1.exp
    have h3 : HasDerivAt (fun z : ℝ => (a - z) ^ 2 - 4 * (a - z) + 8)
        (2 * (a - z) * (-1) - 4 * (-1)) z := by
      have hs : HasDerivAt (fun z : ℝ => a - z) (-1) z := by
        simpa using (hasDerivAt_id z).const_sub a
      have := ((hs.pow 2).sub (hs.const_mul 4)).add_const 8
      convert this using 1
      push_cast; ring
    have := (h2.mul h3).neg
    convert this using 1
    ring
  have hcont : ContinuousOn (fun z : ℝ => (a - z) ^ 2 * Real.exp (-z / 2) / 2)
      (Set.uIcc (0 : ℝ) a) := by
    fun_prop
  rw [intervalIntegral.integral_eq_sub_of_hasDerivAt hderiv hcont.intervalIntegrable]
  simp only [sub_zero, neg_zero, zero_div, Real.exp_zero]
  ring

end Side24.ImageLedger
