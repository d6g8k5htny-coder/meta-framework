# Architecture conformance — contributor reference

[Back to the repository overview](../README.md#federation-source-contracts).

The command details and dated observations below are retained from the
[reviewed README section](https://github.com/d6g8k5htny-coder/meta-framework/blob/9de940209690d5a128832a685ed51b3b2c178781/README.md#federation-source-contracts).
The C146 audit and subsequent diagnosis remain attributed to their linked
records; this documentation move does not rerun either. Run the commands from
the repository root.

## Federation source contracts

Versioned transport contracts live in [schemas/](../schemas/). They define source references, repository roles, source manifests, and workspace snapshots. These schemas describe identity and routing only; they do not establish theorem truth or scientific status.

The read-only checker [tools/architecture_conformance.py](../tools/architecture_conformance.py) checks declared repository owners and visibility labels, required local paths, reference syntax, optional manifest/snapshot structure, and architecture-authority limits. It does not authenticate the actual sibling checkout commits, recompute the declared artifact digests, or query live permissions. It never writes scientific state.

Run the local fixture tests from this repository:

```bash
python -B -S -m unittest discover -s tests -p 'test_*.py' -v
```

The separate workspace command is conditional on deliberately prepared inputs, not a claim that current default-branch clones form a supported layout:

```bash
python -B -S tools/architecture_conformance.py --workspace /path/to/eight-repo-workspace
```

**Source-cut qualification, 7 October 2026** (checker read at `f063d9dcab51302aaaef6666245cac9cf2307548`): the workspace must supply `meta-framework/registry.json`, the eight sibling directories, and `main/architecture/scientific_state/v1/AUTHORITY_MAP.json`. The required map has a [historical source at main `ebedb780`](https://github.com/d6g8k5htny-coder/main/blob/ebedb7802024fa557e9071e4c9cec7cddc474b89/architecture/scientific_state/v1/AUTHORITY_MAP.json), landed by [main PR98](https://github.com/d6g8k5htny-coder/main/pull/98) into `chatgpt/drive-github-hardening-20260919`, not default `main`. That locates one historical input; it does not establish a complete, compatible eight-repository source cut or authorize copying the map into a current authority surface.

The C146 audit's default-layout run at main `3bcf0e34b15dc38270b163263d62b690884e68df` returned exit 2, `missing main authority map`; [issue15](https://github.com/d6g8k5htny-coder/meta-framework/issues/15) and the [source-bound diagnosis](https://github.com/d6g8k5htny-coder/meta-framework/issues/15#issuecomment-6047261217) retain that evidence. The supported historical-versus-current layout and its source-bound positive, missing-map and wrong-cut tests remain unresolved there. This documentation supplies neither a newly passing layout nor a new source-binding policy.

`WORKSPACE_SNAPSHOT.json` and per-repository `SOURCE_MANIFEST.json` are optional inputs to this checker. Their commit/hash fields receive syntax and structure checks, not comparison with the actual checkouts or payload bytes. The [example snapshot](../examples/workspace_snapshot.json) contains repeated-digit placeholder commits, not reproducible pins; the [conformance tests](../tests/test_architecture_conformance.py) use synthetic directories and an authority-map fixture. Passing those fixtures does not verify a real federation cut. Even structurally valid records can describe the wrong local cut without this checker detecting that mismatch.

Unknown schema major versions, mutable refs, sandbox leakage, scientific-status fields in public registry artifact rows, and architecture ownership of promotion fields fail closed. These refusals do not supply the missing checkout authentication. Existing sandbox path/catalog exclusions and publication boundaries remain unchanged; do not fetch exploratory payloads to manufacture a conformance pass.
