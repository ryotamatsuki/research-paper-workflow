# Equilibrium Continuation Completeness Checklist

Use this checklist for sequential/game-theoretic models whenever a current action changes the state, ordering, active set, participation set, market coverage, matching pattern, network, or other object that affects a downstream subgame.

The purpose is to prevent a local/regular-branch solution from being promoted into an SPNE claim without verifying economically relevant off-path continuations.

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
- [ ] If mixed strategies are required by the stated equilibrium concept, either solve/characterize them or stop the SPNE claim.
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

## 7. Required audit record

Record:

- Equilibrium concept:
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

A sequential model cannot pass the Stage 4 equilibrium gate or later claim SPNE when a material upstream deviation leads to an `UNRESOLVED` or `NUMERICAL_FAILURE` downstream continuation.

FOCs + SOCs + feasibility/interiority on one branch are necessary branch checks, not sufficient global equilibrium certification.
