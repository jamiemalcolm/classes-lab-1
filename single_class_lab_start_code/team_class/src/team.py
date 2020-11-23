class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0
        self.results = {
            "win": 0,
            "loss": 0,
            "draw": 0
        }

    def add_player(self, player_name):
        self.players.append(player_name)

    def has_player(self, player_name):
        for player in self.players:
            if player == player_name:
                return True
        return False

    def league_table(self, result):
        if result == "win":
            self.results["win"] += 1
        elif result == "loss":
            self.results["loss"] += 1
        elif result == "draw":
            self.results["draw"] += 1

    def play_game(self, won):
        if won == True:
            self.points += 3
