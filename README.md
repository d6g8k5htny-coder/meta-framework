# meta-framework — exact-source catalog for the Universal Law research program

[Research home](https://github.com/d6g8k5htny-coder/main) · [Topic guide](https://github.com/d6g8k5htny-coder/main/blob/main/docs/RESEARCH_INDEX.md) · [Status snapshot](https://github.com/d6g8k5htny-coder/main/blob/main/STATUS.md) · [Run the checks](https://github.com/d6g8k5htny-coder/main/blob/main/docs/REPRODUCE.md) · [Live site](https://d6g8k5htny-coder.github.io/main/site/) · [Work queue](https://github.com/d6g8k5htny-coder/main/issues/86)

[![Public catalog source verification](https://github.com/d6g8k5htny-coder/meta-framework/actions/workflows/catalog.yml/badge.svg)](https://github.com/d6g8k5htny-coder/meta-framework/actions/workflows/catalog.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Scientific status authority: none](https://img.shields.io/badge/scientific%20status%20authority-none-lightgrey.svg)](#what-this-catalog-is-and-is-not)

**One file, one job.** [`registry.json`](registry.json) is a small machine-readable catalog. Each entry pins one public research artifact — a proof text, the program that evaluates it, that program's tests, its recorded output, or a byte-identical replica — to an exact GitHub commit, path, byte count and SHA-256, and states its scope in a single line. Together with the read-only [`query-`](https://github.com/d6g8k5htny-coder/query-) tool it answers two questions for any reader: *where exactly is the published source for this result?* and *are the bytes I am holding the bytes that were published?*

## What this catalog is and is not

- **Is:** a routing table from short topic keys to exact source identities, plus a one-line role for every repository in the workspace.
- **Is not:** a status register. No entry states whether a result is accepted, reviewed or open; that lives in the source-linked reviews under [`main`](https://github.com/d6g8k5htny-coder/main) and its [status snapshot](https://github.com/d6g8k5htny-coder/main/blob/main/STATUS.md). A hash proves identity, not correctness, currentness or independent review.
- **Is not:** a complete inventory. Entries are curated after a deliverable exists; the 2,138-row public source inventory is [`main/docs/public-math/sources.json`](https://github.com/d6g8k5htny-coder/main/blob/main/docs/public-math/sources.json).

## How the repositories fit together

| Repository | What you will find there | Start at |
|---|---|---|
| [**main**](https://github.com/d6g8k5htny-coder/main) | The public front door: status snapshot, reading order, reviews, contribution route, GitHub Pages site | [README](https://github.com/d6g8k5htny-coder/main#readme) · [STATUS.md](https://github.com/d6g8k5htny-coder/main/blob/main/STATUS.md) |
| [**Math-**](https://github.com/d6g8k5htny-coder/Math-) | Full proof texts, exact-arithmetic programs, their tests and recorded outputs | [PROOF_INDEX.md](https://github.com/d6g8k5htny-coder/Math-/blob/main/PROOF_INDEX.md) |
| **meta-framework** (this repository) | Exact source identities for curated public artifacts; repository roles | [registry.json](registry.json) |
| [**query-**](https://github.com/d6g8k5htny-coder/query-) | Standard-library, read-only lookup and local byte verification against this catalog | [README](https://github.com/d6g8k5htny-coder/query-#readme) |
| [**google-drive**](https://github.com/d6g8k5htny-coder/google-drive) | Deliberately selected public replicas of Drive outputs, each with a `SOURCE.json` custody record | [replicas/](https://github.com/d6g8k5htny-coder/google-drive/tree/main/replicas) |
| [**Universal-Law-Workspace**](https://github.com/d6g8k5htny-coder/Universal-Law-Workspace) | Federation map; every repository pinned as a submodule at a recorded commit; structural checks | [README](https://github.com/d6g8k5htny-coder/Universal-Law-Workspace#readme) |
| [**governance-**](https://github.com/d6g8k5htny-coder/governance-) | The cross-repository working contract and measured process amendments | [README](https://github.com/d6g8k5htny-coder/governance-#readme) |
| [**trial**](https://github.com/d6g8k5htny-coder/trial) | Engineering integration tests, portable patches, multi-agent access notes | [README](https://github.com/d6g8k5htny-coder/trial#readme) |
| [**sandbox**](https://github.com/d6g8k5htny-coder/sandbox) | Exploratory and adversarial experiments, visible so that failed probes are on record too. Not a source of published results: nothing from it is cataloged, fetched or verified here | [README](https://github.com/d6g8k5htny-coder/sandbox#readme) |

The site at [d6g8k5htny-coder.github.io/main/site](https://d6g8k5htny-coder.github.io/main/site/) renders the status board, a pinned coefficient viewer and the searchable source inventory; its [museum](https://d6g8k5htny-coder.github.io/main/site/museum.html) shows claim cards with quoted scope and source identities.

## What the mathematics is about

The cataloged sources sit on three fronts of one program. Full reading order and the latest reviews are in the [topic guide](https://github.com/d6g8k5htny-coder/main/blob/main/docs/RESEARCH_INDEX.md); the proofs themselves are in [`Math-`](https://github.com/d6g8k5htny-coder/Math-).

- **Gaussian persistence lifetimes.** How long do topological features of a smooth Gaussian random field live? The program derives the leading law for the density of short lifetimes on a fixed torus, evaluates its constant exactly, and bounds the remainder.
- **RN critical-point counting.** When a maximum and a saddle of the field coalesce, do stray critical points appear nearby? These sources turn rare-event probability bounds into expected-count bounds and prove the count bound on a region a fixed distance from the pair.
- **P15 combinatorics.** A local-to-global covering problem for decreasing set families with prices on elements: which families admit cheap covers of their obstructions, at what palette size, and which proposed extensions fail.

Every proof text states its own scope, the exact parent it depends on, and what it does not claim. Author-side derivations, same-author replays and non-author reviews are recorded as separate facts.

## Find a source

| Topic | Exact lookup key | What the source addresses (at its own stated scope) |
|---|---|---|
| SIDE24 coefficient | `side24-coefficient` | The constant in the leading term of the parent lifetime law, evaluated in exact outward rational arithmetic in dimensions 2 and 3; conditional on the parent formula under review at [main #63](https://github.com/d6g8k5htny-coder/main/issues/63) |
| Quantitative lifetime density | `lifetime-remainder` | For the parent's Gaussian model on a fixed torus, the short-lifetime density has leading term `c·ℓ^(-1/3)` with a bounded remainder |
| RN probability-to-count interface | `rn-count-interface` | Exactly when a bound on the probability of a rare pairing failure yields a bound on the expected number of stray critical points, with counterexamples showing the extra count-weighted estimate that is needed |
| RN fixed-remote height-window count | `rn-fixed-remote-window` | On a spatial region a fixed distance from a coalescing maximum–saddle pair, the expected number of critical points in the height window between them is `O(r^3)` |
| P15 original-coordinate family | `p15-realized-covers` | An explicit family, in original coordinates, for which the P15-B cover hypotheses are proved, with nonempty generator covers and an exact palette threshold (816 for the specified cover versus 818 for the whole ground set) |
| P15 unrestricted price counterexample | `p15-price-boundary` | A two-element counterexample: the realized-cover theorem cannot use every admissible transformed price with the same palette |
| P15 restricted transformed-price successor | `p15-price-budget` | The transformed-price budget is restored under two extra hypotheses: every block demand at least 2 and every probability at most 1/4 |
| P15 full probability range and sharp factor | `p15-full-price` | The probability cutoff is removed: for demands at least 2 the budget holds for every independent probability vector, with sharp uniform factor `1/[3 − log(3e − 2)]` |

The third column paraphrases each source's own statement of scope so a reader can choose what to open; it is not a review verdict. Each topic key names the proof text. Where a package also ships code, tests, a recorded output or a replay runner, the companion keys add `-code`, `-tests`, `-output` and `-replay` (for example `p15-full-price-code`); the SIDE24 Drive replica is `side24-coefficient-drive-replica`. The catalog currently holds 22 public artifacts: five `Math-` packages and one `google-drive` replica. All earlier entries are unchanged: a corrected or extended source gets a new entry with its own identity, never an edit to an old one. Scientific discussion of these sources is in the linked reviews on `main` (for example [#65](https://github.com/d6g8k5htny-coder/main/issues/65), [#67](https://github.com/d6g8k5htny-coder/main/issues/67), [#74](https://github.com/d6g8k5htny-coder/main/issues/74), [#76](https://github.com/d6g8k5htny-coder/main/issues/76)) and summarized in the [status snapshot](https://github.com/d6g8k5htny-coder/main/blob/main/STATUS.md); this file does not restate their outcomes.

With sibling checkouts:

```sh
python -B -S ../query-/research_query.py --registry registry.json --key lifetime-remainder
python -B -S ../query-/research_query.py --registry registry.json --key p15-price-budget
python -B -S ../query-/research_query.py --registry registry.json --key p15-full-price
python -B -S ../query-/research_query.py --registry registry.json --verify --workspace ..
```

The lookup tool does not use the network or execute retrieved code. Verification requires the exact listed payloads. `sandbox` is named only as a workspace role: no experiment from it is cataloged or fetched, and the tools refuse `sandbox` paths by construction. (The `repositories` map still records that role with the label `private`; the repository has been public since 2026-09-26 and aligning that label is a coordinated change tracked in the [audit](docs/PUBLIC_FACE_AUDIT_20260927.md#finding-3--sandbox-align-the-wording-with-the-intent).) Catalog metadata is curated, not an independent live permission audit.

### Try it in two minutes

No account, no dependencies beyond Python 3. Clone the catalog, the lookup tool and the mathematics side by side, then list every key, read one entry, and verify every cataloged byte against your local checkout:

```sh
git clone https://github.com/d6g8k5htny-coder/meta-framework.git
git clone https://github.com/d6g8k5htny-coder/query-.git
git clone https://github.com/d6g8k5htny-coder/Math-.git
git clone https://github.com/d6g8k5htny-coder/google-drive.git
python -B -S query-/research_query.py --registry meta-framework/registry.json
python -B -S query-/research_query.py --registry meta-framework/registry.json --key rn-fixed-remote-window
python -B -S query-/research_query.py --registry meta-framework/registry.json --verify --workspace .
```

`--verify` prints the keys whose local bytes match their recorded SHA-256 and reports mismatches explicitly. A pass means the bytes are the published bytes; it does not mean the mathematics is accepted.

## What each entry records

| Field | Meaning |
|---|---|
| `key` | Stable short name used by the lookup tool. Unknown keys are refused, never guessed. |
| `repository` | Short repository name; the full name and role are in the `repositories` map of the same file. |
| `commit` | Full 40-character commit on which the artifact was read back. Mutable refs (`main`, tags) are not accepted. |
| `path` | Path inside that repository at that commit. |
| `bytes` / `sha256` | Exact size and digest of the file at that commit. |
| `scope` | One line stating what the artifact does and does not claim, written by the person who cataloged it. |
| `visibility` | `public` for every cataloged artifact; the lookup tool refuses anything else. |

Top-level fields: `schema_version`, `scientific_status_authority: false`, `campaign` (the historical research push that produced the first entries) and `parent_source` (the parent lifetime theorem whose formula the SIDE24 coefficient evaluates, identified by its review issue and SHA-256; that parent is still under review at [main #63](https://github.com/d6g8k5htny-coder/main/issues/63)).

## How the catalog is checked

The [`catalog.yml`](.github/workflows/catalog.yml) workflow runs on every pull request that touches `registry.json` and on pushes to `main`. It fetches each declared artifact from `raw.githubusercontent.com` at its recorded commit, rejects any byte-length or SHA-256 mismatch, runs the pinned `query-` lookup tool and the pinned cross-repository federation tests from [`trial`](https://github.com/d6g8k5htny-coder/trial) in both normal and optimized Python modes, and uploads the evidence — including on failure — as a workflow artifact. Only the five public repositories can be sources; the job refuses anything else. A green run certifies declared public payload identity and lookup behavior, not scientific acceptance.

## Add useful entries

Add an entry after a real deliverable exists and its identity is read back. Changed source bytes need a new exact identity and an explicit scope, not erasure of the earlier experiment. Coordinate overlapping edits and keep scientific discussion in the linked source reviews and main campaign. Expand this catalog when it improves retrieval or execution, not to manufacture activity. The original pinned federation replay in `trial` intentionally retains its older source snapshot; current local verification can check this larger catalog.

A one-off helper in `query-` prints a candidate entry from a local file: `python -B -S ../query-/catalog_entry_helper.py --help`. It refuses `sandbox` paths, symlinks and mutable commits. A printed stub is a proposal for review, not an entry.

## License and use

Released under the [MIT License](LICENSE), matching [`main`](https://github.com/d6g8k5htny-coder/main/blob/main/LICENSE). Cite the research program via [`main/CITATION.cff`](https://github.com/d6g8k5htny-coder/main/blob/main/CITATION.cff). Contribution routes and the working contract are in [`main/CONTRIBUTING.md`](https://github.com/d6g8k5htny-coder/main/blob/main/CONTRIBUTING.md) and [`governance-`](https://github.com/d6g8k5htny-coder/governance-); agents start at [AGENTS.md](AGENTS.md). A public-facing navigation audit of the whole account, with the fixes it produced and the ones still owed elsewhere, is in [docs/PUBLIC_FACE_AUDIT_20260927.md](docs/PUBLIC_FACE_AUDIT_20260927.md).
