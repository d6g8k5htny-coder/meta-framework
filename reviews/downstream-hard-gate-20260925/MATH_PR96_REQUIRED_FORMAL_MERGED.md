# Math- PR96 merged — required formal evidence bound to math-downstream-gates

**Date:** 2026-09-27T23:49Z.  
**Merge:** `22e79e84917e6bf5bec606c21ce713159d12dddf`  
**Verified head:** `ac9cf41252feca47d29ad3c4b5215082702db28a`  
**Scientific effect:** NONE. Engineering enforcement binding fresh formal evidence to the existing required `math-downstream-gates` check. Does not flip `lemma_closed` / prizes / premises / `LANDING_CLAIMS`.

## Cataloged identities

| Key | Path | Bytes | SHA256 | Posture |
|---|---|---:|---|---|
| `math-pr96-agents` | `AGENTS.md` (Math-) | 2668 | `89f9ef3d6ff5941ba6a417ef2ad64f9e14e436c717cb16ddb2aedf14d6d98fc1` | exact pin |
| `formal-required-checks-doc` | `docs/FORMAL_REQUIRED_CHECKS.md` (Math-) | 4184 | `73f344d3f609f2cf6243f13d91dd73682d0fae0a88b272ef92e530c09b2db271` | exact pin |
| `required-formal-check-tool` | `tools/required_formal_check.py` (Math-) | 5274 | `8eeb96bfa7471fb56747919fa2dfcba395182af737523cb1cf7091da28b1ebde` | exact pin |
| `required-formal-check-tests` | `tests/test_required_formal_check.py` (Math-) | 9243 | `37dece6d29d470f0c7ecda729e5fba61bd4808647976345ba108a02d6245ac5b` | exact pin |
| `math-downstream-gate-workflow-pr96` | `reviews/.../MATH_DOWNSTREAM_GATE_WORKFLOW_PR96.yml` (meta) | 6106 | `823879b3d9f920859b3e55b5fe771643ce93a0e6e81bb04241e07fe694d9fa44` | path-collision replica |
| `formal-lean-workflow-pr96` | `reviews/.../MATH_FORMAL_LEAN_WORKFLOW_PR96.yml` (meta) | 2637 | `480f054a5c125e8d76bff76a38bf8f7b01bca879f6fb819fd3a76899ecbdbd61` | path-collision replica |

Workflows collide with frozen `math-downstream-gate-workflow` / `formal-lean-workflow` Math- paths → meta replicas (same pattern as PR79).

## Non-claims

- No mathematical review; no independence credit claimed by meta-framework.
- Enforcement engineering only; never touches #91.

Cross-ref: `multi-agent-dispatch-20260925-v91`.
