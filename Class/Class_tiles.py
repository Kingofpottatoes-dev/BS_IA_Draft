class Tile:
    def __init__(
        self,
        tile_code,
        blocks_movement=False,
        blocks_projectiles=False,
        is_destructible=False,
        health=None,
        damage=0,
        speed_change=1.0,
        is_bouncer=False,
        hides_hero=False,
        respawn_seconds=None,
        restore_after_dynamic_overlap=False,
        collision_margin=0.0,
        lifetime=None,
        texture=None
    ):
        # Identité
        self.tile_code = tile_code

        # Collisions
        self.blocks_movement = blocks_movement
        self.blocks_projectiles = blocks_projectiles
        self.collision_margin = collision_margin

        # Gameplay
        self.is_destructible = is_destructible
        self.health = health
        self.damage = damage
        self.speed_change = speed_change
        self.is_bouncer = is_bouncer
        self.hides_hero = hides_hero

        # Dynamique
        self.respawn_seconds = respawn_seconds
        self.restore_after_dynamic_overlap = restore_after_dynamic_overlap
        self.lifetime = lifetime  # en ms ou sec selon ton choix

        # Rendu
        self.texture = texture# chemin ou surface pygame

        # État interne
        self.destroyed = False

    # ----------------------
    # Méthodes gameplay
    # ----------------------


    # ----------------------
    # Debug / affichage
    # ----------------------

    def __repr__(self):
        return (
            f"<Tile {self.tile_code} "
            f"walkable={self.is_walkable()} "
            f"lifetime={self.lifetime}>"
        )