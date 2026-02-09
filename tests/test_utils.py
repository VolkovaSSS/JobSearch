from src.utils import filter_vacancies, get_top_vacancies


def test_filter_vacancies(vacancies_class_test):

    filtered_vacancies = filter_vacancies(vacancies_class_test, ["Опыт"])
    assert "Опыт" in str(next(filtered_vacancies))


def test_get_top_vacancies(vacancies_class_test):

    top_vacancies = get_top_vacancies(vacancies_class_test, 30)
    assert top_vacancies[0].salary_from == 180000
    assert top_vacancies[1].salary_from == 170000
