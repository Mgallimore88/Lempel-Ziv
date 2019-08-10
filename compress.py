#! /usr/bin/python3

from encode import encode
import sys

def compress():
    message = sys.stdin.buffer.read()
    encoded_message = encode(message)
    sys.stdout.buffer.write(encoded_message)

if __name__ == "__main__":
    compress()
