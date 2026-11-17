"""Budget/checkpoint bookkeeping for agent-operated BOTH runs. No search execution."""
from dataclasses import dataclass,field
from gate import LIMITS
TRACKS=('STANDARD','EPOCH')

def allocations():
    return {'STANDARD':dict(rounds=3,candidates=7,deep_screens=4,searches=36,inspections=18),'EPOCH':dict(rounds=3,candidates=5,deep_screens=2,searches=24,inspections=12)}
@dataclass
class DualTrack:
    caps:dict=field(default_factory=allocations)
    used:dict=field(default_factory=lambda:{t:dict.fromkeys(LIMITS,0) for t in TRACKS})
    operations:dict=field(default_factory=dict)
    def __post_init__(self):
        if set(self.caps)!=set(TRACKS) or set(self.used)!=set(TRACKS): raise ValueError('track')
        for t in TRACKS:
            if set(self.caps[t])!=set(LIMITS) or set(self.used[t])!=set(LIMITS): raise ValueError('keys')
            if any(type(self.caps[t][k]) is not int or type(self.used[t][k]) is not int or not 0<=self.used[t][k]<=self.caps[t][k] for k in LIMITS): raise ValueError('counts')
    def record(self,track,kind,operation_id,*,reuse=None):
        if track not in TRACKS or kind not in LIMITS or not operation_id.strip() or operation_id in self.operations: raise ValueError('operation')
        if reuse is not None:
            if kind not in {'searches','inspections'} or reuse not in self.operations or self.operations[reuse]['kind']!=kind or self.operations[reuse]['reuse'] is not None: raise ValueError('invalid reuse')
        else:
            if self.used[track][kind]>=self.caps[track][kind]: return False
            self.used[track][kind]+=1
        self.operations[operation_id]=dict(track=track,kind=kind,reuse=reuse);return True
    def transfer(self,from_track,to_track,kind,n):
        if from_track not in TRACKS or to_track not in TRACKS or from_track==to_track or kind not in LIMITS or type(n) is not int or n<0: raise ValueError('transfer')
        if self.caps[from_track][kind]-self.used[from_track][kind]<n: raise ValueError('spent quota')
        self.caps[from_track][kind]-=n;self.caps[to_track][kind]+=n
    def extend(self,track,kind,n,*,authorized=False):
        if not authorized: raise PermissionError('explicit extension required')
        if track not in TRACKS or kind not in LIMITS or type(n) is not int or n<0: raise ValueError('extension')
        self.caps[track][kind]+=n
    def checkpoint(self):
        return {'caps':{t:v.copy() for t,v in self.caps.items()},'used':{t:v.copy() for t,v in self.used.items()},'operations':{k:v.copy() for k,v in self.operations.items()}}
