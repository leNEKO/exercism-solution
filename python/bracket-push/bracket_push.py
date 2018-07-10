SYMBOLS = {
    "braces": r'{}',
    "parentheses": r'()',
    "brackets": r'[]',
}


def is_paired(input_string):
    print(input_string)
    r = []

    for c in input_string:
        for s, p in SYMBOLS.items():
            if c == p[0]:
                r.append(s)
            elif c == p[1]:
                try:
                    if r.pop() != s:
                        return False
                except:
                    return False

    return len(r) == 0
