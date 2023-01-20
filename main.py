import os
from dotenv import load_dotenv
from app.retroachievements.retroachievements import RetroAchievementsWebApiClient
from app.formatting.formatting import Formatting
from app.notifications.notifications import Notifications


if __name__ == "__main__":
    load_dotenv()
    client = RetroAchievementsWebApiClient(
        os.environ["RETROACHIEVEMENTS_USERNAME"],
        os.environ["RETROACHIEVEMENTS_KEY"],
    )
    user = "namelivia"
    data = client.GetUserSummary(user, 5)
    message = ""
    message += f"Usuario: {user}\n"
    message += Formatting.format(data)
    Notifications.send(message)
