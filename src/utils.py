from typing import Iterator

from src.vacancies import Vacancy


def filter_vacancies(vacancies: list[Vacancy], filter_words: list[str]) -> Iterator:
    """Фильтрация вакансий по ключевым словам в title или requirements
    Returns: Итератор - отфильтрованные вакансии"""

    keywords_lower = [keyword.lower() for keyword in filter_words]
    for vacancy in vacancies:
        description_lower = vacancy.requirements.lower()
        if any(keyword in description_lower for keyword in keywords_lower):
            yield vacancy


def get_top_vacancies(vacancies, top_n=5) -> list[Vacancy]:
    """Возвращает вакансий с top_n=5 максимальной зарплатой"""
    return sorted(vacancies, reverse=True)[:top_n]


def print_vacancies(vacancies: list[Vacancy]) -> None:
    """Печать выбранных вакансий"""

    for item in vacancies:
        print(str(item))
