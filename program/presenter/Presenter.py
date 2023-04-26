class Presenter:

    def __init__(self, console, model):
        self.console1 = console
        self.model1 = model
        self.console1.set_presenter(self)

    def add_note1(self, header, text):
        self.model1.add_note(header, text)

    def print1(self):
        self.model1.print()

    def del_note(self, index):
        self.model1.del_note(index)

    def search_note(self, search_word):
        self.model1.search_note(search_word)

    def change_note(self, index, new_header, new_text):
        self.model1.change_note(index, new_header, new_text)

    def sampling_by_date(self, our_date):
        self.model1.sampling_by_date(our_date)

    def save(self):
        self.model1.save()

    def read(self):
        self.model1.read()

    def sort(self):
        self.model1.sort()
