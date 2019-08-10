#! /usr/bin/python3

from encode import encode
from decode import decode
from sys import stdin as input, stdout as output

message = "Hello from inside mainsys"

output.write(encode(input.read()))
encoded_message = encode(message)
print(f"Encoded message: {encoded_message}")
decoded_message = decode(encoded_message)
print(f"Decoded message:{decoded_message}")
