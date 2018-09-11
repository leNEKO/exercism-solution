# we could extend with more symbols here ex.: <> “” «»
SYMBOLS = {
    "braces": r'{}',
    "parentheses": r'()',
    "brackets": r'[]',
}


def is_paired(input_string):
    # init a list for recording open symbols
    r = []

    for c in input_string:
        for s, p in SYMBOLS.items():
            if c == p[0]:  # if match open symbol
                r.append(s)  # record the symbol
            elif c == p[1]:  # if match close symbol
                try:
                    if r.pop() != s:  # if close symbol not match last recorded
                        return False  # ex.: … {[ … }] …
                except:  # if no symbol have been recorded
                    return False  # ex.: … } …

    # if r is empty then all opened symbols where closed in right order
    return len(r) == 0  # True
