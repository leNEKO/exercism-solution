import inflect
P = inflect.engine()

FIRST = "On the # day of Christmas my true love gave to me"
# silly compression
VERSE = [
    "# Turtle Doves",
    "# French Hens",
    "# Call_ Birds",
    "# Gold R_s",
    "# Geese-a-Lay_",
    "# Swans-a-Swimm_",
    "# Maids-a-Milk_",
    "# Ladies Danc_",
    "# Lords-a-Leap_",
    "# Pip% Pip_",
    "# Drumm% Drumm_",
]
END = "a Partridge in a Pear Tree."


def recite(s, e):
    a = []
    for u in range(s, e+1):
        r = [("and " if u > 1 else "") + END]
        for i in range(u-1):
            p = VERSE[i]
            n = P.number_to_words(i+2)
            r.append(p.replace("#", n).replace(
                "_", "ing").replace("%", "ers"))

        c = P.ordinal(P.number_to_words(u))
        r.append(FIRST.replace("#", c))
        a.append(", ".join(r[::-1]))
    return a
