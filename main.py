import pygame
from maze_generator import generate_maze
from maze_solver import solve_bfs, solve_dfs
from maze_visualizer import draw_maze, draw_sidebar

COLS = 20
ROWS = 15
CELL_SIZE = 35
MAZE_W = COLS * CELL_SIZE   # 700
SIDEBAR_W = 200
WIN_W = MAZE_W + SIDEBAR_W  # 900
WIN_H = ROWS * CELL_SIZE    # 525


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIN_W, WIN_H))
    pygame.display.set_caption("Maze Solver — B: BFS  D: DFS  R: Regen")
    clock = pygame.time.Clock()

    grid = generate_maze(COLS, ROWS)
    path = []
    steps = 0
    algo_name = ""

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    path, steps = solve_bfs(grid, (0, 0), (COLS - 1, ROWS - 1))
                    algo_name = "BFS"
                elif event.key == pygame.K_d:
                    path, steps = solve_dfs(grid, (0, 0), (COLS - 1, ROWS - 1))
                    algo_name = "DFS"
                elif event.key == pygame.K_r:
                    grid = generate_maze(COLS, ROWS)
                    path, steps, algo_name = [], 0, ""

        screen.fill((245, 245, 245))
        draw_maze(screen, grid, path, CELL_SIZE)
        draw_sidebar(screen, algo_name, steps, len(path), MAZE_W, SIDEBAR_W, WIN_H)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
