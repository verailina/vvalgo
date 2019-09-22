from vvalgo.scc import Graph, Edge, compute_scc


def test_graph__init__(resources_path):
    """Test graph initialisation."""
    test_input = resources_path / "scc_small.txt"
    graph = Graph(test_input)
    assert graph.vertex_edges == {0: [3], 1: [7], 2: [5], 3: [6], 4: [1],
                                  5: [8], 6: [0], 7: [4, 5], 8: [6, 2]}
    graph = Graph(edges=(Edge(1, 2), Edge(1, 3), Edge(2, 3), Edge(3, 2)))
    assert graph.vertex_edges == {0: [1, 2], 1: [2], 2: [1]}


def test_graph_relabel_vertex():
    """Test the method `relabel_vertex` of the class `Graph`."""
    graph = Graph(edges=(Edge(1, 2), Edge(1, 3), Edge(2, 3), Edge(3, 2)))
    new_labels = [2, 1, 0]
    graph.relabel_vertex(new_labels)
    assert graph.vertex_edges == {2: [1, 0], 1: [0], 0: [1]}


def test_graph_revert_edges():
    """Test the method `revert_edges` of the class `Graph`."""
    graph = Graph(edges=(Edge(1, 2), Edge(1, 3), Edge(2, 3), Edge(3, 2)))



def test_graph_read_edges(resources_path):
    """Test the method `read_edges` of class `Graph`."""
    test_input = resources_path / "scc_small.txt"
    edges = Graph.read_edges(test_input)
    assert edges == [Edge(1, 4), Edge(2, 8), Edge(3, 6), Edge(4, 7), Edge(5, 2),
                     Edge(6, 9), Edge(7, 1), Edge(8, 5), Edge(8, 6), Edge(9, 7),
                     Edge(9, 3)]


def test_compute_scc(resources_path):
    test_input = resources_path / "scc_small.txt"
    graph = Graph(test_input)
    print(compute_scc(graph))
