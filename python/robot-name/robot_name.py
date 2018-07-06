import random

# robot name format config AADDD
ASCIIS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
PADASCII = 2
DIGITS = "0123456789"
PADDIGIT = 3

# max robots
MAX = (len(ASCIIS) ** PADASCII * len(DIGITS) ** PADDIGIT)

# Lame PseudoRandom Generator (LPG)
INIT = random.randint(0, MAX)  # start at random position
CURRENT = INIT
# random step
STEP = MAX // random.choice([i for i in range(1, 100) if (MAX % (MAX // i))
                             in [3, 5, 7, 11, 13, 17, 19, 23]])


def nextId():
    global CURRENT
    value = CURRENT
    CURRENT = (CURRENT + STEP) % MAX
    return value


def baseN(num, b, numerals):  # decimal num into custom base integer
    return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])


def paddedBaseN(num, pad, numerals):  # right padded custom integer
    return str(baseN(num, len(numerals), numerals)).rjust(pad, numerals[0])


class Robot(object):
    def __init__(self):
        self.setName()

    def setName(self):
        # format AADDD
        alpha, digit = divmod(nextId(), 10 ** PADDIGIT)
        self.name = paddedBaseN(alpha, PADASCII, ASCIIS) + \
            paddedBaseN(digit, PADDIGIT, DIGITS)

    def reset(self):
        self.setName()


def main():
    # check if all robots can be created
    total = len(set([nextId() for _ in range(MAX)]))
    assert(
        total == MAX), f":O collision happened {total} / {MAX}"
    # randomness sample
    print([Robot().name for _ in range(100)])


if __name__ == '__main__':
    main()
