from dataclasses import dataclass

@dataclass
class Subject:
    def __init__(self, time="", name="", type="", group = 0 ):
        self.time = time
        self.name = name
        self.type = type
        self.group = group

    # def __eq__(self, other):
    #     if self is other:
    #         return self.time == other.time
    #     else:
    #         return False
