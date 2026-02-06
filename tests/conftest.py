import pytest
from src.vacancies import Vacancy


@pytest.fixture
def vacancy_test1():
    return Vacancy(
        "Python Developer",
        "<https://hh.ru/vacancy/123456>",
        "Понимаешь логику: Знаешь основы Python или JavaScript",
        {"from": 90000, "to": 110000, "currency": "RUR"},
    )


@pytest.fixture
def vacancy_test2():
    return Vacancy(
        "Тестировщик",
        "https://hh.ru/vacancy/130134630",
        "Опыт работы с Docker. Умение писать простые скрипты на PHP, Python",
        {"from": 180000, "to": 200000, "currency": "RUR"},
    )


@pytest.fixture
def vacancy_no_salary():
    return Vacancy(
        "Python Developer",
        "<https://hh.ru/vacancy/123456>",
        "Понимаешь логику: Знаешь основы Python или JavaScript",
        None,
    )
