import os
from dotenv import load_dotenv
from app.retroachievements.retroachievements import RetroAchievementsWebApiClient
from app.formatting.formatting import Formatting
from app.notifications.notifications import Notifications


class RetroAchievementsApprise:
    @staticmethod
    def run():
        load_dotenv()
        user = os.environ["RETROACHIEVEMENTS_USERNAME"]
        client = RetroAchievementsWebApiClient(
            user,
            os.environ["RETROACHIEVEMENTS_KEY"],
        )
        data = client.GetUserSummary(user, 5)
        for game in data["RecentlyPlayed"]:
            Notifications.send(Formatting.format(game))
