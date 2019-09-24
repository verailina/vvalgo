"""Implementation of Karger's random contraction algorithm."""
import random
from typing import Tuple, Dict, Sequence

from vvalgo.graph import Graph


def random_contraction_algorithm(
        graph: Graph) -> Tuple[Dict[int, Sequence[int]], int]:
    """Karger's random contraction algorithm for finding a minimal graph
    contraction.

    Args:
        graph (Graph): Graph to find a contraction for.

    Returns:
        Tuple[Dict[int, Sequence[int]], int]: Mapping from a graph half and
            the actual vertexes that lie inside and contraction size.
    """
    vertices = {v: {v} for v in graph.adj_list.keys()}
    super_vertices = {v: v for v in graph.adj_list.keys()}
    all_edges = {(v, w) if v < w else (w, v)
                 for v in graph.adj_list for w in graph.adj_list[v]}

    while len(vertices) > 2:
        edge = random.choice(list(all_edges))
        v, w = super_vertices[edge[0]], super_vertices[edge[1]]
        if v == w:
            continue
        for end in graph.adj_list[edge[1]]:
            if (edge[1], end) in all_edges:
                all_edges.remove((edge[1], end))
                if end not in vertices[v]:
                    all_edges.add((edge[0], end))
        vertices[v] |= vertices[w]
        for x in vertices[w]:
            super_vertices[x] = v
        del vertices[w]

    return vertices, count_cut_size(vertices, graph)


def count_cut_size(vertices: Dict[int, Sequence[int]], graph: Graph) -> int:
    """Compute contraction size.

    Args:
        vertices (Dict[int, Sequence[int]]): Mapping representing a vertex
            contraction.
        graph (Graph): Initial graph.

    Returns:
        int: Contraction size.
    """
    edges = set()
    vertices = list(vertices.values())
    for v in vertices[0]:
        for w in graph.adj_list[v]:
            if w in vertices[1]:
                edge = ((v, w) if v < w else (w, v))
                edges.add(edge)
    return len(edges)


def find_min_cut(graph: Graph,
                 runs: int = 100) -> Tuple[Dict[int, Sequence[int]], int]:
    """Find a minimal contraction by running Karger's algorithm several times.

    Args:
        graph (Graph): Graph to find contraction for
        runs (int, optional, default 100): Number of runs.
    """
    min_cut = None
    for i in range(runs):
        cur_cut = random_contraction_algorithm(graph)
        if min_cut is None or cur_cut[-1] < min_cut [-1]:
            min_cut = cur_cut
    return min_cut

