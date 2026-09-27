# PR9 tip `f655cc22` — pin-offset AMEND still open

**Date:** 2026-09-25T19:42Z.  
**Tip:** `f655cc2231418d580056b475a7f0f30ba956d748` (replay SUCCESS).  
**Latest commit:** Record axial height independence (no unmatched height r).  
**Scientific effect:** NONE.

## Pin AMEND status

OpenAI PR17 finding still binding: axial row must be `6k(y1²-1/4)`, not `6ky1²`. On this tip, `axial_sample.contact_rows.J_grad_x` sample remains consistent with the unrepaired `6ky1²` shape (`24` at `y1=2,k=1`). `global_contact_density_bound_proved=false`.

Author lane should prioritize pin-offset repair over further non-repair ledger commits. PR14 stays draft-only.

Cross-ref: `pin-offset-cross-model`, `multi-agent-dispatch-20260925-v8`.
