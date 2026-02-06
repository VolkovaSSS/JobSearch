from src.vacancies import Vacancy

def filter_vacancies(vacancies_list: list[Vacancy], filter_words) -> list[Vacancy]:
    """Фильтрация вакансий по ключевым словам"""

    pass


def get_vacancies_by_salary(filtered_vacancies, salary_range):
    """Ранжирует вакансии по зарплате"""

    pass


def sort_vacancies(ranged_vacancies):

    pass


def get_top_vacancies(vacancies, top_n=5):

    return sorted(vacancies, reverse=True)[:top_n]


def print_vacancies(top_vacancies):
    pass