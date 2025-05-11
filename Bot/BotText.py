class BotText:
    start_text = """
           Тут ты можешь получить расписание с сайта https://uni.ivanovo.ac.ru/ для группы Прикладной информатики в цифровой экономике\n
           Расписание проверяется каждые 30 минут. При желание ты можешь подписаться на рассылку уведомлений при изменении в расписании. 
           Для этого вызови команду:\n/subscribe_updates\n
       """

    insert_institute = """Введите институт:"""

    insert_department = """Введите кафедру:"""

    insert_form = """Введите форму обучения:"""

    insert_level = """Введите степень обучения:"""

    insert_course = """Введите курс обучения:"""

    insert_direction = """Введите направление:"""

    insert_subdirection = """Введите поднаправление:"""

    insert_subgroup = """Ведите подгруппу:"""

    @staticmethod
    def print_all(institute: str,
                department: str,
                form: str,
                level: str,
                course: str,
                direction: str,
                subdirection: str,
                subgroup: str):
        return f"""Институт: {institute}\nКафедра: {department}\nФорма обучения: {form}\nСтепень обучения: {level}\nКурс: {course}\nНаправление: {direction}\nПоднаправление: {subdirection}\nПодгруппа: {subgroup}"""