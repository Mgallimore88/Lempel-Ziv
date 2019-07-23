from decoder import Decoder


def decode(message):
    decoder = Decoder(message)
    return decoder.decode()
