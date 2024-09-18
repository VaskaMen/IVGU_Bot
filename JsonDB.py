import json

from WorkDay import WorkDay


class JsonDB:

    def add_new_work_days(self, work_days: list[WorkDay]):
        data = self.read_work_days()
        with open('workDays.json', "w", encoding="utf-8") as f:
            for i in work_days:
                data[f"{i.date}"] = i.dict()
            json.dump(data, f, ensure_ascii=False, indent=4)

    def read_work_days(self) -> dict:
        try:
            data: dict
            with open('workDays.json', "r", encoding="utf-8") as json_file:
                data = json.loads(json_file.read())
            return data
        except Exception as ex:
            return {}