"""Implementation of graph represented by an adjacency list."""
from typing import Dict, List, Tuple, Optional, Union
from pathlib import Path
from operator import itemgetter

from collections import defaultdict


class Graph:
    def __init__(self,
                 adj_list: Dict[int, List[int]]):
        self.adj_list = adj_list
        self.max_vertex = -1
        for v, ends in self.adj_list.items():
            self.max_vertex = max([self.max_vertex, v] + ends)

    @staticmethod
    def from_file(input_path: Path, sep: str = " ") -> "Graph":
        adj_list = defaultdict(list)
        with input_path.open("r") as input_file:
            for line in input_file.readlines():
                items = list(map(int, line.strip().split(sep)))
                adj_list[items[0]] += items[1:]
        return Graph(adj_list)

    def reverse(self) -> "Graph":
        adj_list = defaultdict(list)
        for vertex, ends in self.adj_list.items():
            for end in ends:
                adj_list[end].append(vertex)
        return Graph(adj_list)


class WeightedGraph:
    def __init__(self, adj_list: Dict[int, List[Tuple[int, int]]]):
        self.adj_list = adj_list
        self.max_vertex = -1
        for v, ends in self.adj_list.items():
            self.max_vertex = max([self.max_vertex, v] +
                                  [x[1] for x in ends])

    @staticmethod
    def from_file(input_path: Path, sep: str = " ") -> "WeightedGraph":
        adj_list = defaultdict(list)
        with input_path.open("r") as input_file:
            for line in input_file.readlines():
                items = line.strip().split(sep)
                source = int(line[0])
                adj_list[source] = [tuple(map(int, edge.strip().split(",")))
                                    for edge in items[1:]]

        return WeightedGraph(adj_list)
