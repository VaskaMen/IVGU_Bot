from datetime import datetime, timedelta

import telebot
from telebot import StateMemoryStorage, custom_filters
from telebot.states.sync import StateContext, StateMiddleware

from Bot.BotCreator import BotCreator
from Bot.DateFunctions import DateFunctions
from Bot.BotText import BotText
from Bot.RegisterState import RegisterState
from SQLDB.SQLDBB import SQLDBB

class IvguBot:

    def __init__(self, token: str, sqldb: SQLDBB):
        self.datefun = DateFunctions()
        self.sql = sqldb

        state_storage = StateMemoryStorage()
        self.bot = telebot.TeleBot(token, state_storage= state_storage, use_class_middlewares=True)
        self.bot.add_custom_filter(custom_filters.StateFilter(self.bot))
        self.bot.add_custom_filter(custom_filters.IsDigitFilter())
        self.bot.add_custom_filter(custom_filters.TextMatchFilter())
        self.bot.setup_middleware(StateMiddleware(self.bot))
        self.register_routes()

    def bot_run(self):
        self.bot.polling(none_stop=True, interval=0)


    def register_routes(self):
        @self.bot.message_handler(commands=['start'])
        def start(message, state: StateContext):
            if self.sql.user_select(message.chat.id) is not None:
                state.set(RegisterState.done)
            else:
                state.set(RegisterState.start_registration)
                startmsg = ["Начать"]
                self.bot.send_message(
                    message.chat.id,
                    text=BotText.start_text,
                    reply_markup=BotCreator.create_text_buttons(startmsg))

        @self.bot.message_handler(commands=['register'])
        def start_registration(message, state: StateContext):
            state.set(RegisterState.start_registration)
            registermsg = ["Начать регистрацию"]
            self.bot.send_message(
                message.chat.id,
                text=BotText.register_text,
                reply_markup=BotCreator.create_text_buttons(registermsg))

        @self.bot.message_handler(state = RegisterState.start_registration)
        def handle_start_registration(message, state: StateContext):
            state.set(RegisterState.institute)
            institutes = self.sql.get_list_institutes()
            self.bot.send_message(
                message.from_user.id,
                text=BotText.insert_institute,
                reply_markup=BotCreator.create_text_buttons(institutes,1)
            )

        @self.bot.message_handler(state = RegisterState.institute)
        def handle_institute(message, state: StateContext):
            state.add_data(institute = message.text)
            state.set(RegisterState.form)

            with state.data() as data:
                institute = data.get("institute")
            departments = self.sql.get_list_departments(institute)

            self.bot.send_message(
                message.from_user.id,
                text=BotText.insert_department,
                reply_markup=BotCreator.create_text_buttons(departments,1)
            )

        @self.bot.message_handler(state = RegisterState.form)
        def handle_form(message, state: StateContext):
            state.add_data(department = message.text)
            state.set(RegisterState.level)

            with state.data() as data:
                department = data.get("department")
            forms = self.sql.get_list_department_forms(department)

            self.bot.send_message(
                message.from_user.id,
                text=BotText.insert_form,
                reply_markup=BotCreator.create_text_buttons(forms)
            )

        @self.bot.message_handler(state = RegisterState.level)
        def handle_form(message, state: StateContext):
            state.add_data(form = message.text)
            state.set(RegisterState.course)

            with state.data() as data:
                department = data.get("department")
                form = data.get("form")
            levels = self.sql.get_list_department_form_levels(department,form)

            self.bot.send_message(
                message.from_user.id,
                text=BotText.insert_level,
                reply_markup=BotCreator.create_text_buttons(levels)
            )

        @self.bot.message_handler(state = RegisterState.course)
        def handle_course(message, state: StateContext):
            state.add_data(level = message.text)
            state.set(RegisterState.direction)

            with state.data() as data:
                department = data.get("department")
                form = data.get("form")
                level = data.get("level")
            courses = self.sql.get_list_courses(department, form, level)

            self.bot.send_message(
                message.from_user.id,
                text=BotText.insert_course,
                reply_markup=BotCreator.create_text_buttons(courses)
            )

        @self.bot.message_handler(state = RegisterState.direction)
        def handle_direction(message, state: StateContext):
            state.add_data(course = message.text)
            state.set(RegisterState.subdirection)

            with state.data() as data:
                department = data.get("department")
                form = data.get("form")
                level = data.get("level")
                course = data.get("course")
            directions = self.sql.get_list_directions(department, form, level, course)

            self.bot.send_message(
                message.from_user.id,
                text=BotText.insert_direction,
                reply_markup=BotCreator.create_text_buttons(directions,1)
            )
        @self.bot.message_handler(state = RegisterState.subdirection)
        def handle_direction(message, state: StateContext):
            state.add_data(direction = message.text)
            state.set(RegisterState.subgroup)

            with state.data() as data:
                department = data.get("department")
                form = data.get("form")
                level = data.get("level")
                course = data.get("course")
                direction = data.get("direction")
            subdirections = self.sql.get_list_subdirections(department, form, level, course, direction[:134])

            self.bot.send_message(
                message.from_user.id,
                text=BotText.insert_subdirection,
                reply_markup=BotCreator.create_text_buttons(subdirections)
            )

        @self.bot.message_handler(state = RegisterState.subgroup)
        def handle_subgroup(message, state: StateContext):
            state.add_data(subdirection = message.text)
            state.set(RegisterState.save)

            with state.data() as data:
                department = data.get("department")
                form = data.get("form")
                level = data.get("level")
                course = data.get("course")
                direction = data.get("direction")
                subdirection = data.get("subdirection")
            subgroups = self.sql.get_list_subgroups(department, form, level, course, direction[:134],subdirection[:134])
            self.bot.send_message(
                message.from_user.id,
                text=BotText.insert_subgroup,
                reply_markup=BotCreator.create_text_buttons(subgroups)
            )


        @self.bot.message_handler(state = RegisterState.save)
        def handle_group_id(message, state: StateContext):
            state.add_data(subgroup = message.text)
            state.set(RegisterState.done)
            with state.data() as data:
                institute = data.get("institute")
                department = data.get("department")
                form = data.get("form")
                level = data.get("level")
                course = data.get("course")
                direction = str(data.get("direction")).replace('…','')
                subdirection = str(data.get("subdirection")).replace('…','')
                subgroup = data.get("subgroup")
            group_id = self.sql.get_group_id(department, form, level, course, direction, subdirection,subgroup)

            self.sql.set_user(message.from_user.id,group_id)
            self.sql.commit()
            shchedules = ["Сегодня","Завтра"]

            self.bot.send_message(
                message.from_user.id,
                text=BotText.print_all(institute,department, form, level, course, direction,subdirection, subgroup)
            )

            self.bot.send_message(message.from_user.id,
                             BotText.text_after_registration,
                             reply_markup=BotCreator.create_text_buttons(shchedules))

        @self.bot.message_handler(commands=['schedule'])
        def handle_schedule(message):
            shchedules = ["Сегодня","Завтра"]
            self.bot.send_message(message.from_user.id,
                             BotText.schedule_option,
                             reply_markup=BotCreator.create_text_buttons(shchedules))

        @self.bot.message_handler(commands=['all_schedules'])
        def handle_all_schedules(message):
            group_id = self.sql.user_select(message.from_user.id)[0]
            date = str(datetime.now().date())
            dates = self.sql.get_actual_dates(group_id, date)
            reworked_dates = self.datefun.get_actual_dates(dates)

            self.bot.send_message(message.from_user.id,
                             BotText.schedule_option,
                             reply_markup=BotCreator.create_text_buttons(reworked_dates,1))

        @self.bot.message_handler(content_types=['text'])
        def text(message):
            group_id = self.sql.user_select(message.from_user.id)[0]
            print(f"{datetime.now()} Send message to {message.from_user.id}")
            if message.text == "Сегодня":
                date = str(datetime.now().date())
                workday = self.sql.get_sql_workday(group_id, date)
                self.bot.send_message(message.from_user.id, str(workday), parse_mode='Markdown')
            elif message.text == "Завтра":
                date = datetime.now().date() + timedelta(days=1)
                workday = str(self.sql.get_sql_workday(group_id, str(date)))
                self.bot.send_message(message.from_user.id, workday, parse_mode='Markdown')
            elif self.datefun.check_date_format(message.text):
                date = self.datefun.convert_str_to_date(message.text)
                workday = self.sql.get_sql_workday(group_id, str(date))
                self.bot.send_message(message.from_user.id, str(workday), parse_mode='Markdown')

