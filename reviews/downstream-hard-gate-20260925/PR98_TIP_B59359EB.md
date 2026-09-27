# main PR98 tip move — `b59359eb`

**Date:** 2026-09-26T00:51Z.  
**Prior tip:** `69e9b526fa6fea4468475705c599d454427eb603` (noted in `pr98-tip-69e9b526`)  
**New tip:** `b59359ebb972351802c7bf343363811a8e83150b`  
**Parent:** `69e9b526`  
**Headline:** fix(#90): allow unresolved→monitorable when core content unchanged  
**Scientific effect:** NONE. Tip move / CI ≠ `#90` close.

## Engineering read (nonauthor, meta only)

- Base `1ae02b9`→merged tip failed event-compare: attaching Q0 `source_bindings` changed path-level `semantic_digest`, so E6 blocked coverage repair.
- Unresolved→monitorable now gates on `semantic_digest_core` (bindings list removed; statement/edges/scalars remain).
- At poll: navigation + loss-only SUCCESS; verify still IN_PROGRESS.
- Frozen prior tip notes retained; this is the successor tip watch.

## Still required

1. Terminal verify green on `b59359eb` (or newer tip).
2. Retarget trial PR138 off stale subject `cc6a578b`.
3. `#90` transition-gate external immutable bindings + second-source mutation control.

Meta-framework does not edit PR98.

Cross-ref: `pr98-tip-69e9b526`, `pr98-green-readback`, `multi-agent-dispatch-20260925-v30`.
