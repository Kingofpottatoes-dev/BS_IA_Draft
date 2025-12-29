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