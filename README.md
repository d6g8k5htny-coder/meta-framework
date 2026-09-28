[![Universal Law — mathematics, evidence and verification](https://raw.githubusercontent.com/d6g8k5htny-coder/main/6168a1efc42dc6eabae3ce91623d6e16d3c92fd6/docs/site/brand/banner.svg)](https://d6g8k5htny-coder.github.io/main/site/)

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
| P15 full probability range and sharp factor | `p15-full-price`, `p15-full-price-nonauthor-review`, `p15-full-price-nonauthor-check`, `math-pr63-p15-full-price-accept` |
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
| Multi-agent dispatch plan | `multi-agent-dispatch-20260925` … `-v77` |
| Downstream hard gate (PR13) | `downstream-hard-gate` … (baca69c, frozen) |
| Downstream hard gate (PR15 merged) | `downstream-hard-gate-pr15` … |
| Merged D5 Hermite / axial density | `d5-finite-r-hermite-*`, `axial-density-*`, `math-pr19-pr21-merged` |
| Merged D5 annulus / thin-tube | `rn-fixed-annulus-*`, `rn-thin-tube-*`, `rn-annulus-bridge-*`, `math-pr22-pr28-merged` |
| Merged D5 collision mechanism | `collision-mechanism-*` |
| Proof availability index | `proof-availability-index`, `transverse-bound-candidate`, `math-pr54-proof-index-merged` |
| Lifetime parent custody / FC-10 gate | `lifetime-parent-*`, `lifetime-parent-erratum-congruence`, `lifetime-parent-erratum-pointer`, `lifetime-parent-cap-pairing-identities`, `landing-claims-manifest-pr50`, `landing-claims-manifest-pr66`, `math-pr66-landing-reviewed-scoped`, `downstream-gate-fc10-*`, `downstream-gate-fc10-replica-source`, `landing-claims-pr50-replica-source`, `catalog-ci-repair-20260926`, `math-pr50-pr51-merged` |
| Merged D5 contact / landing claims | `contact-kernel-tail-*`, `contact-small-gap-*`, `d1-section9-borel-repair`, `landing-claims-*`, `math-d5-landing-20260926`, `peer-coordination-20260926-v26`, `peer-coordination-20260926-v27`, `math-pr50-pr51-merged`, `peer-coordination-20260926-v28`, `peer-coordination-20260926-v31`, `peer-coordination-20260926-v33`, `peer-coordination-20260926-v34`, `peer-coordination-20260926-v35`, `peer-coordination-20260926-v36`, `peer-coordination-20260926-v37`, `peer-coordination-20260926-v38`, `peer-coordination-20260926-v39`, `peer-coordination-20260926-v40`, `peer-coordination-20260926-v41`, `peer-coordination-20260926-v42`, `peer-coordination-20260926-v43`, `peer-coordination-20260926-v44`, `peer-coordination-20260926-v45`, `peer-coordination-20260926-v46`, `peer-coordination-20260926-v47`, `peer-coordination-20260926-v48`, `peer-coordination-20260926-v49`, `peer-coordination-20260926-v50`, `peer-coordination-20260926-v51`, `peer-coordination-20260926-v52`, `peer-coordination-20260926-v53`, `peer-coordination-20260926-v54`, `peer-coordination-20260926-v55`, `peer-coordination-20260926-v56`, `peer-coordination-20260926-v57`, `peer-coordination-20260926-v58`, `peer-coordination-20260926-v59`, `peer-coordination-20260926-v60`, `peer-coordination-20260926-v61`, `peer-coordination-20260926-v62` |
| Two-key review topology (gov PR4) | `review-topology-merged`, `governance-pr4-merged` |
| PR98 / #90 engineering | `pr98-green-readback`, `pr98-tip-69e9b526`, `pr98-tip-b59359eb`, `pr98-green-b59359eb`, `issue90-engineering-gate-closed`, `math-pr15-merged`, `peer-coordination-20260925-v13`, `peer-coordination-20260925-v14`, `peer-coordination-20260925-v16`, `peer-coordination-20260925-v17`, `peer-coordination-20260925-v18`, `peer-coordination-20260925-v20`, `peer-coordination-20260925-v21`, `peer-coordination-20260925-v22`, `peer-coordination-20260925-v23`, `peer-coordination-20260925-v24`, `math-d5-landing-20260926`, `peer-coordination-20260926-v26`, `peer-coordination-20260926-v27`, `math-pr50-pr51-merged`, `peer-coordination-20260926-v28`, `peer-coordination-20260926-v31`, `peer-coordination-20260926-v33`, `peer-coordination-20260926-v34`, `peer-coordination-20260926-v35`, `peer-coordination-20260926-v36`, `peer-coordination-20260926-v37`, `peer-coordination-20260926-v38`, `peer-coordination-20260926-v39`, `peer-coordination-20260926-v40`, `peer-coordination-20260926-v41`, `peer-coordination-20260926-v42`, `peer-coordination-20260926-v43`, `peer-coordination-20260926-v44`, `peer-coordination-20260926-v45`, `peer-coordination-20260926-v46`, `peer-coordination-20260926-v47`, `peer-coordination-20260926-v48`, `peer-coordination-20260926-v49`, `peer-coordination-20260926-v50`, `peer-coordination-20260926-v51`, `peer-coordination-20260926-v52`, `peer-coordination-20260926-v53`, `peer-coordination-20260926-v54`, `peer-coordination-20260926-v55`, `peer-coordination-20260926-v56`, `peer-coordination-20260926-v57`, `peer-coordination-20260926-v58`, `peer-coordination-20260926-v59`, `peer-coordination-20260926-v60`, `peer-coordination-20260926-v61`, `peer-coordination-20260926-v62` |
| PR9 pin AMEND / density / maps / thin-tube | `pin-offset-cross-model`, `math-pr19-repair-candidate`, `math-pr21-axial-density`, `math-pr22-thin-tube`, `tip-3242d1ff` |
| Trial Batch410 no-promotion audit | `trial-batch410-audit-watch`, `trial-status-guard-snapshot`, `trial-pr143-batch410-merged` |
| Trial Batch416 living republish | `trial-batch416-tip-eng-brief`, `trial-batch416-unfreeze-brief`, `trial-pr144-batch416-merged` |
| Trial Batch453 idle no-promotion | `trial-batch453-tip-eng-idle`, `trial-batch453-unfreeze-brief`, `trial-pr145-batch453-merged` |
| Trial Batch455 living republish | `trial-batch455-tip-eng-brief`, `trial-batch455-unfreeze-brief`, `trial-pr146-batch455-merged` |
| Trial Batch546 tip_sync Soft Intent | `trial-batch546-tip-sync-watch-brief`, `trial-batch546-tip-sync-inv-pin-brief`, `trial-pr147-batch546-merged` |
| Math- PR70 hardening custody | `hardening-custody-manifest`, `hardening-custody-verify`, `hardening-custody-readme`, `math-pr70-hardening-custody-merged`, `math-pr75-proof-index-nav-merged`, `math-downstream-gate-workflow`, `math-downstream-gate-workflow-pr79`, `math-pr79-actions-bump-merged`, `math-pr59-transverse-unavailable-merged`, `h5-rim-contract-repair`, `h5-rim-contract-review-response`, `h5-rim-contract-py`, `h5-rim-contract-test`, `h5-rim-contract-verify`, `h5-rim-contract-workflow`, `bf-six-pin-workflow`, `bf-six-pin-scalar-*`, `bf-six-pin-hessian-*`, `bf-source-integrity`, `bf-source-integrity-test`, `math-pr89-bf-six-pin-merged`, `formal-lean-workflow`, `formal-lean-manifest`, `formal-lean-gate`, `formal-lean-gate-test`, `formal-lean-lakefile`, `formal-lean-toolchain`, `formal-lean-lake-manifest`, `formal-lean-core-root`, `formal-lean-algebra-v2`, `formal-lean-probability-v2`, `formal-lean-original-algebra`, `formal-lean-original-probability`, `formal-lean-scope`, `math-pr92-formal-lean-merged`, `transverse-contact-asymptotic`, `transverse-contact-geometry-cubic`, `transverse-contact-import-readme`, `transverse-contact-source-binding`, `math-pr94-transverse-import-merged`, `transverse-companion-collision-theorem`, `transverse-companion-exact-checks`, `transverse-companion-diagnostic-kernel`, `transverse-companion-fresh-replay`, `transverse-companion-readme`, `transverse-companion-hist-diagnostic`, `transverse-companion-hist-manifest`, `transverse-companion-hist-delivery-readme`, `transverse-companion-hist-verification`, `math-pr95-companions-merged`, `contact-kernel-substitute-note`, `contact-kernel-substitute-verify`, `math-pr80-contact-kernel-merged`, `drive-hole-substitutes-ledger`, `math-pr81-drive-hole-ledger-merged`, `public-reading-map`, `math-pr88-public-reading-map-merged`, `pin-neighborhood-recon-note`, `pin-neighborhood-recon-algebra`, `math-pr53-pin-neighborhood-merged`, `cycle4-public-reading-map`, `cycle4-benjamin-alpha-4pin`, `cycle4-benjamin-reduced-frame`, `cycle4-harper-closed-forms`, `cycle4-harper-d5-obstruction-ledger`, `cycle4-harper-readme`, `cycle4-harper-sard-g-a1-lemma`, `cycle4-harper-schur-diagnostic`, `cycle4-harper-test-closed-forms`, `cycle4-harper-test-ftt-conditional-mean`, `cycle4-harper-test-schur-diagnostic`, `cycle4-lucas-sard-g-a1-applied`, `math-pr87-cycle4-harper-merged`, `math-pr96-agents`, `formal-required-checks-doc`, `required-formal-check-tool`, `required-formal-check-tests`, `math-downstream-gate-workflow-pr96`, `formal-lean-workflow-pr96`, `math-pr96-required-formal-merged`, `d5-microdisk-note`, `d5-microdisk-quartic`, `math-pr82-d5-microdisk-merged`, `math-pr86-h5-rim-contract-merged`, `peer-coordination-20260926-v91`, `peer-coordination-20260926-v90`, `peer-coordination-20260926-v89`, `peer-coordination-20260926-v88`, `peer-coordination-20260926-v87`, `peer-coordination-20260926-v86`, `peer-coordination-20260926-v85`, `peer-coordination-20260926-v84`, `peer-coordination-20260926-v83`, `peer-coordination-20260926-v82`, `peer-coordination-20260926-v81`, `peer-coordination-20260926-v80`, `peer-coordination-20260926-v79`, `peer-coordination-20260926-v78`, `peer-coordination-20260926-v77`, `peer-coordination-20260926-v76`, `peer-coordination-20260926-v75`, `peer-coordination-20260926-v74`, `peer-coordination-20260926-v73`, `peer-coordination-20260926-v72`, `peer-coordination-20260926-v71`, `peer-coordination-20260926-v70`, `peer-coordination-20260926-v69`, `peer-coordination-20260926-v68`, `peer-coordination-20260926-v67`, `main-pr157-actions-bump-merged`, `peer-coordination-20260926-v66`, `math-pr76-gate-name-merged`, `math-pr78-vault-security-merged`, `stage-e-custody-manifest`, `stage-e-custody-verify`, `stage-e-custody-readme`, `math-pr83-stage-e-recovery-merged`, `h5-ledger-custody-manifest`, `h5-ledger-custody-verify`, `h5-ledger-custody-readme`, `math-pr84-h5-ledger-recovery-merged`, `lifetime-parent-erratum-congruence`, `lifetime-parent-erratum-pointer`, `lifetime-parent-cap-pairing-identities`, `p15-ascii-3e-minus-2`, `math-pr64-erratum-merged`, `math-pr85-custody-notes-merged`, `peer-coordination-20260926-v65`, `main-pr164-h5-links-merged`, `peer-coordination-20260926-v64`, `main-pr162-falsifier-links-merged`, `peer-coordination-20260926-v63`, `oa-pr70-custody-claim-watch`, `oa-pr70-byte-copy-verify-20260926`, `math-pr70-tip-drift-44901b5c`, `peer-coordination-20260926-v43`, `peer-coordination-20260926-v44`, `peer-coordination-20260926-v45`, `peer-coordination-20260926-v46`, `peer-coordination-20260926-v47`, `peer-coordination-20260926-v48`, `peer-coordination-20260926-v49`, `peer-coordination-20260926-v50`, `peer-coordination-20260926-v51`, `peer-coordination-20260926-v52`, `peer-coordination-20260926-v53`, `peer-coordination-20260926-v54`, `peer-coordination-20260926-v55`, `peer-coordination-20260926-v56`, `peer-coordination-20260926-v57`, `peer-coordination-20260926-v58`, `peer-coordination-20260926-v59`, `peer-coordination-20260926-v60`, `peer-coordination-20260926-v61`, `peer-coordination-20260926-v62` |
| main public shop / intake notes | `main-pr189-op-privacy-allow-merged`, `main-pr188-required-formal-merged`, `main-pr187-queue-recon-s7-merged`, `main-pr186-dropbox-import-merged`, `main-pr185-op-privacy-merged`, `main-pr184-dropbox-reconcile-merged`, `main-pr183-formal-ci-failclosed-merged`, `main-pr181-formal-converge-merged`, `main-pr182-library-publication-merged`, `main-pr180-release-custody-merged`, `main-pr179-queue-recon-s6-merged`, `main-pr178-formal-layer1-merged`, `main-pr177-formal-guidance-merged`, `main-pr176-exact-version-merged`, `main-pr175-embedded-q0-merged`, `main-pr174-queue-reconciliation-merged`, `main-pr173-source-census-merged`, `main-pr171-h3-rung-gate-merged`, `main-pr170-grok-part1-merged`, `main-pr169-h3-interval-merged`, `main-pr168-r2-autonomy-merged`, `main-pr134-claims-firewall-merged`, `main-pr148-operator-directive-merged`, `main-pr136-noncertifying-merged`, `main-pr140-pinned-sources-merged`, `main-pr166-museum-conditionals-merged`, `main-pr161-lb-rate-hold-merged`, `main-pr159-drive-lane-map-merged`, `main-pr163-grok-session-merged`, `main-pr135-interval-prose-merged`, `main-pr145-public-shop-merged`, `main-pr147-intake-example-merged`, `main-pr149-shop-links-merged`, `main-pr151-museum-merged`, `main-pr152-single-account-docs-merged`, `main-pr153-intake-gate-merged`, `main-pr150-side24-chart-merged`, `main-pr155-museum-complete-merged`, `main-pr156-intake-nonfinite-merged`, `main-pr158-museum-cache-merged`, `query-pr17-math-tip-refresh-merged`, `query-pr18-math-tip-refresh-merged` |
| Cross-model lanes | `cross-model-lanes` |
| Review-notes index | `review-notes-index` … `-v92` |

The catalog contains 592 public artifacts (CI upper bound 600), including code, tests, outputs, the full-price replay runner, the fixed-remote RN sources, the merged downstream hard-gate package (PR13 + PR15 identities), SHA-matched public Drive replicas (SIDE24 enclosure, marked-cylinder, matrix-cap/lifetime, consecutive-palette, P15-B), merged Math- D5 Hermite/axial-density identities, merged Math- PR70 hardening-custody MANIFEST/verify/readme, merged Math- PR83 STAGE_E falsifier recovery MANIFEST/verify/readme, merged Math- PR84 H5 ledger recovery MANIFEST/verify/readme, merged Math- PR86 H5 rim contract repair package, merged Math- PR82 D5 nested microdisk NOTE+QUARTIC, merged Math- PR89 BF six-pin scalar+hessian certificates, merged Math- PR92 source-bound Lean formal lane, merged Math- PR94 transverse-contact import, merged Math- PR95 collision companions, merged Math- PR80 contact-kernel reconstruction, merged Math- PR81 drive-hole ledger, merged Math- PR88 PUBLIC_READING_MAP, merged Math- PR53 pin-neighborhood recon, merged Math- PR87 cycle-4 Harper packet, merged Math- PR96 required formal gates, note-only main PR189 OP-PRIVACY allow, note-only main PR188 required formal, note-only main PR187 queue recon §7, note-only main PR186 Dropbox import, note-only main PR185 OP-PRIVACY, note-only main PR184 Dropbox reconcile, note-only main PR183 formal CI fail-closed, note-only main PR181 formal converge, note-only main PR182 library publication, note-only main PR180 release custody, note-only main PR179 queue recon §6, note-only main PR178 Layer 1 formal SIDE24 pilot, note-only main PR177 formal guidance/museum, note-only main PR176 exact-version recovery, note-only main PR175 embedded q0 recovery, note-only main PR174 queue reconciliation, note-only main PR173 source census, note-only main PR171 H3-RUNG-FLOOR gate, note-only main PR170 Grok Part1, note-only main PR169 H3 interval claims_check, note-only main PR168 R2/autonomy, note-only main PR134 claims firewall, note-only main PR148 operator-directive, note-only main PR136 noncertifying/float-labelling, note-only main PR140 pinned-sources index, note-only main PR166 museum conditionals, note-only main PR161 LB-RATE HOLD landing, note-only main PR159 drive-lane-map, note-only main PR163 grok-session replay ledger, note-only main PR135 interval prose/test hardening, merged Math- PR76 downstream-gate workflow display name, merged governance- two-key review topology, and nonauthor review/replay routing notes. All earlier identities remain unchanged. Campaign dispatch [#61](https://github.com/d6g8k5htny-coder/main/issues/61) is closed as superseded by [#86](https://github.com/d6g8k5htny-coder/main/issues/86). Future agent actions follow `multi-agent-dispatch-20260925-v91`. The full-range theorem removes the probability ceiling but retains demand>=2 and the realized-family hypotheses; [review #74](https://github.com/d6g8k5htny-coder/main/issues/74) remains open. The demand-one counterexample is not retracted. Math- PR7/PR9 mesoscopic work is coordinated via notes only until merge; not cataloged as finished sources. The hard-gate package is engineering integrity control (`lemma_closed` stays false), not analytic acceptance. `#90` is CLOSED at engineering-gate scope only (PR98 merge `ebedb780`; `promotion_permission:false`); not theorem acceptance. Catalog includes Math- PR63 P15 full-price nonauthor ACCEPT. trial PR138 still subject-stale vs `cc6a578b`.

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

## Federation source contracts

Versioned transport contracts live in [schemas/](schemas/). They define source references, repository roles, source manifests, and workspace snapshots. These schemas describe identity and routing only; they do not establish theorem truth or scientific status.

The read-only checker [tools/architecture_conformance.py](tools/architecture_conformance.py) validates repository ownership, public/private boundaries, immutable snapshot refs, optional source manifests, and architecture-authority limits. It never writes scientific state.

Run:

```bash
python -B -S -m unittest discover -s tests -p 'test_*.py' -v
python -B -S tools/architecture_conformance.py --workspace /path/to/eight-repo-workspace
```

Unknown schema major versions, mutable refs, sandbox leakage, scientific-status fields in public registry artifact rows, and architecture ownership of promotion fields fail closed.