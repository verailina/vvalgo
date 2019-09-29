from pathlib import Path
import pytest

from vvalgo.scc import Graph, compute_scc, compute_sizes


@pytest.fixture()
def small_graph(resources_path) -> Graph:
    """Small test graph."""
    test_input = resources_path / "scc_small.txt"
    graph = Graph.from_file(test_input)
    return graph


def test_compute_scc(resources_path):
    test_input = resources_path / "scc_small.txt"
    graph = Graph.from_file(test_input)
    scc = compute_scc(graph)
    sizes = compute_sizes(scc)
    assert sizes == [3, 3, 3]


def test_compute_scc_big_sample(resources_path):
    """Test scc on a big sample data."""
    test_input = resources_path / "scc_sample.txt"
    graph = Graph.from_file(test_input)
    scc = compute_scc(graph)
    size = compute_sizes(scc)
    assert size[:5] == [434821, 968, 459, 313, 211]


def test_standford():
    tst_dir = Path("D:/repos/stanford-algs/testCases/course2/assignment1SCC")
    total, fail = 0, 0
    for item in tst_dir.iterdir():
        if item.name.startswith("input"):
            output_path = Path(str(item).replace("input", "output"))
            graph = Graph.from_file(item)
            scc = compute_scc(graph)
            result_sizes = ",".join(map(str, (compute_sizes(scc, graph) +
                                              [0 for i in range(5)])[:5]))
            expected_sizes = output_path.read_text().strip()

            if result_sizes != expected_sizes:
                print(item.name)
                print("Mine: ", result_sizes)
                print("Expected: ", expected_sizes)
                print("------")
                fail += 1
            total += 1

    print(f"fail / total: {fail}/{total}")
