from random import choice
from string import ascii_lowercase, digits
from uuid import uuid4


class Generator:
    @staticmethod
    def email() -> str:
        return f"vladislav_dovgun_12_{uuid4()}@yandex.ru"

    @staticmethod
    def login(length: int = 5) -> str:
        return "".join(choice(ascii_lowercase) for i in range(length))

    @staticmethod
    def password(length: int = 3) -> str:
        return "".join(choice(digits) for i in range(length)) + "".join(
            choice(ascii_lowercase) for i in range(length)
        )
