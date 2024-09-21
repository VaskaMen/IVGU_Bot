from attr import dataclass


@dataclass
class User:
    id: int
    get_changes: bool