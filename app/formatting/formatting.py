import logging

logger = logging.getLogger(__name__)


class Formatting:
    @staticmethod
    def format(data: dict) -> str:
        message = ""
        logger.info("Formatting data")
        message += f"Jugados recientemente: {data['RecentlyPlayedCount']}\n"
        for game in data["RecentlyPlayed"]:
            message += (
                f"{game['LastPlayed']} - {game['Title']} ({game['ConsoleName']})\n"
            )
        return message
