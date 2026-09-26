# Meta-framework — exact-source research routing

[Research home](https://github.com/d6g8k5htny-coder/main) · [Topic guide](https://github.com/d6g8k5htny-coder/main/blob/main/docs/RESEARCH_INDEX.md) · [Run the checks](https://github.com/d6g8k5htny-coder/main/blob/main/docs/REPRODUCE.md) · [Work queue](https://github.com/d6g8k5htny-coder/main/issues/61)

[registry.json](registry.json) maps all eight repository roles and a curated set of public artifacts to exact commits, paths, byte counts, SHA256 identities and scope. It is not a second scientific-status register or a complete Drive inventory. A hash proves identity, not correctness, currentness or independent review.

## Find a source

| Topic | Exact lookup key |
|---|---|
| SIDE24 coefficient | `side24-coefficient` |
| Marked-cylinder CAP criterion | `marked-cylinder-cap` |
| Uniform matrix-cap / lifetime candidate | `matrix-cap-lifetime` |
| Quantitative lifetime density | `lifetime-remainder` |
| RN probability-to-count interface | `rn-count-interface` |
| RN fixed-remote height-window count | `rn-fixed-remote-window` |
| Nonauthor notes on draft mesoscopic reduction | `rn-mesoscopic-reduction-notes` |
| P15 original-coordinate family | `p15-realized-covers` |
| P15 unrestricted price counterexample | `p15-price-boundary` |
| P15 restricted transformed-price successor | `p15-price-budget` |
| P15 full probability range and sharp factor | `p15-full-price` |
| Consecutive-capacity palette optimum | `consecutive-palette` |
| Nonauthor #76 / #63 / #74 challenge notes | `rn-fixed-remote-notes`, `matrix-cap-lifetime-notes`, `p15-full-price-notes` |
| ENG-03 independent replay receipt | `eng-replay-20260925` |
| Downstream-first route index | `downstream-route-20260925` / `downstream-route-20260925-v2` |
| Nonauthor #67 / #65 challenge notes | `lifetime-remainder-notes`, `side24-coefficient-notes` |
| Nonauthor RN count-interface notes | `rn-count-interface-notes` |
| PAL-02 consecutive vs realized matching | `pal02-matching-notes` |
| P15 price boundary→budget→full crosswalk | `p15-price-crosswalk-notes` |
| Nonauthor marked-cylinder CAP notes | `marked-cylinder-cap-notes` |
| P15-B original (Drive replica) | `p15-b-original` |
| Downstream hard gate (#90/#86) | `downstream-hard-gate` |
| Downstream route (post-#61) | `downstream-route-20260925-v3` |
| Math- PR9 chart coordination notes | `rn-mesoscopic-chart-notes` |
| Multi-agent dispatch plan | `multi-agent-dispatch-20260925` … `-v32` |
| Downstream hard gate (PR13) | `downstream-hard-gate` … (baca69c, frozen) |
| Downstream hard gate (PR15 merged) | `downstream-hard-gate-pr15` … |
| Merged D5 Hermite / axial density | `d5-finite-r-hermite-*`, `axial-density-*`, `math-pr19-pr21-merged` |
| Merged D5 annulus / thin-tube | `rn-fixed-annulus-*`, `rn-thin-tube-*`, `rn-annulus-bridge-*`, `math-pr22-pr28-merged` |
| Merged D5 collision mechanism | `collision-mechanism-*` |
| Lifetime parent custody / FC-10 gate | `lifetime-parent-*`, `landing-claims-manifest-pr50`, `downstream-gate-fc10-*`, `downstream-gate-fc10-replica-source`, `landing-claims-pr50-replica-source`, `catalog-ci-repair-20260926`, `math-pr50-pr51-merged` |
| Merged D5 contact / landing claims | `contact-kernel-tail-*`, `contact-small-gap-*`, `d1-section9-borel-repair`, `landing-claims-*`, `math-d5-landing-20260926`, `peer-coordination-20260926-v26`, `peer-coordination-20260926-v27`, `math-pr50-pr51-merged`, `peer-coordination-20260926-v28`, `peer-coordination-20260926-v31` |
| Two-key review topology (gov PR4) | `review-topology-merged`, `governance-pr4-merged` |
| PR98 / #90 engineering | `pr98-green-readback`, `pr98-tip-69e9b526`, `pr98-tip-b59359eb`, `pr98-green-b59359eb`, `math-pr15-merged`, `peer-coordination-20260925-v13`, `peer-coordination-20260925-v14`, `peer-coordination-20260925-v16`, `peer-coordination-20260925-v17`, `peer-coordination-20260925-v18`, `peer-coordination-20260925-v20`, `peer-coordination-20260925-v21`, `peer-coordination-20260925-v22`, `peer-coordination-20260925-v23`, `peer-coordination-20260925-v24`, `math-d5-landing-20260926`, `peer-coordination-20260926-v26`, `peer-coordination-20260926-v27`, `math-pr50-pr51-merged`, `peer-coordination-20260926-v28`, `peer-coordination-20260926-v31` |
| PR9 pin AMEND / density / maps / thin-tube | `pin-offset-cross-model`, `math-pr19-repair-candidate`, `math-pr21-axial-density`, `math-pr22-thin-tube`, `tip-3242d1ff` |
| Cross-model lanes | `cross-model-lanes` |
| Review-notes index | `review-notes-index` … `-v33` |

The catalog contains 227 public artifacts (CI upper bound 256), including code, tests, outputs, the full-price replay runner, the fixed-remote RN sources, the merged downstream hard-gate package (PR13 + PR15 identities), SHA-matched public Drive replicas (SIDE24 enclosure, marked-cylinder, matrix-cap/lifetime, consecutive-palette, P15-B), merged Math- D5 Hermite/axial-density identities, merged governance- two-key review topology, and nonauthor review/replay routing notes. All earlier identities remain unchanged. Campaign dispatch [#61](https://github.com/d6g8k5htny-coder/main/issues/61) is closed as superseded by [#86](https://github.com/d6g8k5htny-coder/main/issues/86). Future agent actions follow `multi-agent-dispatch-20260925-v32`. The full-range theorem removes the probability ceiling but retains demand>=2 and the realized-family hypotheses; [review #74](https://github.com/d6g8k5htny-coder/main/issues/74) remains open. The demand-one counterexample is not retracted. Math- PR7/PR9 mesoscopic work is coordinated via notes only until merge; not cataloged as finished sources. The hard-gate package is engineering integrity control (`lemma_closed` stays false), not analytic acceptance. `#90` remains OPEN; PR98 tip `b59359eb` is CI-green after D1/Q0+#90 binding + semantic_digest_core E6 repair; #90 remains OPEN pending transition-gate external bindings, second-source mutation, and retargeted nonauthor re-review.

With sibling checkouts:

```sh
python -B -S ../query-/research_query.py --registry registry.json --key lifetime-remainder
python -B -S ../query-/research_query.py --registry registry.json --key matrix-cap-lifetime
python -B -S ../query-/research_query.py --registry registry.json --key marked-cylinder-cap
python -B -S ../query-/research_query.py --registry registry.json --key consecutive-palette
python -B -S ../query-/research_query.py --registry registry.json --key p15-price-budget
python -B -S ../query-/research_query.py --registry registry.json --key p15-full-price
python -B -S ../query-/research_query.py --registry registry.json --key downstream-hard-gate
python -B -S ../query-/research_query.py --registry registry.json --key p15-b-original
python -B -S ../query-/research_query.py --registry registry.json --key review-notes-index
python -B -S ../query-/research_query.py --registry registry.json --verify --workspace ..
```

The lookup tool does not use the network or execute retrieved code. Verification requires the exact listed payloads. Private `sandbox` is named only as a workspace role: no private artifact is cataloged or fetched. Catalog metadata is curated, not an independent live permission audit.

## Add useful entries

Add an entry after a real deliverable exists and its identity is read back. Changed source bytes need a new exact identity and an explicit scope, not erasure of the earlier experiment. Coordinate overlapping edits and keep scientific discussion in the linked source reviews and main campaign. Expand this catalog when it improves retrieval or execution, not to manufacture activity. The original pinned federation replay in `trial` intentionally retains its older source snapshot; current local verification can check this larger catalog.
