from encode import encode
from decoding import decode


message = "Compres se s text  with many symbols !\"£$%^&*()¬`_-+={|}~[]#;',./:@<>?|\\ \n and newlines too!\n and dictionary entries over TEN. But there is a bug - \nfind it by deleting everthing from the end of this sentence \nall the way back to the capitalised number ten, \nand replace it with the number ten to see the bug."
encoded_message = encode(message)
print(f"Encoded: {encoded_message}")
decoded_message = decode(encoded_message)
print(f"decoded: {decoded_message}")
