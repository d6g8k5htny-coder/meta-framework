# Meta-framework — exact-source research routing

[Research home](https://github.com/d6g8k5htny-coder/main) · [Topic guide](https://github.com/d6g8k5htny-coder/main/blob/main/docs/RESEARCH_INDEX.md) · [Run the checks](https://github.com/d6g8k5htny-coder/main/blob/main/docs/REPRODUCE.md) · [Work queue](https://github.com/d6g8k5htny-coder/main/issues/61)

[registry.json](registry.json) maps all eight repository roles and a curated set of public artifacts to exact commits, paths, byte counts, SHA256 identities and scope. It is not a second scientific-status register or a complete Drive inventory. A hash proves identity, not correctness, currentness or independent review.

## Find a source

| Topic | Exact lookup key |
|---|---|
| SIDE24 coefficient | `side24-coefficient` |
| Quantitative lifetime density | `lifetime-remainder` |
| RN probability-to-count interface | `rn-count-interface` |
| P15 original-coordinate family | `p15-realized-covers` |
| P15 unrestricted price counterexample | `p15-price-boundary` |
| P15 restricted transformed-price successor | `p15-price-budget` |
| P15 full probability range and sharp factor | `p15-full-price` |

The catalog contains 18 public artifacts, including code, tests, outputs, the full-price replay runner and the selected coefficient Drive replica. All earlier thirteen entries remain unchanged. The full-range theorem removes the probability ceiling but retains demand>=2 and the realized-family hypotheses; [review #74](https://github.com/d6g8k5htny-coder/main/issues/74) remains open. The demand-one counterexample is not retracted.

With sibling checkouts:

```sh
python -B -S ../query-/research_query.py --registry registry.json --key lifetime-remainder
python -B -S ../query-/research_query.py --registry registry.json --key p15-price-budget
python -B -S ../query-/research_query.py --registry registry.json --key p15-full-price
python -B -S ../query-/research_query.py --registry registry.json --verify --workspace ..
```

The lookup tool does not use the network or execute retrieved code. Verification requires the exact listed payloads. Private `sandbox` is named only as a workspace role: no private artifact is cataloged or fetched. Catalog metadata is curated, not an independent live permission audit.

## Formal verification lane (Layer 1)

The catalog now also routes machine-checked proofs. Every claim document carries a `formalization` record with `status` in `none | specified | proved | kernel-checked` and an `alignment_review` state; the top-level `formal_verification` block pins the backend (Lean 4 `v4.35.0-rc3`, Mathlib `c55e6e78…`), the allowed axioms and the vocabulary. These fields are a mechanical verification level of the encoded Lean statement, not scientific status: `kernel-checked` never implies `PROVED_REVIEWED`, and an unreviewed statement alignment stays `open`.

| Surface | Path |
|---|---|
| Specification, lanes, hard-gate extension, per-repository handoff | [`docs/FORMAL_VERIFICATION.md`](docs/FORMAL_VERIFICATION.md) |
| Glossary: project terms → standard mathematics → Lean/Mathlib | [`docs/FORMAL_GLOSSARY.md`](docs/FORMAL_GLOSSARY.md) |
| Pilot Lean development (SIDE24 image ledger) and handoff to `Math-` | [`formal/`](formal/README.md) |
| Informal ↔ formal statement alignment ledger | [`formal/STATEMENTS.md`](formal/STATEMENTS.md) |
| Fail-closed status checker (stdlib) | [`tools/formal_status_check.py`](tools/formal_status_check.py) |
| CI: `lake build` + axiom audit + status check | [`.github/workflows/formal.yml`](.github/workflows/formal.yml) |

```sh
python3 -B -S tools/formal_status_check.py --registry registry.json --lean-root formal/lean
python3 -B -S -m unittest discover -s tests -p 'test_*.py'
```

## Add useful entries

Add an entry after a real deliverable exists and its identity is read back. Changed source bytes need a new exact identity and an explicit scope, not erasure of the earlier experiment. Coordinate overlapping edits and keep scientific discussion in the linked source reviews and main campaign. Expand this catalog when it improves retrieval or execution, not to manufacture activity. The original pinned federation replay in `trial` intentionally retains its older source snapshot; current local verification can check this larger catalog.
