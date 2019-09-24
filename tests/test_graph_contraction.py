import random

from vvalgo.graph import Graph
from vvalgo.graph_contraction import (random_contraction_algorithm,
                                      find_min_cut)


def test_random_contraction_algorithm():
    """Test a single run of random contraction algorithm."""
    random.seed(123)
    graph = Graph({1: {2, 4}, 2: {1, 3, 4}, 3: {2, 4}, 4: {1, 2, 3}})
    assert random_contraction_algorithm(graph) == ({1: {1, 2, 4}, 3: {3}}, 2)

    graph = Graph({1: {3, 2, 4}, 2: {1, 3, 4}, 3: {2, 3, 4}, 4: {1, 2, 3}})
    assert random_contraction_algorithm(graph) == ({1: {1, 4}, 3: {2, 3}}, 4)

    graph = Graph({1: {2}, 2: {1}})
    assert random_contraction_algorithm(graph) == ({1: {1}, 2: {2}}, 1)
    graph = Graph({1: {2, 3}, 2: {1}, 3: {1}})
    assert random_contraction_algorithm(graph) == ({2: {2}, 3: {1, 3}}, 1)


def test_find_min_cut():
    """Test minimal cut search."""
    random.seed(123)
    graph = Graph({1: {2, 4}, 2: {1, 3, 4}, 3: {2, 4}, 4: {1, 2, 3}})
    assert find_min_cut(graph)[1] == 2

    graph = Graph({1: {3, 2, 4}, 2: {1, 3, 4}, 3: {2, 1, 4}, 4: {1, 2, 3}})
    assert find_min_cut(graph)[-1] == 3

    graph = Graph({1: {2, 3}, 2: {1}, 3: {1}})
    assert find_min_cut(graph)[-1] == 1

    graph = Graph({1: {2, 4}, 2: {3, 1}, 3: {4, 2}, 4: {1, 3}})
    assert find_min_cut(graph)[-1] == 2


def test_find_min_cut_big(resources_path):
    """Test minimal cut search for a big graph."""
    graph = Graph.from_file((resources_path / "graph_contraction_sample.txt"))
    res = find_min_cut(graph, 1000)
    assert res[-1] == 17
