class Encoder:
    def __init__(self, input_message, buffer_length, EOF_symbol="\4"):
        self.input_message = input_message.decode()
        self.length = len(input_message)
        self.encoded_message = []
        self.dictionary = {}
        self.index = 0
        self.dict_number = 0
        self.debug = False
        self.current_word = self.input_message[self.index]
        self.dict_symbol = "\3"
        self.EOF_symbol = EOF_symbol
        self.buffer_length = buffer_length
        # print(f"encoder.buffer_length = {self.buffer_length}")

    def encode(self):

        while True:  # Loop until end of message
            self.next_letter = self.input_message[self.index + 1]
            if self.is_finished():
                self.encoded_message.append(self.current_word)
                break

            if str(self.current_word) not in self.dictionary:
                #  current word not encountered before:
                self.encoded_message.append(self.current_word)
                # current_word added to output string
                self.dictionary[self.current_word] = self.dict_number
                # current_word added to dictionary
                self.dict_number += 1
                if self.is_finished():
                    break
                self.index += 1
                self.current_word = self.input_message[self.index]

            elif (self.current_word + self.next_letter) in self.dictionary:
                # Current word encountered before:
                # add next letter to current word and start again
                self.current_word += self.next_letter
                self.index += 1
                if self.is_finished():
                    self.encoded_message.append(self.current_word)
                    break

            else:
                # Adding next letter to current word makes a new word.
                dict_KEY = self.dictionary.get(self.current_word)
                # Write current word's dict KEY + next letter to output.
                self.encoded_message.append(
                    self.dict_symbol + str(dict_KEY) + self.next_letter
                )
                # Add current word + next letter to dictionary.
                self.dictionary[self.current_word + self.next_letter] = self.dict_number
                self.dict_number += 1
                # next unparsed letter is n + 2
                if self.is_finished(2):
                    break
                self.index += 2
                self.current_word = self.input_message[self.index]
        print("".join(self.encoded_message))
        return "".join(self.encoded_message)


    def is_finished(self, index_increment=1, offset = 1):
        # print(f"finishing index {self.index}")
        return self.index + index_increment + offset >= self.buffer_length

        self.print_status()  # Debug

    def print_status(self):
        if self.debug is True:
            print("***")
            print(f"index = {self.index}")
            print(f"encoded message = {self.encoded_message}")
            print(f"current dictionary = {self.dictionary}")
            print(f"current word = {self.current_word}")
            print(f"next letter = {self.next_letter}")
