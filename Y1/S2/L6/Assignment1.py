import pygame
import random
import sys

# Constants
GRID_SIZE = 100
WINDOW_SIZE = 800
CELL_SIZE = WINDOW_SIZE // GRID_SIZE
FPS = 10

# Cell states
EMPTY = 0
TREE = 1
BURNING = 5
BURNED = 3

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (255, 0, 0)
DARK_GRAY = (50, 50, 50)


environment_phase = "growth"   # "growth", "drought", "collapse"
phase_timer = 0
PHASE_DURATION = 100  # frames (~30 seconds at 10 FPS)

def create_grid():
    grid = []
    for _ in range(GRID_SIZE):
        row = []
        for _ in range(GRID_SIZE):
            r = random.random()
            if r < 0.02:
                row.append(BURNING)
            elif r < 0.72:
                row.append(TREE)
            else:
                row.append(EMPTY)
        grid.append(row)
    return grid

def count_burning_neighbors(grid, x, y):
    burning = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx = x + dx
            ny = y + dy
            if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
                if grid[nx][ny] == BURNING:
                    burning += 1
    return burning

# Add this global variable near the top of your file (outside functions)
environment_bias = 0.0  # -1.0 (collapse) → 0 (neutral) → +1.0 (growth)

   

def update_grid(grid):
    global environment_phase, phase_timer

    total = GRID_SIZE * GRID_SIZE
    phase_timer += 1

    if phase_timer >= PHASE_DURATION:
        phase_timer = 0
        environment_phase = random.choice(["growth", "drought", "collapse"])

    # Count populations
    tree_count = sum(row.count(TREE) for row in grid)
    burning_count = sum(row.count(BURNING) for row in grid)
    burned_count = sum(row.count(BURNED) for row in grid)
    empty_count = sum(row.count(EMPTY) for row in grid)

    tree_ratio = tree_count / total
    burning_ratio = burning_count / total
    empty_ratio = empty_count / total

    # ---- Phase Bias (strong but not extreme) ----
    if environment_phase == "growth":
        ignition_probability = 0.25
        regeneration_probability = 0.10
        spontaneous_fire = 0.0005

    elif environment_phase == "drought":
        ignition_probability = 0.55
        regeneration_probability = 0.02
        spontaneous_fire = 0.004

    else:  # collapse
        ignition_probability = 0.35
        regeneration_probability = 0.01
        spontaneous_fire = 0.0

    # ---- Hard limits ----
    MAX_RATIO = 0.6
    MIN_RATIO = 0.10

    # Ceiling control
    if tree_ratio > MAX_RATIO:
        regeneration_probability *= 0.2
        ignition_probability *= 1.3

    if burning_ratio > MAX_RATIO:
        ignition_probability *= 0.2

    if empty_ratio > MAX_RATIO:
        regeneration_probability *= 2

    # Floor control
    if tree_ratio < MIN_RATIO:
        regeneration_probability *= 3

    if burning_ratio < MIN_RATIO:
        ignition_probability *= 2
        spontaneous_fire += 0.003

    if empty_ratio < MIN_RATIO:
        regeneration_probability *= 0.5

    ignition_probability = min(1.0, ignition_probability)
    regeneration_probability = min(0.25, regeneration_probability)

    new_grid = [[EMPTY for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            state = grid[x][y]

            if state == TREE:
                if count_burning_neighbors(grid, x, y) > 0:
                    if random.random() < ignition_probability:
                        new_grid[x][y] = BURNING
                    else:
                        new_grid[x][y] = TREE
                elif random.random() < spontaneous_fire:
                    new_grid[x][y] = BURNING
                else:
                    new_grid[x][y] = TREE

            elif state == BURNING:
                new_grid[x][y] = BURNED

            elif state == BURNED:
                if random.random() < regeneration_probability:
                    new_grid[x][y] = TREE
                else:
                    new_grid[x][y] = BURNED

            else:  # EMPTY
                if random.random() < regeneration_probability * 0.5:
                    new_grid[x][y] = TREE
                else:
                    new_grid[x][y] = EMPTY

    return new_grid


def draw_grid(screen, grid):
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            state = grid[x][y]
            if state == EMPTY:
                color = BLACK
            elif state == TREE:
                color = GREEN
            elif state == BURNING:
                color = RED
            else:
                color = DARK_GRAY
            rect = pygame.Rect(y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, color, rect)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Forest Fire Cellular Automata")
    clock = pygame.time.Clock()

    grid = create_grid()
    paused = False

    running = True
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
                elif event.key == pygame.K_r:
                    grid = create_grid()
                    paused = False

        if not paused:
            grid = update_grid(grid)

        draw_grid(screen, grid)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()