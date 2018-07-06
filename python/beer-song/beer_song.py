def recite(start, take=1):
    verses = []
    for i in range(take):
        k = start - i
        v = verse(k)
        verses += v + [""]
    return verses[0:-1]


def verse(i):
    verse = [
        "{b} on the wall, {b}.".format(b=bottles(i)).capitalize(),
        "{t}, {b} on the wall.".format(t=take(i), b=bottles(i-1)).capitalize(),
    ]
    return verse


def bottles(i):
    i = i if i >= 0 else 99
    return "{q} bottle{s} of beer".format(
        q=i or "no more",
        s="s" if (i > 1) or (i == 0) else ""
    )


def take(i):
    if i > 0:
        return "take {q} down and pass it around".format(
            q="one" if i > 1 else "it"
        )
    else:
        return "go to the store and buy some more"
