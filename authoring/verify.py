import json,unittest,math
import generate as g
class ContentChecks(unittest.TestCase):
 def test_catalog(self):
  p=json.loads((g.ROOT/'problems.json').read_text());self.assertEqual(len(p),1000);self.assertEqual([q['id'] for q in p],list(range(1,1001)));self.assertEqual(len({q['statement'] for q in p}),1000)
  for q in p:
   self.assertEqual(len(q['samples']),2);self.assertEqual(len(q['practice']),4)
   for t in q['samples']+q['practice']:self.assertLess(abs(int(t['output'])),2**63)
 def test_array_reference(self):
  self.assertEqual(g.run_lengths([1,2,2,3],lambda x,y:y>x),[2,2]);self.assertEqual(g.lis_ending([3,1,2,2,5]),[1,1,2,2,3]);self.assertEqual(g.F[0]['fn']([-3,0,4,4]),[3,4,0]);self.assertEqual(g.F[14]['fn']([1,-2,3]),[1,-1,2,-2,1,3])
 def test_number_reference(self):
  self.assertEqual(g.prime_factors(360),[2,2,2,3,3,5]);self.assertEqual(g.fibs(8),[1,1,2,3,5,8]);self.assertEqual(g.divisor_counts(6),[1,2,2,3,2,4]);self.assertEqual(g.totients(6),[1,1,2,2,4,2]);self.assertFalse(g.prime(-7));self.assertTrue(g.prime(9973))
 def test_string_reference(self):
  self.assertEqual(g.lcp('ababa','abaca'),3);self.assertEqual(g.unique_window('abac'),2);self.assertEqual(g.F[58]['fn']('aba'),[1,3,1,1]);self.assertEqual(g.F[60]['fn']('ababa'),[0,0,1,2,3])
 def test_matrix_reference(self):
  self.assertEqual(g.F[70]['fn']([[1,2],[3,4]]),[3,7]);self.assertEqual(g.F[74]['fn']([[1,2],[3,4]]),[10]);self.assertEqual(g.F[83]['fn']([[1,2],[3,4]]),[1,3,4,10])
 def test_graph_reference(self):
  graph=[{1,2},{0,2},{0,1,3},{2},set()];self.assertEqual(g.bfs(graph,0),[0,1,1,2,-1]);self.assertEqual(sorted(map(len,g.components(graph))),[1,4]);self.assertEqual(g.bridge_parts(graph),[1]);self.assertEqual(g.F[99]['fn'](graph),[1,0]);self.assertEqual(g.F[92]['fn'](graph),[1,1,1,0,0])
 def test_variant_reference(self):
  b=[-3,0,2,2,5];self.assertEqual([v[2](b) for v in g.V],[3,2,5,-3,6,2,3,42,4,8])
if __name__=='__main__':unittest.main(verbosity=2)
