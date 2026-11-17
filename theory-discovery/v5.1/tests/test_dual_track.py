import unittest
from dual_track import DualTrack
class Tests(unittest.TestCase):
    def test_share_once(self):
        d=DualTrack();self.assertTrue(d.record('STANDARD','searches','q1'));self.assertTrue(d.record('EPOCH','searches','q2',reuse='q1'));self.assertEqual(sum(v['searches'] for v in d.used.values()),1)
    def test_no_ghost_reuse(self):
        with self.assertRaises(ValueError):DualTrack().record('EPOCH','searches','q2',reuse='q1')
    def test_duplicate(self):
        d=DualTrack();d.record('STANDARD','searches','q1')
        with self.assertRaises(ValueError):d.record('EPOCH','searches','q1')
    def test_transfer_resume(self):
        d=DualTrack();d.record('STANDARD','searches','q1');d.transfer('STANDARD','EPOCH','searches',3);b=DualTrack(**d.checkpoint());self.assertEqual(b.caps['EPOCH']['searches'],27);self.assertEqual(sum(v['searches'] for v in b.caps.values()),60);self.assertEqual(b.used['STANDARD']['searches'],1)
    def test_exhausted(self):
        d=DualTrack();d.transfer('EPOCH','STANDARD','searches',24);self.assertFalse(d.record('EPOCH','searches','q1'));self.assertTrue(d.record('STANDARD','searches','q1'))
    def test_extend_requires_authorization(self):
        d=DualTrack()
        with self.assertRaises(PermissionError):d.extend('EPOCH','searches',3)
        d.extend('EPOCH','searches',3,authorized=True);self.assertEqual(d.caps['EPOCH']['searches'],27)
