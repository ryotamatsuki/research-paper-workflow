# Evidence Ledger

Historical research label: Evidence-status register for the retail-service worked case

Canonical workflow mapping: Supports Stage 1 verification, Stage 2/6 literature integrity, and provenance requirements

Research status: Documentation ledger only; not a submission-level verification archive

This ledger deliberately distinguishes project provenance from externally reproducible evidence. `worked-case provenance != submission bibliography verification`.

## Status vocabulary

- `VERIFIED` — checked within the historical research process or logically established from the stated setup; still reproduce in a production repository when material.
- `REPORTED / REQUIRES REPRODUCTION` — reported in the prior research conversation, but code/proof artifacts are not archived here.
- `LITERATURE-VERIFIED` — bibliographic/proposition claim was previously checked against an external source; any publication manuscript should still preserve exact source records.
- `INSTITUTIONALLY SUGGESTIVE` — useful motivation but not proof of a model primitive.
- `CONJECTURE` — numerical or provisional theoretical support only.
- `REJECTED` — branch/result rejected by mathematical, literature, or conceptual audit.

## Mathematical and theoretical claims

| Claim | Type | Status | Evidence basis | Reproduction needed? |
|---|---|---|---|---|
| Stage 1 service condition `e* = (ell/k) q_L*` | Mathematical | `REPORTED / REQUIRES REPRODUCTION` | Prior research conversation reported a full symbolic derivation and identity checks | Yes — production SymPy script and proof record |
| `q_L → 0 ⇒ e → 0` under sales-margin-only financing | Mathematical / conceptual | `REPORTED / REQUIRES REPRODUCTION` | Direct implication of the reported Stage 1 FOC | Yes for publication; retained as historical decision basis |
| Stage 1 wholesale ordering `w_L < benchmark < w_R` | Mathematical | `REPORTED / REQUIRES REPRODUCTION` | Prior symbolic analysis | Yes |
| Static service contract can support `q_L=0, e>0` | Theoretical feasibility | `VERIFIED` at conceptual level | A sales-independent service payment/capacity contract can finance service without local sales | Yes for any specific formal contract used in a paper |
| Static service-only former dealer equals generic third party absent payoff-relevant history | Conceptual | `VERIFIED` | If actors have identical technology, information, and contracts, the historical label does not enter payoffs | No for the logic; yes for any specific formal comparison |
| Installed base can preserve service demand after local retail exit | Conceptual | `VERIFIED` | Stock of past durable sales can remain positive when current local sales are zero | Yes for any formal dynamic model |
| Provider-independent installed base does not create former-dealer advantage | Conceptual | `VERIFIED` | `I_t` affects market/service demand but not provider-specific technology by assumption | No for the logical point |
| Legacy service capital can make former dealer different from fresh provider | Theoretical component | `VERIFIED` conditionally on `K_L>K_P` | Payoff-relevant provider-specific state changes service technology/value | Yes; must justify `K` economically |
| Candidate law `K_{t+1}=(1-δ_K)K_t+φq_{Lt}` | Model primitive | `CONJECTURE` / unresolved | Used as a tractable historical candidate; causal link from sales to service capability is not yet microfounded | Yes — main blocker |
| Dynamic result `q_L1>q_R1` / dealer-favoring wholesale terms | Mathematical candidate | `REPORTED / REQUIRES REPRODUCTION` | Prior two-period symbolic analysis under candidate accumulation law | Yes — after microfoundation is selected |
| Premature private service-network exit relative to social optimum | Welfare candidate | `REPORTED / REQUIRES REPRODUCTION` | Prior threshold/welfare exercise | Yes |
| True hysteresis | Theoretical claim | `REJECTED` at current stage | Existing branch establishes state dependence, not entry/exit irreversibility | N/A unless future model adds required structure |

## Literature claims

| Claim | Type | Status | Evidence basis | Reproduction needed? |
|---|---|---|---|---|
| Classical retail-service / vertical-restraint literature overlaps with generic service externality results | Literature | `REPORTED / REQUIRES RE-VERIFICATION` | Prior literature audit identified classic service and vertical-control papers | Yes — rerun closest-paper matrix |
| Xu–Fu–Fan (2020) threatens generic O2O/service-sharing novelty | Literature | `REPORTED / REQUIRES RE-VERIFICATION` | Prior research conversation treated it as a close service-sharing paper | Yes |
| Chai–Duan–Huo (2021) threatens a service-spillover/wholesale-price contribution | Literature | `REPORTED / REQUIRES RE-VERIFICATION` | Prior proposition-level discussion | Yes |
| Lei–Li–Cheng (2024) is close to cross-channel local service sharing | Literature | `REPORTED / REQUIRES RE-VERIFICATION` | Prior research conversation | Yes |
| Zhang–Lim–Ye (2025) is critical for joint distribution/service-channel choice | Literature | `REPORTED / REQUIRES RE-VERIFICATION` | Prior research conversation | Yes |
| Li et al. (2016) and related work cover generic service-provider choice/outsourcing | Literature | `REPORTED / REQUIRES RE-VERIFICATION` | Prior research conversation | Yes |
| Installed-base/aftermarket dynamics are known components | Literature | `REPORTED / REQUIRES RE-VERIFICATION` | Prior Stage 3 literature gate | Yes |
| Relationship-specific dealer/service investment is a known component | Literature | `REPORTED / REQUIRES RE-VERIFICATION` | Prior Stage 3 literature gate | Yes |

This repository intentionally does not claim that every bibliographic detail above is submission-ready. A production project must use `checklists/LITERATURE_AUDIT_CHECKLIST.md` and re-open the closest papers.

## Institutional claims

| Claim | Type | Status | Evidence basis | Reproduction needed? |
|---|---|---|---|---|
| Local dealers can provide installation, repair, maintenance, home visits, and consumer support | Institutional motivation | `INSTITUTIONALLY SUGGESTIVE` | General motivating practice discussed in the historical project | Yes for any industry-specific claim |
| Manufacturer-specific training, tools, certification, or technical know-how can create relationship-specific capability | Institutional motivation | `INSTITUTIONALLY SUGGESTIVE` | Prior institutional/literature search identified examples in dealer/service settings | Yes, with primary sources where possible |
| Panasonic pays a sales-independent service retainer to local dealers | Institutional claim | `REJECTED / NOT ESTABLISHED` | No verified public primary-source basis was established in the historical project | Do not claim without new evidence |
| Service-only facilities exist in some durable-goods dealer systems | Institutional motivation | `REPORTED / REQUIRES RE-VERIFICATION` | Prior research found examples; this case does not archive source records | Yes |

## Evidence limitation

This PR performs no new full external literature or institutional audit and adds no new symbolic/numerical proof. It documents what the historical research process relied on and marks what must be independently reproduced before a paper can rely on it.
