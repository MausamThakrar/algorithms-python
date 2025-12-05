from collections import deque
from typing import Dict, List, Set


Graph = Dict[str, List[str]]


def bfs(graph: Graph, start: str) -> List[str]:
    """Breadth-first search traversal from a starting node."""
    visited: Set[str] = set()
    order: List[str] = []
    queue: deque[str] = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            order.append(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)

    return order


def dfs(graph: Graph, start: str) -> List[str]:
    """Depth-first search traversal from a starting node."""
    visited: Set[str] = set()
    order: List[str] = []

    def _dfs(node: str):
        if node in visited:
            return
        visited.add(node)
        order.append(node)
        for neighbor in graph.get(node, []):
            _dfs(neighbor)

    _dfs(start)
    return order
