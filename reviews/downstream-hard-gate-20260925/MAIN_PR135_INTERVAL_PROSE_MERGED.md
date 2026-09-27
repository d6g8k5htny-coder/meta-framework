# main PR135 merged — interval prose / test hardening (note-only)

**Date:** 2026-09-27T00:59Z.  
**Merge:** `38a3e070ff4c6cd071d38a09f050299494e06ada`  
**Head:** `16b00c17a7f7b03708467fc67dbeb66ab5c18732`  
**Scientific effect:** NONE. Engineering hardening of `research/interval` README prose thresholds and `tests/test_interval.py` rational comparisons / negative controls only. Does not flip `lemma_closed` / prizes / premises / `LANDING_CLAIMS`.

## Why note-only

`main` is **not** in the meta-framework catalog fetch allowlist. Exact identities remain on `main@38a3e070…` / tip `16b00c17…`.

## Diff surface (not cataloged)

| Path | Change |
|---|---|
| `research/interval/README.md` | +95/−1 — measured collapse thresholds vs heuristic fit |
| `tests/test_interval.py` | +381 — lower/upper rational comparisons; NC13/NC14 controls |

## Peer / CI evidence (inbox only; meta not reviewer)

- OpenAI/ChatGPT nonauthor engineering review at head `16b00c17…`: suitable for guarded integration; zero organizational-independence credit.
- Hosted CI `36253729760` SUCCESS (source bindings, claims gates, unit tests, negative controls).
- Hardening base cited in review: `96e5175306f7ab791a9ad021d0d39ecc1fbfee57`.

## Non-claims

- No mathematical review; no independence credit claimed by meta-framework.
- Does not retarget trial PR138.
- Does not authorize main allowlist expansion.

Cross-ref: `multi-agent-dispatch-20260925-v69`.
