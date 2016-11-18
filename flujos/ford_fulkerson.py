#
# Algoritmo que toma como entrada un grafo de flujo. Esto es, un grafo con un
#   nodo inicial representando 's' y un nodo final representando 't'.
# Retorna el flujo maximo
#
# 
import pytest
from collections import namedtuple
from digraph import *

"""  

USAGE EXAMPLE:
    graph = generateGraphMagically()
    ff = FordFulkerson(graph)
    ff.run()
    maxFlow = ff.maxFlow
    minCut = ff.minCut()
    minCutSources = ff.minCutSources()

"""
class FordFulkerson:

    Tag = namedtuple('Tag', ['fromNode', 'type', 'residualCap'])

    def __init__(self, graph):
        self.graph = graph
        self.flows = {edge: 0 for edge in graph.iter_edges()}
        self.MAX_CAPACITIES = {edge: edge.weight for edge in graph.iter_edges()}
        self.tags = {}
        self.maxFlow = None
        self.minCutSourceVertex = None

    """ Add tag to toTagNode
        Returns toTagNode if was tagged, or None if it could not be tagged """
    def _tag(self, fromNode, toTagNode):
        positiveEdge = next((e for e in self.graph.adj_e(fromNode) if e.destination == toTagNode), None) # edge from --> toTag
        negativeEdge = next((e for e in self.graph.adj_e(toTagNode) if e.destination == fromNode), None) # edge toTag --> from
        fromNodeResidualCap = self.tags[fromNode].residualCap

        if positiveEdge and self.flows[positiveEdge] < self.MAX_CAPACITIES[positiveEdge]:
            edgeNetCapacity = self.MAX_CAPACITIES[positiveEdge] - self.flows[positiveEdge]
            residualCapacity = min(fromNodeResidualCap, edgeNetCapacity)
            self.tags[toTagNode] = FordFulkerson.Tag(fromNode, '+1', residualCapacity)
            return toTagNode
        elif negativeEdge and self.flows[negativeEdge] > 0:
            residualCapacity = min(fromNodeResidualCap, self.flows[negativeEdge])
            self.tags[toTagNode] = FordFulkerson.Tag(fromNode, '-1', residualCapacity)
            return toTagNode
        else:
            return None

    def _tagPathRecursive(self, node, sink):
        adjacentNodes = self.graph.adj_all(node)
        if sink in adjacentNodes:
            sinkWasReached = bool(self._tag(node, sink))
            if sinkWasReached:
                return True
        toTagNodes = [v for v in adjacentNodes if v not in self.tags]
        taggedNodes = filter(lambda x: x is not None, [self._tag(node, v) for v in toTagNodes])
        for neighbour in taggedNodes:
            sinkWasReached = self._tagPathRecursive(neighbour, sink)
            if sinkWasReached:
                return True
        
        # And if sink was not reached...
        return False

    """ Tags every node processed until sink is reached, filling self.tags
        Returns True if sink was reached """
    def _tagPath(self, source, sink):
        self.tags.clear()
        self.tags[0] = FordFulkerson.Tag(None, '+1', float('inf'))
        return self._tagPathRecursive(source, sink)

    """ Returns a sorted list of Edges representing the path from source to sink
        As 'yapa' it returns also the minimum capacity of those tags """
    def _getPathFromTags(self):
        path = []
        node = self.graph.last_node()
        minCapacity = float('inf')
        while node != 0:
            previousNode = self.tags[node].fromNode
            minCapacity = min(minCapacity, self.tags[node].residualCap)
            path.insert(0, next(edge for edge in self.graph.adj_e(previousNode) if edge.destination == node))
            node = previousNode
        return path, minCapacity
    
    """ Calculates min cut and stores it in self.minCut """
    def _calculateMinCut(self):
        # Construct Residual Graph from Max Flox Graph
        residualGraph = self._generateResidualGraph()

        # Do DFS from Source and mark any vertex as visited
        visited = [False for i in xrange(residualGraph.V())]
        residualGraph.markAsVisited(0, visited)

        # Get source vertices that were visited (incluided in MIN CUT)
        self.minCutSourceVertex = [vertex for vertex in residualGraph.adj(0) if visited[vertex]]

        """
        # Calculates MIN CUT
        # Any Edge that has one vertex visited and other not visited
        # is part of the MIN CUT.
        minCut = []
        for i in xrange(self.graph.V):
            for j in xrange(self.graph.V):
                if (visited[i] && !visited[j] && residualGraph.hasEdge(i, j))
                    AGREGAR EN MIN CUT
        """

    """ Generate Residual Graph from origin graph """
    def _generateResidualGraph(self):
        residualGraph = Digraph(self.graph.V())

        for edge, capacity in self.flows.items():
            vertexSource = edge.source
            vertexDestination = edge.destination
            weight = edge.weight
            residualGraph.add_edge(vertexSource, vertexDestination, weight - capacity)
            residualGraph.add_edge(vertexDestination, vertexSource, capacity)

        return residualGraph


    """ Calculates maximum flow of a graph and stores it in self.maxFlow.
        Calculates min cut and stores it in self.minCut """
    def run(self):
        sinkWasReached = self._tagPath(0, self.graph.last_node()) # opposite to max flow reached
        while sinkWasReached:
            path, minCapacity = self._getPathFromTags()
            for edge in path:
                self.flows[edge] += int(self.tags[edge.destination].type) * minCapacity
            sinkWasReached = self._tagPath(0, self.graph.last_node())

        self.maxFlow = 0
        for edge in self.graph.adj_e(0):
            self.maxFlow += self.flows[edge]

        self._calculateMinCut()
