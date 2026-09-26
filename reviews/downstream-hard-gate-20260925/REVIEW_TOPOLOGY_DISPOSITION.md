# Distinct-lane disposition — governance- PR4 `REVIEW_TOPOLOGY.md`

**Date:** 2026-09-25T18:38Z.  
**Reviewer lineage:** Cursor meta-framework agent `bc-01a0d95b-5971-7bb3-a1ce-5090c49d5cb8` (distinct from OpenAI author).  
**Target:** governance- PR #4 tip `da195ed4f4c2f7d59e0fe05539cf0e7021b3de80`  
**Path:** `REVIEW_TOPOLOGY.md`  
**Identity:** 4695 B, SHA256 `87fa5e5508d9a0646ee322ffce7c4e99072f38eeb01d1aaa31f2dae31080ea2e`  
**Gate satisfied:** main PR98 tip `044928047dc330724bd7829744d7898dee2cada5` verify/navigation/loss-only **green**.  
**Disposition:** `AMEND_REQUIRED`  
**Scientific effect:** NONE. No edit to governance- in this step (findings return to author).

## Clause verdicts

| ID | Verdict | Notes |
|---|---|---|
| T1 | **AMEND_REQUIRED** | Independence is stated as validator-derived “where possible,” but this file is prose only. Amend to name the **machine home** (main `#95` v1.2 `review_records[]` / scientific_state checker) and state explicitly that markdown alone cannot qualify a review as `independent=true`. |
| T2 | ACCEPT | Orthogonal axes + “status engine consumes only qualifying review records”; does not create a second theorem-status register. |
| T3 | ACCEPT | Fail-closed rule 2: digest change stales prior reviews. |
| T4 | ACCEPT (policy) | Partial-scope ban is clear; machine containment still depends on schema companion. |
| T5 | ACCEPT | Rule 8 separates emergency merge from scientific-status change. |
| T6 | **AMEND_REQUIRED** | Same-family default `independent=false` is good, but the exception path (“explicit project policy”) is underspecified. Amend to require that any exception policy is itself an **exact cataloged identity** with machine-checkable lineage tokens. |
| T7 | ACCEPT | Rule 5: reviewer edits ⇒ amendment evidence; fresh distinct-lineage review required. |
| T8 | **AMEND_REQUIRED** | Negative controls (self-review, stale-digest, partial-scope, accept-after-amend) are required by `#95` v1.2 commentary but **absent from this file**. Amend to mandate those controls (inline or normative cross-ref to the schema PR that owns them). |

## What not done

- No edit to `REVIEW_TOPOLOGY.md` (no edit-and-approve).
- No merge recommendation until OpenAI amends and a distinct lane re-checks the new digest.
- PR98 green does **not** close `#90` (Math- PR15 replay still failing; pins/RESULTS pending).

Cross-ref: `review-topology-challenge`, `multi-agent-dispatch-20260925-v5`.
