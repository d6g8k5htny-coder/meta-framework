# Exact demanded palettes for consecutive capacity supports, including nonmatroids

Object: **P15-CONSECUTIVE-CAPACITY-PALETTES-20260924-v1**. Author: OpenAI / ChatGPT, 24 September 2026.
Task PAL-01, campaign #61. Author-side structural application; no independent acceptance, unrestricted prize closure or historical novelty claim.

## 1. The new applicable class, not a claimed new coloring theory

The predecessor #59 solves a matroid-presenting support system using Edmonds' partition theorem. A nonmatroid rejection of that route does not prove that every other exact structural route fails. Here a DIFFERENT, overlapping class admits a direct demanded-palette construction.

There are n blocks with nonnegative integer demands d_i. A global label can be assigned to a set I of blocks, at most once per block. There are complete capacity constraints

    |I intersection A_j| <= c_j,

where c_j are nonnegative integers. Assume the input supplies a permutation of the block indices under which every nonempty A_j is a consecutive interval. This must be checked, not assumed from an appealing drawing. It is the capacity sets that are consecutive in an order of BLOCKS. The transpose convention for interval incidence in other papers can be different.

The task is to find palettes P_i of at least d_i distinct labels that satisfy every capacity constraint for every label, while minimizing the total number K of available labels. By deleting superfluous memberships, exact demands are sufficient and may be assumed.

For the P15-B palette-separation interface, a crossing support e forbids one label from appearing on every block in e, equivalently the capacity constraint A=e, c=|e|-1. Complete identification of the ACTUAL crossing supports and compatible local demands is still a separate mathematical premise.

## 2. Exact optimum

A zero-capacity set containing positive total demand is infeasible. A zero-capacity set of zero total demand can be ignored for the ratio. Otherwise set

    R=max( max_i d_i, max_{j:c_j>0} d(A_j)/c_j ),
    K_star=ceil(R),            d(A)=sum_{i in A}d_i.        (1)

Empty maxima are zero; in particular all-zero demand has K_star=0.

**Theorem.** Under the supplied consecutive-order premise, (1) is the exact palette optimum.

Necessity is immediate: d_i distinct labels need K>=d_i, and each of K labels supplies at most c_j memberships in A_j, hence d(A_j)<=Kc_j.

For sufficiency let K=K_star>0. Form an ordered sequence of d_1 demand positions for the first block in the supplied order, then d_2 positions for the next, and so on. Color successive positions cyclically by

    0,1,...,K-1,0,1,... .

Each block occupies one consecutive segment of length d_i<=K, so its positions receive DISTINCT labels. No copying of random coordinates or probabilistic independence is involved; these positions are bookkeeping for color demand.

Each A_j consists of consecutive blocks, hence occupies one consecutive segment of length d(A_j) in that demand sequence. Every residue modulo K occurs at most ceil(d(A_j)/K) times in any such segment. Since d(A_j)<=Kc_j and c_j is an integer, this is at most c_j. Because each block uses a label at most once, demand-position counts equal block-incidence counts. Every capacity constraint is satisfied. QED.

The proof needs neither exchange nor a matroid representation. It does not extend to arbitrary supports by deleting the consecutive-order premise.

## 3. Exact lower certificates and the fractional optimum

A maximizing singleton in (1), or a maximizing capacity set with weight 1/c_j on its blocks and zero elsewhere, is an explicit dual lower witness. Every allowed color class has dual weight at most one, so its total objective R lower-bounds the number of colors fractionally.

The fractional independent-class covering optimum equals R. Since R is rational, choose a positive integer t with tR integer; scale demands by t and apply (1), obtaining an integral cover of tR labels. Divide its class multiplicities by t. This gives fractional cost R and the opposite inequality follows from the dual witness. Thus the integral optimum is exactly the ceiling of the fractional optimum on this consecutive-support class.

This is another structural integer-rounding property, not a claim about general hypergraph palettes. It is proved directly here and not inferred from #59's matroid condition.

## 4. Nonmatroid example and why a supplied order matters

