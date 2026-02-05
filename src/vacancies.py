from locale import currency


class Vacancy:
    title: str
    link: str
    requirements: str
    salary_currency: str
    salary: str


    def __init__(self, title, link, requirements, salary_currency, salary):
        self.title = title
        self.link = link
        self.salary = salary
        self.requirements = requirements

    @classmethod
    def cast_to_object_list(cls, vacancies: list) -> list:
        """Преобразовывает список словарей вакансий (сырой ответ из API) в список экземпляров класса Vacancy"""
        list_of_vacancies = []
        for item in vacancies:
            print(item)
            salary_dict = item.get("salary")
            salary_currency = salary_dict.get("currency", "")
            salary_min = salary_dict.get("from", 0)
            salary_max = salary_dict.get("to", 0)
            if salary_min == 0:
                salary = salary_max
            elif salary_max == 0:
                salary = salary_min
            else:
                salary = round((salary_min + salary_max) / 2, 2)

            list_of_vacancies.append(cls(item.get("name"), item.get("url",""), item.get("requirements",""), salary_currency, salary))

        return list_of_vacancies

    def to_dict(self):
        return {"title": self.title, "salary": self.salary, "link": self.link}


# vacancies_list = [vacancy.to_dict() for vacancy in vacancies]
# with open('data.json', 'w') as f:
#     json.dump(data, f, indent=4)


def filter_vacancies(vacancies_list, filter_words):
    """Фильтрация вакансий по ключевым словам"""

    pass


def get_vacancies_by_salary(filtered_vacancies, salary_range):
    """Ранжирует вакансии по зарплате"""

    pass


def sort_vacancies(ranged_vacancies):

    pass


def get_top_vacancies(sorted_vacancies, top_n):

    pass


def print_vacancies(top_vacancies):
    pass
