"""Metadata routing only; evidence truth, novelty, creative quality require research judgment."""
from dataclasses import dataclass, field
from typing import Mapping

LANES=frozenset(f'L{i}' for i in range(1,9))
DEEP={'MODEL_RESULT','FULL_MODEL_PROOF'}
PRIMARY=DEEP|{'ABSTRACT_ONLY','AUTHOR_SUMMARY'}
ROUTES={'NEW_MECHANISM','NEW_RESULT','GENERALIZATION','CORRECTION','INSTITUTIONAL_COMPARISON','APPLICATION'}
CORE={'L2','L4','L8'}
LIMITS={'rounds':3,'candidates':12,'deep_screens':6,'searches':60,'inspections':30}

@dataclass(frozen=True)
class Source:
    id:str
    depth:str
    location:str=''
    mapping:str=''
    decisive:bool=True
    adequate_for_claim:bool=False

@dataclass(frozen=True)
class Objection:
    id:str
    issue:str
    disposition:str # REFUTED / AUDITABLE / FATAL_UNRESOLVED
    next_test:str=''
    evidence_ref:str=''
    source_ids:tuple[str,...]=()

@dataclass
class Candidate:
    id:str
    fingerprint:str
    target:str
    falsifier:str
    question:str=''
    economic_learning:str=''
    predictive_contrast:str=''
    route_type:str=''
    benchmark:str=''
    delta:str=''
    economic_motivation:str=''
    minimum_test:str=''
    parent_mapping:str=''
    residual_distinction:str=''
    sources:tuple[Source,...]=()
    lanes:Mapping[str,str]=field(default_factory=dict)
    lane_evidence:Mapping[str,tuple[str,...]]=field(default_factory=dict)
    na_reasons:Mapping[str,str]=field(default_factory=dict)
    objections:tuple[Objection,...]=()
    risk_reviewed:bool=False
    removal_test:str=''
    red_team:str=''
    absorbed_evidence:str=''
    absorption_source_ids:tuple[str,...]=()
    no_residual_reason:str=''
    no_residual_evidence:str=''
    parent_ids:tuple[str,...]=()
    successor_delta:str=''
    epoch_reframe:str=''
    epoch_settings:tuple[str,...]=()
    epoch_prediction:str=''
    epoch_necessity:str=''
    author_selected:bool=False
    # v5 migration retains unclassified blockers; never silently promote.
    legacy_blockers:tuple[str,...]=()

@dataclass(frozen=True)
class Decision:
    maturity:str
    disposition:str
    novelty:str
    eligible:bool
    reasons:tuple[str,...]=()

@dataclass
class Budget:
    limits:dict=field(default_factory=lambda:LIMITS.copy())
    used:dict=field(default_factory=lambda:dict.fromkeys(LIMITS,0))
    def __post_init__(self):
        if set(self.limits)!=set(LIMITS) or set(self.used)!=set(LIMITS) or any(type(self.used[k]) is not int or type(self.limits[k]) is not int or not 0<=self.used[k]<=self.limits[k] for k in LIMITS): raise ValueError('invalid checkpoint')
    def consume(self,kind,n=1):
        if kind not in self.limits or type(n) is not int or n<0: raise ValueError('invalid operation')
        if self.used[kind]+n>self.limits[kind]: return False
        self.used[kind]+=n; return True
    def extend(self,limits,*,authorized=False):
        if not authorized: raise PermissionError('explicit extension required')
        if any(k not in self.limits or type(v) is not int or v<self.limits[k] for k,v in limits.items()): raise ValueError('invalid extension')
        self.limits.update(limits)
    def checkpoint(self): return {'limits':self.limits.copy(),'used':self.used.copy()}


def signature(c):
    return tuple(' '.join(x.casefold().split()) for x in (c.fingerprint,c.target,c.falsifier))

