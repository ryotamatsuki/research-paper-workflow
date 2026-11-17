import unittest
from dataclasses import replace
from gate import *

def fixture():
    # Synthetic declared metadata, not claims of actual literature searches.
    return Candidate('X','actors timing choices','conditional welfare ranking','same ranking under removal',question='when do two institutions differ?',economic_learning='which regime dominates by cost',predictive_contrast='ranking varies with cost',route_type='INSTITUTIONAL_COMPARISON',benchmark='one existing regime',delta='alternative feasible royalty',economic_motivation='institutional variation',minimum_test='compare two equilibria',parent_mapping='existing pricing model',residual_distinction='joint welfare ranking across distinct regimes',sources=(Source('S','MODEL_RESULT','section 2','benchmark model differs on feasible policy',True,True),),lanes={l:'SCOPED' for l in CORE},lane_evidence={l:(f'SYNTHETIC-{l}',) for l in CORE},objections=(Objection('O','related alternative regime','AUDITABLE','compare its payoff function','S §2',('S',)),),risk_reviewed=True)

def full():
    return replace(fixture(),lanes=dict.fromkeys(LANES,'COMPLETED'),lane_evidence={l:(f'SYNTHETIC-{l}',) for l in LANES},objections=(Objection('O','related model','REFUTED',evidence_ref='synthetic mapping'),),removal_test='benchmark recovery',red_team='SELF_RED_TEAM')

