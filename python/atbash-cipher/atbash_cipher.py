from string import ascii_lowercase

ABC = ascii_lowercase
ZYX = ABC[::-1]


def encode(plain_text):
    encoded = ""
    for c in plain_text:
        clow = c.lower()
        try:
            k = ABC.index(clow)
            nc = ZYX[k]
        except:
            if str(c).isdigit():
                nc = c
            else:
                nc = ""
        encoded += nc
    encoded = " ".join(encoded[i:i+5] for i in range(0, len(encoded), 5))
    return encoded


def decode(ciphered_text):
    decoded = ""
    for c in ciphered_text:
        clow = c.lower()
        try:
            k = ZYX.index(clow)
            nc = ABC[k]
        except:
            if str(c).isdigit():
                nc = c
            else:
                nc = ""
        decoded += nc
    return decoded
