def Entity_intersects_tile(cx, cy, r, tx, ty):
    """
    Vérifie si un cercle (cx, cy, r) touche le carré [tx, tx+1] x [ty, ty+1]
    """
    closest_x = max(tx, min(cx, tx + 1))
    closest_y = max(ty, min(cy, ty + 1))

    dx = cx - closest_x
    dy = cy - closest_y

    return dx*dx + dy*dy < r*r