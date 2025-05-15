class BotText:
    start_text = """
           Тут ты можешь получить расписание с сайта https://uni.ivanovo.ac.ru/ для группы Прикладной информатики в цифровой экономике\n
           Расписание проверяется каждые 30 минут. При желании ты можешь подписаться на рассылку уведомлений при изменении в расписании. 
           Для этого вызови команду:\n/subscribe_updates\n
       """

    text_after_registration = """Вы можете пройти повторную регистрацию. Для этого вызови команду /register"""

    register_text = """Для правильной работы бота нам нужно, чтобы вы заполнили данные о том, где вы обучаетесь."""

    insert_institute = """Введите институт:"""

    insert_department = """Введите кафедру:"""

    insert_form = """Введите форму обучения:"""

    insert_level = """Введите степень обучения:"""

    insert_course = """Введите курс обучения:"""

    insert_direction = """Введите направление:"""

    insert_subdirection = """Введите поднаправление:"""

    insert_subgroup = """Ведите подгруппу:"""

    schedule_option = """На какой день вы хотите увидеть расписание?"""

    start_student = '''Хорошо! Нажмите "Начать", чтобы начать регистрацию.'''

    start_choice = """Вы учитель?"""

    teacher_insert ='''Введите ваше ФИО наподобие: "Фамилия Имя.Отчество"'''

    teacher_error = """Не найдено. Попробуйте ещё раз!"""

    teacher_correct = '''Всё хорошо! Теперь вы можете найти своё расписание, нажав на кнопки "Сегодня"|"Завтра" или посмотреть расписание по дням, использовав функцию /all_schedules'''

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