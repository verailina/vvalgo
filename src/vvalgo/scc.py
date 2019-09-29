"""This module contains implementation of Kosaraju's algorithm for computing
graph's strongly connected components.
"""
from typing import Optional, List
from collections import Counter, deque

from vvalgo.graph import Graph


class SCCState:

    def __init__(self, max_vertex: int):
        self.time = 0
        self.current_leader = None
        self.leaders = [None for _ in range(max_vertex + 1)]
        self.marks = [None for _ in range(max_vertex + 1)]
        self.explored = [False for _ in range(max_vertex + 1)]
        self.visited = [False for _ in range(max_vertex + 1)]


def dfs_loop(graph: Graph,
             state: SCCState,
             marks: List[Optional[int]]):
    mark_to_vertex = [None for _ in range(graph.max_vertex + 1)]
    for i, mark in enumerate(marks):
        if mark is not None:
            mark_to_vertex[mark] = i

    for i in range(graph.max_vertex, -1, -1):
        if not state.explored[i]:
            state.current_leader = i
            dfs(i, graph, state, marks, mark_to_vertex)


def dfs(vertex_mark: int,
        graph: Graph,
        state: SCCState,
        vertex_to_mark: List[int],
        mark_to_vertex: List[int]):
    to_explore = deque([vertex_mark])
    state.visited[vertex_mark] = True

    while len(to_explore) > 0:
        vertex_mark = to_explore[0]
        actual_vertex = mark_to_vertex[vertex_mark]

        if state.explored[vertex_mark]:
            state.leaders[actual_vertex] = state.current_leader
            to_explore.popleft()
            state.marks[actual_vertex] = state.time
            state.time += 1

        else:
            state.explored[vertex_mark] = True
            for actual_end in graph.adj_list.get(actual_vertex, []):
                end_mark = vertex_to_mark[actual_end]
                if not state.visited[end_mark]:
                    to_explore.appendleft(end_mark)
                    state.visited[end_mark] = True


def compute_scc(graph: Graph) -> List[Optional[int]]:
    reversed_state = SCCState(graph.max_vertex)
    dfs_loop(graph.reverse(), reversed_state, list(range(graph.max_vertex + 1)))
    state = SCCState(graph.max_vertex)
    dfs_loop(graph, state, marks=reversed_state.marks)
    return state.leaders


def compute_sizes(leaders: List):
    counter = Counter(leaders[1:])
    if None in counter:
        del counter[None]
    return sorted(counter.values(), reverse=True)

