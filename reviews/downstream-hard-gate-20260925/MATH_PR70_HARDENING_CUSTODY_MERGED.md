# Math- PR70 merged — hardening-commit proof custody

**Date:** 2026-09-26T16:00Z.  
**Merge:** `9d7b6802424fb4715b31999066aafca8ee2f3cca`  
**Head (pre-merge tip):** `44901b5c17bdaddaf2fc8444aaf9b1d7a38b5f3d`  
**Prior freeze head:** `b39e9ff7764635e4075cf53b0c22c4c5f25a61e7`  
**Scientific effect:** NONE. Default-branch custody only; does not flip `lemma_closed` / prizes / premises / `LANDING_CLAIMS`.

## Cataloged identities (Math- @ merge)

| Key | Path | Bytes | SHA256 |
|---|---|---:|---|
| `hardening-custody-manifest` | `imports/hardening_ebedb780/MANIFEST.json` | 18262 | `fa7f33839924d340cc1123fe05276f681e6aa12193c68b2d1aa6ab489150d8e3` |
| `hardening-custody-verify` | `imports/hardening_ebedb780/verify.py` | 4198 | `d2959cd27af0ac18f77328c095e3eedc65ce25881044b5c0a98413a50dffeb86` |
| `hardening-custody-readme` | `imports/hardening_ebedb780/README.md` | 7605 | `363ca7e91586e547d4bb62425c73a3cb1f8484c7b8470960945862467be41270` |

MANIFEST sha matches the pre-bound tip-drift identity (`math-pr70-tip-drift-44901b5c`). Git blob for MANIFEST remains `4cc679d65d8af2162fa9915ad7edf35fda16a576`.

## BYTE_COPY rows (pinned by MANIFEST; not re-cataloged individually)

Nine `BYTE_COPY` destinations under `imports/hardening_ebedb780/` are identity-pinned by the MANIFEST above. OpenAI Sol independently reconciled all nine on freeze `b39e9ff7…` (`oa-pr70-byte-copy-verify-20260926`). Post-merge author note confirms `verify.py` exit 0 on `main` and byte-identical `LANDING_CLAIMS` / `PROOF_INDEX` vs pre-merge main. `P15-B` destination sha matches existing catalog key `p15-b-original` — not duplicated.

| Id | Bytes | SHA256 |
|---|---:|---|
| `EC-014` | 11331 | `c5e64b9ba3a906535f1ae58a161d594a427371599c102ae4a68849b087a2f62c` |
| `EC-015` | 7196 | `773b49b6d6930915d452a15243c89e32efa181b2ba7d42ae863c9dbc19393752` |
| `EC-021` | 8269 | `1b9a56a1b4ecca99452743e2f010717f1eca753cf0c7c7919677490cae0072ba` |
| `P02-LM-001` | 17261 | `a07d7df63e1f5810ba6bad5576a80afcbfb02deab0790d7804f45ab9dc798ea0` |
| `P02-LM-002` | 9748 | `0f8f80922feb603e5b6e530eb885a7819b3a98d90d3c42d60a68259af766f7de` |
| `P02-LM-005` | 15009 | `0fe0fad5d8e5519cac0e57a42181aa53560bb38d94f23aea51b63be3f182df8b` |
| `P02-LM-007` | 12936 | `7de9525399327ae512c399274732faeee24e3de5bf7d6d3bc1440837a12ab2fc` |
| `P02-LM-008` | 12160 | `06967d0ba2c2d20550f3bd86ddc97981e324e5f94cd7710996445d507ae2285b` |
| `P15-B` | 6286 | `9b18b6e9abc90d18deef06ab12e3aa7794dad40e1618d99daa88e369c300e8c3` |

`main#59` remains `TRANSCRIPTION` / `not_original_bytes:true` (6819 B, sha `a41bb347…`) — not counted as byte custody.

## Non-claims

- No mathematical review; no independence credit claimed by meta-framework.
- Does not retarget trial PR138.
- Does not authorize main allowlist expansion.

Cross-ref: `oa-pr70-custody-claim-watch`, `oa-pr70-byte-copy-verify-20260926`, `math-pr70-tip-drift-44901b5c`, `multi-agent-dispatch-20260925-v51`.
