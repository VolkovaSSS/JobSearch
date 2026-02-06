from unittest.mock import mock_open, patch
from src.api_utils import HeadHunterAPI


@patch("requests.get")
def test_connect_to_api_success(mock_get):

    hh_api = HeadHunterAPI()
    hh_api._connect_to_api("Python")
    mock_get.return_value.status_code = 200
    mock_get.assert_called_once_with(
        "https://api.hh.ru/vacancies",
        headers={"User-Agent": "HH-User-Agent"},
        params={"text": "Python", "page": 0, "per_page": 20},
    )


@patch("requests.get")
def test_get_vacancies(mock_get):

    hh_api = HeadHunterAPI()
    keyword = "Python"

    mock_get.return_value.json.return_value = {
        "items": [{"name": "Специалист по ведению базы данных", "salary": 50000}]
    }
    mock_get.return_value.status_code = 200
    result = hh_api.get_vacancies(keyword, 1)
    expected = [{"name": "Специалист по ведению базы данных", "salary": 50000}]
    assert result == expected
    mock_get.assert_called_once_with(
        "https://api.hh.ru/vacancies",
        headers={"User-Agent": "HH-User-Agent"},
        params={"text": "Python", "page": 1, "per_page": 20},
    )
