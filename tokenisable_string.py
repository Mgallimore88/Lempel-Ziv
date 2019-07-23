import re


class TokenisableString:
    def __init__(self, string):
        self.string = string
        self.index = 0
        self.length = len(string)

    def has_next(self):
        return self.index < self.length

    def next(self):
        if re.match("[a-zA-Z]", self.string[self.index]):
            char = self.string[self.index]
            self.index += 1
            return char

        number = ''
        while self.has_next() and re.match("[0-9]", self.string[self.index]):
            number += self.string[self.index]
            self.index += 1

        if self.has_next():
            token = number + self.string[self.index]
            self.index += 1
            return token
        else:
            return number
