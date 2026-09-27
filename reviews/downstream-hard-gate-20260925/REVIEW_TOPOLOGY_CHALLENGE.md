# Pre-review challenge ledger — governance- PR4 `REVIEW_TOPOLOGY.md`

**Date:** 2026-09-25T18:15Z.  
**Target:** governance- PR #4 tip `da195ed4f4c2f7d59e0fe05539cf0e7021b3de80`  
**Path:** `REVIEW_TOPOLOGY.md`  
**Identity:** 4695 B, SHA256 `87fa5e5508d9a0646ee322ffce7c4e99072f38eeb01d1aaa31f2dae31080ea2e`  
**Author lane:** OpenAI / ChatGPT (will not self-approve).  
**Assigned reviewer lane:** Cursor or other distinct agent **after main PR98 is stable/green** (#86).  
**This note:** meta-framework challenge surface only — **no ACCEPT / AMEND_REQUIRED disposition yet**.  
**Scientific effect:** NONE.

## Why publish now

Owner review-topology rule is live. Preparing exact challenge clauses lets a distinct reviewer fire immediately when PR98 unblocks, without editing governance- from this write-scoped agent.

## Challenge clauses (must return exact clause ids)

| ID | Question | Fail mode if weak |
|---|---|---|
| T1 | Is lineage independence **machine-enforceable**, or only prose? | Self-review slips through as ACCEPTED |
| T2 | Does this create a **duplicate scientific-status authority** vs main registers / Math gate? | Second claim-status database |
| T3 | After semantic amendment, are prior reviews **automatically stale** (digest match required)? | Stale ACCEPT promotes new text |
| T4 | Is **review_scope** containment enforceable so partial review cannot promote broader nodes? | Scope creep promotion |
| T5 | Are **emergency engineering hotfixes** cleanly separated from scientific-status change? | Hotfix = silent acceptance |
| T6 | Same-provider / same-family default `independent=false` — is the exception policy validator-checkable? | Family self-deal |
| T7 | If reviewer patches authored math, does policy force a **fresh distinct-lineage** review of the new digest? | Reviewer-approves-own-patch |
| T8 | Negative controls present/required: self-review, stale-digest, partial-scope, accept-after-amend? | Rules untested |

## Disposition gate (do not fire yet)

Per #86 assignment: only after PR98 reaches a stable/green head, a distinct-lane reviewer may return `ACCEPT` or `AMEND_REQUIRED` with exact clauses. Findings return to OpenAI for amendment; do not edit-and-approve in one step.

Cross-ref: `arch-v11-coordination`, `multi-agent-dispatch-20260925-v3`, main #95 v1.2.
