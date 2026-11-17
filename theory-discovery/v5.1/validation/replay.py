"""Published-paper-inspired synthetic scenarios; no independent novelty or discovery claim."""
from dataclasses import replace,asdict
from pathlib import Path
import sys,json
sys.path.insert(0,str(Path(__file__).resolve().parents[1]));sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tests'))
from test_gate import fixture,full
from gate import assess,Objection
rows=[]
# All search/objection metadata are synthetic premises of the unit fixture; publications only motivate contribution types.
cs=[('P1',replace(fixture(),id='P1',target='conditional ranking of six royalty regimes'), 'STANDARD',True),('P2',replace(fixture(),id='P2',target='optimal transition along R&D chain under different control rights',route_type='NEW_RESULT'),'STANDARD',True),('N1',replace(full(),id='N1',absorbed_evidence='exact known result assumed in fixture',absorption_source_ids=('S',)),'STANDARD',False),('B1',replace(fixture(),id='B1',objections=(Objection('O','decisive theorem might duplicate target','FATAL_UNRESOLVED'),)),'STANDARD',False),('B2',replace(fixture(),id='B2'),'EPOCH',False),('R1',replace(fixture(),id='R1',parent_ids=('N1',),successor_delta='distinct policy comparison with a different falsifier',target='distinct conditional ranking'),'STANDARD',True)]
for id,c,m,expect in cs:
 d=assess(c,m);assert d.eligible==expect; rows.append({'id':id,'mode':m,'expected_eligible':expect,'decision':asdict(d)})
print(json.dumps(rows,ensure_ascii=False,indent=2))
