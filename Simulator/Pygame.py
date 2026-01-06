import sys
import pygame
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "clean"))
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "Class"))

from Class_Entity_Stats import Entity
# ----------------------
# CONFIG
# ----------------------
TILE_SIZE = 24
MAPS_DIR = os.path.join(os.path.dirname(__file__), "Rankeds_maps", "txt_maps")
MAPS_DIR = "BS_IA_Draft/Rankeds_maps/txt_maps"
SCREEN_BG = (20, 20, 20)

TILE_COLORS = {
    ".":(255, 255, 255),
    "M":(245, 174, 0),
    "X":(245, 174, 0),
    "Y":(245, 174, 0),
    "C":(245, 174, 0),
    "D":(255, 0, 235),
    "I":(196, 196, 196),
    "F":(2, 161, 0),
    "R":(2, 161, 0),
    "W":(0, 156, 147),
    "T":(245, 174, 0),
    "V":(0, 156, 147),
    "B":(196, 150, 0),
    "N":(245, 174, 0),
    "J":(0,0,0),
    "a":(245, 174, 0),
    "7":(255, 87, 87),
    "6":(125, 196, 254),
    "2":(255, 87, 87),
    "1":(125, 196, 254),
    "8":(0,0,0),#objectif dependant du mode HZ/H only car les autres modes l'objectif est un objet remassable
    "x":(102, 102, 102),
    "z":(166, 0, 0),
    "w":(0, 255, 16),
    "v":(102, 102, 102),



}
# ----------------------
# CHARGER LES MAPS
# ----------------------
def load_maps():
    maps = []

    for root, _, files in os.walk(MAPS_DIR):
        for file in files:
            if file.endswith(".txt"):
                path = os.path.join(root, file)
                with open(path, "r") as f:
                    grid = [list(line.rstrip()) for line in f.readlines()]
                maps.append((file, grid))

    return maps

maps = load_maps()
current_map_index = 0

# ----------------------
# INIT PYGAME
# ----------------------
pygame.init()

def create_screen(grid):
    h = len(grid)
    w = len(grid[0])
    return pygame.display.set_mode((w * TILE_SIZE, h * TILE_SIZE))

screen = create_screen(maps[0][1])
pygame.display.set_caption("Brawl Stars Map Viewer")

clock = pygame.time.Clock()

# ----------------------
# MAIN LOOP
# ----------------------
running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                current_map_index = (current_map_index + 1) % len(maps)
                screen = create_screen(maps[current_map_index][1])

            elif event.key == pygame.K_LEFT:
                current_map_index = (current_map_index - 1) % len(maps)
                screen = create_screen(maps[current_map_index][1])

    # ----------------------
    # RENDER
    # ----------------------
    screen.fill(SCREEN_BG)

    name, grid = maps[current_map_index]

    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            color = TILE_COLORS.get(char, (255, 0, 255))
            rect = pygame.Rect(
                x * TILE_SIZE,
                y * TILE_SIZE,
                TILE_SIZE,
                TILE_SIZE
            )
            pygame.draw.rect(screen, color, rect)

    pygame.display.set_caption(f"Map: {name}")
    pygame.display.flip()

pygame.quit()