from typing import Optional


class Vacancy:
    """Класс Вакансия"""

    title: str
    link: str
    requirements: str
    salary_currency: str
    salary_from: int
    salary_to: int

    __slots__ = (
        "title",
        "link",
        "requirements",
        "salary_currency",
        "salary_from",
        "salary_to",
    )

    def __init__(
        self, title: str, link: str, requirements: str, salary: Optional[dict]
    ):
        self.title = title
        self.link = link
        self.__fill_salary(salary)
        self.requirements = requirements

    def __fill_salary(self, salary: dict):
        """Преобразует словарь с данными о зарплате к числам"""
        if salary:
            self.salary_currency = salary.get("currency", "RUR")
            self.salary_from = salary["from"] if salary["from"] else 0
            self.salary_to = salary["to"] if salary["to"] else 0
        else:
            self.salary_currency = "RUR"
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
        return f"Наименование: {self.title}, З/п:{self.salary_from} - {self.salary_to} {self.salary_currency}, Требования: {self.requirements} , Ссылка: {self.link} "

    @classmethod
    def cast_to_object_list(cls, vacancies: list) -> list:
        """Преобразует список словарей вакансий (сырой ответ из API) в список экземпляров класса Vacancy"""
        list_of_vacancies = []
        for item in vacancies:
            print(item)
            list_of_vacancies.append(
                cls(
                    item.get("name"),
                    item.get("alternate_url", ""),
                    item["snippet"].get("requirements", ""),
                    item.get("salary", None),
                )
            )
        return list_of_vacancies

    # def to_dict(self):
    #     return {
    #         "title": self.title,
    #         "currency": self.salary_currency,
    #         "salary": self.requirements,
    #         "link": self.link,
    #     }
