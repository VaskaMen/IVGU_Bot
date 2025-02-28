import json

from JsonDB.JsonDBBase import JsonDBBase


class DepartmentsDB(JsonDBBase):
    def add_departments(self, departments: dict[str, str]):
        data = self.read_file()
        with open(self.file_name, "w", encoding="utf-8") as file:
            for department in departments:
                data[f"{department}"] = departments[department]
            json.dump(data, file, ensure_ascii=False, indent=4)