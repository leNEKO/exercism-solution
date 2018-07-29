import re
import math


def encode(plain_text):
    # remove all but alpha symbols and make it lower case
    flat = re.sub(r"[\W]", "", plain_text.lower())
    if flat == "":  # if empty
        return ""

    size = len(flat)
    sq = math.ceil(size ** .5)
    c = sq
    r = math.ceil(size / c)

    flat = flat.ljust(c*r)
    return " ".join([''.join(flat[i::c]) for i in range(c)])
