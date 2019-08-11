from .encoder import Encoder


def encode(message, buffer_length):
    encoder = Encoder(message, buffer_length)
    return encoder.encode()
