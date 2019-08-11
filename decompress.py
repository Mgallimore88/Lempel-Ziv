#! /usr/bin/python3

from decoding import decode
import sys

def decompress():
    message = sys.stdin.buffer.read()
    print(f"Read_c: {len(message)}", file=sys.stderr)
    decompressed_message = decode(message)
    output_length = len(decompressed_message)
    print(f"decoded length {output_length}", file=sys.stderr)
    sys.stdout.write(decompressed_message)

if __name__ == "__main__":
    decompress()

