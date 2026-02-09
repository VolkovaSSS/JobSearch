from src.api_utils import HeadHunterAPI
from src.file_utils import JSONSaver
from src.utils import filter_vacancies, get_top_vacancies


class UserMenu:
    """Класс для взаимодействия с пользователем"""

    def __init__(self):
        """Инициализация меню"""
        self.menu_items = {
            1: ("Выполнить запрос вакансий с сайта hh.ru", self.get_vacancies_from_hh),
            2: ("Получить Топ вакансий по зарплате", self.get_top_vacancies_from_json),
            3: (
                "Получить вакансии с ключевым словом в описании",
                self.get_vacancies_by_key_from_json,
            ),
            4: ("Очистить файл с вакансиями", self.clear_vacancies_from_json),
            0: ("Выход", None),
        }

    def display_menu(self) -> None:
        """Отображение меню на экране"""

        print("\n" + "=" * 30)
        print("МЕНЮ")
        print("=" * 30)
        for key, (description, _) in sorted(self.menu_items.items()):
            print(f"{key}. {description}")
        print("=" * 30)

    def run(self) -> None:
        """Запуск меню с обработкой выбора пользователя"""

        while True:
            self.display_menu()
            try:
                choice = int(input("Выберите пункт меню: "))
            except ValueError:
                print("Ошибка! Введите целое число.")
                continue
            if choice == 0:
                print("Выход из программы...")
                break
            if choice in self.menu_items:
                description, function = self.menu_items[choice]
                if function:
                    print(f"\nВыбрано: {description}")
                    function()
                else:
                    print("Неверный пункт меню! Попробуйте снова.")
            else:
                print("Неверный пункт меню! Попробуйте снова.")

    @staticmethod
    def get_vacancies_from_hh() -> None:
        """Запрос вакансий с сайта hh.ru и запись в файл"""
        keyword = input("Введите ключевое слово для поиска: ")
        hh_api = HeadHunterAPI()
        hh_vacancies = hh_api.get_vacancies(keyword)
        json_saver = JSONSaver()
        json_saver.add_data(hh_vacancies)
        print(f"Запрос выполнен. Данные сохранены в файл {json_saver.filename}")

    @staticmethod
    def get_top_vacancies_from_json() -> None:
        """Топ вакансий по зарплате"""

        try:
            top_n = int(input("Введите целое число - количество вакансий для топа: "))
            json_saver = JSONSaver()
            vacancies = json_saver.get_vacancies()
            top_vacancies = get_top_vacancies(vacancies, top_n)
            for item in top_vacancies:
                print(str(item))
        except ValueError:
            print("Ошибка! Количество вакансий д.б. числом.")

    @staticmethod
    def get_vacancies_by_key_from_json() -> None:
        """Вывод вакансий по ключевому слову в requirements"""

        keywords = input("Введите слова поиска через пробел: ")
        keywords_list = keywords.split()
        json_saver = JSONSaver()
        vacancies = json_saver.get_vacancies()
        if keywords_list and vacancies:
            filtered_vacancies = filter_vacancies(vacancies, keywords_list)
            for item in filtered_vacancies:
                print(str(item))
        else:
            print(f"Нет данных по {keywords}")

    @staticmethod
    def clear_vacancies_from_json() -> None:
        """Удаление всех вакансий из файла"""

        json_saver = JSONSaver()
        json_saver.delete_data()
