"""Implementation of graph represented by an adjacency list."""
from typing import Dict, Set
from pathlib import Path

from collections import defaultdict


class Graph:
    def __init__(self, adj_list: Dict[int, Set[int]]):
        self.adj_list = adj_list

        self.max_vertex = -1
        for v, ends in self.adj_list.items():
            self.max_vertex = max({v} | ends | {self.max_vertex})

    @staticmethod
    def from_file(input_path: Path) -> "Graph":
        adj_list = defaultdict(set)
        with input_path.open("r") as input_file:
            for line in input_file.readlines():
                items = list(map(int, line.strip().split(" ")))
                adj_list[items[0]] |= set(items[1:])
        return Graph(adj_list)

    def reverse(self) -> "Graph":
        adj_list = defaultdict(set)
        for vertex, ends in self.adj_list.items():
            for end in ends:
                adj_list[end].add(vertex)
        return Graph(adj_list)
