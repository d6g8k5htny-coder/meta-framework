# Math- PR92 merged — source-bound Lean verification lane

**Date:** 2026-09-27T21:50Z.  
**Merge:** `867d9e34b60186ff46ab5b3ecf8ad5ba6a5cc8b4`  
**Verified head (source tip):** `cc2989c1280f4f227d0c6aa30c8841d6ba01e46e`  
**Scientific effect:** NONE. Engineering formal lane only; preserves scientific verdicts; does not flip `lemma_closed` / prizes / premises / `LANDING_CLAIMS` / PROOF_INDEX ACCEPT rows.

## Cataloged identities (Math- @ merge tip)

| Key | Path | Bytes | SHA256 |
|---|---|---:|---|
| `formal-lean-workflow` | `.github/workflows/formal-lean.yml` | 1807 | `75a0a98b083a35b5192d6a0e5cd253c5c773944bcd88db353c6dd520e4f3660d` |
| `formal-lean-manifest` | `formal/manifest.json` | 3358 | `8a479e7c453ed6171fdbe5e61c315ef6b30ea45b45e5510bfba5cc156976eb3f` |
| `formal-lean-gate` | `formal/gate.py` | 12954 | `4f14a78bbc6e9b7f929648b13ad3a9ae467256db4be9792e3667680e697a5c94` |
| `formal-lean-gate-test` | `formal/tests/test_gate.py` | 8471 | `5df769901bbf53a7a434c2794c8685242ecfdc32f15d72fae8c2030dff7a9aa2` |
| `formal-lean-lakefile` | `formal/lakefile.toml` | 274 | `d629891716c169404d1f0d76492441c8dd66f1e790b1b8b0819e51c8d5059255` |
| `formal-lean-toolchain` | `formal/lean-toolchain` | 25 | `d5edba4e4b8faad9c1baeadb265716d20d03be4d1a2647dc5e35b0c0325bea7b` |
| `formal-lean-lake-manifest` | `formal/lake-manifest.json` | 3553 | `d63753befccc21923783a5085148e3ff028d97134ea52f5a08bd87ecf1b0b043` |
| `formal-lean-core-root` | `formal/ResearchFormalCoreR1.lean` | 90 | `f905b97411b4a8a5e0ba046ba0805dd9889e2276eac072a0e44c0e9b6ee5fe3f` |
| `formal-lean-algebra-v2` | `formal/ResearchFormalCoreR1/AlgebraV2.lean` | 1970 | `4480708263c40a2f7f03f12ef7e15f0eb4f8193c2dccbb253921a7ec251863c3` |
| `formal-lean-probability-v2` | `formal/ResearchFormalCoreR1/ProbabilityCompanionsV2.lean` | 3498 | `338452a0c2ba24d016059354d543cc995b8cb29c9d4a41d98bb93499f5f8cb8f` |
| `formal-lean-original-algebra` | `formal/originals/Algebra.lean.txt` | 1963 | `4c196820c4db8fafc288dd35642828ba577e3544d60aba7d1d6d24f14ad1e8ae` |
| `formal-lean-original-probability` | `formal/originals/ProbabilityCompanions.lean.txt` | 3505 | `4ace6600a476859982c8851ae9097c89b082d3c96291b3c8330bd4cc00bae65d` |
| `formal-lean-scope` | `formal/SCOPE.md` | 3832 | `350732d7a501fd37d15632b13bd2ac30b8a6d87259b9a3b0931639041a1cfb84` |

## Not cataloged (present on tip; retrieval via merge note)

`formal/README.md`, `COMPATIBILITY.md`, `GLOSSARY.md`, `blueprint/src/content.tex`, `evidence/initial-build-failure.log`, `AGENTS.md` delta.

## Peer / CI evidence (inbox only; not re-reviewed here)

- Owner: first Lean run FAILED (compiler repairs in successor); hosted successor then merged.
- Meta-framework is not the reviewer; same-account reviews carry zero organizational-independence credit.

## Non-claims

- No mathematical review; no independence credit claimed by meta-framework.
- Does not promote Lean kernel receipts to prize/theorem acceptance.
- Does not retarget trial PR138; never touches #91.
- Does not authorize main allowlist expansion.

Cross-ref: `multi-agent-dispatch-20260925-v81`.
