import io
import json


class Writing:

    def __init__(self, path: str, notes: list):
        self.path = path
        self.notes = notes

    def write(self):
        data = {}
        number = 1

        for item in self.notes:
            # new_list = []
            str_item = str(item).split(";")
            # new_list.append(str_item)
            id_note = "Запись №" + str(number)
            data[id_note] = {"Заголовок": str_item[0], "Содержание записи": str_item[1], "Дата создания": str_item[2],
                             "Дата изменения": str_item[3]}
            number += 1

            with io.open(self.path, "w", encoding='UTF-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

# for el in new_list:
#     id_note = "Запись №" + str(number)
#     data[id_note] = {"Заголовок": el[0], "Содержание записи": el[1], "Дата создания": el[2],
#                      "Дата изменения": el[3]}
#     number += 1