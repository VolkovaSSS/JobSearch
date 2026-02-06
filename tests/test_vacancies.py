def test_vacancy_init(vacancy_test1):
    """Успешная инициализация"""

    assert vacancy_test1.title == "Python Developer"
    assert vacancy_test1.link == "<https://hh.ru/vacancy/123456>"
    assert (
        vacancy_test1.requirements
        == "Понимаешь логику: Знаешь основы Python или JavaScript"
    )
    assert vacancy_test1.salary_from == 90000
    assert vacancy_test1.salary_to == 110000
    assert vacancy_test1.salary_currency == "RUR"


def test_vacancy_init_no_salary(vacancy_no_salary):
    """Инициализация при отсутствии данных о зарплате"""

    assert vacancy_no_salary.title == "Python Developer"
    assert vacancy_no_salary.link == "<https://hh.ru/vacancy/123456>"
    assert (
        vacancy_no_salary.requirements
        == "Понимаешь логику: Знаешь основы Python или JavaScript"
    )
    assert vacancy_no_salary.salary_from == 0
    assert vacancy_no_salary.salary_to == 0
    assert vacancy_no_salary.salary_currency == "RUR"


def test_compare_salary(vacancy_test1, vacancy_test2):
    """Сравнение двух вакансий по зарплате"""

    expected_result = True
    assert vacancy_test1.__lt__(vacancy_test2) == expected_result


def test_vacancy_str(vacancy_test1):
    """ Тест вывода на печать """

    assert 'Наименование: Python Developer, З/п:90000 - 110000 RUR, ' in str(vacancy_test1)
