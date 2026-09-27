# main PR180 merged — release custody snapshot + Lean toolchain replay (note-only)

**Date:** 2026-09-27T22:38Z.  
**Merge:** `4c5bc12f6f91f6bb45e98afc47d53c4ddd52507d`  
**Head:** `86c34eeae8244621e10418df0b065962d4ba34d4`  
**Scientific effect:** NONE. Read-only release snapshot tooling and pinned Lean toolchain replay. Does not flip `lemma_closed` / prizes / premises / `LANDING_CLAIMS`.

## Why note-only

`main` is **not** in the meta-framework catalog fetch allowlist. Exact identities remain on `main@4c5bc12f…` / tip `86c34eea…`.

## Diff surface (not cataloged)

`tools/release_snapshot.py`, `tools/formal_execution_context.py`, tests, `.github/workflows/release-snapshot.yml`, `docs/RELEASE_OPERATIONS.md`, superpowers plan/spec.

## Non-claims

- No mathematical review; no independence credit claimed by meta-framework.
- Does not retarget trial PR138; never touches #91.
- Does not authorize main allowlist expansion.

Cross-ref: `multi-agent-dispatch-20260925-v84`.
