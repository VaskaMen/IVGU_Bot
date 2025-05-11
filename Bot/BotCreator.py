from telebot import types
from telebot.types import ReplyKeyboardMarkup


class BotCreator:

    @staticmethod
    def create_text_buttons(texts:list[str]) -> ReplyKeyboardMarkup:
        keyboard = types.ReplyKeyboardMarkup(row_width=2)
        buttons = [types.InlineKeyboardButton(str(text),callback_data = str(text)) for text in texts]
        keyboard.add(*buttons)
        return keyboard