# ENG-03 independent replay receipt — 2026-09-25

**Agent:** Cursor cloud on `meta-framework` (Python 3.12.3; `python3.11` not installed in this environment).  
**Meaning:** same-author finite tests and validation wrappers re-executed from published Math- bytes. Not analytic review, not 24-jet closure, not scientific-status change.

## Exact sources replayed

| Package | Commit | Path | Tests |
|---|---|---|---|
| RN fixed-remote | `191ea7d541a486736ba7bbddfd4eac25a6c4567b` | `frontiers/remote_window_20260924` | 28 OK normal; 28 OK optimized (`-O`) |
| P15 full-price | `f9938338f92590108b163ec96901038d84b70bb9` | `frontiers/full_price_20260924` | 36 OK normal |
| SIDE24 coefficient | `e329fba1e927a12dbb4f0d1556f85f39284d17a9` | `coefficients/side24_v1` | 30 OK normal |

Commands (representative):

```sh
python3 -B -S -m unittest -v test_remote_window
python3 -B -O -S -m unittest -v test_remote_window
python3 -B -S -m unittest -v test_full_price
python3 -B -S -m unittest -v test_coefficient
```

## Catalog verify

Sibling-workspace `query- --verify` against the 26-entry catalog (including Drive parent replicas) matched every declared public payload earlier in this run. Catalog CI on PR #6 reported `verify-catalog` SUCCESS.

## Limits

- No mutation-harness re-run beyond what the package unit tests encode (remote-window `run_validation.py` requires an `--output` directory; not invoked in this receipt).
- No Python 3.11 binary available here; 3.12.3 is the independent interpreter used.
- ChatGPT's prior 3.11.16 campaign replay remains a separate observation; this receipt neither confirms nor overwrites it.

Scientific effect: NONE.
