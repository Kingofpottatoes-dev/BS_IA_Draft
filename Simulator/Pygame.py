import sys
import pygame
import os
from Command_effect_affichage import *
sys.path.append(os.path.join(os.path.dirname(__file__), "clean"))
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "Class"))

from Class.Class_Entity_Stats import Entity_stats
from Tiles_Color import TILE_COLORS

# ----------------------
# CONFIG
# ----------------------
TILE_SIZE = 24
MAPS_DIR = os.path.join(os.path.dirname(__file__), "Rankeds_maps", "txt_maps")
SCREEN_BG = (20, 20, 20)
CONSOLE_HEIGHT = 30

# ----------------------
# CHARGER LES MAPS
# ----------------------
def load_maps():
    global MAPS_DIR
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
font = pygame.font.SysFont("consolas", 18)

def create_screen(grid):
    h = len(grid)
    w = len(grid[0])
    return pygame.display.set_mode((w * TILE_SIZE, h * TILE_SIZE + CONSOLE_HEIGHT))

screen = create_screen(maps[0][1])
pygame.display.set_caption("Brawl Stars Map Viewer")

clock = pygame.time.Clock()

# ----------------------
# CONSOLE
# ----------------------
console_active = False
console_input = ""
# ----------------------
# COMMAND LST
# ----------------------
def execute_command(cmd):
    parts = cmd.split()
    if not parts:
        return

    if parts[0] == "break" and len(parts) == 3:
        try:
            x = int(parts[1])
            y = int(parts[2])
            break_tile(x, y)
        except ValueError:
            print("Commande invalide")
    elif parts[0] == "place" and len(parts) == 4:
        try:
            x = int(parts[1])
            y = int(parts[2])
            tile_char = parts[3]
            place_tile(x, y, tile_char)
        except ValueError:
            print("Commande invalide")

# ----------------------
# MAIN LOOP
# ----------------------
running = True
while running:
    clock.tick(60)
# ----------------------
# LISTE EVENTS
# ----------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:

            # toggle console (F1)
            if event.key == pygame.K_F1:
                console_active = not console_active

            elif console_active:
                if event.key == pygame.K_RETURN:
                    execute_command(console_input)
                    console_input = ""
                elif event.key == pygame.K_BACKSPACE:
                    console_input = console_input[:-1]
                else:
                    console_input += event.unicode

            else:
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

    # ----------------------
    # CONSOLE RENDER
    # ----------------------
    if console_active:
        pygame.draw.rect(
            screen,
            (10, 10, 10),
            (0, screen.get_height() - CONSOLE_HEIGHT,
             screen.get_width(), CONSOLE_HEIGHT)
        )

        txt = font.render("> " + console_input, True, (0, 255, 0))
        screen.blit(txt, (5, screen.get_height() - CONSOLE_HEIGHT + 5))

    pygame.display.set_caption(f"Map: {name}")
    pygame.display.flip()

pygame.quit()