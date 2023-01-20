import os
from dotenv import load_dotenv
from app.retroachievements.retroachievements import RetroAchievementsWebApiClient
from app.notifications.notifications import Notifications


if __name__ == "__main__":
    load_dotenv()
    user = os.environ["RETROACHIEVEMENTS_USERNAME"]
    client = RetroAchievementsWebApiClient(
        user,
        os.environ["RETROACHIEVEMENTS_KEY"],
    )
    data = client.GetUserSummary(user, 5)
    Notifications.send(
        f"Usuario: {user}\n",
        [f"https://media.retroachievements.org/UserPic/{user}.png"],
    )
    Notifications.send(f"Jugados recientemente: {data['RecentlyPlayedCount']}\n")
    for game in data["RecentlyPlayed"]:
        message = f"{game['LastPlayed']} - {game['Title']} ({game['ConsoleName']})\n"
        Notifications.send(
            message, ["https://media.retroachievements.org" + game["ImageIcon"]]
        )
