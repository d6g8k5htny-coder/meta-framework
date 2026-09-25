# Architecture coordination — #95 v1.1 digests + #90 residual cases

**Date:** 2026-09-25T18:10Z.  
**Sources:** main #86 / #90 / #95 owner comments; live main PR98 tip `d765efaa98b75d066a296c3747084fb8e99abd06`.  
**Lane:** meta-framework routing only (D7 write lease remains on PR98).  
**Scientific effect:** NONE.

## Four orthogonal axes (#95 v1.1)

| Axis | Role | Must not proxy |
|---|---|---|
| `semantic_digest` | H(canonical scientific content + typed deps/sub_obligations) | Manual fingerprint alone |
| `evidence_digest` | H(evidence identities) | Theorem truth |
| `verification_level` | L0–L5 checker/formal depth | Scientific acceptance |
| `scientific_status` | Campaign register disposition | Hash/CI green |

Migration requirement: old records crosswalked, not silently rewritten.

## Residual #90 loss-only cases (assigned to PR98)

1. Edge-only changes must seed reverse impact.
2. Statement/domain/source changes must be detected even if a manual fingerprint is copied unchanged.
3. Changed controlling node must self-hold in impact output.
4. `required` must be JSON boolean exactly (`0` must not skip premises); duplicate edges rejected.

Impact remains revalidation HOLD/proposal only — never promotion permission. Close #90 only after these pass full CI on real hardening `claims/graph.json` before/after inputs.

## What meta-framework does / does not do

- **Does:** record exact tip OID, keep dispatch current, refuse scientific-status flips.
- **Does not:** edit PR98 schema/adapter bodies; does not claim #90 closed while verify is in progress.

Cross-ref: `downstream-hard-gate`, `multi-agent-dispatch-20260925-v2`.
