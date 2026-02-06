import json
import os
from typing import Dict, Any, List
from abc import ABC, abstractmethod
from src.vacancies import Vacancy


class FileHandler(ABC):
    """Абстрактный класс для работы с файлами"""

    @abstractmethod
    def get_data(self) -> List[Dict[str, Any]]:
        """Получение данных из файла"""
        pass

    @abstractmethod
    def add_data(self, data: List[Dict[str, Any]]) -> None:
        """Добавление данных в файл"""
        pass

    @abstractmethod
    def delete_data(self, criteria: Dict[str, Any]) -> None:
        """Удаление данных из файла по условию"""
        pass


class JSONSaver(FileHandler):
    """Класс для работы с JSON-файлами с данными о вакансиях"""

    """Сохранение информации о вакансиях в файл"""

    def __init__(self, filename: str = "data/vacancies.json"):
        self.__filename = filename

    @property
    def filename(self) -> str:
        """Получение имени файла"""
        return self.__filename

    def get_data(self) -> List[Dict[str, Any]]:
        """
        Получение данных о вакансиях из JSON-файла
        Returns: Список словарей с вакансиями
        """
        if not os.path.exists(self.__filename):
            return []
        try:
            with open(self.__filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                return data if isinstance(data, list) else []
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    @staticmethod
    def convert_vacancies(vacancies: List[Dict[str, Any]]) -> List[Vacancy]:
        """Преобразует список словарей в список объектов класса Vacancy """
        return [Vacancy(**vacancy) for vacancy in vacancies]

    def get_vacancies(self) -> List[Vacancy]:
        """ Получение списка объектов Vacancy из JSON-файла """

        vacancies = self.get_data()
        return self.convert_vacancies(vacancies)

    @staticmethod
    def _is_duplicate(existing_data: List[Dict[str, Any]], new_url: str) -> bool:
        """
        Проверка на дублирование вакансии
        Args:
            existing_data: Существующие данные
            new_url: Новая вакансия для проверки
        Returns: True если дубликат найден, иначе False
        """
        if not existing_data:
            return False
        if next((item for item in existing_data if item["link"] == new_url), None):
            return True
        else:
            return False

    def add_data(self, vacancies: List[Dict[str, Any]]) -> None:
        """
        Добавление данных в JSON-файл
        Args: data: Список словарей с данными для добавления
        """
        if not vacancies:
            return
        existing_data = self.get_data()
        for vacancy in vacancies:
            if not self._is_duplicate(existing_data, vacancy["alternate_url"]):
                existing_data.append({"name": vacancy["name"], "link": vacancy["alternate_url"], "salary": vacancy["salary"],
                                      "requirements": vacancy["snippet"]["requirement"]})

        with open(self.__filename, "w", encoding="utf-8") as file:
            json.dump(existing_data, file, ensure_ascii=False, indent=2)

    def delete_data(self, criteria: Dict[str, Any] = None) -> None:
        """
        Удаление данных из JSON-файла по условию
        Args:
            criteria: Словарь с условиями для удаления
                Пример: {"id": "123"} или {"title": "Python разработчик"}
        """
        if not criteria:
            with open(self.__filename, "w", encoding="utf-8") as file:
                json.dump([], file, ensure_ascii=False, indent=2)

    #     existing_data = self.get_data()
    #
    #     # Фильтруем данные, оставляя только те, которые НЕ соответствуют условию
    #     filtered_data = []
    #     for item in existing_data:
    #         should_keep = True
    #         for key, value in criteria.items():
    #             if item.get(key) == value:
    #                 should_keep = False
    #                 break
    #
    #         if should_keep:
    #             filtered_data.append(item)
    #
    #     # Сохраняем отфильтрованные данные
    #     with open(self.__filename, "w", encoding="utf-8") as file:
    #         json.dump(filtered_data, file, ensure_ascii=False, indent=2)
    #
    # def clear_all_data(self) -> None:
    #     """Очистка всех данных из файла"""
    #     with open(self.__filename, "w", encoding="utf-8") as file:
    #         json.dump([], file, ensure_ascii=False, indent=2)
    #
    # def read_file(self) -> list:
    #     """Метод, который читает данные из файла"""
    #     try:
    #         with open(self.__filename, "r", encoding="utf-8") as file:
    #             return json.load(file)
    #     except (json.JSONDecodeError, FileNotFoundError):
    #         return []
    #
    # def _write_file(self, data: list) -> None:
    #     """Метод, который записывает данные в файл"""
    #     with open(self.__filename, "w", encoding="utf-8") as file:
    #         json.dump(data, file, ensure_ascii=False, indent=4)
    #
    # def add_vacancy(self, new_vacancy) -> None:
    #     """Добавляет вакансию в json-файл"""
    #     vacancies = self.read_file()
    #     for vacancy in vacancies:
    #         if new_vacancy.to_dict().get("vacancy_id") != vacancy.get("vacancy_id"):
    #             vacancies.append(new_vacancy.to_dict())
    #             self._write_file(vacancies)
    #         elif not vacancies:
    #             vacancies.append(new_vacancy)
    #             self._write_file(vacancies)
    #         else:
    #             print("Нет новых вакансий для добавления")


# json_saver = JSONSaver()
# json_saver.delete_data()

