import re


class LempelStringIterator:
    def __init__(self, string):
        self.string = string
        self.index = 0
        self.length = len(string)

    def has_next(self):
        return self.index < self.length

    # Returns a tuple (number, character)
    def next(self):
        if re.match("[a-zA-Z\s]", self.string[self.index]):
            char = self.string[self.index]
            self.index += 1
            return None, char

        number = ''
        if self.has_next() and re.match("%", self.string[self.index]):
            self.index += 1
            while self.has_next() and re.match("0-9", self.string[self.index]):
                number += self.string[self.index]
                self.index += 1

        if self.has_next():
            char = self.string[self.index]
            self.index += 1
            return int(number), char
        else:
            return int(number), None
