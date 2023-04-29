import json


class Reading:

    def __init__(self, path, notes):
        self.path = path
        self. notes = notes

    def read(self):

        with open(self.path, encoding='UTF-8') as file:
            data = json.load(file)
            my_string = ""

            for key, value in data.items():
                for key2, value2 in value.items():
                    my_string += value2 + ";"
                my_string = my_string[:-1] + '/'
            my_string = my_string[:-1]

            self.notes = my_string.split('/')
        return self.notes
