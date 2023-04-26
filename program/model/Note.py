class Note:

    def __init__(self, header, text, date_note_was_created):
        self.header = header
        self.text = text
        self.date_note_was_created = date_note_was_created

    def __repr__(self):
        return self.header + "; " + self.text + "; " + self.date_note_was_created

