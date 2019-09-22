from typing import Dict, Set
from pathlib import Path
from collections import defaultdict


class Graph:
    def __init__(self, adj_list: Dict[int, Set[int]]):
        self.adj_list = adj_list

    @staticmethod
    def from_file(input_path: Path) -> "Graph":
        adj_list = dict()
        with input_path.open("r") as input_file:
            for line in input_file.readlines():
                items = list(map(int, line.split(" ")))
                adj_list[items[0]] = set(items[1:])
        return Graph(adj_list)
