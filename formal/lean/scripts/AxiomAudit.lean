import Side24Formal
import Lean

/-!
# Axiom audit for the Layer 1 pilot

Run from `formal/lean` after `lake build`:

    lake env lean scripts/AxiomAudit.lean > axioms.txt

For every theorem under the `Side24` namespace this prints one line

    AXIOMS <declaration> [<axiom>, ...]

followed by `DECLARED_AXIOM <name>` for every `axiom` declared under `Side24`, and the totals
`AUDIT_THEOREMS <count>` and `AUDIT_SORRY <count>`.

Policy enforced here (nonzero exit on violation):

* Core axioms `propext`, `Classical.choice`, `Quot.sound` are always allowed.
* `sorryAx` is tolerated only so that a statement can be catalogued as `specified`; it is
  counted and reported, and `tools/formal_status_check.py` refuses any theorem that uses it
  unless the catalog lists exactly that theorem with status `specified`.
* Project assumptions must be declared as `axiom`s under `Side24.Assumptions`; they are
  reported and the catalog must list them under `assumed_axioms`. Any other axiom — including
  `Lean.ofReduceBool` from `native_decide` and axioms declared elsewhere — fails immediately.
-/

open Lean Elab Command

namespace Side24.Audit

def coreAxioms : List Name := [``propext, ``Classical.choice, ``Quot.sound]

def assumptionsRoot : Name := `Side24.Assumptions

def isTolerated (a : Name) : Bool :=
  coreAxioms.contains a || a == ``sorryAx || assumptionsRoot.isPrefixOf a

elab "#audit_axioms " ns:ident : command => do
  let env ← getEnv
  let root := ns.getId
  let mut theorems : Array Name := #[]
  let mut declaredAxioms : Array Name := #[]
  for (n, ci) in env.constants.toList do
    if root.isPrefixOf n && !n.isInternal then
      match ci with
      | .thmInfo _ => theorems := theorems.push n
      | .axiomInfo _ => declaredAxioms := declaredAxioms.push n
      | _ => pure ()
  let sorted := theorems.qsort (fun a b => a.toString < b.toString)
  let mut bad : Array (Name × Name) := #[]
  let mut sorryCount : Nat := 0
  for n in sorted do
    let collected ← collectAxioms n
    let axioms := collected.qsort (fun a b => a.toString < b.toString)
    logInfo m!"AXIOMS {n} {axioms.toList}"
    if axioms.contains ``sorryAx then
      sorryCount := sorryCount + 1
    for a in axioms do
      if !isTolerated a then
        bad := bad.push (n, a)
  for a in declaredAxioms.qsort (fun a b => a.toString < b.toString) do
    logInfo m!"DECLARED_AXIOM {a}"
    if !assumptionsRoot.isPrefixOf a then
      bad := bad.push (a, a)
  logInfo m!"AUDIT_THEOREMS {sorted.size}"
  logInfo m!"AUDIT_SORRY {sorryCount}"
  if sorted.isEmpty then
    throwError "axiom audit found no theorems under namespace {root}"
  if !bad.isEmpty then
    throwError "disallowed axioms: {bad.toList}"

end Side24.Audit

#audit_axioms Side24
