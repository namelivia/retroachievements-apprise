from unittest import TestCase
from .retroachievements import RetroAchievementsWebApiClient
import mock


class TestRetroAchievements(TestCase):
    def setUp(self):
        self.client = RetroAchievementsWebApiClient("user", "api_key")

    @mock.patch("app.retroachievements.retroachievements.requests")
    def test_getting_game_info(self, m_requests):
        self.client.GetGameInfo("some_game_id")
        m_requests.get.assert_called_once_with(
            "https://retroachievements.org/API/API_GetGame.php?z=user&y=api_key&i=some_game_id"
        )
