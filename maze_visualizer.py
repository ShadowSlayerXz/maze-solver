import pygame

WALL_COLOR   = (20, 20, 20)
PATH_COLOR   = (255, 165, 0)
START_COLOR  = (50, 200, 50)
END_COLOR    = (200, 50, 50)
BG_COLOR     = (245, 245, 245)
SIDEBAR_BG   = (30, 30, 30)
TEXT_COLOR   = (255, 255, 255)
DIM_COLOR    = (160, 160, 160)
ACCENT_COLOR = (100, 210, 255)
TITLE_COLOR  = (255, 220, 50)

_fonts = {}


def _get_fonts():
    if not _fonts:
        _fonts["title"] = pygame.font.SysFont("monospace", 16, bold=True)
        _fonts["label"] = pygame.font.SysFont("monospace", 13)
        _fonts["value"] = pygame.font.SysFont("monospace", 20, bold=True)
    return _fonts


def draw_maze(surface, grid, path, cell_size, offset_x=0, offset_y=0):
    rows = len(grid)
    cols = len(grid[0])
    path_set = set(path) if path else set()

    for row in range(rows):
        for col in range(cols):
            px = offset_x + col * cell_size
            py = offset_y + row * cell_size
            cell = grid[row][col]

            if col == 0 and row == 0:
                color = START_COLOR
            elif col == cols - 1 and row == rows - 1:
                color = END_COLOR
            elif (col, row) in path_set:
                color = PATH_COLOR
            else:
                color = BG_COLOR

            pygame.draw.rect(surface, color, (px, py, cell_size, cell_size))

            if cell["N"]:
                pygame.draw.line(surface, WALL_COLOR, (px, py), (px + cell_size, py), 2)
            if cell["S"]:
                pygame.draw.line(surface, WALL_COLOR, (px, py + cell_size), (px + cell_size, py + cell_size), 2)
            if cell["W"]:
                pygame.draw.line(surface, WALL_COLOR, (px, py), (px, py + cell_size), 2)
            if cell["E"]:
                pygame.draw.line(surface, WALL_COLOR, (px + cell_size, py), (px + cell_size, py + cell_size), 2)


def draw_sidebar(surface, algo_name, steps, path_len, sidebar_x, sidebar_width, height):
    pygame.draw.rect(surface, SIDEBAR_BG, (sidebar_x, 0, sidebar_width, height))

    fonts = _get_fonts()
    font_title = fonts["title"]
    font_label = fonts["label"]
    font_value = fonts["value"]

    def blit(text, font, color, y):
        surf = font.render(text, True, color)
        surface.blit(surf, (sidebar_x + 12, y))
        return y + surf.get_height() + 6

    y = 18
    y = blit("MAZE SOLVER", font_title, TITLE_COLOR, y)
    y += 10

    y = blit("Algorithm", font_label, DIM_COLOR, y)
    y = blit(algo_name if algo_name else "---", font_value, ACCENT_COLOR, y)
    y += 10

    y = blit("Steps taken", font_label, DIM_COLOR, y)
    y = blit(str(steps), font_value, TEXT_COLOR, y)
    y += 10

    y = blit("Path length", font_label, DIM_COLOR, y)
    y = blit(str(path_len), font_value, TEXT_COLOR, y)
    y += 20

    y = blit("-- Controls --", font_label, DIM_COLOR, y)
    y += 4
    y = blit("B  BFS solve", font_label, TEXT_COLOR, y)
    y = blit("D  DFS solve", font_label, TEXT_COLOR, y)
    y = blit("R  Regenerate", font_label, TEXT_COLOR, y)
    blit("Esc  Quit", font_label, TEXT_COLOR, y)
