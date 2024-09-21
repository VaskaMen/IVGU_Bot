import json


from JsonDBBase import JsonDBBase
from User import User


class UserDB(JsonDBBase):

    def add_new_user(self, user: User):
        data = self.read_file()
        with open(self.file_name, "w", encoding="utf-8") as f:
            data[f"{user.id}"] = user.__dict__
            json.dump(data, f, ensure_ascii=False, indent=4)


    def get_all_users(self) -> list[User]:
        data = self.read_file()
        users: list[User] = list()
        for i in data:
            users.append(self.json_to_user(data[f'{i}']))
        return users


    def json_to_user(self, json: dict) -> User:
        return User(
            int(json['id']),
            bool(json['get_changes'])
        )