from datetime import datetime
from program.model.Note import Note
from program.model.Reading import Reading
from program.model.Writing import Writing


class Model:

    def __init__(self):
        self.notes = []

    def add_note(self, header, text):
        note = Note(header, text, datetime.today().strftime('%d.%m.%Y %H:%M'))
        self.notes.append(note)

    def print(self):
        # print(self.notes)
        for i in self.notes:
            print(i)

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

    def change_note(self, index, new_note):
        self.notes[index-1] = new_note

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

    def sort(self):
        print(self.notes[0][0])