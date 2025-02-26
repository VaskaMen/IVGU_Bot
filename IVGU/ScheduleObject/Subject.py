from dataclasses import dataclass

@dataclass
class Subject:
    def __init__(self, time="", name="", type="", group = 0 ):
        self.time = time
        self.name = name
        self.type = type
        self.group = group