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
        State=None,            # [(state_name, duration_ticks), ...]
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
class BrawlerPlayed:
    def __init__(
            self,
            coords,#tuple x,y
            deplacement,#(vx,vy)
            HP,#int
            max_Hp,#int
            Speed,#int
            ReloadSpeed, #nmuni/s
            Muni,#float compris entre 0 et 1
            State,#[(State,duration_left),...]
            SP,#[indice du sp,Buffed or not]
            Gadjet,#[indice du gadjet,Buffed or not]
            Gear1,#[indice du gear]
            Gear2,#[indice du gear] Gear1!=Gear2
            Hyper,#[A l'hyper ou pas,Buffed or not]
            Ult_charge,#float 0>1
            Ult_Uses,#int
            Can_attack,#bool
            

            


    ):
        self.coords=coords
