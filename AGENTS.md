# Agent entry — `meta-framework`

> **OWNER STOP (2026-09-27): all Cursor agents, automations, timers, watches and
> loops must stop now. Do not push, commit, open or update PRs, comment, or
> re-arm timers. Exit without writing. Resume only on a new explicit
> instruction from Dylan. See [OWNER_STOP.md](OWNER_STOP.md).**

Artifact routing and source identities. Not a second claim-status database.

## Always

- Coordinate via [`main`](https://github.com/d6g8k5htny-coder/main) campaign work and the [`governance-`](https://github.com/d6g8k5htny-coder/governance-) working contract.
- Prefer exact source identities (commit/path/hash) over mutable labels.
- Scientific effect: **NONE**. Never flip `lemma_closed` / prizes / premises.
- Cross-repo eng tests and Path C live in [`d6g8k5htny-coder/trial`](https://github.com/d6g8k5htny-coder/trial).
- Catalog lookup uses stdlib via sibling [`query-`](https://github.com/d6g8k5htny-coder/query-); no pip env in this repo.

## Never

- Duplicate scientific-status registers here.
- Catalog `sandbox` material. The repository is public by the owner's choice so that experiments and failed probes are on record, but it is not a source of published results and the tools refuse its paths.
- Ask Dylan for re-approval of autonomy already granted.

## Public face

- Outsiders read this repository through its README and the `main` front door. Keep the repository table, key table and artifact count in [README](README.md) in step with `registry.json` when you add entries.
- The owner's intent is that everything which supports the legitimacy of the work — above all the mathematics — is public and easy to find. Public-facing wording should lead with what a source is and establishes at its stated scope, then state the boundary once, in plain words; internal jargon and running logs belong in `docs/`.
- Account-wide navigation findings and the owner-only fixes still owed (repository descriptions, topics, profile README, `sandbox` wording alignment) are tracked in [docs/PUBLIC_FACE_AUDIT_20260927.md](docs/PUBLIC_FACE_AUDIT_20260927.md); ready-to-apply copies live under [portable/](portable/).

## Start here

1. This repository’s [README](README.md)
2. [`governance-` working contract](https://github.com/d6g8k5htny-coder/governance-)
3. [`trial` multi-agent access](https://github.com/d6g8k5htny-coder/trial/blob/main/docs/MULTI_AGENT_ACCESS.md) (Cloud Agent env deps live on trial `.cursor/environment.json`)