Take A_1={0,1}, A_2={1,2}, both with capacity1. The allowed sets contain {1} and {0,2}, but no element of the latter can augment the former. Hence the independence system is not a matroid. Both constraints are consecutive in the order0,1,2, so this theorem nevertheless applies:

    K_star=max(d_0+d_1,d_1+d_2).

For unit demands, palettes {0},{1},{0} attain2. The failed exchange test is correct for the matroid route; it is not a reason to reject this separate construction.

For six blocks of demand408 and the five adjacent-pair constraints {i,i+1}, i=0,...,4, the optimum is816. One compressed solution is408 labels on {0,2,4} and408 on {1,3,5}. A pair constraint proves the816 lower bound. Pairwise-disjoint palettes would use2448.

This six-block example has DIFFERENT crossing supports from #59's all-fifteen-four-block matroid example. The coincident816 answer and similar displayed coloring do not make the original downset hypotheses interchangeable.

A minimal refusal is the triangle of pair constraints {0,1},{1,2},{0,2}, all capacity1 and all demands1. Formula(1) alone would give2, but every pair conflicts, so the true optimum is3. No linear order makes all three pair sets consecutive. The code rejects a nonconsecutive constraint instead of returning this false optimum.

The program tests the SUPPLIED order. A rejection says that order is invalid, not that no other order could work. This distinction is tested with a reordered valid instance. Circular consecutiveness is not substituted for linear consecutiveness; the triangle also explains that danger.

## 5. Compression and implementation complexity

A block's consecutive demand segment produces at most two intervals of labels in [0,K), after reducing its endpoints modulo K; a block using every label produces the single interval [0,K). The union of interval endpoints is contained in0,K and the starts/ends of the n block segments modulo K, so there are at most2n+1 elementary constant-incidence pieces. Adjacent pieces with the same support are combined.

`interval_palette.py` therefore does not enumerate all K labels or all sum(d_i) demand positions. It uses exact integer arithmetic, a sorted endpoint sweep and explicit support lists. The number of sweep endpoints is O(n), but explicitly emitting a support at every piece can take O(n^2) space/time in the worst case. Input validation also reads every supplied capacity-set member. This is not a falsely advertised linear-time algorithm or an implementation of general consecutive-ones recognition.

The verifier checks that label intervals partition[0,K), every membership is legal and distinct, all block demands are met exactly, every capacity is respected, and the lower witness agrees with the instance. It does not establish that an abstract input is the actual P15 support family.

The separate bounded reference optimizer enumerates allowed color incidences and uses a memoized residual-demand recurrence, without using (1), cyclic placement or consecutive structure. The comparison is finite software evidence, not a substitute for the theorem proof. Large-demand controls ensure output remains compressed.

## 6. P15 binding and exclusions

When every COMPLETE crossing support e is consecutive in the supplied order, the exact P15 palette count is

    K_star=max( max_i d_i,
                max_e ceil(sum_{i in e}d_i/(|e|-1)) ).    (2)

A singleton support with positive demand is infeasible. P15-B may consume these palettes only with its actual compatible local covers, hazard/price assumptions, original coordinate independence and support-completeness proof. None of those facts is inferred from the optimizer or its test inputs.

This extends the menu of exact structural tools beyond the matroid-only route, not the unrestricted prize result. Nonconsecutive instances remain available to the prior general finite optimizer or other justified methods.

## 7. Primary-source reconnaissance and attribution

Antoniadis, Hueffner, Lenzner, Moldenhauer and Souza, *Balanced Interval Coloring*, arXiv:1012.3932v1, Sections2.1-2.4 and Theorem6, were inspected. That paper proves balanced coloring results using consecutive-ones/total-unimodularity structure and discusses the failure of discrepancy-one behavior for circular arcs. Its interval incidence orientation is explicitly distinguished from our order of block-demand segments. Balanced coloring of interval structures is established mathematics, not a project novelty claim.

The proof here is the elementary cyclic demanded-segment application to our stated capacity interface, with an explicit P15 crosswalk, compressed implementation and source/hypothesis refusals. No theorem from the paper is needed as an unproved black box for the cyclic argument above. General matroid partition remains the explicitly attributed Edmonds1965 import in the predecessor, not in this proof.
