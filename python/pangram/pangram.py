import string


def is_pangram(sentence):
    bingo = set(string.ascii_lowercase)
    for char in sentence.lower():
        if char in bingo:
            bingo.remove(char)
        if len(bingo) == 0:
            # print("BINGO!")
            return True
    return False


def is_pangram_malaca(sentence):
    return all(char in sentence.lower() for char in string.ascii_lowercase)


def main():
    from timeit import timeit
    s = "abcdefghijklmnopqrstuvwxyz"
    for f in ("is_pangram", "is_pangram_malaca"):
        setup = f"from __main__ import {f}"
        cmd = f'{f}("{s}")'
        print(cmd)
        r = timeit(cmd, number=10000, setup=setup)
        print(f, r)


if __name__ == '__main__':
    main()
