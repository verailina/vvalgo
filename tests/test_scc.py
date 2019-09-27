import pytest

from vvalgo.scc import (Graph, dfs, dfs_loop, SCCState, compute_scc,
                        compute_sizes)


@pytest.fixture()
def small_graph(resources_path) -> Graph:
    """Small test graph."""
    test_input = resources_path / "scc_small.txt"
    graph = Graph.from_file(test_input)
    return graph


def test_dfs(small_graph):
    """Test dfs algorithm."""
    state = SCCState()
    state.time = 1
    state.current_leader = 0
    dfs(0, Graph({0: {1}}), state)
    assert state.time == 3
    assert state.current_leader == 0
    assert state.marks[1] == 2
    assert state.marks[0] == 3

    state = SCCState()
    dfs(9, small_graph.reverse(), state)
    assert state.time == 6
    assert state.marks == {2: 2, 3: 4, 5: 1, 6: 5, 8: 3, 9: 6}


def test_dfs_loop(small_graph):
    """Test the function `dfs_loop`"""
    reversed_state = SCCState()
    dfs_loop(small_graph.reverse(), reversed_state)
    assert reversed_state.time == 9
    assert reversed_state.marks == {5: 1, 2: 2, 8: 3, 3: 4, 6: 5, 9: 6, 1: 7,
                                    4: 8, 7: 9}
    print(reversed_state.leaders)


def test_compute_scc(resources_path):
    test_input = resources_path / "scc_small.txt"
    graph = Graph.from_file(test_input)
    scc = compute_scc(graph)
    assert scc == {7: 9, 1: 9, 4: 9, 9: 6, 3: 6, 6: 6, 8: 3, 5: 3, 2: 3}
    sizes = compute_sizes(scc)
    print(sizes)


def test_compute_scc_big_sample(resources_path):
    """Test scc on a big sample data."""
    test_input = resources_path / "scc_1.txt"
    graph = Graph.from_file(test_input)
    scc = compute_scc(graph)
    size = compute_sizes(scc)

    print(size)
#1: 104592,89,64,61,54
#2: 600516,319,191,178,177