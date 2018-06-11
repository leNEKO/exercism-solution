import string


def is_pangram(sentence):
    bingo = set(string.ascii_lowercase)
    for char in sentence.lower():
        if char in bingo:
            bingo.remove(char)
        if len(bingo) == 0:
            print("BINGO!")
            return True
    return False
