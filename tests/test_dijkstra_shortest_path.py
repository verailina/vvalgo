"""Tests for Dijkstra shortest path algorithm."""
from pathlib import Path

import pytest

from vvalgo.graph import WeightedGraph
from vvalgo.dijkstra_shortest_path import find_shortest_path_length


def test_find_shortest_path_length():
    # Empty graph
    g = WeightedGraph({})
    with pytest.raises(ValueError, match="invalid source 0"):
        find_shortest_path_length(g, 0)

    # Single vertex graph
    assert find_shortest_path_length(WeightedGraph({1: []})) == [0]

    # Two vertex graph
    assert find_shortest_path_length(WeightedGraph({1: [(2, 1)]})) == [0, 1]

    # Two vertex graph with back edge
    assert find_shortest_path_length(
        WeightedGraph({1: [(2, 1)], 2: [(1, 1)]})) == [0, 1]

    # Three vertex graph
    assert (find_shortest_path_length(
        WeightedGraph({1: [(2, 1), (3, 3)], 2: [(3, 1)]})) == [0, 1, 2])


def test_find_shortest_path_length_stanford():
    tst_dir = Path(
        "D:/repos/stanford-algs/testCases/course2/assignment2Dijkstra")
    control_vertices = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    for item in tst_dir.iterdir():
        if item.name.startswith("input"):
            print(item)
            output_path = Path(str(item).replace("input", "output"))
            graph = WeightedGraph.from_file(item, sep="\t")
            res_dist = find_shortest_path_length(graph)
            results = [res_dist[i - 1] for i in control_vertices]
            expected_results = output_path.read_text().strip()
            print(",".join(map(str, results)))
            print(expected_results)
            assert ",".join(map(str, results)) == expected_results


def test_merge_sort_count_big(resources_path):
    """Test the function `find_shortest_path_length` on a big example."""
    graph = WeightedGraph.from_file(
        resources_path / "dijkstra_sample.txt", sep="\t")
    control_vertices = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    res_dist = find_shortest_path_length(graph)
    results = [res_dist[i - 1] for i in control_vertices]
    print(",".join(map(str, results)))
