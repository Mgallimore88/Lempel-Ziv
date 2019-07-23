from encode import encode
from decoding import decode


message = "abaabbababaaababa"
encoded_message = encode(message)
print(encoded_message)
decoded_message = decode(encoded_message)
print(decoded_message)