class GateTests(unittest.TestCase):
    def status(self,c,mode='STANDARD'):return assess(c,mode)
    def test_standard_promising(self): self.assertTrue(self.status(fixture()).eligible); self.assertEqual(self.status(fixture()).maturity,'PROMISING')
    def test_standard_unresolved_not_certified(self): self.assertEqual(self.status(fixture()).novelty,'UNRESOLVED')
    def test_known_model_result(self): self.assertTrue(self.status(replace(fixture(),route_type='NEW_RESULT')).eligible)
    def test_generalization(self): self.assertTrue(self.status(replace(fixture(),route_type='GENERALIZATION')).eligible)
    def test_correction(self): self.assertTrue(self.status(replace(fixture(),route_type='CORRECTION')).eligible)
    def test_application(self): self.assertTrue(self.status(replace(fixture(),route_type='APPLICATION')).eligible)
    def test_abstract_usable_triage_only(self): self.assertEqual(self.status(replace(fixture(),sources=(Source('S','ABSTRACT_ONLY','abstract','relevant comparison'),))).maturity,'PROMISING')
    def test_fatal_abstract_hold(self): self.assertFalse(self.status(replace(fixture(),objections=(Objection('O','same theorem likely','FATAL_UNRESOLVED'),))).eligible)
    def test_absorbed(self): self.assertEqual(self.status(replace(fixture(),absorbed_evidence='direct relabeling',absorption_source_ids=('S',))).novelty,'ABSORBED')
    def test_shallow_not_absorbed(self): self.assertEqual(self.status(replace(fixture(),sources=(Source('S','ABSTRACT_ONLY'),),absorbed_evidence='looks similar',absorption_source_ids=('S',))).disposition,'HOLD')
    def test_unclassified_decisive_source(self):self.assertFalse(self.status(replace(fixture(),sources=fixture().sources+(Source('S2','UNAVAILABLE'),))).eligible)
    def test_missing_query(self):self.assertFalse(self.status(replace(fixture(),lane_evidence={})).eligible)
    def test_missing_delta(self):self.assertFalse(self.status(replace(fixture(),delta='')).eligible)
    def test_missing_test(self):self.assertFalse(self.status(replace(fixture(),minimum_test='')).eligible)
    def test_missing_source(self):self.assertFalse(self.status(replace(fixture(),sources=())).eligible)
    def test_missing_objection_review(self):self.assertFalse(self.status(replace(fixture(),risk_reviewed=False)).eligible)
    def test_open_audit_unbounded(self):self.assertFalse(self.status(replace(fixture(),objections=(Objection('O','near result','AUDITABLE',evidence_ref='S'),))).eligible)
    def test_fake_refutation_missing_evidence(self):self.assertFalse(self.status(replace(full(),objections=(Objection('O','near result','REFUTED'),))).eligible)
    def test_full_prescreen(self):self.assertEqual(self.status(full()).maturity,'PRE_SCREEN_SURVIVED')
    def test_full_lane_missing_downgrade(self):self.assertEqual(self.status(replace(full(),lane_evidence={l:('q',) for l in LANES-{'L7'}})).maturity,'PROMISING')
    def test_epoch_no_reframe(self):self.assertFalse(self.status(full(),'EPOCH').eligible)
    def test_epoch_two_contexts_not_enough(self):self.assertFalse(self.status(replace(full(),epoch_reframe='a',epoch_settings=('A','B'),epoch_prediction='b'),'EPOCH').eligible)
    def test_epoch_full(self):self.assertTrue(self.status(replace(full(),epoch_reframe='a',epoch_settings=('A','B'),epoch_prediction='b',epoch_necessity='c'),'EPOCH').eligible)
    def test_epoch_promising_not_handoff(self):self.assertFalse(self.status(replace(fixture(),epoch_reframe='a',epoch_settings=('A','B'),epoch_prediction='b',epoch_necessity='c'),'EPOCH').eligible)
    def test_author_select(self):self.assertEqual(route([replace(fixture(),author_selected=True)])[0],'STAGE0_HANDOFF')
    def test_author_cannot_override_fatal(self):self.assertNotEqual(route([replace(fixture(),author_selected=True,risk_reviewed=False)])[0],'STAGE0_HANDOFF')
    def test_budget_with_candidate(self):self.assertEqual(route([fixture()],budget_exhausted=True)[0],'AUTHOR_SELECTION')
    def test_budget_no_candidate(self):self.assertEqual(route([],budget_exhausted=True)[0],'HOLD_BUDGET')
    def test_duplicate_killed(self):self.assertEqual(assess(replace(fixture(),id='Y'),killed=[fixture()]).disposition,'MERGED')
    def test_successor_distinct(self):self.assertTrue(assess(replace(fixture(),id='Y',target='new result',parent_ids=('X',),successor_delta='different predicted ranking'),killed=[fixture()]).eligible)
    def test_successor_no_delta(self):self.assertFalse(self.status(replace(fixture(),parent_ids=('X',))).eligible)
    def test_reopen_with_evidence(self):self.assertTrue(assess(fixture(),killed=[fixture()],new_evidence_ref='new source version').eligible)
    def test_unsupported_no_residual(self):self.assertEqual(self.status(replace(fixture(),no_residual_reason='known theory')).disposition,'HOLD')
    def test_supported_no_residual(self):self.assertEqual(self.status(replace(fixture(),no_residual_reason='tautology',no_residual_evidence='same quantity on both sides')).disposition,'REJECT')
    def test_legacy(self):self.assertFalse(self.status(replace(fixture(),legacy_blockers=('unclassified',))).eligible)
    def test_budget_resume(self):
        b=Budget();self.assertTrue(b.consume('searches',60)); self.assertFalse(b.consume('searches'));b2=Budget(**b.checkpoint());self.assertFalse(b2.consume('searches'))
        with self.assertRaises(PermissionError):b2.extend({'searches':70})
        b2.extend({'searches':70},authorized=True); self.assertTrue(b2.consume('searches'));self.assertEqual(b2.used['searches'],61)
    def test_duplicate_ids(self):
        with self.assertRaises(ValueError):route([fixture(),fixture()])
    def test_two_selection(self):
        with self.assertRaises(ValueError):route([replace(fixture(),author_selected=True),replace(fixture(),id='Y',author_selected=True)])
if __name__=='__main__':unittest.main()