def assess(c,mode='STANDARD',killed=(),*,new_evidence_ref=''):
    if mode not in {'STANDARD','EPOCH'}: raise ValueError('invalid mode')
    def result(m,d,n,eligible=False,*reasons): return Decision(m,d,n,eligible,tuple(reasons))
    if not all(x.strip() for x in (c.id,c.fingerprint,c.target,c.falsifier)): return result('DISCOVERY','HOLD','UNSCREENED',False,'incomplete candidate identity')
    if any(signature(c)==signature(k) for k in killed) and not new_evidence_ref.strip(): return result('DISCOVERY','MERGED','UNRESOLVED',False,'same rejected signature')
    if c.parent_ids and not c.successor_delta.strip(): return result('DISCOVERY','HOLD','UNRESOLVED',False,'successor requires substantive change')
    ds=[s for s in c.sources if s.decisive]
    supported={s.id for s in ds if s.depth in DEEP and s.location and s.mapping and s.adequate_for_claim}
    if c.absorbed_evidence:
        if c.absorption_source_ids and set(c.absorption_source_ids)<=supported:
            return result('DISCOVERY','REJECT','ABSORBED',False,c.absorbed_evidence)
        return result('DISCOVERY','HOLD','UNRESOLVED',False,'absorption allegation not verified')
    if c.no_residual_reason:
        if c.no_residual_evidence.strip(): return result('DISCOVERY','REJECT','UNRESOLVED',False,c.no_residual_reason)
        return result('DISCOVERY','HOLD','UNRESOLVED',False,'no-residual assertion lacks reasoned evidence')
    missing=[k for k in ('question','economic_learning','predictive_contrast','benchmark','delta','economic_motivation','minimum_test','parent_mapping','residual_distinction') if not getattr(c,k).strip()]
    if c.route_type not in ROUTES: missing.append('contribution route')
    if not any(s.decisive and s.depth in PRIMARY and s.location.strip() and s.mapping.strip() for s in c.sources): missing.append('closest primary source and comparison')
    for l in sorted(CORE):
        if c.lanes.get(l) not in {'COMPLETED','SCOPED'} or not any(x.strip() for x in c.lane_evidence.get(l,())): missing.append('targeted search '+l)
    if not c.risk_reviewed or not c.objections: missing.append('explicit strongest-objection review')
    if len({o.id for o in c.objections})!=len(c.objections): missing.append('duplicate objection ID')
    for o in c.objections:
        if not o.id.strip() or not o.issue.strip() or o.disposition not in {'REFUTED','AUDITABLE','FATAL_UNRESOLVED'}: missing.append('invalid objection')
        elif o.disposition=='REFUTED' and not o.evidence_ref.strip(): missing.append('refutation evidence '+o.id)
        elif o.disposition=='AUDITABLE' and (not o.next_test.strip() or not o.evidence_ref.strip()): missing.append('bounded audit plan/evidence '+o.id)
        elif o.disposition=='FATAL_UNRESOLVED': missing.append('fatal open threat '+o.id)
    for src in ds:
        if src.id not in supported and not any(src.id in o.source_ids and o.disposition in {'AUDITABLE','FATAL_UNRESOLVED'} for o in c.objections):
            missing.append('inadequate decisive source lacks risk classification '+src.id)
    if c.legacy_blockers: missing.append('legacy blockers require explicit reclassification')
    if missing: return result('DISCOVERY','HOLD','UNRESOLVED',False,*missing)
    # PROMISING is research-worthiness, never novelty clearance. Scope and finite next test remain mandatory.
    outstanding=[]
    for s in ds:
        if s.id not in supported: outstanding.append('source depth/mapping '+s.id)
    for l in sorted(LANES):
        if c.lanes.get(l)=='COMPLETED' and any(x.strip() for x in c.lane_evidence.get(l,())): continue
        if l=='L1' and c.lanes.get(l)=='NA' and c.na_reasons.get(l,'').strip(): continue
        outstanding.append('full search '+l)
    outstanding += ['open audit '+o.id for o in c.objections if o.disposition=='AUDITABLE']
    if not c.removal_test.strip(): outstanding.append('removal test')
    if not c.red_team.strip(): outstanding.append('adversarial review')
    if mode=='EPOCH':
        if not (c.epoch_reframe.strip() and len({s.strip() for s in c.epoch_settings if s.strip()})>=2 and c.epoch_prediction.strip() and c.epoch_necessity.strip()):
            return result('DISCOVERY','HOLD','UNRESOLVED',False,'epoch-specific substantive reframe absent',*outstanding)
        if outstanding: return result('PROMISING','HOLD','UNRESOLVED',False,*outstanding)
    if outstanding: return result('PROMISING','ACTIVE','UNRESOLVED',True,*outstanding)
    return result('PRE_SCREEN_SURVIVED','ACTIVE','PRE-SCREEN SURVIVED',True)

def route(candidates,*,mode='STANDARD',budget_exhausted=False,exhausted_in_scope=False,killed=()):
    if len({c.id for c in candidates})!=len(candidates): raise ValueError('duplicate candidate ID')
    outcomes={c.id:assess(c,mode,killed) for c in candidates}
    selected=[c.id for c in candidates if c.author_selected and outcomes[c.id].eligible]
    if len(selected)>1: raise ValueError('one project handoff per decision')
    if selected: return 'STAGE0_HANDOFF',outcomes
    if any(d.eligible for d in outcomes.values()): return 'AUTHOR_SELECTION',outcomes
    if budget_exhausted: return 'HOLD_BUDGET',outcomes
    if exhausted_in_scope: return 'EXHAUSTED_IN_SCOPE',outcomes
    return 'RECYCLE_OR_CONTINUE',outcomes

def migrate_v5(record):
    """Loss-aware migration; old records must be re-audited, not silently upgraded."""
    fields=Candidate.__dataclass_fields__
    d={k:v for k,v in record.items() if k in fields}
    d['sources']=tuple(Source(**s) for s in record.get('sources',[]))
    d['legacy_blockers']=tuple(record.get('material_blockers',[]))
    # No legacy lane had query-level evidence. Old rejection is not certified by reason text alone.
    d['author_selected']=False
    return Candidate(**d)
