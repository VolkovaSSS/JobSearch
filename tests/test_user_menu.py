import pytest
from src.user_menu import UserMenu


@pytest.fixture
def test_menu() -> UserMenu:
    return UserMenu()


def test_init_menu(test_menu: UserMenu) -> None:
    """Тест инициализации меню"""
    assert test_menu.menu_items[0][0] == "Выход"
    assert test_menu.menu_items[1][0] == "Выполнить запрос вакансий с сайта hh.ru"
    assert test_menu.menu_items[2][0] == "Получить Топ вакансий по зарплате"
    assert (
        test_menu.menu_items[3][0] == "Получить вакансии с ключевым словом в описании"
    )
    assert test_menu.menu_items[4][0] == "Очистить файл с вакансиями"


def test_display_menu(test_menu: UserMenu, capsys) -> None:
    """Тест вывода меню на экран"""

    test_menu.display_menu()
    captured = capsys.readouterr()
    assert "Получить Топ вакансий" in captured.out
