import requests

import seecret
from Telegram.TelegramObjects.RichWorkdayTable import RichWorkdayTable


class RichMessageSender:
    rich_workday_table = RichWorkdayTable()

    @staticmethod
    def send_message(html: str, user_id):
        url = (
            f"https://api.telegram.org/"
            f"bot{seecret.token}/sendRichMessage"
        )
        response = requests.post(
            url,
            json={
                "chat_id": user_id,
                "rich_message": {
                    "html": html
                }
            },
            timeout=15
        )

    @staticmethod
    def edit_message(html: str, message_chat_id, message_id):
        url = (
            f"https://api.telegram.org/"
            f"bot{seecret.token}/editMessageText"
        )
        response = requests.post(
            url,
            json={
                "chat_id": message_chat_id,
                "message_id": message_id,
                "rich_message": {
                    "html": html
                }
            },
            timeout=15
        )