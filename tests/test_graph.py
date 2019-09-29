from typing import Dict, Set
from pathlib import Path

import pytest

from vvalgo.graph import Graph


@pytest.fixture()
def graph_adj_list() -> Dict[int, Set[int]]:
    """Graph adjacency list."""
    return {0: {1, 2, 3}, 1: {2, 3}, 2: {0, 1}, 3: {1}}


@pytest.fixture()
def graph_file(tmpdir, graph_adj_list):
    graph_path = Path(tmpdir / "graph.txt")
    graph_path.write_text("\n".join([str(k) + " " + " ".join(map(str, values))
                                     for k, values in graph_adj_list.items()]))
    return graph_path


def test_graph__init__(graph_adj_list):
    """Test graph initialisation."""
    graph = Graph(adj_list=graph_adj_list)
    assert graph.adj_list == graph_adj_list
    assert graph.max_vertex == 3


def test_graph_reverse(graph_adj_list):
    """Test reverse of graph."""
    graph = Graph(adj_list=graph_adj_list)
    reversed_graph = graph.reverse()
    assert reversed_graph.adj_list == {0: {2}, 1: {0, 2, 3}, 2: {0, 1},
                                       3: {0, 1}}
    assert reversed_graph.max_vertex == 3


def test_graph_from_file(graph_file, graph_adj_list):
    """Test creation of graph from a file."""
    graph = Graph.from_file(graph_file)
    assert graph.adj_list == graph_adj_list
    assert graph.max_vertex == 3
