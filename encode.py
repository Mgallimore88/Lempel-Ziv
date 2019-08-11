from encoder import Encoder


EOF_symbol = "not used"


def encode(message, buffer_length):
    encoder = Encoder(message, buffer_length)
    return encoder.encode()
