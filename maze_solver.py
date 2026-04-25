from collections import deque


def get_neighbors(grid, x, y):
    cell = grid[y][x]
    rows = len(grid)
    cols = len(grid[0])
    neighbors = []
    if not cell["N"] and y > 0:
        neighbors.append((x, y - 1))
    if not cell["S"] and y < rows - 1:
        neighbors.append((x, y + 1))
    if not cell["E"] and x < cols - 1:
        neighbors.append((x + 1, y))
    if not cell["W"] and x > 0:
        neighbors.append((x - 1, y))
    return neighbors


def solve_bfs(grid, start, end):
    if start == end:
        return [start], 0
    queue = deque([(start, [start])])
    visited = {start}
    steps = 0
    while queue:
        (x, y), path = queue.popleft()
        steps += 1
        if (x, y) == end:
            return path, steps
        for nx, ny in get_neighbors(grid, x, y):
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))
    return [], steps


def solve_dfs(grid, start, end):
    if start == end:
        return [start], 0
    stack = [(start, [start])]
    visited = {start}
    steps = 0
    while stack:
        (x, y), path = stack.pop()
        steps += 1
        if (x, y) == end:
            return path, steps
        for nx, ny in get_neighbors(grid, x, y):
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                stack.append(((nx, ny), path + [(nx, ny)]))
    return [], steps
