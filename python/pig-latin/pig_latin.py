import re

VOYELLE = "aeiouy"
CONSONNE = "bcdfghjklmnpqrstvwxz"


def translate(text):
    # rules 2+3+4
    pattern = "^(squ|qu|y|[" + CONSONNE + "]+)([" + VOYELLE + "].*)$"
    words = []
    for word in text.split(" "):
        mc = re.search(pattern, word)
        if mc and not re.search(r"ay$", word):
            pig_word = mc.group(2) + mc.group(1) + "ay"
        else:
            # rules 1
            pig_word = word + "ay"
        words.append(pig_word)
    return " ".join(words)
