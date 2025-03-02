class SQLCommands:

    @staticmethod
    def add_subject(name:str):
        return f"""insert or ignore into Subject(name) values('{name}')"""

    @staticmethod
    def find_subject_by_name(name:str):
        return f"""select * from Subject where name = '{name}'"""

    @staticmethod
    def find_subject_by_id(id:int):
        return f"""select * from Subject where id = {id}"""