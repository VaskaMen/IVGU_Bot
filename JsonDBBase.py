import json
from typing import Any


class JsonDBBase:

    file_name = 'NewDB.json'

    def __init__(self, file_name: str):
        self.file_name = file_name

    def read_file(self) -> dict:
        try:
            data: dict
            with open(self.file_name, "r", encoding="utf-8") as json_file:
                data = json.loads(json_file.read())
            return data
        except Exception as ex:
            return {}