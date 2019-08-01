class Encoder:
    def __init__(self, input_message, EOF_symbol='!'):
        self.input_message = input_message
        self.rest_of_string = input_message
        self.encoded_message_ = []
        self.current_word = []
        self.dictionary = {}
        self.index = 0
        self.dict_number = 0


    def encode(self):
        #  do on receipt of message
        self.running = True
        self.current_word = self.input_message[self.index]
        #  Loop through this until end of message
        while self.running:
            print("***")
            print(f"index = {self.index}")
            print(f"encoded message = {self.encoded_message_}")
            print(f"current dictionary = {self.dictionary}")
            print(f"current word = {self.current_word}")

            #  K = next letter
            K = self.input_message[self.index + 1]
            print(f'K = {K}')

            if str(self.current_word) not in self.dictionary:
                #  case for unique current word:
                self.encoded_message_.append(self.current_word)
                print(f"{self.current_word} added to output string")
                self.dictionary[self.current_word] = self.dict_number
                print(f"{self.current_word} added to dictionary at {self.dict_number}")
                self.dict_number += 1
                self.index += 1
                self.current_word = self.input_message[self.index]
                self.check_for_end()
                if self.running is False:
                    break

            else:  # current word encountered before:
                #  check whether next letter makes a new word
                if (self.current_word + K) in self.dictionary:
                    print("adding next letter to current word")
                    #  add next letter to current word and start again
                    self.current_word += K
                    print(f"old word in dict. new word = {self.current_word}")
                    self.index += 1
                elif (self.current_word + K) not in self.dictionary:
                    print("adding next letter makes a new word")
                    #  case for new word encountered
                    #  Add to dict, output corresponding dict CODE + K, reset current word
                    dict_KEY = self.dictionary.get(self.current_word)
                    self.encoded_message_.append(str(dict_KEY) + K)
                    print(f"{str(dict_KEY) + K} added to output string")
                    self.dictionary[self.current_word + K] = self.dict_number
                    self.dict_number += 1
                    #  increase index by 2 since new word is current + 1
                    #  so next unparsed letter is current + 2
                    self.check_for_end(2)
                    if self.running is False:
                        break
                    self.index += 2
                    self.current_word = self.input_message[self.index]
            
        return self.encoded_message_
        print(f"Final dictionary {self.dictionary}")

    def check_for_end(self, index_increment=1):
        if self.input_message[self.index + index_increment] == "!":
            self.running = False
        
            

