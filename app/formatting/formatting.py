import logging

logger = logging.getLogger(__name__)


class Formatting:
    @staticmethod
    def _get_game_link(game_id: str) -> str:
        return f"https://retroachievements.org/game/{game_id}"

    @staticmethod
    def format(game: dict) -> str:
        game_link = Formatting._get_game_link(game["GameID"])
        return f"{game['LastPlayed']} - [{game['Title']} ({game['ConsoleName']})]({game_link})"
