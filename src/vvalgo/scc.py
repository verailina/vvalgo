"""This module contains implementation of Kosaraju's algorithm for computing
graph's strongly connected components.
"""
from typing import Optional, Sequence, Tuple, Dict
from dataclasses import dataclass
from collections import defaultdict
from pathlib import Path


@dataclass()
class Edge:
    start: int
    end: int

    def __post_init__(self):
        self.start -= 1
        self.end -= 1


class Graph:
    def __init__(self,
                 input_file: Optional[Path] = None,
                 edges: Optional[Sequence[Edge]] = None,
                 node_lists: Optional[Dict[int, Sequence[int]]] = None):
        if input_file is not None and edges is not None:
            raise ValueError("either `input_file` or `edges` can be specified.")

        if node_lists is not None:
            self.vertex_edges = node_lists

        else:
            if input_file is not None:
                edges = self.read_edges(input_file)

            self.vertex_edges = defaultdict(list)
            for edge in edges:
                self.vertex_edges[edge.start].append(edge.end)

        self.n = max(self.vertex_edges.keys())

    @staticmethod
    def read_edges(input_file: Path) -> Sequence[Edge]:
        with input_file.open("r") as input_file:
            lines = [map(int, line.split(" "))
                     for line in input_file.readlines()]
            return [Edge(*line) for line in lines]

    def relabel_vertex(self, new_labels: Sequence[int]):
        self.vertex_edges = {new_labels[v]: [new_labels[w] for w in values]
                             for v, values in self.vertex_edges.items()}

    def revert_edges(self) -> "Graph":
        new_edges = defaultdict(list)
        for v, ends in self.vertex_edges.items():
            for w in ends:
                new_edges[w].append(v)
        return Graph(node_lists=new_edges)


class DFS:
    def __init__(self, n: int):
        self.explored = [False for i in range(n)]
        self.leader = [None for i in range(n)]
        self.finish_time = [0 for i in range(n)]
        self.time = 0
        self.current_leader = None
        self.n = n - 1

    def dfs(self, graph: Graph, node: int):
        self.explored[node] = True
        self.leader[node] = self.current_leader
        print(f"Internal dfs exploring {node}")
        for end in graph.vertex_edges[node]:
            if not self.explored[end]:
                self.dfs(graph, end)
        self.time += 1
        self.finish_time[node] = self.time

    def dfs_loop(self, graph):
        node = self.n
        while node >= 0:
            if not self.explored[node]:
                self.current_leader = node
                self.dfs(graph, node)


def compute_scc(graph: Graph):
    graph_rev = graph.revert_edges()
    dfs = DFS(graph_rev.n)
    print(graph_rev.vertex_edges)
    # dfs.dfs_loop(graph_rev)
    # print(dfs.leader)
    # print(dfs.explored)
    # print(dfs.finish_time)
    # graph.relabel_vertex(dfs.finish_time)
    # dfs = DFS(graph.n)
    # dfs.dfs_loop(graph)
    # print(dfs.leader)





