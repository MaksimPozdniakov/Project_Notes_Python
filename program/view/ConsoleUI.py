class ConsoleUI:
    def __init__(self):
        self.presenter = None

    def set_presenter(self, presenter):
        """Устанавливает объект презентера в консоли."""
        self.presenter = presenter

    def start(self):
        while True:
            menu_str = """
            Главное меню
            1. Открыть блокнот
            2. Показать все записи
            3. Добавить новую запись
            4. Удалить запись
            5. Найти запись
            6. Изменить запись
            7. Выборка по дате
            8. Сохранить 
            9. Закрыть программу
            """
            print(menu_str)

            inp = int(input("Сделайте выбор: "))

            if inp > 9 or inp < 1:
                print('В меню такого пункта нет.')

            match inp:
                case 1:
                    print("Блокнот открыт")
                    self.presenter.read()
                case 2:
                    self.presenter.print1()
                    self.sort()
                case 3:
                    self.add()
                    print('Запись добавлена.')
                case 4:
                    self.del_note()
                case 5:
                    self.search_note()
                case 6:
                    self.change_note()
                    print('Запись изменена.')
                case 7:
                    self.sampling_by_date()
                case 8:
                    self.presenter.save()
                    print("Все изменения сохранены.")
                case 9:
                    print("Блокнот закрыт")
                    exit()

    def add(self):
        header = input("Укажите заголовок: ")
        my_note = input("Введите новую заметку: ")
        self.presenter.add_note1(header, my_note)

    def del_note(self):
        self.presenter.print1()
        choice = int(input("Какую запись хотите удалить: "))
        self.presenter.del_note(choice)

    def search_note(self):
        search_word = input("Что будем искать: ")
        self.presenter.search_note(search_word)

    def change_note(self):
        self.presenter.print1()
        index = int(input("Какую запись нужно изменить: "))
        new_header = input("Введите новый заголовок: ")
        new_text = input("Введите новый текст: ")
        self.presenter.change_note(index, new_header, new_text)

    def sampling_by_date(self):
        our_date = input("Введите интересующую дату: ")
        self.presenter.sampling_by_date(our_date)

    def sort(self):
        while True:
            user_answer = input("Вы хотите отсортировать записи? (Да\Нет) ").upper()
            if user_answer == "ДА" or user_answer == 'LF':
                print("Если нужно отсортировать по дате создания нажмите 1 \n"
                      "Если нужно отсортировать по дате изменения нажмите 2 \n")
                user_answer2 = int(input("Сделайте выбор: "))
                if user_answer2 == 1:
                    self.presenter.sort(1)
                    break
                else:
                    self.presenter.sort(2)
                    break
            else:
                print('Что-то вы не то ввели.')
