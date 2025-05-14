from telebot import types
from telebot.types import ReplyKeyboardMarkup


class BotCreator:

    @staticmethod
    def create_text_buttons(texts:list[str],row_width: int = 2) -> ReplyKeyboardMarkup:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=row_width)
        buttons = [types.InlineKeyboardButton(str(text),callback_data = str(text)) for text in texts]
        keyboard.add(*buttons)
        return keyboard