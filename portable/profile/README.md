# Dylan Roy — Universal Law research program

**Gaussian random fields, persistent homology, and reproducible multi-model mathematical research.**

[Start at the front door](https://github.com/d6g8k5htny-coder/main) · [Status snapshot](https://github.com/d6g8k5htny-coder/main/blob/main/STATUS.md) · [Read the proofs](https://github.com/d6g8k5htny-coder/Math-/blob/main/PROOF_INDEX.md) · [Live site](https://d6g8k5htny-coder.github.io/main/site/) · [Verify a source](https://github.com/d6g8k5htny-coder/query-)

The program studies persistence lifetimes and critical-point geometry of Gaussian random fields, with exact rational arithmetic wherever a bound is claimed, negative controls for every checker, and a fail-closed review workflow in which a merge, a green CI run or a matching hash never promotes mathematical status. Several AI models work in the same repositories under one owner; reviews record who wrote what and what was independently checked.

## Start here

1. [**main**](https://github.com/d6g8k5htny-coder/main) — what the program studies, how to read it, and where to contribute.
2. [**STATUS.md**](https://github.com/d6g8k5htny-coder/main/blob/main/STATUS.md) — what is accepted at what scope, what is open, and the exact review each row rests on.
3. [**Math- proof index**](https://github.com/d6g8k5htny-coder/Math-/blob/main/PROOF_INDEX.md) — full proof texts with runnable, standard-library checks.
4. [**Live site**](https://d6g8k5htny-coder.github.io/main/site/) — status board, pinned SIDE24 coefficient viewer, searchable 2,138-row source inventory, and the [verification museum](https://d6g8k5htny-coder.github.io/main/site/museum.html) of claim cards.

## What the mathematics is about

- **Gaussian persistence lifetimes** — how long topological features of a smooth Gaussian random field live. The program derives the leading law for the density of short lifetimes on a fixed torus, evaluates its constant (SIDE24) exactly in dimensions 2 and 3, and bounds the remainder. [Reading order](https://github.com/d6g8k5htny-coder/main/blob/main/docs/RESEARCH_INDEX.md#gaussian-persistence)
- **Critical-point counting near coalescing pairs (RN)** — when a maximum and a saddle merge, do stray critical points appear nearby? Exact probability-to-count interfaces, a fixed-remote-region count theorem, and a reviewed fixed-annulus theorem in dimension 2. [Reading order](https://github.com/d6g8k5htny-coder/main/blob/main/docs/RESEARCH_INDEX.md#rn-counting)
- **P15 combinatorics** — a local-to-global covering problem for priced decreasing set families: an explicit realized family with exact palette thresholds, a counterexample to the naive price extension, and the restored budget with its sharp constant. [Reading order](https://github.com/d6g8k5htny-coder/main/blob/main/docs/RESEARCH_INDEX.md#p15-combinatorics)

Every proof states its own scope and the parent it depends on. Counterexamples and failed extensions are published beside the positive results, because a record that shows what did not work is part of what makes the rest credible.

## Repositories

| Repository | Purpose |
|---|---|
| [main](https://github.com/d6g8k5htny-coder/main) | Public front door: status, reading order, reviews, contribution route, GitHub Pages site |
| [Math-](https://github.com/d6g8k5htny-coder/Math-) | Proofs, exact-arithmetic programs, tests, recorded outputs, proof index |
| [query-](https://github.com/d6g8k5htny-coder/query-) | Read-only exact-source lookup and local byte verification (Python standard library only) |
| [meta-framework](https://github.com/d6g8k5htny-coder/meta-framework) | Machine-readable catalog: topic key → pinned commit, path, bytes, SHA-256, scope |
| [google-drive](https://github.com/d6g8k5htny-coder/google-drive) | Deliberately selected public replicas of Drive outputs with source custody records |
| [Universal-Law-Workspace](https://github.com/d6g8k5htny-coder/Universal-Law-Workspace) | Federation map with every repository pinned as a submodule at a recorded commit |
| [governance-](https://github.com/d6g8k5htny-coder/governance-) | Cross-repository working contract and measured process amendments |
| [trial](https://github.com/d6g8k5htny-coder/trial) | Engineering integration tests, portable patches, multi-agent access notes |

## Verify something in two minutes

No account or dependency install is needed. The query package's own tests run from a clean clone:

```sh
git clone https://github.com/d6g8k5htny-coder/query-.git
cd query-
python -B -S -m unittest discover -s tests -p 'test_*.py' -v
```

To check that a published proof's bytes are the bytes on record, clone `meta-framework`, `Math-` and `google-drive` beside it and run `python -B -S research_query.py --registry ../meta-framework/registry.json --verify --workspace ..`. A pass verifies identity; it does not verify a theorem.

## How status is written here

- **ACCEPT — scoped**: a source-bound technical review accepted the stated object at its declared hypotheses, and nothing more.
- **AMEND / open**: a defect or gap is recorded and visible; the object is not flattened into a solved claim.
- **Engineering only**: infrastructure such as `query-`, the workspace map and CI. Useful, but it carries no theorem-acceptance meaning.

Details and the current rows: [STATUS.md](https://github.com/d6g8k5htny-coder/main/blob/main/STATUS.md).

## Contributing

Read [CONTRIBUTING.md](https://github.com/d6g8k5htny-coder/main/blob/main/CONTRIBUTING.md), pick a [good first task](https://github.com/d6g8k5htny-coder/main/issues?q=is%3Aissue+is%3Aopen+label%3Agood-first-task), or follow the [public contributions board](https://github.com/users/d6g8k5htny-coder/projects/1/views/1). Everything is released under the MIT License; citation metadata is in [CITATION.cff](https://github.com/d6g8k5htny-coder/main/blob/main/CITATION.cff).
