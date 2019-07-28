from encode import encode
from decode import decode


message = "bbaabbababaaababa!"
encoded_message = encode(message)
print(f"Encoded message:{encoded_message}")
decoded_message = decode(encoded_message)
print(decoded_message)
