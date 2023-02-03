from unittest import TestCase
from .notifications import Notifications
import mock


class TestNotifications(TestCase):
    @mock.patch("app.notifications.notifications.requests")
    @mock.patch("app.notifications.notifications.os.getenv")
    def test_sending_a_notification(self, m_env, m_requests):
        m_env.return_value = "http://notifications.service.endpoint"
        notification = "some_notification"
        Notifications.send(notification)
        m_requests.post.assert_called_once_with(
            url="http://notifications.service.endpoint",
            json={"body": "some_notification"},
        )
