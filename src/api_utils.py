import requests
from typing import List, Dict
from abc import ABC, abstractmethod


class Parser(ABC):
    """Класс - родитель классов работы с API"""

    @abstractmethod
    def connect_to_api(self, search_string):
        """Соединение с сайтом"""
        pass

    @abstractmethod
    def get_vacancies(self, search_string, page_n):
        """Получение вакансий с сайта"""
        pass


class HeadHunterAPI(Parser):
    """Класс для работы с API HeadHunter"""

    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 20}
        self.vacancies = []
        # super().__init__()

    def connect_to_api(self, search_string: str):
        """
        Метод подключения к API HH
        :param search_string: строка поиска вакансий
        :return: Ответ от API или None в случае ошибки
        """
        try:
            self.__params["text"] = search_string
            response = requests.get(
                self.__url, headers=self.__headers, params=self.__params
            )
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            print(f"Ошибка при подключении к API: {e}")
            return None

    def get_vacancies(self, search_string: str, page_n: int = 5) -> List[Dict]:
        """Метод получения и обработки данных о вакансиях
        :param page_n: кол-во страниц
        :param search_string: строка поиска вакансий
        :return: Список обработанных вакансий"""
        self.__params["text"] = search_string
        all_vacancies = []
        while self.__params.get("page") != page_n:
            vacancies = self.connect_to_api(search_string).json().get("items", [])
            if isinstance(vacancies, list):
                all_vacancies.extend(vacancies)
            self.__params["page"] += 1
        return all_vacancies
