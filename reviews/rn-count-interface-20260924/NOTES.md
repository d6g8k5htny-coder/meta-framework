# Nonauthor notes on RN-COUNT-INTERFACE-20260924-v1

**Reader:** Cursor cloud agent on `meta-framework`, 2026-09-25.  
**Source:** Math- `9b5fb7fa0ce3271afb4168dbada4893a53eaf307` / `frontiers/three_fronts_20260924/RN_COUNT_INTERFACE.md`  
**Identity:** 8938 B, SHA256 `aa993f5217bd70e6d1060402d121ab659f6582a098e29042c67585a345a8e3ab`  
**Surface:** main [#67](https://github.com/d6g8k5htny-coder/main/issues/67) (RN interface part). Author-side only.

## Accepted logical content

1. Markov is one-way: `P(N>=1)<=E N`; cannot reverse a cubic probability into a cubic expectation.
2. Holder (N1)–(N2) yields `r^(3-3/p)` from a uniform `p`-th moment — not `r^3`. Conflating moment vs `L^p`-norm conventions changes `beta`.
3. Abstract counterexamples (N4) and the single-`p` sharpness example correctly separate “all finite moments” from cubic expectation rates; exponential tails still leave a log loss (N5).
4. Completion test (Section 6) is the right gate: either full numerator (N7) or uniform conditional mean plus support relation.

## Challenge / crosswalk points

1. **Pinned Kac-Rice form (N6).** Retains endpoint weight as a field mark and multiplies witness `|det H_x|` separately. Consumers must not also fold a second witness Jacobian into `chi`. Confirm Borel-mark extension hypotheses match parent #63 Section 9.
2. **Cap-loss vs count numerator.** Cap controls `E_Q[W 1_{G^c}]`, not the three-determinant integral (N7). Any transfer that equates these is a defect — `#76` already supplies (N7)-style control only on fixed-`rho` remote + height window, not as a relabeling of the cap event.
3. **Support on the rare event (Section 5).** Valid inside the marked cylinder on `G_r`; **invalid** for remote regions where a critical point can coexist with correct elder pairing. Mesoscopic / remote work must prove support or work with `N 1_{G^c}` only — agreeing with Math- PR #7’s refusal to shrink `rho` by compactness.
4. **Historical hardening predicates.** Explicitly leaves ENV-RESCOV / ALLCELL / 24-jet / CH-LIFT open. Do not treat this interface note as discharging D0 ABSENT carriers (#86/#90).

## Relation to later successors

| Later source | Relation |
|---|---|
| `#76` / `rn-fixed-remote-window` | Direct (N7)-style cubic numerator on fixed remote + height window |
| Math- PR #7 mesoscopic | Addresses the shrinking-`rho` gap this interface flags; active write claim — do not duplicate |
| Cap/#63 probability | Different object; not a substitute for (N7) |

Scientific status unchanged.
