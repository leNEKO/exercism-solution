import re


def pingpong(i, rails):  # ping pong modulo
    spec = rails - 1
    return abs((i+rails - 1) % ((spec * 2)) - spec)


def encode(message, rails):
    r = [[] for i in range(rails)]  # init rails

    for i, c in enumerate(re.sub("\W", "", message)):
        k = pingpong(i, rails)
        r[k].append(c)

    return re.sub("\W", "", "".join([item for sublist in r for item in sublist]))


def decode(m, rails):
    r = [[] for i in range(rails)]  # init rails

    # init zigzag
    for i, _ in enumerate(m):
        k = pingpong(i, rails)
        r[k].append(".")

    # fill the zigzag
    m_gen = (c for c in m)
    for y, row in enumerate(r):
        for x, _ in enumerate(row):
            c = next(m_gen)
            r[y][x] = c

    # read the zigzag
    decoded = ""
    for k, _ in enumerate(m):
        kr = pingpong(k, rails)
        decoded += r[kr][0]
        r[kr] = r[kr][1:]

    return decoded
