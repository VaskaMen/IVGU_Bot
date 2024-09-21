from attr import dataclass


@dataclass
class Subject:
    time: str
    name: str
    type: str

    # def __eq__(self, other):
    #     if self is other:
    #         return self.time == other.time
    #     else:
    #         return False
