# sandbox — public exploratory workspace

Exploratory and adversarial experiments for the Universal Law research program: quick probes, attempts to break a candidate argument, numerical scouting, and anything else that is useful to try before it is worth a proof. The repository is **public on purpose**, so that failed probes are on record next to the results they informed.

[Research home](https://github.com/d6g8k5htny-coder/main) · [Topic guide](https://github.com/d6g8k5htny-coder/main/blob/main/docs/RESEARCH_INDEX.md) · [Status snapshot](https://github.com/d6g8k5htny-coder/main/blob/main/STATUS.md) · [Proofs](https://github.com/d6g8k5htny-coder/Math-) · [Working contract](https://github.com/d6g8k5htny-coder/governance-)

## What this repository is not

Nothing here is a published result. An experiment becomes a result only when it lands in [`Math-`](https://github.com/d6g8k5htny-coder/Math-) with a stated scope and a source-bound review. Accordingly:

- **Do not** copy sandbox files, outputs, paths or hashes into the public source catalog ([`meta-framework/registry.json`](https://github.com/d6g8k5htny-coder/meta-framework/blob/main/registry.json)), into public workflow artifacts, or into [`google-drive`](https://github.com/d6g8k5htny-coder/google-drive) replicas. The [`query-`](https://github.com/d6g8k5htny-coder/query-) tools refuse `sandbox` paths by construction.
- **Do not** read a green probe here as a theorem, a closed lemma or a discharged obligation.
- Scientific effect of anything in this repository: **none**. `lemma_closed`, prizes and premises are never changed from here.

## Where things live

| Repository | Responsibility |
|---|---|
| [`main`](https://github.com/d6g8k5htny-coder/main) | Research campaign, reviews, status, integration |
| [`Math-`](https://github.com/d6g8k5htny-coder/Math-) | Proofs, exact computations, reproducible calculations |
| [`trial`](https://github.com/d6g8k5htny-coder/trial) | Engineering integration tests and portable patches |
| [`governance-`](https://github.com/d6g8k5htny-coder/governance-) | Cross-repository working contract |
| `sandbox` (this repository) | Experiments only; visible, but never exported as a result |

## Contents

Experiments are grouped under [`experiments/`](experiments/), one directory per probe, each with the script that ran and the observation it produced. Agent entry: [AGENTS.md](AGENTS.md).
