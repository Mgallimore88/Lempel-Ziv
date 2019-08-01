from encode import encode
from decoding import decode


message = "aaa!bjklb"
encoded_message = encode(message)
print(f"Encoded message:{encoded_message}")
decoded_message = decode(encoded_message)
print(decoded_message)
