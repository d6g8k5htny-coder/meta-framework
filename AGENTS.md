# Agent entry — `meta-framework`

> **HISTORICAL STOP NOTICE:** [`OWNER_STOP.md`](OWNER_STOP.md) preserves the
> 2026-09-27 Cursor stop byte-for-byte as historical evidence. Dylan Roy lifted
> that stop on 2026-10-05 in the adopted
> [owner decision](https://github.com/d6g8k5htny-coder/main/blob/7c4cef8c6a2ca4b6f984e5e45108037c2caec4e1/governance/OWNER_DECISION_20261005_CURSOR.md).
> Cursor agents may work only when requested for bounded tasks; they do not
> self-assign repository changes or arm permanent timers, watches, or loops.

Artifact routing and source identities. Not a second claim-status database.

Current and future agents: read the [15 October 2026 standing owner mandate](https://github.com/d6g8k5htny-coder/main/blob/b665307520948308a53d190d7341bf301df3b3a2/governance/OWNER_MANDATE_20261015.md)
alongside the [standing owner delegation (current)](https://github.com/d6g8k5htny-coder/main/blob/main/governance/OP-AUTONOMY-20260923-v2.1.md)
([reviewed 15 October delegation snapshot](https://github.com/d6g8k5htny-coder/main/blob/b665307520948308a53d190d7341bf301df3b3a2/governance/OP-AUTONOMY-20260923-v2.1.md) for source-bound audit)
and this repository's effective working rules. Carry both canonical links in
new-agent onboarding and handoffs. Linking them does not prove recipient reading
or grant scientific authority, a security exemption or new platform permission.

## Always

- Coordinate via [`main`](https://github.com/d6g8k5htny-coder/main) campaign work and the [`governance-`](https://github.com/d6g8k5htny-coder/governance-) working contract.
- Prefer exact source identities (commit/path/hash) over mutable labels.
- Scientific effect: **NONE**. Never flip `lemma_closed` / prizes / premises.
- Historical cross-repo engineering tests and Path C material remain in [`d6g8k5htny-coder/trial`](https://github.com/d6g8k5htny-coder/trial) (observed archived on 15 October 2026). Route new work through [main's current workflow](https://github.com/d6g8k5htny-coder/main/blob/main/governance/OP-WORKFLOW-20260930.md) and [active coordination board #419](https://github.com/d6g8k5htny-coder/main/issues/419).
  [Previous board #307](https://github.com/d6g8k5htny-coder/main/issues/307) and
  [board #229](https://github.com/d6g8k5htny-coder/main/issues/229) remain readable history;
  this pointer does not transfer, renew or release any earlier claim.
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
3. [`trial` multi-agent access](https://github.com/d6g8k5htny-coder/trial/blob/main/docs/MULTI_AGENT_ACCESS.md) (historical launch-environment notes; archived `.cursor/environment.json` is not current runtime or access-permission authority)
