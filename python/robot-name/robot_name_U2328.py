from random import choice
import string

letters = string.ascii_uppercase
numbers = string.digits


class Robot(object):
    _occupied_names = [""]

    def __init__(self):
        self.reset()

    def reset(self):
        self.name = Robot.generate_new_name()

    @classmethod
    def generate_new_name(cls):
        name = ""
        while name in cls._occupied_names:
            name = (
                choice(letters)
                + choice(letters)
                + choice(numbers)
                + choice(numbers)
                + choice(numbers)
            )
        cls._occupied_names.append(name)
        return name


def main():
    # robot name format config AADDD
    ASCIIS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    PADASCII = 2
    DIGITS = "0123456789"
    PADDIGIT = 3

    # max robots
    MAX = (len(ASCIIS) ** PADASCII * len(DIGITS) ** PADDIGIT)

    for i in range(MAX):
        r = Robot()
        # print(i, r.name)


if __name__ == '__main__':
    main()
