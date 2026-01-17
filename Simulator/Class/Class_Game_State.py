from Brawler_Loader import Brawler
class GameState:
    def __init__(self,
                 map,
                 mode,
                 Historique=None,
                 time=0,
                 Score1=0,
                 score2=0,
                 Team1=[],
                 Team2=[],
                 draft_order = [1,2,2,1,1,2],
                current_pick = 0,
                draft_finished = False
                    ):
        self.map=map
        self.mode=mode
        self.time=time
        self.Score1=Score1
        self.Score2=score2
        self.is_paused = True
        self.Historique=Historique if Historique is not None else []
        self.Team1=Team1
        self.Team2=Team2
        self.draft_order = draft_order
        self.current_pick = current_pick
        self.draft_finished = draft_finished

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
    def pick_brawler(self, brawler_name):
        # Verification
        if self.draft_finished:
            print("Draft déjà terminée !")
            return
        all_picked = self.team1 + self.team2
        if brawler_name in all_picked:
            print(f"{brawler_name} a déjà été choisi ! Choisissez un autre brawler.")
            return
        # Enregistrement du pick
        team_num = self.draft_order[self.current_pick]
        if team_num == 1:
            self.team1.append(brawler_name)
        else:
            self.team2.append(brawler_name)
        # Passage au pick suivant
        self.current_pick += 1
        if self.current_pick >= len(self.draft_order):
            self.draft_finished = True
            self.start_game()
        else:
            next_team = self.draft_order[self.current_pick][0]
            print(f"Next pick: Team {next_team}")

    def start_game(self):
        self.game_started = True
        print("Draft terminé, game lancé ! Timer activé.")