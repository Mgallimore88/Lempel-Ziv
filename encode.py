from encoder import Encoder

def encode(message):
    encoder = Encoder(message)
    return encoder.encode()
