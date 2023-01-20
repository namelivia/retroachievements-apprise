import os
import requests
import logging

logger = logging.getLogger(__name__)


class Notifications:
    @staticmethod
    def send(message: str, attachments=[]):
        logger.info("Sending notifications")
        data = {"body": message}
        for attachment in attachments:
            data["attach"] = attachment
        response = requests.post(
            url=os.getenv("NOTIFICATIONS_SERVICE_ENDPOINT"), json=data
        )
        logger.info(response.text)
