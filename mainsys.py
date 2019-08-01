from encode import encode
from decode import decode
from sys import stdin as input, stdout as output

message = "ahhhhhhhhhhhhh!!"

output.write(encode(input.read()))

print(f"Encoded message:{encoded_message}")
decoded_message = decode(encoded_message)
print(decoded_message)
