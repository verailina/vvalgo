"""Implementation of Dijkstra shortest path algorithm."""
from typing import Sequence
import heapq

from vvalgo.graph import WeightedGraph

INFINITY = 10**6


def find_shortest_path_length(
        graph: WeightedGraph, source: int = 1) -> Sequence[int]:
    if source not in graph.adj_list:
        raise ValueError(f"invalid source {source}, is not in graph")
    shortest_path_dist = [INFINITY] * (graph.max_vertex + 1)
    shortest_path_dist[source] = 0
    heap = [(d, i) for i, d in enumerate(shortest_path_dist[1:], 1)]
    heapq.heapify(heap)
    while len(heap) > 0:
        dist, vertex = heapq.heappop(heap)
        for end, weight in graph.adj_list.get(vertex, []):
            if shortest_path_dist[end] > dist + weight:
                shortest_path_dist[end] = dist + weight
        heap = [(shortest_path_dist[i], i) for _, i in heap]
        heapq.heapify(heap)

    return shortest_path_dist[1:]
