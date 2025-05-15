import seecret
from SQLDB.SQLDBB import SQLDBB
from TelegramBot import IvguBot

sql = SQLDBB()
ivgu_bot = IvguBot(seecret.token, sql)


while True:
    try:
        ivgu_bot.bot.polling(none_stop=True, interval=0)
    except Exception as ex:
        print(ex)