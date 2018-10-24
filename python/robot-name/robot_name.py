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
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
          41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
r = [i for i in range(1, 100) if (MAX % (MAX // i))
     in primes]

STEP = MAX // random.choice(r)


def nextId():
    global CURRENT
    value = CURRENT
    CURRENT = (CURRENT + STEP) % MAX
    return value


def baseN(num, numerals):  # decimal num into custom base integer
    return ((num == 0) and numerals[0]) or (baseN(num // len(numerals), numerals).lstrip(numerals[0]) + numerals[num % len(numerals)])


def paddedBaseN(num, pad, numerals):  # right padded custom integer
    return str(baseN(num, numerals)).rjust(pad, numerals[0])


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
    print(paddedBaseN(30, 2, "ABCD"))
    # check if all robots can be created
    # total = len(set([nextId() for _ in range(MAX)]))
    # assert(
    #     total == MAX), f":O collision happened {total} / {MAX}"
    # # randomness sample
    # print([Robot().name for _ in range(100)])


if __name__ == '__main__':
    main()
