import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from maze_solver import solve_bfs, solve_dfs

def make_cell(n=True, s=True, e=True, w=True):
    return {"N": n, "S": s, "E": e, "W": w, "visited": True}

def test_bfs_finds_shortest_path():
    # 2x2: (0,0) -E-> (1,0) -S-> (1,1)
    grid = [
        [make_cell(e=False),        make_cell(w=False, s=False)],
        [make_cell(),               make_cell(n=False)],
    ]
    path, steps = solve_bfs(grid, (0, 0), (1, 1))
    assert path == [(0, 0), (1, 0), (1, 1)]
    assert steps > 0

def test_bfs_straight_line():
    # 3x1: (0,0) -> (1,0) -> (2,0)
    grid = [
        [make_cell(e=False), make_cell(w=False, e=False), make_cell(w=False)],
    ]
    path, steps = solve_bfs(grid, (0, 0), (2, 0))
    assert path == [(0, 0), (1, 0), (2, 0)]

def test_bfs_no_path_returns_empty():
    # 2x1: wall between cells stays up
    grid = [
        [make_cell(), make_cell()],
    ]
    path, steps = solve_bfs(grid, (0, 0), (1, 0))
    assert path == []

def test_dfs_finds_a_path():
    grid = [
        [make_cell(e=False),        make_cell(w=False, s=False)],
        [make_cell(),               make_cell(n=False)],
    ]
    path, steps = solve_dfs(grid, (0, 0), (1, 1))
    assert path[0] == (0, 0)
    assert path[-1] == (1, 1)
    assert steps > 0

def test_dfs_no_path_returns_empty():
    grid = [
        [make_cell(), make_cell()],
    ]
    path, steps = solve_dfs(grid, (0, 0), (1, 0))
    assert path == []

def test_start_equals_end():
    grid = [
        [make_cell(), make_cell()],
    ]
    path, steps = solve_bfs(grid, (0, 0), (0, 0))
    assert path == [(0, 0)]
