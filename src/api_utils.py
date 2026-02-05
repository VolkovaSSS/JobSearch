import requests
from abc import ABC, abstractmethod


class Parser(ABC):
    """Класс - родитель классов работы с API"""

    # Phyton Создать класс для работы с API ,  в котором Реализован метод подключения к API ,
    # Реализован метод получения данных .

    @classmethod
    @abstractmethod
    def __init__(cls):
        pass

    def connect_to_api(self, params=None):
        """Соединение с сайтом"""
        pass

    def get_vacancies(self, keyword):
        """Получение вакансий с сайта"""
        pass


class HeadHunterAPI(Parser):
    """Класс для работы с API HeadHunter"""

    def __init__(self):
        self.url = "https://api.hh.ru/vacancies"
        self.headers = {"User-Agent": "HH-User-Agent"}
        self.params = {"text": "", "page": 0, "per_page": 100}
        self.vacancies = []
        # super().__init__()

    def connect_to_api(self, params=None):
        """
        МЕТОД ПОДКЛЮЧЕНИЯ: базовый запрос к API.
        Отправляет запрос на базовый URL + endpoint.
        Метод подключения к API HH и получения данных о вакансиях
        :param params: Словарь параметров запроса
        :return: Ответ от API или None в случае ошибки
        """
        try:
            # Выполнение GET-запроса к API
            # url = f"{self.base_url}/{endpoint}"
            # response = requests.get(url, params=params)
            response = requests.get(self.url, headers=self.headers, params=params)
            # Проверка успешности запроса
            response.raise_for_status()
            # Возврат JSON-ответа
            return response.json()
        except requests.RequestException as e:
            # Обработка ошибок подключения
            print(f"Ошибка при подключении к API: {e}")
            return None

    def get_vacancies(self, keyword: str) -> list:
        """Метод получения и обработки данных о вакансиях
        :param search_params: Параметры поиска вакансий
        :return: Список обработанных вакансий"""

        # Вызов метода подключения перед получением данных
        # self.params['text'] = keyword
        # return self.connect_to_api("vacancies", params) vacancies[0]

        self.params["text"] = keyword
        while self.params.get("page") != 5:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()["items"]
            self.vacancies.extend(vacancies)
            self.params["page"] += 1
        return self.vacancies


class HHVacancyParser:

    def connect_to_api(self, params=None):
        """
        Метод подключения к API HH и получения данных о вакансиях
        :param params: Словарь параметров запроса
        :return: Ответ от API или None в случае ошибки
        """
        try:
            # Выполнение GET-запроса к API
            response = requests.get(self.api_url, headers=self.headers, params=params)
            # Проверка успешности запроса
            response.raise_for_status()
            # Возврат JSON-ответа
            return response.json()

        except requests.RequestException as e:
            # Обработка ошибок подключения
            print(f"Ошибка при подключении к API: {e}")
            return None

    def get_vacancies(self, search_params=None):
        """Метод получения и обработки данных о вакансиях
        :param search_params: Параметры поиска вакансий
        :return: Список обработанных вакансий"""
        # Параметры по умолчанию, если не переданы
        if search_params is None:
            search_params = {
                "text": "Python разработчик",  # Пример поиска
                "area": 1,  # Москва
                "page": 0,
                "per_page": 50,
            }
        # Вызов метода подключения к API
        api_response = self.connect_to_api(params=search_params)


class HHApiClient:
    def __init__(self):
        self.base_url = "https://api.hh.ru"

    def _send_request(self, endpoint: str, params: dict = None) -> dict:
        """
        МЕТОД ПОДКЛЮЧЕНИЯ: базовый запрос к API.
        Отправляет запрос на базовый URL + endpoint.
        """
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_vacancies(self, employer_id: str) -> list:
        """
        МЕТОД ПОЛУЧЕНИЯ ДАННЫХ: использует метод подключения.
        """
        # Вызов метода подключения перед получением данных
        params = {"employer_id": employer_id, "per_page": 100}
        return self._send_request("vacancies", params)
