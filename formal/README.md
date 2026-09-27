# `formal/` — Layer 1 formal verification pilot

Scientific effect: NONE. A kernel-checked Lean theorem verifies the statement written in the
Lean file at the Lean kernel's trust boundary. It does not verify translation fidelity,
imported informal hypotheses, currentness or nonauthor acceptance. Those obligations stay
where the [working contract](https://github.com/d6g8k5htny-coder/governance-) already puts
them.

Architecture, status vocabulary and the hard-gate extension are specified in
[`docs/FORMAL_VERIFICATION.md`](../docs/FORMAL_VERIFICATION.md). Terminology mapping is in
[`docs/FORMAL_GLOSSARY.md`](../docs/FORMAL_GLOSSARY.md).

## Contents

| Path | Purpose |
|---|---|
| [`lean/`](lean/) | Lake project `Side24Formal` pinned to Lean `v4.35.0-rc3` and Mathlib `v4.35.0-rc3` (`c55e6e78…`) |
| [`lean/Side24Formal/ImageLedger.lean`](lean/Side24Formal/ImageLedger.lean) | Pilot: the SIDE24 image ledger and the §1 cone integral, 15 theorems, standard axioms only |
| [`lean/scripts/AxiomAudit.lean`](lean/scripts/AxiomAudit.lean) | Fail-closed audit: every theorem under `Side24` may depend only on `propext`, `Classical.choice`, `Quot.sound` |
| [`STATEMENTS.md`](STATEMENTS.md) | Alignment ledger: informal statement ↔ Lean declaration, added/dropped hypotheses, what is NOT formalized |

## Why this lives here (handoff note for `Math-`)

The natural home for formal proofs is `Math-` (candidate proofs and reproducible calculations).
This pilot was produced by a Cloud Agent whose write scope is `meta-framework` only (push to
`Math-`/`main` returns 403 for `cursor[bot]`, as recorded in the governance contract). It is
published here as a self-contained, byte-identified handoff so that any agent with `Math-`
write access can move it:

1. Copy `formal/lean/` into `Math-` next to `coefficients/side24_v1/` (or a `formal/`
   directory there), keep the toolchain and manifest pins, and run the workflow steps below.
2. Re-index the moved files in `registry.json` with their new commit/path/hash and update the
   `formalization.lean_artifact` pointers. Do not delete this copy's history; supersede it.
3. Route a nonauthor lane-F2 alignment review at the moved identity.

Until that happens the catalog points at this copy. Both copies are equally kernel-checked;
only the identity differs.

## Reproduce

```sh
# Lean toolchain manager; installs the pinned toolchain on first use.
curl -sSf https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh | sh -s -- -y --default-toolchain none
source ~/.elan/env
cd formal/lean
lake exe cache get              # Mathlib .olean cache (network; several GB)
lake build                      # kernel-checks Side24Formal
lake env lean scripts/AxiomAudit.lean > /tmp/axioms.txt   # nonzero exit on sorry/native_decide/extra axioms
cd ../..
python3 -B -S tools/formal_status_check.py --registry registry.json --lean-root formal/lean --axiom-report /tmp/axioms.txt
```

The last command is stdlib-only and is what CI runs. It re-parses the axiom report,
re-hashes every Lean file the catalog claims, and refuses statuses that the evidence does not
support.

## Authorship and status

Lean proofs here were written with AI assistance (Cursor) and are labelled author-side. The
kernel check is machine evidence; the alignment review in `STATEMENTS.md` is open. Per
artifact, the catalog records `formalization.status` for the artifact's main claim and
`formalization.lemma_status` for its best-formalized component; for `side24-coefficient` the
main claim is `none` and component lemmas are `kernel-checked` once CI has rebuilt them at the
indexed identity.
