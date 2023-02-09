import random as rand
from typing import Iterator, Protocol, TypeAlias
from faker import Faker

faker = Faker()

T_LOGIN: TypeAlias = str
T_PASSWORD: TypeAlias = str


class UserProtocol(Protocol):
    login: T_LOGIN
    password: T_PASSWORD


class User:
    def __init__(self, login, password) -> None:
        self.login = login
        self.password = password

    def get_dict(self):  # if needed
        login_and_password = {self.login: self.password}
        return login_and_password

    def __repr__(self):
        return self.login, self.password

    def __str__(self):
        return f"{self.login}, {self.password}"


def generate_user() -> Iterator[UserProtocol]:
    unique_login = (
        f"{((faker.first_name()).lower())[:rand.randint(1, 3)]}"
        f"_{(faker.last_name()).lower()}{rand.randint(1, 2022)}"
    )
    unique_password = unique_login[::-1]
    new_user: UserProtocol = User(unique_login, unique_password)
    yield new_user


def generate_and_validate_users_list(amount: int) -> int:
    users_list = set()
    login_list = set()
    while len(login_list) != amount:
        temporary_user = next(generate_user())
        if temporary_user.login not in login_list:
            users_list.add(temporary_user)
            login_list.add(temporary_user.login)
    return len(login_list)


def main():
    amount = 100_000
    if generate_and_validate_users_list(amount) == amount:
        return "Everything OK"


if __name__ == "__main__":
    main()
