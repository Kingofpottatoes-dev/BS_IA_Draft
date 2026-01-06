from Class_tiles import Tile
class GameMap:

    def __init__(self, map_data, tiles):
        self.map_data = map_data      # tableau de chars
        self.tiles = tiles            # dict id -> Tile
        self.height = len(map_data)
        self.width = len(map_data[0])

 

    def tile_at(self, x, y):
        return self.tiles[self.map_data[y][x]]

    def is_walkable_circle(self, x, y, hitbox):
        # Tiles potentiellement touchées
        min_x = int(x - hitbox)
        max_x = int(x + hitbox)
        min_y = int(y - hitbox)
        max_y = int(y + hitbox)

        for ty in range(min_y, max_y + 1):
            for tx in range(min_x, max_x + 1):
                tile = self.tile_at(tx, ty)
                if tile and tile.blocks_movement:
                    if circle_intersects_tile(x, y, hitbox, tx, ty):
                        return False
        return True
    