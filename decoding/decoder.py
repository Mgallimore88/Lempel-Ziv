from .lempel_string_iterator import LempelStringIterator


class Decoder:
    def __init__(self, message):
        self.message = message.decode()
        self.string_iterator = LempelStringIterator(self.message)
        self.dictionary = {}
        self.dictionary_index = 0
        self.decoded_message = ''

    def decode(self):
        while self.string_iterator.has_next():
            number, character = self.string_iterator.next()

            if number is not None and character:
                decoded_message_component = self.dictionary[number] + character
                self.add_to_dictionary(decoded_message_component)
                self.add_to_decoded_message(decoded_message_component)
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
