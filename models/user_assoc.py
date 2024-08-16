from enum import Enum
from dataclasses import dataclass

class Role(Enum):
    ADMIN = 1
    USER = 2


@dataclass
class User:
    id: int
    login: str
    password_hash: str
    reg_date: int
    role: Role


class UserAssoc:
    def __init__(self) -> None:
        pass