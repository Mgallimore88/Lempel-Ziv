from tokenisable_string import TokenisableString


def decode(message):
    tokenisable_string = TokenisableString(message)
    while tokenisable_string.has_next():
        token = tokenisable_string.next()
        print(token)

    return message
