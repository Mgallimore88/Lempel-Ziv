from tokenisable_string import TokenisableString


class Decoder:
    def __init__(self, message):
        self.message = message
        self.tokenisable_string = TokenisableString(self.message)
        self.dictionary = {}
        self.dictionary_index = 1
        self.decoded_message = ''

    def decode(self):
        while self.tokenisable_string.has_next():
            number, character = self.tokenisable_string.next()
            if number and character:
                decoded_token = self.dictionary[number] + character
                self.add_to_dictionary(decoded_token)
                self.add_to_decoded_message(decoded_token)
            elif character:
                self.add_to_dictionary(character)
                self.add_to_decoded_message(character)
            elif number:
                self.add_to_decoded_message(self.dictionary[number])

        return self.decoded_message

    def add_to_dictionary(self, string):
        self.dictionary[self.dictionary_index] = string
        self.dictionary_index += 1

    def add_to_decoded_message(self, string):
        self.decoded_message += string
