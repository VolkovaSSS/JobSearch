import os
import pytest
from pathlib import Path
from unittest.mock import mock_open, patch
from src.file_utils import JSONSaver

@pytest.fixture
def file_vacancies():
    base_dir = Path(__file__).resolve().parents[1]
    return Path(f"{base_dir}/data/vacancies.json")


@pytest.fixture
def json_saver_test():
    json_saver = JSONSaver()


@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data='[{"title": "Стажер", "link": "https://", "requirements": "Понимаешь логику}]')
def test_get_data_file_correct(mock_data):
    json_s = JSONSaver()
    assert json_s.get_data() == [{"title": 'Стажер', "link": 'https://', "requirements": 'Понимаешь логику'}]


@patch("builtins.open", new_callable=mock_open, read_data="AAPL, AMZN, GOOGL, MSFT, TSLA")
def test_get_user_settings_file_wrong(mock_data, file_user_settings):
    assert get_user_settings(file_user_settings) == {}


@patch("builtins.open", new_callable=mock_open, read_data="")
def test_get_user_settings_empty(mock_data, file_user_settings):
    assert get_user_settings(file_user_settings) == {}


def test_get_user_settings_no_file():
    """Тест ошибки чтения файла настроек пользователя"""
    with pytest.raises(Exception):
        get_user_settings("../data/no_file.json")