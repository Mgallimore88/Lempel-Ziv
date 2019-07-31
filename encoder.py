class Encoder:
    def __init__(self, input_message):
        self.input_message = input_message
        self.rest_of_string = input_message
        self.iterable_input = []
        self.encoded_message_ = []
        self.current_word = []
        self.dictionary = {}
        self.index = 0
        self.dict_number = 0
        #  turn message string into an iterable list
        for letter in self.input_message:
            self.iterable_input.append(letter)

    def encode(self):
        #  do on receipt of message
        self.running = True
        self.current_word.append(self.iterable_input[self.index])
        #  Loop through this until end of message
        while self.running:
            print(self.current_word)
            #  K = next letter
            K = self.iterable_input[self.index + 1]
            if K == "!":
                self.running = False
            if (self.current_word[0]) not in self.dictionary:
                #  case for single letter not in dict:
                self.encoded_message_.append(self.current_word)
                print(f"{self.current_word} added to output string")
                self.dictionary[self.current_word[0]] = self.dict_number
                self.dict_number += 1
                self.index += 1
                self.current_word = self.iterable_input[self.index]
            else:  #  self.current_word[0] in self.dictionary:
                #  check whether next letter makes a new word
                if (self.current_word[0] + K) in self.dictionary:
                    print("adding next letter to current word")
                    #  add next letter to current word and start again
                    self.current_word[0].append(K)
                    print(f"old word in dict. new word = {self.current_word}")
                    self.index += 1
                elif (self.current_word[0] + K) not in self.dictionary:
                    print("found a new word")
                    #  case for new word encountered
                    #  Add to dict, output corresponding dict CODE + K, reset curent word
                    dict_KEY = self.dictionary.get((self.current_word[0]))
                    self.encoded_message_.append(str(dict_KEY) + str(K))
                    print(f"{str(dict_KEY) + str(K)} added to output string")
                    self.dictionary[self.current_word[0] + K] = self.dict_number
                    self.dict_number += 1
                    self.index += 1
                    self.current_word = self.iterable_input[self.index]
                    print(f"new dictionary = {self.dictionary}")
        print(f"FINAL dictionary {self.dictionary}")
        return self.encoded_message_
        
