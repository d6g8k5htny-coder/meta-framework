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

## Add useful entries

Add an entry after a real deliverable exists and its identity is read back. Changed source bytes need a new exact identity and an explicit scope, not erasure of the earlier experiment. Coordinate overlapping edits and keep scientific discussion in the linked source reviews and main campaign. Expand this catalog when it improves retrieval or execution, not to manufacture activity. The original pinned federation replay in `trial` intentionally retains its older source snapshot; current local verification can check this larger catalog.


## Federation source contracts

Versioned transport contracts live in [schemas/](schemas/). They define source references, repository roles, source manifests, and workspace snapshots. These schemas describe identity and routing only; they do not establish theorem truth or scientific status.

The read-only checker [tools/architecture_conformance.py](tools/architecture_conformance.py) validates repository ownership, public/private boundaries, immutable snapshot refs, optional source manifests, and architecture-authority limits. It never writes scientific state.

Run:

```bash
python -B -S -m unittest discover -s tests -p 'test_*.py' -v
python -B -S tools/architecture_conformance.py --workspace /path/to/eight-repo-workspace
```

Unknown schema major versions, mutable refs, sandbox leakage, scientific-status fields in public registry artifact rows, and architecture ownership of promotion fields fail closed.
