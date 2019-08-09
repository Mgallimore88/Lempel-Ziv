class Encoder:
    def __init__(self, input_message, EOF_symbol="!"):
        self.input_message = input_message
        self.encoded_message = []
        self.dictionary = {}
        self.index = 0
        self.dict_number = 0
        self.debug = False
        self.is_finished = False
        self.current_word = self.input_message[self.index]

    def encode(self):

        while True:  # Loop until end of message
            self.next_letter = self.input_message[self.index + 1]
            self.check_for_end()
            if self.is_finished:
                self.encoded_message.append(self.current_word)
                break

            if str(self.current_word) not in self.dictionary:
                #  current word not encountered before:
                self.encoded_message.append(self.current_word)
                # current_word added to output string
                self.dictionary[self.current_word] = self.dict_number
                # current_word added to dictionary
                self.dict_number += 1
                self.check_for_end()
                if self.is_finished:
                    break
                self.index += 1
                self.current_word = self.input_message[self.index]

            elif (self.current_word + self.next_letter) in self.dictionary:
                # Current word encountered before:
                # add next letter to current word and start again
                self.current_word += self.next_letter
                self.index += 1
                self.check_for_end()
                if self.is_finished:
                    self.encoded_message.append(self.current_word)
                    break

            else:
                # Adding next letter to current word makes a new word.
                dict_KEY = self.dictionary.get(self.current_word)
                # Write current word's dict KEY + next letter to output.
                self.encoded_message.append(str(dict_KEY) + self.next_letter)
                # Add current word + next letter to dictionary.
                self.dictionary[self.current_word + self.next_letter] = self.dict_number
                self.dict_number += 1
                self.check_for_end(2)  # next unparsed letter is n + 2
                if self.is_finished:
                    break
                self.index += 2
                self.current_word = self.input_message[self.index]

        print(f"Final dictionary {self.dictionary}")
        return "".join(self.encoded_message)

    def check_for_end(self, index_increment=1):
        if self.input_message[self.index + index_increment] == "!":
            self.is_finished = True

        self.print_status() # Debug

    def print_status(self):
        if self.debug is True:
            print("***")
            print(f"index = {self.index}")
            print(f"encoded message = {self.encoded_message}")
            print(f"current dictionary = {self.dictionary}")
            print(f"current word = {self.current_word}")
            print(f"next letter = {self.next_letter}")
