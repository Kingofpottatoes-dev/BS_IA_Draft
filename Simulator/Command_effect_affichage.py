def break_tile(x, y):
    name, grid = maps[current_map_index]
    if 0 <= y < len(grid) and 0 <= x < len(grid[y]):
        grid[y][x] = "."  # vide
def place_tile(x, y, tile_char):
    name, grid = maps[current_map_index]
    if 0 <= y < len(grid) and 0 <= x < len(grid[y]):
        grid[y][x] = tile_char