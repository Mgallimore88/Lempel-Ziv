from encode import encode
from decoding import decode


message = "Compresses text with spacessssssssssssssssssssssssssssssssssss!"
encoded_message = encode(message)
print(f"Encoded: {encoded_message}")
decoded_message = decode(encoded_message)
print(f"decoded: {decoded_message}")
