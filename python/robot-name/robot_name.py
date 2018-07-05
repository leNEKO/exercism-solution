import random


PADASCII = 2
PADDIGIT = 3

DIGITS = "0123456789"
ASCIIS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

MAX = len(ASCIIS) ** PADASCII * len(DIGITS) ** PADDIGIT

# lame pseudo random (LPR)
ASCIIS = "".join(random.sample(ASCIIS, len(ASCIIS)))
DIGITS = "".join(random.sample(DIGITS, len(DIGITS)))
CURRENT = random.randint(0, MAX)
STEP = MAX // 3


def baseN(num, b, numerals):
    return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])


def decToWhatever(num, pad, numerals):
    return str(baseN(num, len(numerals), numerals)).rjust(pad, numerals[0])


def numToName(num):
    alpha, digit = divmod(num, 10 ** PADDIGIT)
    return decToWhatever(alpha, PADASCII, ASCIIS) + decToWhatever(digit, PADDIGIT, DIGITS)


class Robot(object):
    def __init__(self):
        self.setName()

    def setName(self):
        global CURRENT, STEP, MAX
        self.name = numToName(CURRENT)
        # LPR
        CURRENT = (CURRENT + STEP) % MAX

    def getName(self):
        return self.name

    def reset(self):
        self.setName()
