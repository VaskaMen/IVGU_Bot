from Telegram.Bot.DateFunctions import DateFunctions
from IVGU.ScheduleObject.WorkDay import WorkDay


class RichWorkdayTable:

    def __init__(self):
        self.table = ''

    datefun = DateFunctions()

    def build_schedule_buttons(self, selected_weekday_num: int):
        buttons = self.__build_rich_buttons(selected_weekday_num)
        self.table += f"""
        <tg-button-row align="center">
            {buttons}
        </tg-button-row>
        """

        return self

    @staticmethod
    def __build_rich_buttons(selected_weekday_num: int):

        days = [
            ("Пн", 0),
            ("Вт", 1),
            ("Ср", 2),
            ("Чт", 3),
            ("Пт", 4),
            ("Сб", 5),
            ("Вс", 6)
        ]

        buttons = ""

        for name, weekday in days:

            style = "primary" if weekday == selected_weekday_num else "link"

            buttons += (
                f'<tg-button '
                f'type="callback_data" '
                f'style="{style}" '
                f'data="weekday_{weekday}">'
                f'{name}'
                f'</tg-button>'
            )

        return buttons

    def build_schedule_table(self, workday: WorkDay):
        date = workday.date
        date = self.datefun.get_actual_dates([date])[0]
        self.table = f"""
                <h2>📅 {date}</h2>

                <table bordered>
                    <tr>
                        <th>Время</th>
                        <th>Занятие</th>
                    </tr>
                """

        for lesson in workday.lessons:
            time_start = lesson.time.split("-")[0]
            time_end = lesson.time.split("-")[1]
            time_start = time_start.replace(' ', '')
            time_end = time_end.replace(' ', '')
            self.table += f"""
            <tr>
                <td align="center">
                    <h3>
                        <b>{time_start}</b>
                        <br>
                        -
                        <br>
                        {time_end}
                    </h3>
                </td>

                <td align="center">
                    <b>{lesson.name}</b>
                    <br>
                    <br>
                    <b>{lesson.type_subject}</b>
                    <br>
            """

            for teacher_place in lesson.teacher_places:
                self.table += f"""
                    <i>{teacher_place.teacher}</i>
                    <br>
                    <br>
                    <b>{teacher_place.place}<b>
            """
            self.table += f"""
                </td>
            </tr>
            """

        self.table += """
                </table>
                """

        return self