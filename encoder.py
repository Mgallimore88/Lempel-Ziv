class Encoder:
    def __init__(self, input_message):
        self.input_message = input_message
        self.rest_of_string = input_message
        self.iterable_input = []
        self.encoded_message = []
        self.current_word = []
        self.dictionary = {}
        self.index = 0
        self.dict_number = 0
        #  turn message string into an iterable list this too long for black formatter autopep8
        for letter in self.input_message:
            self.iterable_input.append(letter)

    def encode(self):
        # do on receipt of message
        self.running = True
        self.current_word.append(self.iterable_input[self.index])
        # Loop through this until end of message
        while(self.running):
            print(self.current_word)
            #  K = next letter
            K = self.iterable_input[self.index + 1]
            if K == "!":
                self.running = False
            if (self.current_word) not in self.dictionary:
                #  case for single letter not in dict:
                self.encoded_message.append(self.current_word)
                self.dictionary[self.dict_number] = (self.current_word)
                self.dict_number += 1
                self.index += 1
            if (self.current_word) in self.dictionary:
                #  check whether next letter makes a new word
                if (self.current_word + K) in self.dictionary:
                    #  add next letter to current word and start again
                    self.current_word.append(K)
                    index += 1
                elif str(self.current_word + K) not in self.dictionary:
                    #  case for new word encountered
                    #  Add to dict, output corresponding dict CODE + K
                    dict_KEY = self.dictionary.get((self.current_word))
                    self.encoded_message.append(dict_KEY + K)
                    self.dictionary[dict_number] = (self.current_word + K)
                    self.dict_number += 1
                    index += 1
                



        return self.encoded_message
