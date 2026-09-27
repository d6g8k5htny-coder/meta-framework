# main PR188 merged — required formal verification through mandatory verify (note-only)

**Date:** 2026-09-27T23:26Z.  
**Merge:** `3592abbd5df433cb1816b69204e740a7cf00ca07`  
**Head:** `211999277ab8a363dd51320f970e8928b1e0f1e0`  
**Scientific effect:** NONE. Require fresh formal verification through existing mandatory verify check (`required_formal_check`). Does not flip `lemma_closed` / prizes / premises / `LANDING_CLAIMS`.

## Why note-only

`main` is **not** in the meta-framework catalog fetch allowlist. Exact identities remain on `main@3592abbd…` / tip `21199927…`.

## Diff surface (not cataloged)

`tools/required_formal_check.py`, `tests/test_required_formal_check.py`, `docs/FORMAL_REQUIRED_CHECKS.md`, workflow wiring, AGENTS pointer.

## Non-claims

- No mathematical review; no independence credit claimed by meta-framework.
- Does not retarget trial PR138; never touches #91.
- Does not authorize main allowlist expansion.

Cross-ref: `multi-agent-dispatch-20260925-v87`.
