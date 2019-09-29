"""Implementation of graph represented by an adjacency list."""
from typing import Dict, List, Tuple, Optional
from pathlib import Path

from collections import defaultdict


class Graph:
    def __init__(self,
                 adj_list: Dict[int, List[int]],
                 weights: Optional[Dict[Tuple[int, int], int]] = None):
        self.adj_list = adj_list
        self.weights = dict() if weights is None else weights
        self.max_vertex = -1
        for v, ends in self.adj_list.items():
            self.max_vertex = max([self.max_vertex, v] + ends)

    @staticmethod
    def from_file(input_path: Path, weighted: bool = False) -> "Graph":
        if weighted:
            return Graph._from_file_weighted(input_path)
        adj_list = defaultdict(list)
        with input_path.open("r") as input_file:
            for line in input_file.readlines():
                items = list(map(int, line.strip().split(" ")))
                adj_list[items[0]] += items[1:]
        return Graph(adj_list)

    @staticmethod
    def _from_file_weighted(input_path: Path) -> "Graph":
        adj_list = defaultdict(list)
        weights = dict()
        with input_path.open("r") as input_file:
            for line in input_file.readlines():
                items = line.strip().split(" ")
                source = int(line[0])
                edges = [tuple(map(int, edge.strip().split(",")))
                         for edge in items[1:]]
                adj_list[source] = [edge[0] for edge in edges]
                for end, weight in edges:
                    weights[(source, end)] = weight
        return Graph(adj_list, weights)

    def reverse(self) -> "Graph":
        adj_list = defaultdict(list)
        for vertex, ends in self.adj_list.items():
            for end in ends:
                adj_list[end].append(vertex)
        return Graph(adj_list)
