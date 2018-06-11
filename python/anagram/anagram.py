def detect_anagrams(word: str, candidates: list) -> list:
    ''' less dumb way to do this :) '''
    anagrams: list = []
    ws = sorted(list(word.lower()))
    for c in candidates:
        cs = sorted(list(c.lower()))
        print(cs, ws)
        if (cs == ws) and (c.lower() != word.lower()):
            anagrams.append(c)

    return anagrams
