from dataclasses import dataclass

@dataclass
class Subject:
    def __init__(self, time="", name="", type="", subgroup = 0 ):
        self.time = time
        self.name = name
        self.type = type
        self.subgroup = subgroup