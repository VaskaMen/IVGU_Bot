import telebot
from telebot import StateMemoryStorage, custom_filters, types
from telebot.states.sync import StateContext, StateMiddleware

from Bot.BotCreator import BotCreator
from Bot.BotText import BotText
from Bot.RegisterState import RegisterState
from SQLDB.SQLDBB import SQLDBB

key = "7665754490:AAH7ugdV42S3Vxlm6sUZjnY2GwKh800xRRM"

week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
sql = SQLDBB()

state_storage = StateMemoryStorage()
bot = telebot.TeleBot(key,state_storage= state_storage, use_class_middlewares=True)
bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.add_custom_filter(custom_filters.IsDigitFilter())
bot.add_custom_filter(custom_filters.TextMatchFilter())
bot.setup_middleware(StateMiddleware(bot))

@bot.message_handler(commands=['start'])
def start(message: types.Message, state: StateContext):
    state.set(RegisterState.institute)
    institutes = sql.get_list_institutes()
    bot.send_message(
        message.chat.id,
        text=BotText.start_text
    )
    bot.send_message(
        message.from_user.id,
        text=BotText.insert_institute,
        reply_markup=BotCreator.create_text_buttons(institutes)
    )

@bot.message_handler(state = RegisterState.institute)
def handle_institute(message, state: StateContext):
    state.add_data(institute = message.text)
    state.set(RegisterState.form)

    with state.data() as data:
        institute = data.get("institute")
    departments = sql.get_list_departments(institute)

    bot.send_message(
        message.from_user.id,
        text=BotText.insert_department,
        reply_markup=BotCreator.create_text_buttons(departments)
    )

@bot.message_handler(state = RegisterState.form)
def handle_form(message, state: StateContext):
    state.add_data(department = message.text)
    state.set(RegisterState.level)

    with state.data() as data:
        department = data.get("department")
    forms = sql.get_list_department_forms(department)

    bot.send_message(
        message.from_user.id,
        text=BotText.insert_form,
        reply_markup=BotCreator.create_text_buttons(forms)
    )

@bot.message_handler(state = RegisterState.level)
def handle_form(message, state: StateContext):
    state.add_data(form = message.text)
    state.set(RegisterState.course)

    with state.data() as data:
        department = data.get("department")
        form = data.get("form")
    levels = sql.get_list_department_form_levels(department,form)

    bot.send_message(
        message.from_user.id,
        text=BotText.insert_level,
        reply_markup=BotCreator.create_text_buttons(levels)
    )

@bot.message_handler(state = RegisterState.course)
def handle_course(message, state: StateContext):
    state.add_data(level = message.text)
    state.set(RegisterState.direction)

    with state.data() as data:
        department = data.get("department")
        form = data.get("form")
        level = data.get("level")
    courses = sql.get_list_courses(department, form, level)

    bot.send_message(
        message.from_user.id,
        text=BotText.insert_course,
        reply_markup=BotCreator.create_text_buttons(courses)
    )

@bot.message_handler(state = RegisterState.direction)
def handle_direction(message, state: StateContext):
    state.add_data(course = message.text)
    state.set(RegisterState.subdirection)

    with state.data() as data:
        department = data.get("department")
        form = data.get("form")
        level = data.get("level")
        course = data.get("course")
    directions = sql.get_list_directions(department, form, level, course)

    bot.send_message(
        message.from_user.id,
        text=BotText.insert_direction,
        reply_markup=BotCreator.create_text_buttons(directions)
    )
@bot.message_handler(state = RegisterState.subdirection)
def handle_direction(message, state: StateContext):
    state.add_data(direction = message.text)
    state.set(RegisterState.subgroup)

    with state.data() as data:
        department = data.get("department")
        form = data.get("form")
        level = data.get("level")
        course = data.get("course")
        direction = data.get("direction")
    subdirections = sql.get_list_subdirections(department, form, level, course, direction[:134])

    bot.send_message(
        message.from_user.id,
        text=BotText.insert_subdirection,
        reply_markup=BotCreator.create_text_buttons(subdirections)
    )

@bot.message_handler(state = RegisterState.subgroup)
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
    subgroups = sql.get_list_subgroups(department, form, level, course, direction[:134],subdirection[:134])

    bot.send_message(
        message.from_user.id,
        text=BotText.insert_subgroup,
        reply_markup=BotCreator.create_text_buttons(subgroups)
    )

@bot.message_handler(state = RegisterState.save)
def handle_direction(message, state: StateContext):
    state.add_data(subgroup = message.text)
    state.set(RegisterState.done)

    with state.data() as data:
        institute = data.get("institute")
        department = data.get("department")
        form = data.get("form")
        level = data.get("level")
        course = data.get("course")
        direction = data.get("direction")
        subdirection = data.get("subdirection")
        subgroup = data.get("subgroup")

    group_id = sql.get_group_id(department, form, level, course, direction, subdirection,subgroup)
    sql.add_user(message.from_user.id,group_id)

    bot.send_message(
        message.from_user.id,
        text=BotText.print_all(institute,department, form, level, course, direction,subdirection, subgroup)
    )
    

bot.polling(none_stop=True, interval=0)