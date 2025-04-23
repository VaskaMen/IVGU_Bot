class TeacherPlace:
    def __init__(self, teacher:str="",place:str=""):
        self.teacher = teacher
        self.place = place

    def __str__(self):
        return f"{self.teacher},{self.place}"