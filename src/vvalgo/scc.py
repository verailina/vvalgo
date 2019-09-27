"""This module contains implementation of Kosaraju's algorithm for computing
graph's strongly connected components.
"""
from typing import Optional, Dict, Set
from dataclasses import dataclass, field
from collections import Counter, deque

from vvalgo.graph import Graph


@dataclass()
class SCCState:
    time: int = 0
    current_leader: Optional[int] = None
    leaders: Dict[int, int] = field(default_factory=dict)
    marks: Dict[int, int] = field(default_factory=dict)
    explored: Set[int] = field(default_factory=set)


def dfs_loop(graph: Graph,
             state: SCCState,
             marks: Optional[Dict[int, int]] = None):
    mark_to_vertex = ({j: i for i, j in marks.items()}
                      if marks is not None else None)
    for i in range(graph.max_vertex, 0, -1):
        if i not in state.explored:
            state.current_leader = i
            dfs(i, graph, state, marks, mark_to_vertex)
    return marks


def dfs(vertex_mark: int,
        graph: Graph,
        state: SCCState,
        vertex_to_mark: Optional[Dict[int, int]] = None,
        mark_to_vertex: Optional[Dict[int, int]] = None):
    if vertex_to_mark is None:
        vertex_to_mark = {}
    if mark_to_vertex is None:
        mark_to_vertex = {}
    to_explore = deque([vertex_mark])

    while len(to_explore) > 0:
        vertex_mark = to_explore[0]
        actual_vertex = mark_to_vertex.get(vertex_mark, vertex_mark)

        if vertex_mark in state.explored:
            state.leaders[vertex_mark] = state.current_leader
            to_explore.popleft()
            state.time += 1
            state.marks[vertex_mark] = state.time

        else:
            for actual_end in graph.adj_list.get(actual_vertex, []):
                end_mark = vertex_to_mark.get(actual_end, actual_end)
                if end_mark not in state.explored:
                    to_explore.appendleft(end_mark)

            state.explored.add(vertex_mark)


def compute_scc(graph: Graph) -> Dict[int, int]:
    reversed_state = SCCState()
    dfs_loop(graph.reverse(), reversed_state)
    state = SCCState()
    dfs_loop(graph, state, marks=reversed_state.marks)
    return state.leaders


def compute_sizes(leaders: Dict[int, int]):
    counter = Counter(leaders.values())
    # from collections import defaultdict
    # results = defaultdict(set)
    # for v, s in leaders.items():
    #     results[s].add(v)
    # print(results)
    # for v, ss in sorted(results.items(), key=lambda x: len(x[1]), reverse=True):
    #     print(v, len(ss))
    return sorted(counter.values(), reverse=True)

