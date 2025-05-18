class TeacherPlace:
    def __init__(self, teacher:str="",place:str=""):
        self.teacher = teacher
        self.place = place

    def __eq__(self, other):
        if isinstance(other, TeacherPlace):
            return self.place == other.place and self.teacher == other.teacher
        return False

    def __str__(self):
        return f"{self.teacher},{self.place}"