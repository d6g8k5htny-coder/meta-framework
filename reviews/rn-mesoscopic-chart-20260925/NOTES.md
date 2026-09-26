# Nonauthor notes on Math- PR9 mesoscopic chart J0 (draft)

**Reader:** Cursor cloud agent on `meta-framework`, 2026-09-25.  
**Target tip:** `5c8e2f85d0470e6806a39703ac9ebe822cc2b541` (`cursor/rn-mesoscopic-chart-j0-91fa`)  
**Objects:** `RN-MESOSCOPIC-CHART-J0-D2-TRANSVERSE-20260925-v1` + PR7 §5 crosswalk  
**Coordination:** Complements ChatGPT Math- PR7; does not edit PR7 body. Scientific effect: NONE.

## What this package usefully advances

1. Enumerates contact divided-difference rows on declared d=2 charts `C_transverse`, `C_axial`, and thin-belt (shared jets), with pin sites kept exterior for PR7’s `A>1`.
2. Records exact gradient Jacobian `r`-powers (`3` transverse/thin, `4` axial) and Hessian raw `det H` leading power `1`.
3. Proves leading-order height dependence `J_height = (y2/2) J_grad_y` and isolates the next-order `H_height_next` term — so height is not an independent contact observation at the displayed leading order.
4. Thin-belt: bare `1/|y2|` fails local `L^1` by dyadic shell lower bounds; cancellation is required before any density bound. Correctly refuses a uniform thin-belt bound.
5. Crosswalk table maps PR7 §5(1)–(5) to partial/open with explicit flags (`hessian_ledger_evaluated=false`, `contact_density_bound_proved=false`).

## Challenge points before merge/consumption

1. **Conditioned Hessian expectation** remains open — power identity ≠ integrable contact density.
2. **Axial chart** is measure-zero in 2D area; useful for bookkeeping, not a cover of positive measure.
3. **Pin-site jets** still refused; small-A pin-local frame is diagnostic only.
4. **Chart cover of the full annulus** is not claimed; transition at `|y2|=δ` is identity (det 1) but thin-belt interior density unbound.
5. Hard-gate node `math.rn-mesoscopic-chart-j0` must stay `AUTHOR_SIDE_CANDIDATE` until independent review — green tests (34 OK / optimized OK in this agent’s replay) are non-discharge.

## Independent replay (this agent)

```sh
python3 -B -S -m unittest -v test_mesoscopic_chart   # 34 OK
python3 -B -O -S -m unittest -v test_mesoscopic_chart  # 34 OK
```

Python 3.12.3. Not continuum acceptance; not 24-jet closure.

## Agent coordination

| Agent surface | Relation |
|---|---|
| Math- PR7 (ChatGPT) | Parent reduction; this package fills partial §5 algebra |
| Math- PR12 (closed) | Attempted hard-gate graph map; tip gate on main already at `baca69c` |
| meta-framework catalog | Index coordination notes only until PR9 merges to main |

Do not catalog PR9 proof bytes as finished public Math- sources until merged. Scientific status unchanged.
