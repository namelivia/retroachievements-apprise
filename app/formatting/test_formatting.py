from unittest import TestCase
from .formatting import Formatting
import json


class TestFormatting(TestCase):
    def test_formatting(self):
        data = {
            "GameID": "2",
            "LastPlayed": "15/03/2023",
            "Title": "Some Other Game",
            "ConsoleName": "Some Other Console",
        }
        formatted_message = Formatting.format(data)
        assert (
            formatted_message
            == "15/03/2023 - [Some Other Game (Some Other Console)](https://retroachievements.org/game/2)"
        )
