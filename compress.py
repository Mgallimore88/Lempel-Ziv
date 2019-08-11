#! /usr/bin/python3

from encoding import encode
import sys


def compress():

    message = sys.stdin.buffer.read()
    print(f"length before compression : {len(message)}", file=sys.stderr)
    buffer_length = len(message.decode())
    print(f"buffer_length = {buffer_length}", file=sys.stderr)
    compressed_buff = encode(message, buffer_length)
    print(f"length after compression : {len(compressed_buff)}", file=sys.stderr)


if __name__ == "__main__":
    compress()
