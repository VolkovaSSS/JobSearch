from typing import Dict, List

import pytest

from src.file_utils import JSONSaver
from src.vacancies import Vacancy


@pytest.fixture
def vacancy_test1() -> Vacancy:
    return Vacancy(
        "Python Developer",
        "<https://hh.ru/vacancy/123456>",
        "Понимаешь логику: Знаешь основы Python или JavaScript",
        {"from": 90000, "to": 110000, "currency": "RUR"},
    )


@pytest.fixture
def vacancy_test2() -> Vacancy:
    return Vacancy(
        "Тестировщик",
        "https://hh.ru/vacancy/130134630",
        "Опыт работы с Docker. Умение писать простые скрипты на PHP, Python",
        {"from": 180000, "to": 200000, "currency": "RUR"},
    )


@pytest.fixture
def vacancy_no_salary() -> Vacancy:
    """Список вакансий - словарей"""
    return Vacancy(
        "Python Developer",
        "<https://hh.ru/vacancy/123456>",
        "Понимаешь логику: Знаешь основы Python или JavaScript",
        None,
    )

@pytest.fixture
def vacancies_from_api() -> List[Dict]:
    return [
        {
            "name": "Инженер отдела IT",
            "alternate_url": "https://hh.ru/vacancy/129336877",
            "salary": {"from": 170000, "to": 180000, "currency": "RUR", "gross": None},
            "snippet": {"requirement": "Уверенные знания Phyton."},
        },
        {
            "name": "Аналитик данных",
            "alternate_url": "https://hh.ru/vacancy/129356483",
            "salary": None,
            "snippet": {"requirement": "Продвинутый уровень владения excel"},
        }]


@pytest.fixture
def vacancies_test() -> List[Dict]:
    return [
        {
            "title": "Инженер отдела информационных технологий",
            "link": "https://hh.ru/vacancy/129336877",
            "salary": {"from": 170000, "to": 180000, "currency": "RUR", "gross": None},
            "requirements": "Уверенные практические знания Linux. Опыт автоматизации работы ble, Phyton.",
        },
        {
            "title": "Аналитик данных",
            "link": "https://hh.ru/vacancy/129356483",
            "salary": None,
            "requirements": "Продвинутый уровень владения excel, PQ, SQL. Базовые знания Phyton. "
                            "Опыт работы с системами визуализации...",
        },
        {
            "title": "Специалист по искусственному интеллекту",
            "link": "https://hh.ru/vacancy/129858315",
            "salary": None,
            "requirements": "Высшее образование (Техническое, IT). Опытный пользователь MS Office. "
                            "Программирование (Phyton, Julia, Scala, Java). Фреймворки машинного обучения "
                            "(TensorFlow, PyTorch, Scikit-learn...",
        },
        {
            "title": "Инженер",
            "link": "https://hh.ru/vacancy/129445216",
            "salary": {"from": 78000, "to": None, "currency": "RUR"},
            "requirements": "Наличие навыков: - чтение чертежей. Компьютерные навыки: Qform 3D, Fidesys, Macr Mentat.",
        },
        {
            "title": "Начинающий специалист (аналитик НПФ/УК)",
            "link": "https://hh.ru/vacancy/127487891",
            "salary": None,
            "requirements": "высшее образование (экономическое, управление рисками, прикладная математика). ",
        },
        {
            "title": "Финансовый аналитик в финтех",
            "link": "https://hh.ru/vacancy/129935159",
            "salary": {"from": 180000, "to": None, "currency": "RUR"},
            "requirements": "Знание Microsoft Excel, Power Pivot и Power Query. Знание Phyton",
        },
        {
            "title": "Разработчик С++ (стажер)",
            "link": "https://hh.ru/vacancy/129450352",
            "salary": None,
            "requirements": "Базовые знания языков программирования С++, С. Базовые знание скриптовых языков: Phyton",
        },
        {
            "title": "Разработчик (Отдел разработки ИТ инструментов расчёта ЗП)",
            "link": "https://hh.ru/vacancy/129997406",
            "salary": {"from": 100000, "to": 100000, "currency": "RUR"},
            "requirements": "Знание принципов ООП, языков программирования: JavaScript, Phyton; XML‚ HTML.",
        },
    ]


@pytest.fixture
def vacancies_class_test(vacancies_test) -> List[Vacancy]:
    """Список объектов класса Vacancy"""

    json_s = JSONSaver()
    return json_s.convert_vacancies(vacancies_test)
