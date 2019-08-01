class Encoder:
    def __init__(self, input_message, EOF_symbol="!"):
        self.input_message = input_message
        self.encoded_message = []
        self.dictionary = {}
        self.index = 0
        self.dict_number = 0
        self.debug = True

    def encode(self):
        #  do on receipt of message
        self.running = True
        self.current_word = self.input_message[self.index]

        while self.running:  # Loop until end of message
            self.next_letter = self.input_message[self.index + 1]
            self.print_status()
            self.check_for_end()
            if self.running is False:
                self.encoded_message.append(self.current_word)
                break

            #  current word not encountered before:
            if str(self.current_word) not in self.dictionary:
                self.encoded_message.append(self.current_word)
                print(f"{self.current_word} added to output string")
                self.dictionary[self.current_word] = self.dict_number
                print(f"{self.current_word} added to dictionary at {self.dict_number}")
                self.dict_number += 1
                self.check_for_end()
                if self.running is False:
                    break
                self.index += 1
                self.current_word = self.input_message[self.index]

            else:  # current word encountered before:
                #  check whether next letter makes a new word
                if (self.current_word + self.next_letter) in self.dictionary:
                    #  add next letter to current word and start again
                    print("Adding next letter to current word")
                    self.current_word += self.next_letter
                    print(f"Old word in dict. New word = {self.current_word}")
                    self.index += 1
                    self.check_for_end()
                    if self.running is False:
                        self.encoded_message.append(self.current_word)
                        break

                elif (self.current_word + self.next_letter) not in self.dictionary:
                    # Next letter makes a new word.
                    # Write current word's dict KEY + next letter to output.
                    # Add current word + next letter to dictionary.
                    # Reset current word.
                    print("adding next letter makes a new word")
                    dict_KEY = self.dictionary.get(self.current_word)
                    self.encoded_message.append(str(dict_KEY) + self.next_letter)
                    print(f"{str(dict_KEY) + self.next_letter} added to output string")
                    self.dictionary[
                        self.current_word + self.next_letter
                    ] = self.dict_number
                    self.dict_number += 1
                    self.check_for_end(2)  # next unparsed letter is n + 2
                    if self.running is False:
                        break
                    self.index += 2
                    self.current_word = self.input_message[self.index]

        print(f"Final dictionary {self.dictionary}")
        return ''.join(self.encoded_message)

    def check_for_end(self, index_increment=1):
        if self.input_message[self.index + index_increment] == "!":
            self.running = False

    def print_status(self):
        if self.debug is True:
            print("***")
            print(f"index = {self.index}")
            print(f"encoded message = {self.encoded_message}")
            print(f"current dictionary = {self.dictionary}")
            print(f"current word = {self.current_word}")
            print(f"next letter = {self.next_letter}")
