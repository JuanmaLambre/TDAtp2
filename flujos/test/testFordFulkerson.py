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

    def test_calculateMaxFlow(self):
        fordFulkerson = ff.FordFulkerson(GRAPH)
        fordFulkerson.run()
        self.assertEquals(fordFulkerson.maxFlow, 2)

    def test_calculateMaxFlowAgain(self):
        fordFulkerson = ff.FordFulkerson(GRAPH_2)
        fordFulkerson.run()
        self.assertEquals(fordFulkerson.maxFlow, 19)

        


if __name__ == '__main__':
    unittest.main()
