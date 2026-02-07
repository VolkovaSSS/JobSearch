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
    read_data='[{"title": "Стажер", "link": "https://", "requirements": "Понимаешь логику"}]')
def test_get_data_file_success(mock_data):
    json_s = JSONSaver()
    assert json_s.get_data() == [{"title": 'Стажер', "link": 'https://', "requirements": 'Понимаешь логику'}]\


def test_get_data_no_file():
    """Тест ошибки чтения файла"""
    json_s = JSONSaver("no_file.json")
    assert json_s.get_data() == []
    # with pytest.raises(FileNotFoundError):
    #     json_s.get_data()