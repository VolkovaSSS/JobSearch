class Vacancy:
    """Класс Вакансия"""

    # __slots
    title: str
    link: str
    requirements: str
    salary_currency: str
    salary_from: float
    salary_to: float

    def __init__(self, title: str, link: str, requirements: str, salary: dict):
        self.title = title
        self.alternate_url = link
        self.__fill_salary(salary)
        self.requirements = requirements

    def __fill_salary(self, salary: dict):
        """Преобразует словарь с данными о зарплате к числам"""
        if salary:
            self.salary_currency = salary.get("currency", "RUR")
            self.salary_from = salary["from"] if salary["from"] else 0
            self.salary_to = salary["to"] if salary["to"] else 0
        else:
            self.salary_currency = "руб"
            self.salary_from = 0
            self.salary_to = 0

    @staticmethod
    def get_average(num1: float, num2: float):
        """Вычисляет среднее, при условии, что один из аргументов = 0"""
        return num1 if num2 == 0 else num2 if num1 == 0 else round((num1 + num2) / 2)

    def __lt__(self, other):
        """<"""
        return self.get_average(self.salary_from, self.salary_to) < self.get_average(
            other.salary_from, other.salary_to
        )

    def __str__(self):
        """Строка вывода вакансии"""
        return f"Наименование: {self.title}, З/п:{self.salary_from} - {self.salary_to} {self.salary_currency}, Требования: {self.requirements} , Ссылка: {self.alternate_url} "

    @classmethod
    def cast_to_object_list(cls, vacancies: list) -> list:
        """Преобразовывает список словарей вакансий (сырой ответ из API) в список экземпляров класса Vacancy"""
        list_of_vacancies = []
        for item in vacancies:
            print(item)
            list_of_vacancies.append(
                cls(
                    item.get("name"),
                    item.get("alternate_url", ""),
                    item.get("requirements", ""),
                    item.get("salary")                )
            )
        return list_of_vacancies

    def to_dict(self):
        return {
            "title": self.title,
            "currency": self.salary_currency,
            "salary": self.requirements,
            "link": self.link,
        }


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
