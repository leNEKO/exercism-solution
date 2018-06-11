import string


def rotate(text, key):
    ''' done fast, sure there is clever way to factorised this '''
    ascii = string.ascii_lowercase
    rotated = ""
    for c in text:
        clow = c.lower()
        try:
            k = ascii.index(clow)
            rk = (k + key) % len(ascii)
            nc = ascii[rk]
            if c.islower() is False:
                nc = nc.upper()
        except:
            nc = c
        rotated += nc
    return rotated
