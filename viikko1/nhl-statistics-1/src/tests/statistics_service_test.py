import unittest
from statistics_service import StatisticsService
from player import Player
from enum import Enum

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_returns_none_if_player_doesnt_exist(self):
        result = self.stats.search("Selänne")
        self.assertEqual(result, None)

    def test_search_returns_correct_player_if_exists(self):
        result = self.stats.search("Kurri")
        self.assertEqual(result.name, "Kurri")

    def test_team_returns_a_list_of_players_of_given_team(self):
        players = self.stats.team("EDM")
        self.assertEqual(len(players), 3)

    def test_top_returns_players_with_most_points(self):
        topPlayers = self.stats.top(2)
        self.assertEqual(topPlayers[0].name, "Gretzky")
        self.assertEqual(topPlayers[1].name, "Lemieux")

    def test_top_returns_top_goals_with_goals_key(self):
        topGoals = self.stats.top(2, SortBy.GOALS)
        self.assertEqual(topGoals[0].name, "Lemieux")
        self.assertEqual(topGoals[1].name, "Yzerman")

    def test_top_returns_top_assists_with_assists_key(self):
        topAssists = self.stats.top(2, SortBy.ASSISTS)
        self.assertEqual(topAssists[0].name, "Gretzky")
        self.assertEqual(topAssists[1].name, "Yzerman")

    def test_top_returns_top_points_with_points_key(self):
        topPlayers = self.stats.top(2, SortBy.POINTS)
        self.assertEqual(topPlayers[0].name, "Gretzky")
        self.assertEqual(topPlayers[1].name, "Lemieux")
