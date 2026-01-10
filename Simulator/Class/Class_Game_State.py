class GameState:
    def __init__(self,map,Team1,Team2,mode,time,Score,Historique=None):
        self.map=map
        self.Team1=Team1
        self.Team2=Team2
        self.mode=mode
        self.time=time
        self.Score=Score
        self.is_paused = False
        self.Historique=Historique if Historique is not None else []
    def pause(self):
        self.is_paused = True
    def resume(self):
        self.is_paused = False
    def last_frame(self):
        if self.time!=0:
            return self.Historique[self.time-1]
    def update(self,new_state):
        self.Historique.append(new_state)
        self.time+=1