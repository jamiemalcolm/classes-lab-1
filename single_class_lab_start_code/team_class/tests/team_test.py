import unittest
from src.team import Team


class TestTeam(unittest.TestCase):
    def setUp(self):
        players = ["Derice Bannock", "Sanka Coffie",
                   "Junior Bevil", "Yul Brenner"]
        self.team = Team("Cool Runnings", players, "Irv Blitzer")

   # @unittest.skip("delete this line to run the test")
    def test_team_has_name(self):
        self.assertEqual("Cool Runnings", self.team.name)

   # @unittest.skip("delete this line to run the test")
    def test_team_has_players(self):
        self.assertEqual(4, len(self.team.players))

   # @unittest.skip("delete this line to run the test")
    def test_team_has_coach(self):
        self.assertEqual("Irv Blitzer", self.team.coach)

   # @unittest.skip("delete this line to run the test")
    def test_coach_can_be_changed(self):
        self.team.coach = "John Candy"
        self.assertEqual("John Candy", self.team.coach)

   # @unittest.skip("delete this line to run the test")
    def test_can_add_new_player_to_team(self):
        new_player = "Jeff"
        self.team.add_player(new_player)
        self.assertEqual(5, len(self.team.players))

   # @unittest.skip("delete this line to run the test")
    def test_check_player_in_team__found(self):
        self.assertEqual(True, self.team.has_player("Junior Bevil"))

   # @unittest.skip("delete this line to run the test")
    def test_check_player_in_team__not_found(self):
        self.assertEqual(False, self.team.has_player("Usain Bolt"))

   # @unittest.skip("delete this line to run the test")
    def test_team_has_points(self):
        self.assertEqual(0, self.team.points)

   # @unittest.skip("delete this line to run the test")
    def test_play_game__win(self):
        self.team.play_game(True)
        self.assertEqual(3, self.team.points)

   # @unittest.skip("delete this line to run the test")
    def test_play_game__lose(self):
        self.team.play_game(False)
        self.assertEqual(0, self.team.points)

   # @unittest.skip("delete this line to run the test")
    def test_league_table__draw(self):
        result = "draw"
        self.team.league_table(result)
        self.assertEqual(1, self.team.results["draw"])

    def test_league_table__win(self):
        result = "win"
        self.team.league_table(result)
        self.assertEqual(1, self.team.results["win"])

    def test_league_table__loss(self):
        result = "loss"
        self.team.league_table(result)
        self.assertEqual(1, self.team.results["loss"])

    def test_add_multiple_players(self):
        player_name1 = "jimmy nutron"
        player_name2 = "issac newton"
        player_name3 = "dave chappel"
        self.team.add_multiple_players(
            player_name1, player_name2, player_name3)
        self.assertEqual(7, len(self.team.players))
