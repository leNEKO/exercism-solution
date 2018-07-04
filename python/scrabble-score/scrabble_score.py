SCOREMAP = {
    "aeioulnrst": 1,
    "dg": 2,
    "bcmp": 3,
    "fhvwy": 4,
    "k": 5,
    "jx": 8,
    "qz": 10
}


def score(word):
    total = 0
    for c in word.lower():
        for ks, val in SCOREMAP.items():
            if c in ks:
                total += val
                break
    return total
