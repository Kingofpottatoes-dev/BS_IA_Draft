from Class_Map import game_map
class BrawlerPlayed:
    def __init__(
        self,
        coords,                # (x, y)
        deplacement,           # (vx, vy)
        HP,                    # int
        max_Hp,                # int
        Speed,                  # int
        ReloadSpeed,           # float (munitions / seconde)
        Muni,                  # float [0,1]
        Texture,
        State=None,            # [(state_name, duration_ticks), ...] lst_state=[hided,fasted,slowed,stunted,poisonCrow,poisonByron,burnedAmnber,rooted,shielded,feared,charmed,muted,upsidedown,marked_RT,marked_Belle,immune,invicible,unkillable,dmg_boosted]
        SP=None,               # (index_sp, buffed)
        Gadjet=None,           # (index_gadget, buffed)
        Gear1=None,            # index
        Gear2=None,            # index (Gear1 != Gear2)
        Hyper=None,            # (enabled, buffed)
        Ult_charge=0.0,        # float 0>1
        Ult_Uses=0,            # int
        Can_attack=True,        # bool
    ):
        # Position et mouvement
        self.coords = coords
        self.deplacement = deplacement
        self.x, self.y = coords
        self.vx, self.vy = deplacement

        # Vie
        self.HP = HP
        self.max_Hp = max_Hp
        self.is_dead = False

        # Stats dynamiques
        self.Speed = Speed
        self.ReloadSpeed = ReloadSpeed
        self.Muni = Muni  # 0 → vide, 1 → plein

        # États (poison, slow, stun, etc.)
        self.State = State if State is not None else []

        # Personnalisation / compétences
        self.SP = SP            # (index, buffed)
        self.Gadjet = Gadjet    # (index, buffed)
        self.Gear1 = Gear1
        self.Gear2 = Gear2
        self.Hyper = Hyper      # (enabled, buffed)

        # Ultime
        self.Ult_charge = Ult_charge
        self.Ult_Uses = Ult_Uses

        # Combat
        self.Can_attack = Can_attack
        # Apparence
        self.Texture = Texture

        def try_move(self):
            if 'stun' in [state[0] for state in self.State] or 'root' in [state[0] for state in self.State]:
                return self.coords
            else:
                self.coords = (self.coords[0] + self.deplacement[0], self.coords[1])
                if game_map.collides(self):
                    self.coords = (self.coords[0] - self.deplacement[0], self.coords[1])
                self.coords = (self.coords[0], self.coords[1] + self.deplacement[1])
                if game_map.collides(self):
                    self.coords = (self.coords[0], self.coords[1] - self.deplacement[1])