#! /usr/bin/python3

from encode import encode
import sys

def compress():

    message = sys.stdin.buffer.read()
    print(f"Read: {len(message)}", file=sys.stderr)
    buffer_length = len(message.decode())
    print(f"buffer_length = {buffer_length}", file=sys.stderr)
    compressed_buff = encode(message, buffer_length)


if __name__ == "__main__":
    compress()
