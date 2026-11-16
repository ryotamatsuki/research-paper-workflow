# Equilibrium Continuation Completeness Checklist

Use the equilibrium-analysis contract below for every strategic model. Apply the continuation-specific sections whenever a current action changes the state, ordering, active set, participation set, market coverage, matching pattern, network, or other object that affects downstream play. Mark genuinely inapplicable items with reasons; do not silently skip material obligations.

The purpose is to prevent a local/regular-branch solution from being promoted into an SPNE claim without verifying economically relevant off-path continuations.

## 0. Equilibrium-analysis contract (Stages 1, 3, 4, 4A, 7, 7.5A, 8)

- [ ] Specify horizon, timing, simultaneous/sequential moves, chance, observability, perfect/imperfect information, complete/incomplete information, types, information sets, feasible contingent strategies and beliefs as applicable.
- [ ] Choose and justify the equilibrium concept and solution method from the game and research question. Static complete-information: Nash; static private-information: Bayesian Nash; finite sequential games: SPNE with backward induction/recursion wherever proper-subgame structure permits; incomplete/imperfect-information dynamic games: a suitable precisely defined PBE, sequential equilibrium or other refinement when belief-based sequential rationality is needed; infinite-horizon/state games: appropriate recursive/fixed-point or other methods (e.g., Markov perfect equilibrium with stated stationarity/state restrictions). These examples are not automatic assignments.
- [ ] Declare strategy class and completeness target before solving: pure / mixed / behavioral, full strategies or assessments versus outcomes, parameter domain, and any justified equilibrium-selection or refinement restrictions.
- [ ] Stage 1 records a provisional contract and reconstructs the starting object; Stage 3 selects scope; Stage 4 solves it; Stage 4A independently attacks it; Stage 7 tests equilibrium-dependent welfare; Stage 7.5A certifies wording/scope; Stage 8 freezes the final contract. Reassess at the earliest affected stage if timing, information, admissible strategies or concept changes.
- [ ] Do not force pure SPNE on all models or adopt a refinement simply because it yields the preferred result. An optimization-only model records strategic-equilibrium checks as not applicable.

## 1. Game-domain definition

- [ ] Every player's complete strategy set is stated, including boundary and off-path actions.
- [ ] Consumer/agent choice sets are explicit. Do not infer an adjacent-only, local, segmented, or restricted choice set from a convenient demand formula.
- [ ] Payoffs are defined for every feasible history required by the equilibrium concept, or the model explicitly restricts histories/strategies and economically defends that restriction.
- [ ] Ties, coincident actions/locations, zero shares, entry/exit, participation changes, and ordering changes are defined where they can occur.
- [ ] The metric/technology/allocation rule used after an off-path action is stated independently of the equilibrium branch.

## 2. Continuation completeness

For every downstream subgame that matters for an upstream deviation:

- [ ] Re-solve the downstream game after the deviation; do not reuse an on-path formula outside its validity domain.
- [ ] Distinguish a candidate satisfying FOCs/SOCs from a Nash equilibrium over the full strategy set.
- [ ] Search for finite/global deviations, not only infinitesimal deviations.
- [ ] Enumerate or otherwise solve relevant active sets, corners, kinks, ordering changes, regime switches, and boundary solutions.
- [ ] If pure-strategy equilibrium may fail to exist, detect and report nonexistence rather than silently substituting the regular branch.
- [ ] For finite-horizon sequential games solve terminal decisions first, then all relevant proper subgames by backward induction/backward recursion over the full continuation-equilibrium correspondence. Include those off path; if a different method is used, establish equivalence or justify why recursion is inapplicable.
- [ ] If pure equilibrium fails in any required subgame, explicitly assess mixed/behavioral continuations. When pure equilibria exist, also assess whether mixed equilibria could materially alter the claim. Pure-only scope requires economic justification and explicit exclusions; a pure-SPNE existence result cannot be advertised as a complete SPNE characterization.
- [ ] For mixed/behavioral equilibria, check support enumeration or a suitable analytic characterization, best-response equality for actions in support, inequalities for excluded actions, probabilities and boundary/degenerate supports, plus global deviations over actual feasible actions. For continuous strategies use an appropriate distribution/support argument rather than assuming finite support.
- [ ] Where information sets and beliefs matter, verify sequential rationality, Bayes updating on path and the chosen concept's off-path belief/consistency conditions. Do not treat a node inside a nonsingleton information set as a proper subgame. For sequential equilibrium verify its consistency requirement, not merely arbitrary off-path beliefs.
- [ ] If equilibrium is multiple, state the continuation-selection rule and test whether the headline result depends on it.

## 3. Solver-failure semantics — fail closed

