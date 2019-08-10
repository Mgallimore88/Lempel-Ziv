from encoder import Encoder
EOF_symbol = "\4"


def encode(message):
    encoder = Encoder(message + EOF_symbol)
    return encoder.encode()
