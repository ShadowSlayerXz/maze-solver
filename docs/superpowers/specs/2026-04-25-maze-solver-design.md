# Maze Solver — Design Spec
_Date: 2026-04-25_

## Overview

A pygame-based maze solver for a college algorithms project. Demonstrates BFS and DFS as solving algorithms on a randomly generated maze. The user can switch between algorithms interactively and see stats for each run.

## Algorithms

- **Maze Generation:** DFS recursive backtracking (already implemented in `maze_generator.py`)
- **Maze Solving — BFS:** Breadth-first search; guarantees the shortest path; explores level by level
- **Maze Solving — DFS:** Depth-first search; finds a path but not necessarily the shortest; explores deep first

## Window Layout

- Total window size: 900×600 px
- Left panel (~700px wide): maze grid
- Right panel (~200px wide): sidebar

### Maze Grid
- 20 columns × 15 rows of cells
- Each cell: ~35×35 px
- Start: top-left cell (0, 0)
- End: bottom-right cell (19, 14)
- Walls drawn as lines; solved path highlighted in a distinct color

### Sidebar
- Current algorithm name (BFS or DFS)
- Steps taken (total cells visited during search)
- Path length (cells in the final path)
- Key hints: B = BFS, D = DFS, R = regenerate

## File Responsibilities

| File | Responsibility |
|---|---|
| `maze_generator.py` | `generate_maze(cols, rows)` → grid (already done) |
| `maze_solver.py` | `solve_bfs(grid, start, end)` and `solve_dfs(grid, start, end)`, each returns `(path, steps_count)` |
| `maze_visualizer.py` | `draw_maze(surface, grid, path)` and `draw_sidebar(surface, algo_name, steps, path_len)` |
| `main.py` | pygame event loop; handles B/D/R keypresses; wires all modules together |

## Data Flow

1. `generate_maze(20, 15)` → `grid`
2. On keypress B or D: `solve_bfs(grid, (0,0), (19,14))` or `solve_dfs(grid, (0,0), (19,14))` → `(path, steps)`
3. `draw_maze(surface, grid, path)` + `draw_sidebar(surface, algo, steps, len(path))`

## Grid Data Structure

Each cell in `grid[row][col]` is a dict:
```python
{"N": bool, "S": bool, "E": bool, "W": bool, "visited": bool}
```
`True` = wall present, `False` = wall removed (passage open).

## Solver Return Contract

Both `solve_bfs` and `solve_dfs` return:
- `path`: list of `(x, y)` tuples from start to end (empty list if no solution)
- `steps_count`: int — total cells popped/visited during the search

## Controls

| Key | Action |
|---|---|
| `B` | Solve with BFS and display result |
| `D` | Solve with DFS and display result |
| `R` | Regenerate maze and clear current solution |
| Close window | Quit |

## Out of Scope

- Animation / step-by-step visualization
- Diagonal movement
- Custom maze size input
- Saving/loading mazes
