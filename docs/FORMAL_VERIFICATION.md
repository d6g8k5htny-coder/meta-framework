# Formal verification layer — specification and routing

Object: FORMAL-VERIFICATION-LAYER-20260927-v1. Author: Cursor (AI), on the owner instruction of
Dylan Roy (27 September 2026) to incorporate machine-checked formal proof into the existing
provenance/scope/review stack. Disposition: engineering specification and routing; a process
amendment candidate for the [governance contract](https://github.com/d6g8k5htny-coder/governance-).
Scientific effect: NONE. Nothing here flips `lemma_closed`, prizes, premises or any review verdict.

## 1. What this adds and what it leaves alone

The current system is a **Layer 0** stack: byte identities (commit/path/SHA256), explicit scope
statements, distinct review lanes (author derivation, same-author replay, nonauthor analytic
review), the fail-closed Math- hard gate, the work-lease ledger, and the public museum/catalog
surfaces. None of this is replaced.

**Layer 1** adds formal specification and kernel-checked proof. It gives one new kind of
evidence — a proof checked by a small trusted kernel — and one new obligation — verifying that
the formal statement matches the informal one. Everything else (provenance, scope, independence,
scientific acceptance) keeps its existing meaning and owner.

| Kept from Layer 0 | Gained from Layer 1 |
|---|---|
| SHA256/commit binding of every artifact | The Lean source is itself an artifact with the same binding |
| Scope statements and "does not claim" lists | Scope becomes the hypothesis list of a Lean theorem |
| Hard gate: green tests, hashes, self-review are non-discharge | Hard gate: additionally, no `kernel-checked` label without a CI kernel build at the indexed identity |
| Author-side / nonauthor distinction | Same distinction applied to Lean proofs and to statement alignment |
| Reconnaissance memos, explicit open obligations | Unformalized dependencies become explicit Lean `axiom`s with scope notes, or stay listed as NOT formalized |

Formalization status is a **mechanical verification level**. The review topology already
separates "semantic digest, evidence digest, mechanical verification level, scientific status
and review evidence". `kernel-checked` therefore never implies `PROVED_REVIEWED`, and
`PROVED_REVIEWED` never implies `kernel-checked`.

## 2. Status vocabulary

Every proof artifact (claim document) in `registry.json` carries a `formalization` object.
`tools/formal_status_check.py` enforces the rules below; the schema is in §6.

| `status` | Meaning | Required evidence |
|---|---|---|
| `none` | No Lean statement exists for this artifact's main claim | — |
| `specified` | A Lean statement compiles; proof may be `sorry` | `lean_artifact`, `theorems` |
| `proved` | Proof script compiles locally without `sorry` under the pinned toolchain; author-attested | `specified` + `authorship`; axiom audit passes locally |
| `kernel-checked` | The shared CI lane rebuilt the exact indexed Lean bytes, the axiom audit passed (only `propext`, `Classical.choice`, `Quot.sound`), and the run is cited | `proved` + nonempty `evidence` (CI run URL) |

`lemma_status` uses the same vocabulary for the best-formalized *component* of an artifact whose
main claim is not (yet) formal. It never substitutes for `status`.

`alignment_review` records lane F2 (§3): `none`, `open`, `accepted`, `amend_required`. The author
of the Lean file cannot set `accepted`; it requires a nonauthor review bound to the exact Lean
file SHA256 and Mathlib commit. `kernel-checked` with `alignment_review: open` is a legitimate and
expected intermediate state and must be displayed as such.

Downgrades are automatic: a changed Lean byte invalidates `kernel-checked` and `accepted` until
re-run and re-reviewed (the checker compares catalog hashes to the working tree).

## 3. Verification lanes

Existing lanes (unchanged): author derivation; same-author replay (tests, mutants, `run_validation`);
nonauthor analytic review (main issue threads, governance amendments); reconnaissance.

New lanes:

| Lane | What it checks | Who / what | Output |
|---|---|---|---|
| **F1 kernel build** | The Lean file compiles; no `sorry`, `native_decide` or extra axioms | CI (`.github/workflows/formal.yml`: `lake build` + `AxiomAudit.lean` + `formal_status_check.py`) | Run URL → `evidence` |
| **F2 alignment review** | Each Lean statement says what the quoted informal statement says: same quantifiers, domain, constants, normalizations | Nonauthor reviewer (organizational independence graded separately, per review topology) | Verdict bound to Lean SHA256 + Mathlib commit → `alignment_review` |
| **F3 AI-prover cross-check** | An independent prover (e.g. Goedel-Prover, DeepSeek-Prover, AlphaProof-style) produces a kernel-accepted proof of the *same* Lean statement | Optional CI lane or offline run; the kernel check is identical | Recorded as additional evidence, never as independence credit by itself |
| **F4 external review** | Papers in standard terminology (glossary) with the Lean development as supplementary material | Journals / independent formalizers | Links recorded in the artifact `scope`/review threads, not as a status flip |

Lane F2 is the load-bearing new obligation. The kernel proves the theorem; the reviewer checks
that the theorem is the right one. Reviewers do not re-prove and do not grade the informal proof.

## 4. Hard-gate extension (fail-closed)

Implemented in this repository now:

1. **Kernel build in CI.** `formal.yml` runs on every change under `formal/`, `registry.json`
   or `tools/`. It builds the Lake project with the Mathlib cache, runs the axiom audit with the
   allowlist `propext,Classical.choice,Quot.sound`, and then runs `formal_status_check.py`.
2. **Byte binding.** Every catalog artifact whose path ends in `.lean` and lives in this
   repository must hash-match the working tree. Editing a Lean file without re-indexing fails.
3. **Status ≤ evidence.** `kernel-checked` without a CI run URL fails; `specified`/`proved`/
   `kernel-checked` without a resolvable `lean_artifact` fails; `alignment_review: accepted`
   without a nonauthor `alignment_reviewer` fails; any status above `none` for a `.lean`
   artifact that is not a claim document is refused.
4. **Vocabulary is closed.** Unknown status strings, Booleans-as-strings, duplicate JSON keys
   and non-object `formalization` fields are rejected.

Proposed for `Math-` (handoff; requires `Math-` write access and its own exact-replay pins):

- Extend `frontiers/downstream_gate_20260925/hard_gate.py` node records with an optional
  `mechanical_verification` sub-record `{level, lean_identity, ci_run, alignment_review}` using
  the vocabulary above. `CONTROLLING_ELIGIBLE` and `REQUIRED_SATISFIED` are **unchanged**; the
  new record is an additional, displayed criterion, not a replacement for `PROVED_REVIEWED`.
- Add a distinct display tier "kernel-checked and reviewed" = `PROVED_REVIEWED` ∧
  `kernel-checked` ∧ `alignment_review: accepted`. It is a stronger label, not a shortcut: a
  node may reach it only after both the analytic and the formal lanes are complete.
- Regenerate `SOURCE_FILES` pins, `RESULTS` and `run_validation` in the same change, as the
  governance amendment on Math- exact-replay identities requires.

Proposed for `main` (handoff): show the formalization fields of `registry.json` on the museum
pages as their own column ("Formal: none / specified / proved / kernel-checked; alignment:
open/accepted"), sourced from this catalog so no second status register is created.

## 5. Handling the specific challenges

**Non-standard terminology.** [`FORMAL_GLOSSARY.md`](FORMAL_GLOSSARY.md) maps every project term
to a standard object and, where available, to a Mathlib type. A term that cannot be mapped is
either ill-defined or genuinely new; new terms need a definition in Lean and a literature
comparison before any theorem about them is labelled above `specified`.

**Parent theorem dependencies.** Formalize the parent first when feasible. Otherwise introduce it
as an explicit Lean `axiom` in a dedicated `Assumptions.lean` with a docstring: "assumed for this
development; not independently verified; source identity …". The axiom audit will list it, the
catalog must record it under `assumed_axioms`, and the artifact's status is capped at `proved`
(never `kernel-checked` in the unconditional sense) until the axiom is discharged. This is the
formal analogue of the existing "conditional on unreviewed parent" scope sentences.

**Numerical bounds.** Decimal endpoints are exact rationals in Lean; `norm_num` decides them
(pilot rows A1–A4). Special-function bounds go through Mathlib inequalities such as
`Real.sum_le_exp_of_nonneg` and `Real.add_one_le_exp` (rows A5–A7) rather than floating point.
Where the informal proof uses an outward interval computation, the formal target is the same
inequality with rational endpoints, proved by exact arithmetic; the Python interval code stays as
same-author replay evidence, not as the proof.

**AI authorship.** Lean proofs written by an AI agent are author-side. The kernel check is
machine evidence; lane F2 still needs a distinct reviewer, and organizational independence is
graded exactly as the review topology grades it for prose (same provider/model family earns no
credit; unknown provenance earns none).

**Other proof systems.** Lean 4 + Mathlib is the primary backend. Coq and Metamath ports are
optional; if attempted, catalog them as separate artifacts with their own `formalization`
records. AI provers are lane F3 inputs, not backends.

## 6. Catalog schema (`registry.json`, `schema_version` stays 1)

Top-level `formal_verification` object (tolerated by the pinned `query-` loader; documents the
backend, vocabulary and allowlist). Per-artifact `formalization` object:

```json
{
  "status": "none | specified | proved | kernel-checked",
  "lemma_status": "none | specified | proved | kernel-checked",
  "lean_artifact": "<catalog key of the .lean artifact>",
  "theorems": ["Fully.Qualified.Lean.Name", "..."],
  "assumed_axioms": [],
  "alignment_review": "none | open | accepted | amend_required",
  "alignment_reviewer": "<provider / model / agent>, distinct from authorship",
  "alignment_ledger": "formal/STATEMENTS.md",
  "authorship": "<who wrote the Lean proof; label AI authorship explicitly>",
  "evidence": ["https://github.com/.../actions/runs/<id>"],
  "note": "free text: what the formal object does and does not cover"
}
```

Rules are enforced by `tools/formal_status_check.py`; the vocabulary and allowlist live in the
top-level block so that both the checker and readers use one source.

## 7. Repository responsibilities and coordination notice

This section is the cross-repository notice. Agents in every repository should read it before
touching formalization fields, Lean sources or promotion logic. It follows the existing rule that
work is published where the write scope is and coordinated through `main` and the governance
contract.

| Repository | Responsibility under Layer 1 |
|---|---|
| `meta-framework` (this repo) | Owns the specification, glossary, catalog schema, `formal_status_check.py`, and the pilot handoff copy of the Lean project. Routes to formal artifacts; not a status database. |
| `Math-` | Intended canonical home for Lean developments (`formal/` or beside each proof directory). Extends `hard_gate.py` per §4 with regenerated pins. Publishes each new theorem's `STATEMENTS.md` row set. |
| `main` | Campaign discussion: open one issue per formalization target; museum surfaces display the formalization fields from this catalog; `docs/REPRODUCE.md` gains the Lean build steps. |
| `governance-` | Adopts §2–§4 as a process amendment after nonauthor review; adds lane F2 to `REVIEW_TOPOLOGY.md`; work leases for Lean files use `write_scope` prefixes like `formal/lean/`. |
| `query-` | No change required now (extra fields are tolerated). Optional: `--formal` flag printing the `formalization` object for a key. |
| `trial` | Cross-repo engineering test that a moved Lean project still builds; Cloud Agent env may add `elan` install to `.cursor/environment.json` when a repo needs Lean in CI-less runs. |
| `google-drive` | Replicas of Lean sources only if the Drive source is verified public; same custody rules. |
| `sandbox` | Private experiments; nothing exported automatically. |

Write-scope fact (measured 27 September 2026): the Cloud Agent producing this specification can
push only to `meta-framework`; `git push --dry-run` to `Math-` and `main` returned 403 for
`cursor[bot]`. The Lean pilot is therefore published here with a handoff note
([`formal/README.md`](../formal/README.md)). The owner has pre-approved the actions needed to
complete the move; an agent with `Math-` write access should perform steps 1–3 of that note
without requesting re-approval.

## 8. Roadmap and current state

| Step | State (27 Sep 2026) | Next action |
|---|---|---|
| 1. Pilot on SIDE24 | **Done, partial scope.** 15 theorems covering the §2 image ledger (`e^(288/125) > 10`, `e^(-288) < 10^(-125)`, tail ratio `512e^(-864) < 1/2`, tail sum `≤ 2e^(-288)`), the rational ledger constants, and the §1 cone integral. Standard axioms only. The main coefficient bounds are NOT formalized. | Lane F2 review of `formal/STATEMENTS.md`; then §1 Gaussian moments (`D_1 = 4/3`) as the next target. |
| 2. Glossary | v1 published (`FORMAL_GLOSSARY.md`). | Extend as each new theorem is formalized; every new term needs a row before its theorem is `specified`. |
| 3. Formalization review lane | Defined (F2, §3) with reviewer checklist in `STATEMENTS.md`. | Governance amendment; first review assignment via `main`. |
| 4. CI integration | Done here (`formal.yml`, `formal_status_check.py`). Proposed for `Math-` (§4). | Math- author with write access implements the hard-gate sub-record. |
| 5. Expand | Not started beyond the pilot. Candidates in dependency order: SIDE24 §1 moments and formula (1); PRICE-BUDGET exact rational checker statements; P15 full-price sharp factor arithmetic; RN count-interface counterexamples (finite, exact). | One theorem per PR, each with `STATEMENTS.md` rows and glossary entries. |
| 6. External validation | Not started. | After ≥1 full theorem is `kernel-checked` + `accepted`, prepare a standard-terminology note with the Lean development attached. |
| 7. AI-prover cross-check | Not started. | Run an independent prover on the pilot statements; record success/failure as F3 evidence only. |

## 9. Non-goals

- No second scientific-status register. Formalization fields describe the Lean artifact, not
  the theorem's acceptance.
- No reinterpretation of historical evidence: earlier same-author replays, failed pins and
  reviews stay as recorded.
- No claim that Mathlib, Lean or elan are themselves verified beyond their published trust
  boundaries (kernel + `leanchecker`/external checkers when run).
- No private `sandbox` material.
