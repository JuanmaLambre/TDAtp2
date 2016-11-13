import unittest
import sys
sys.path.append('..')
import ford_fulkerson as ff
from digraph import *


"""  GRAPH:                 """
"""                         """
"""         1               """
"""        * \              """
"""     3 /   \ 2           """
"""      /     *   2        """
"""     S       3---->T     """
"""      \     *            """
"""     5 \   / 4           """
"""        * /              """
"""         2               """
"""                         """
GRAPH = Digraph(5)
GRAPH.add_edge(0, 1, 3)
GRAPH.add_edge(1, 3, 2)

GRAPH.add_edge(0, 2, 5)
GRAPH.add_edge(2, 3, 4)
GRAPH.add_edge(3, 4, 2)
 

"""  GRAPH_2:               """
"""             4           """
"""         1------>2       """
"""        *|\      ^\      """
"""     10/ | \     | \10   """
"""      /  |  \    |  *    """
"""     S   |   \8  |6  T   """
"""      \  |2   \  |  *    """
"""     10\ |     \ | /10   """
"""        *v      *|/      """
"""         3------>4       """
"""             9           """
"""                         """
GRAPH_2 = Digraph(6)
GRAPH_2.add_edge(0, 1, 10)
GRAPH_2.add_edge(0, 3, 10)

GRAPH_2.add_edge(1, 2,  4)
GRAPH_2.add_edge(1, 3,  2)
GRAPH_2.add_edge(1, 4,  8)
GRAPH_2.add_edge(2, 5, 10)
GRAPH_2.add_edge(3, 4,  9)

GRAPH_2.add_edge(4, 2,  6)
GRAPH_2.add_edge(4, 5, 10)


"""  GRAPH_3:               """
"""            inf          """
"""         1------>2       """
"""        * \      ^\      """
"""     10/   \inf    \50   """
"""      /     \       *    """
"""     S       \       T   """
"""      \       \     *    """
"""     10\       \   /5    """
"""        *v      * /      """
"""         3------>4       """
"""            inf          """
"""                         """
GRAPH_3 = Digraph(6)
GRAPH_3.add_edge(0, 1, 10)
GRAPH_3.add_edge(0, 3, 10)

GRAPH_3.add_edge(1, 2, 100000)
GRAPH_3.add_edge(1, 4, 100000)
GRAPH_3.add_edge(3, 4, 100000)

GRAPH_3.add_edge(2, 5, 50)
GRAPH_3.add_edge(4, 5, 5)


"""  GRAPH_4:               """
"""            inf          """
"""         1------>4       """
"""        * \       \      """
"""     10/   \inf    \15   """
"""      / 10  \      5*    """
"""     S--*2------>5--* T  """
"""      \       \     *    """
"""     10\       \   /15   """
"""        *v      * /      """
"""         3------>6       """
"""            inf          """
"""                         """
GRAPH_4 = Digraph(8)

GRAPH_4.add_edge(0, 1, 10)
GRAPH_4.add_edge(0, 2, 10)
GRAPH_4.add_edge(0, 3, 10)

GRAPH_4.add_edge(1, 4, 100000)
GRAPH_4.add_edge(1, 6, 100000)
GRAPH_4.add_edge(2, 5, 100000)
GRAPH_4.add_edge(3, 6, 100000)

GRAPH_4.add_edge(4, 7, 15)
GRAPH_4.add_edge(5, 7, 5)
GRAPH_4.add_edge(6, 7, 15)


"""  GRAPH_5:               """
"""            inf          """
"""         1------>4       """
"""        * \       \      """
"""     10/   \inf    \5    """
"""      / 10  \     15*    """
"""     S--*2------>5--* T  """
"""      \       \     *    """
"""     10\       \   /8    """
"""        *v      * /      """
"""         3------>6       """
"""            inf          """
"""                         """
GRAPH_5 = Digraph(8)

GRAPH_5.add_edge(0, 1, 10)
GRAPH_5.add_edge(0, 2, 10)
GRAPH_5.add_edge(0, 3, 10)

GRAPH_5.add_edge(1, 4, 100000)
GRAPH_5.add_edge(1, 6, 100000)
GRAPH_5.add_edge(2, 5, 100000)
GRAPH_5.add_edge(3, 6, 100000)

GRAPH_5.add_edge(4, 7, 5)
GRAPH_5.add_edge(5, 7, 15)
GRAPH_5.add_edge(6, 7, 8)


class FordFulkersonTest(unittest.TestCase):

    def test_tagPath(self):
        fordFulkerson = ff.FordFulkerson(GRAPH)
        sinkReached = fordFulkerson._tagPath(0, 4)
        self.assertTrue(sinkReached)
        self.assertTrue(1 in fordFulkerson.tags)
        self.assertTrue(3 in fordFulkerson.tags)
        self.assertTrue(4 in fordFulkerson.tags)

    def test_findAnotherPathIfFull(self):
        saturatedEdge = GRAPH.edges[1][0]
        fordFulkerson = ff.FordFulkerson(GRAPH)
        fordFulkerson.flows[saturatedEdge] = saturatedEdge.weight
        fordFulkerson._tagPath(0, 4)
        self.assertTrue(2 in fordFulkerson.tags)
        self.assertTrue(3 in fordFulkerson.tags)
        self.assertTrue(4 in fordFulkerson.tags)

    def test_calculateMaxFlow_GRAPH_1(self):
        fordFulkerson = ff.FordFulkerson(GRAPH)
        fordFulkerson.run()
        self.assertEquals(fordFulkerson.maxFlow, 2)

    def test_calculateMaxFlow_GRAPH_2(self):
        fordFulkerson = ff.FordFulkerson(GRAPH_2)
        fordFulkerson.run()
        self.assertEquals(fordFulkerson.maxFlow, 19)

    def test_calculateMaxFlow_GRAPH_3(self):
        fordFulkerson = ff.FordFulkerson(GRAPH_3)
        fordFulkerson.run()
        self.assertEquals(fordFulkerson.maxFlow, 15)

    def test_calculateMaxFlow_GRAPH_4(self):
        fordFulkerson = ff.FordFulkerson(GRAPH_4)
        fordFulkerson.run()
        self.assertEquals(fordFulkerson.maxFlow, 25)

    def test_calculateMaxFlow_GRAPH_5(self):
        fordFulkerson = ff.FordFulkerson(GRAPH_5)
        fordFulkerson.run()
        self.assertEquals(fordFulkerson.maxFlow, 23)        

    def test_calculateSourcesIncluidedInMINCUT_GRAPH_3(self):
        fordFulkerson = ff.FordFulkerson(GRAPH_3)
        fordFulkerson.run()
        self.assertEquals(fordFulkerson.getMinCutSources(), [3])

    def test_calculateSourcesIncluidedInMINCUT_GRAPH_4(self):
        fordFulkerson = ff.FordFulkerson(GRAPH_4)
        fordFulkerson.run()
        self.assertEquals(fordFulkerson.getMinCutSources(), [2])

    def test_calculateSourcesIncluidedInMINCUT_GRAPH_5(self):
        fordFulkerson = ff.FordFulkerson(GRAPH_5)
        fordFulkerson.run()
        self.assertEquals(fordFulkerson.getMinCutSources(), [3, 1])      


if __name__ == '__main__':
    unittest.main()
