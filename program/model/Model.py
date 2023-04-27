from datetime import datetime
from program.model.Note import Note
from program.model.Reading import Reading
from program.model.Writing import Writing


class Model:

    def __init__(self):
        self.notes = []

    def add_note(self, header, text):
        note = Note(header, text, datetime.today().strftime('%d.%m.%Y %H:%M'),
                    datetime.today().strftime('%d.%m.%Y %H:%M'))
        self.notes.append(note)

    def print(self):
        # for item in self.notes:
        #     new_list = str(item).split(";")
        #     print('{} | {} | Дата создания: {} | Дата редактирования: {}'.format(new_list[0], new_list[1],
        #                                                                          new_list[2], new_list[3]))

        data_list = []
        for item in self.notes:
            list_item = str(item).split(";")
            data = {"Заголовок": list_item[0], "Содержание записи": list_item[1], "Дата создания": list_item[2],
                    "Дата изменения": list_item[3]}
            data_list.append(data)
        number = 1
        for el in data_list:
            list_el = str(el).replace('{', '').replace('}', '').replace("'","")
            print(str(number) + ') ' + list_el)
            number += 1

    def del_note(self, index):
        self.notes.pop(index-1)

    def search_note(self, search_word):
        new_list = []
        for el in self.notes:
            str_el = str(el)
            new_list.append(str_el)

        for el in new_list:
            if search_word in el:
                print(el)

    def change_note(self, index, new_header, new_text):
        my_list = self.notes[index-1].split(";")
        my_list[0] = new_header
        my_list[1] = new_text
        my_list[3] = datetime.today().strftime('%d.%m.%Y %H:%M')
        my_str = ""
        for item in my_list:
            my_str += item + ";"
        my_str = my_str[:-1]
        self.notes[index-1] = my_str

    def sampling_by_date(self, our_date):
        new_list = []
        for el in self.notes:
            str_el = str(el)
            new_list.append(str_el)

        for el in new_list:
            if our_date in el:
                print(el)

    def save(self):
        sss = Writing("C:/Users/PMPav/Desktop/Projects/Project_Notes_Python/program/db/Notebook.json", self.notes)
        sss.write()

    def read(self):
        rrr = Reading("C:/Users/PMPav/Desktop/Projects/Project_Notes_Python/program/db/Notebook.json", self.notes)
        self.notes = rrr.read()

    def sort(self, user_choice):
        data_list = []

        for item in self.notes:
            list_item = str(item).split(";")

            data = {"Заголовок": list_item[0], "Содержание записи": list_item[1], "Дата создания": list_item[2],
                             "Дата изменения": list_item[3]}
            data_list.append(data)

        if user_choice == 1:
            stocks = sorted(data_list, key=lambda x: datetime.strptime(x["Дата создания"], '%d.%m.%Y %H:%M'),
                            reverse=False)
        else:
            stocks = sorted(data_list, key=lambda x: datetime.strptime(x["Дата изменения"], '%d.%m.%Y %H:%M'),
                            reverse=False)

        number = 1
        for i in stocks:
            list_i = str(i).replace('{', '').replace('}', '').replace("'","")
            print(str(number) + ') ' + list_i)
            number += 1




