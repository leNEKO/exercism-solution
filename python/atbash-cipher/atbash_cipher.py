from string import ascii_lowercase


def codec(text):
    encoded = ""
    ABC = ascii_lowercase
    ZYX = ascii_lowercase[::-1]
    for c in text.lower():
        try:
            k = ABC.index(c)
            nc = ZYX[k]
        except:
            if str(c).isdigit():
                nc = c
            else:
                nc = ""
        encoded += nc
    return encoded


def encode(plain_text):
    encoded = codec(plain_text)
    return " ".join(encoded[i:i+5] for i in range(0, len(encoded), 5))


def decode(ciphered_text):
    return codec(ciphered_text)
