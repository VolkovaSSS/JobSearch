from src.vacancies import Vacancy


def filter_vacancies(vacancies: list[Vacancy], filter_words: list[str]) -> list[Vacancy]:
    """Фильтрация вакансий по ключевым словам в title или requirements
    Returns: Отфильтрованный список вакансий"""

    if not filter_words or not vacancies:
        return vacancies
    keywords_lower = [keyword.lower() for keyword in filter_words]

    filtered_vacancies = []
    for vacancy in vacancies:
        title_lower = vacancy.title.lower()
        description_lower = vacancy.requirements.lower()
        if any(keyword in title_lower or keyword in description_lower
               for keyword in keywords_lower):
            filtered_vacancies.append(vacancy)

    return filtered_vacancies


def get_vacancies_by_salary(filtered_vacancies, salary_range):
    """Ранжирует вакансии по зарплате"""

    pass


def sort_vacancies(ranged_vacancies):
    """ Сортировка по зарплате"""
    pass


def get_top_vacancies(vacancies, top_n=5) -> list[Vacancy]:
    """ Возвращает вакансий с top_n=5 максимальной зарплатой"""
    return sorted(vacancies, reverse=True)[:top_n]


def print_vacancies(top_vacancies: list[Vacancy]) -> None:
    """ Печать выбранных вакансий"""

    for item in top_vacancies:
        print(str(item))
