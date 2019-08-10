#! /usr/bin/python3

from decoding import decode
import sys

def decompress():
    message = sys.stdin.buffer.read()
    decoded_message = decode(message)
    sys.stdout.buffer.write(decoded_message)

if __name__ == "__main__":
    decompress()
