def circle_intersects_tile(cx, cy, radius, tx, ty):
    # coordonnées du carré (tile)
    left = tx
    right = tx + 1
    top = ty
    bottom = ty + 1

    # plus proche point du carré au centre du cercle
    nearest_x = max(left, min(cx, right))
    nearest_y = max(top, min(cy, bottom))

    # distance au centre du cercle
    dx = cx - nearest_x
    dy = cy - nearest_y

    return dx*dx + dy*dy < radius*radius

