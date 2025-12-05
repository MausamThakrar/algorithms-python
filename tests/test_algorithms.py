from src.sorting import bubble_sort, merge_sort
from src.searching import linear_search, binary_search
from src.graphs import bfs, dfs


def test_sorting():
    arr = [5, 1, 4, 2, 8]
    expected = [1, 2, 4, 5, 8]

    assert bubble_sort(arr) == expected
    assert merge_sort(arr) == expected


def test_searching():
    arr = [1, 2, 4, 5, 8]
    assert linear_search(arr, 4) == 2
    assert linear_search(arr, 10) is None

    assert binary_search(arr, 4) == 2
    assert binary_search(arr, 10) is None


def test_graph_traversals():
    graph = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["D"],
        "D": [],
    }

    bfs_order = bfs(graph, "A")
    dfs_order = dfs(graph, "A")

    assert bfs_order[0] == "A"
    assert set(bfs_order) == {"A", "B", "C", "D"}
    assert dfs_order[0] == "A"
    assert set(dfs_order) == {"A", "B", "C", "D"}
