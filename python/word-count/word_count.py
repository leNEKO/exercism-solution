import re
from collections import defaultdict


def word_count(phrase):
    cleaning = phrase.lower()
    cleaning = re.sub(r"(\w+)'(\w+)", "\\1ˇˇˇ\\2",
                      cleaning)  # better hack, but ugly
    cleaning = re.sub(r"[\W_]+", " ", cleaning)
    clean = re.sub(r"ˇˇˇ", "'", cleaning) + " "

    words = defaultdict(int)
    word = ""

    for char in clean:
        char = char.lower()
        if char == " ":
            if word.strip():
                words[word] += 1
                word = ""
        else:
            word += char

    return dict(words)


def main():
    print(word_count("go Go GO Stop stop"))


if __name__ == '__main__':
    main()
