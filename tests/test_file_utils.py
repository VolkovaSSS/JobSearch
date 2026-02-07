from unittest.mock import mock_open, patch
from typing import Dict, List

from src.file_utils import JSONSaver


def test_init_class():
    json_s = JSONSaver()
    assert "vacancies.json" in str(json_s.filename)


@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data='[{"title": "Стажер", "link": "https://", "requirements": "Понимаешь логику"}]',
)
def test_get_data_file_success(mock_data):
    json_s = JSONSaver()
    assert json_s.get_data() == [
        {"title": "Стажер", "link": "https://", "requirements": "Понимаешь логику"}
    ]


@patch("builtins.open", new_callable=mock_open, read_data='title')
def test_get_data_wrong_format(mock_data, capsys):
    json_s = JSONSaver()
    captured = capsys.readouterr()
    result = json_s.get_data()
    captured = capsys.readouterr()
    assert  "В файле - некорректные данные. Операция не выполнена\n" == captured.out
    assert result == []


def test_get_data_no_file():
    """Тест ошибки чтения файла"""
    json_s = JSONSaver("no_file.json")
    assert json_s.get_data() == []


def test__is_duplicate(vacancies_test: List[Dict]):
    """ Проверка дублей """
    json_s = JSONSaver()
    result = json_s._is_duplicate(vacancies_test, "https://hh.ru/vacancy/129356483")
    assert result

    result = json_s._is_duplicate(vacancies_test, "https://hh.ru/vacancy/130134630")
    assert result == False

def test_is_duplicate_empty():
    """ Проверка дублей с пустым списком """
    json_s = JSONSaver()
    result = json_s._is_duplicate([], "https://hh.ru/vacancy/129356483")
    assert result == False


def test_add_data_empty(capsys):
    """ Проверка записи в файл при отсутствии данных """
    json_s = JSONSaver()
    json_s.add_data([])
    captured = capsys.readouterr()
    assert "Нет данных для добавления" in captured.out


def test_add_data(vacancies_from_api):
    """ Проверка записи в файл при отсутствии данных """
    json_s = JSONSaver("test_file.json")
    json_s.add_data(vacancies_from_api)
    test_vacancies = json_s.get_vacancies()

    assert test_vacancies[0].title == "Инженер отдела IT"
    assert test_vacancies[1].link == "https://hh.ru/vacancy/129356483"
    assert len(test_vacancies) == 2
    vacancy_del = test_vacancies[1]
    json_s.delete_data(vacancy_del)
    test_vacancies = json_s.get_vacancies()
    assert len(test_vacancies) == 1
    json_s.delete_data()

