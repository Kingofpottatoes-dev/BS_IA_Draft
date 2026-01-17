import os
import  sys
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), "Class"))
from Class.Class_Game_State import GameState
from pygame import current_maps
def break_tile(x, y,):
    name, grid = current_maps
    if 0 <= y < len(grid) and 0 <= x < len(grid[y]):
        grid[y][x] = "."  # vide
def place_tile(x, y, tile_char):
    name, grid = current_maps
    if 0 <= y < len(grid) and 0 <= x < len(grid[y]):
        grid[y][x] = tile_char
def Start_Game():
    game_state = GameState(map=current_maps[1], mode="")
    return game_state