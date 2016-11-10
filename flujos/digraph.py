# -*- coding: utf-8 -*-
from collections import namedtuple


class Digraph(object):
  """Grafo dirigido y pesado con un número fijo de vértices.

  Los vértices son siempre números enteros no negativos. El primer vértice
  es 0.

  El grafo se crea vacío, se añaden las aristas con add_edge(). Una vez
  creadas, las aristas no se pueden eliminar, pero siempre se puede añadir
  nuevas aristas.   
  """
  def __init__(g, vertexNo):
    """Construye un grafo sin aristas de V vértices.
    """
    g.edges = {}
    g.vertices = vertexNo
    for v in xrange(vertexNo):
        g.edges[v] = []

  def V(g):
    """Número de vértices en el grafo.
    """
    return g.vertices

  def E(g):
    """Número de aristas en el grafo.
    """
    return sum([len(g.edges[e]) for e in g.edges])

  def last_node(g):
    return g.vertices - 1

  def adj_e(g, v):
    """Itera sobre los aristas incidentes _desde_ v.
    """
    return g.edges[v]

  def adj(g, v):
    """Itera sobre los vértices adyacentes a ‘v’.
    """
    return [e.destination for e in g.edges[v]]

  def adj_all(g, v):
    adjs = g.adj(v)
    for node in xrange(g.vertices):
      if v in g.adj(node) and node not in adjs:
        adjs.append(node)
    return adjs

  def add_edge(g, u, v, weight=0):
    """Añade una arista al grafo.
    """
    g.edges[u].append(Edge(u, v, weight))

  def __iter__(g):
    """Itera de 0 a V."""
    return iter(xrange(g.V()))

  def iter_edges(g):
    """Itera sobre todas las aristas del grafo.

    Las aristas devueltas tienen los siguientes atributos de solo lectura:

        • e.src
        • e.dst
        • e.weight
    """
    return iter([x for e in g.edges for x in g.edges[e]])


Edge = namedtuple('Edge', ['source', 'destination', 'weight'])
