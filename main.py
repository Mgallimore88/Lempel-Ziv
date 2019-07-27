from encode import encode
from decode import decode


message = "abaabbababaaababa!"
encoded_message = encode(message)
print(encoded_message)
decoded_message = decode(encoded_message)
print(decoded_message)
