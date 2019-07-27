class Encoder:
    def __init__(self, input_message):
        self.input_message = input_message
        self.rest_of_string = input_message
        self.iterable_message = []
        self.current_word = []
        self.dictionary = {}
        self.first_time = True
        self.index = 0
        self.dict_number = 0


        #  turn message string into an iterable list
        for letter in message:
            self.iterable_message.append[letter]
        
    def encode(self.iterable_message):
        self.running = True
        # do on receipt of message
        self.current_word.append(self.iterable_message[self.index])
        while(self.running):
            K = self.iterable_message[self.index + 1]
            if str(self.current_word) in self.dictionary:
                #  check whether next letter makes a unique word
                if str(self.current_word + K) in self.dictionary):
                    #  add next letter to current word and start again
                    self.current_word.append(K)
                    index += 1
                else if str(self.current_word + K) not in self.dictionary):
                    #  case for new word encountered
                    #  Add to dict, output corresponding dict CODE + K
                    dict_CODE = self.dictionary.get()                  
                    self.dictionary[dict_number] = str(current_word+ K)]
                    self.dict_number += 1

                    




    return encoded_message

