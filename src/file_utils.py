import json
import os
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Dict, List

from src.vacancies import Vacancy


class FileHandler(ABC):
    """Абстрактный класс для работы с файлами"""

    @abstractmethod
    def get_vacancies(self) -> List[Vacancy]:
        """Получение данных о вакансиях из файла"""
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

    def __init__(self, filename: str = "vacancies.json"):
        base_dir = Path(__file__).resolve().parents[1]
        full_filename = Path(f"{base_dir}/data/{filename}")
        self.__filename = full_filename

    @property
    def filename(self) -> Path:
        """Получение имени файла"""
        return self.__filename

    def get_data(self) -> List[Dict[str, Any]]:
        """
        Получение данных о вакансиях из JSON-файла
        Returns: Список словарей с вакансиями
        """
        if not os.path.exists(self.__filename):
            print("Файл пустой")
            return []
        try:
            with open(self.__filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                return data if isinstance(data, list) else []
        except (json.JSONDecodeError, ValueError):
            print("В файле - некорректные данные. Операция не выполнена")
            return []

    @staticmethod
    def convert_vacancies(vacancies: List[Dict[str, Any]]) -> List[Vacancy]:
        """Преобразует список словарей в список объектов класса Vacancy"""
        return [Vacancy(**vacancy) for vacancy in vacancies]

    def get_vacancies(self) -> List[Vacancy]:
        """Получение списка объектов Vacancy из JSON-файла"""

        vacancies = self.get_data()
        return self.convert_vacancies(vacancies)

    @staticmethod
    def _is_duplicate(existing_data: List[Dict[str, Any]], new_url: str) -> bool:
        """
        Проверка на дублирование вакансии
        Args:
            existing_data: Существующие данные
            new_url: url новой вакансии для проверки
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
            print("Нет данных для добавления")
            return
        existing_data = self.get_data()
        for vacancy in vacancies:
            if not self._is_duplicate(existing_data, vacancy["alternate_url"]):
                existing_data.append(
                    {
                        "title": vacancy["name"],
                        "link": vacancy["alternate_url"],
                        "salary": vacancy["salary"],
                        "requirements": vacancy["snippet"].get("requirement", ""),
                    }
                )

        with open(self.__filename, "w", encoding="utf-8") as file:
            json.dump(existing_data, file, ensure_ascii=False, indent=2)

    def delete_data(self, del_vacancy: Vacancy = None) -> None:
        """
        Удаление данных из JSON-файла по условию
        Args:
            del_vacancy: объект класса Vacancy для удаления
            Если не указан, удаляются все данные
        """
        if not del_vacancy:
            with open(self.__filename, "w", encoding="utf-8") as file:
                json.dump([], file, ensure_ascii=False, indent=2)
        else:
            del_link = del_vacancy.link
            if not del_link:
                print(
                    "Ссылка не заполнена, нет возможности для отбора. Удаление не выполнено"
                )
            existing_data = self.get_data()

            filtered_data = [
                item for item in existing_data if item.get("link", "") != del_link
            ]
            with open(self.__filename, "w", encoding="utf-8") as file:
                json.dump(filtered_data, file, ensure_ascii=False, indent=2)
