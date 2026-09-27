# main PR134 merged — claims firewall fail-closed hardening (note-only)

**Date:** 2026-09-27T18:43Z.  
**Merge:** `8fb541e3736e21dae02b1b10fbcc4722aceeb2c0`  
**Head:** `8f5818098b0622c99f5b37b57f0184bf4f5fd0e0`  
**Scientific effect:** NONE. Engineering firewall fail-closed on malformed/unknown carrier inputs; committed claim graph unchanged; no grade moves. Does not flip `lemma_closed` / prizes / premises / `LANDING_CLAIMS`.

## Why note-only

`main` is **not** in the meta-framework catalog fetch allowlist. Exact identities remain on `main@8fb541e3…` / tip `8f581809…`.

## Diff surface (not cataloged)

`tools/claims_check.py` (`CarrierIndexUnreadable`, unknown-carrier / non-string status refusals, `certifying_without_evidence` summary), `tests/test_claims_firewalls.py`, `claims/README.md` FW-FLOAT-NOT-CERTIFIED row.

## Non-claims

- No mathematical review; no independence credit claimed by meta-framework.
- Does not retarget trial PR138.
- Does not authorize main allowlist expansion.

Cross-ref: `multi-agent-dispatch-20260925-v77`.
