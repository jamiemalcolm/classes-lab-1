class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0

    def add_player(self, player_name):
        self.players.append(player_name)

    def has_player(self, player_name):
        for player in self.players:
            if player == player_name:
                return True
        return False