Every numerical/symbolic routine used in equilibrium certification must classify outcomes explicitly:

- `SOLVED_EQUILIBRIUM`
- `SOLVED_NO_EQUILIBRIUM` when nonexistence is actually established
- `MULTIPLE_EQUILIBRIA`
- `UNRESOLVED`
- `NUMERICAL_FAILURE`

Rules:

- [ ] `None`, NaN, exception, failed convergence, invalid active set, or branch violation is never treated as evidence that an economic deviation is unprofitable.
- [ ] An unresolved continuation makes the upstream equilibrium certification unresolved unless a separate proof shows that history is irrelevant or infeasible.
- [ ] Filtering infeasible parameter draws is allowed only when infeasibility follows from primitives, not because the preferred equilibrium formula failed.
- [ ] Report counts and locations of every unresolved/failed continuation encountered in a global audit.

## 4. Independent payoff reconstruction

For at least one high-stakes equilibrium claim:

- [ ] Construct an independent direct-payoff/allocation evaluator from primitives that does not call the candidate equilibrium solver.
- [ ] Use it to test unilateral deviations against the reported equilibrium.
- [ ] For spatial/discrete-choice models, directly assign/integrate consumers over the stated complete choice set for selected adversarial price/action profiles.
- [ ] For allocation/matching/participation models, independently recompute the allocation after adversarial deviations.
- [ ] Reproduce at least one on-path benchmark and deliberately test profiles outside the regular branch.

## 5. Adversarial history generation

Do not sample only around the candidate equilibrium. Include histories designed to break the maintained branch:

- [ ] large unilateral deviations;
- [ ] actions near rivals/thresholds/boundaries;
- [ ] ordering reversals or crossings;
- [ ] market-share collapse or dominance;
- [ ] active-set changes;
- [ ] extreme but feasible prices/actions;
- [ ] points where the closed-form branch returns invalid/interior-condition failure.

Any discovered counterexample becomes a permanent regression test.

## 6. Sequential-equilibrium/SPNE certification

Before writing `SPNE`, `subgame-perfect`, `whole-domain`, `global best response`, or equivalent:

- [ ] Identify every class of off-path history induced by an upstream unilateral deviation.
- [ ] Establish a valid downstream continuation for those histories or explicitly narrow the strategy/game domain.
- [ ] Verify the upstream deviation using the re-solved downstream continuation payoff.
- [ ] Confirm that no solver failure was discarded from the deviation set.
- [ ] Separate on-path equilibrium verification from off-path continuation verification in the report.
- [ ] For each claimed equilibrium class establish existence/nonexistence, necessity and sufficiency, and uniqueness/multiplicity as applicable. Exclude additional equilibria using an exhaustive partition, analytic correspondence or equivalent proof; checking a proposed candidate's deviations is insufficient.
- [ ] Distinguish equilibrium paths/allocations from complete contingent strategies and (where applicable) belief assessments. For ties, do not equate one fixed tie-break with the set of all equilibrium continuations.
- [ ] For restricted pure/Markov/stationary or selected-equilibrium claims, justify the restriction, explicitly label what is excluded and assess whether exclusions matter for the headline or welfare conclusions. An existence-only theorem may remain such; do not assert uniqueness/completeness without proof.

## 7. Required audit record

Record:

- Equilibrium concept and economic justification:
- Solution method and reason for applicability:
- Declared strategy class and completeness target:
- Information sets and belief/consistency requirements:
- Full strategies/assessments versus outcomes:
- Existence/nonexistence, necessity/sufficiency and additional-equilibrium exclusion proof:
- Mixed/behavioral support coverage and justified exclusions:
- Material equilibrium-selection/welfare sensitivity:
- Full strategy/history domain:
- Regular/local branch used, if any:
- Off-path history classes checked:
- Active sets/corners checked:
- Independent payoff evaluator:
- Global-deviation method:
- Solver outcome taxonomy:
- Number of unresolved continuations:
- Counterexamples found:
- Pure-equilibrium nonexistence encountered?:
- Multiplicity encountered?:
- Continuation-selection assumption, if any:
- Final continuation verdict: `PASS / UNRESOLVED / FAIL`

## 8. Gate rule

A sequential model cannot pass the Stage 4 equilibrium gate or later claim SPNE when a material upstream deviation leads to an `UNRESOLVED` or `NUMERICAL_FAILURE` downstream continuation. Across strategic models, an unresolved equilibrium, support or belief issue material to the declared claim blocks the corresponding gate. A justified narrower theorem may be certified only within its proved scope; no unrestricted or selection-independent language may outrun the evidence.

FOCs + SOCs + feasibility/interiority on one branch are necessary branch checks, not sufficient global equilibrium certification.
