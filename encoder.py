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

                    
                    
                    
            
            

                
            self.output_message.append(current_word)
            self.iterable_message.pop(0)
            self.index = 0
        while : 
            self.current_word = self.iterable_message[index]
            while self.finished is False:
                self.current_word.append(self.iterable_message[index])
                #  loop through this whilst rest of message is being sent
                K = self.iterable_message[index + 1]

                if self.current_word + K in dictionary:
                    self.current_word.append(K)
                    self.index += 1

                    




        else:
            #  iterate to end of message
            current_wor
            if str(current_word + k)


    




    encode_this_word()

    return encoded_message



def encode_this_word():
        for i in message:

    if current_word + K is not in dictionary:
        current_word.append(K)


def iterate():
    i = i + 1


