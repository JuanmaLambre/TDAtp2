#!/usr/bin/python

#
# Este script ....
# 
#

import sys;
import ford_fulkerson as ff
from digraph import *


def main(projects_file):
    """ 
    """

    # Load Projects and Areas from File
    file = open(projects_file, "rw")
    NAreas = int(file.readline())
    MProjects = int(file.readline())

    # Load Projects and Areas into Graph
    graph = Digraph(2 + NAreas + MProjects)
    sourcePosition = 0
    sinkPosition = 2 + NAreas + MProjects - 1
    areasPosition = [area for area in range(MProjects + 1, MProjects + NAreas + 1)]
    projectsPosition = [area for area in range(1, MProjects + 1)]

    for area in areasPosition:
        # Add Cost for Area
        cost = int(file.readline())
        graph.add_edge(area, sinkPosition, cost)

    for project in projectsPosition:
        projectAreaEdges = file.readline().split()
        projectAreaEdges = [int(area) for area in projectAreaEdges]
        revenue = projectAreaEdges[0]

        # Add Revenue for project
        graph.add_edge(sourcePosition, project, revenue)

        # Link projects to areas
        for area in projectAreaEdges[1:]:
            graph.add_edge(project, areasPosition[area - 1], 10000000)    #INFINITO


    fordFulkerson = ff.FordFulkerson(graph)
    fordFulkerson.run()
    print "Max Flow: " + str(fordFulkerson.maxFlow)
    print "Selected Projects: " + str(fordFulkerson.minCutSourceVertex)     
     

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError('Se debe ingresar como unico argumento el nombre del archivo de proyectos')
    sys.exit(main(sys.argv[1]))