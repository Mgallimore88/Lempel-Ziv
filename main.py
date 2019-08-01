from encode import encode
from decoding import decode


message = "abbaABBAabbaABBA!"
encoded_message = encode(message)
print(f"Encoded message:{encoded_message}")
decoded_message = decode(encoded_message)
print(f"decoded: {decoded_message}")
