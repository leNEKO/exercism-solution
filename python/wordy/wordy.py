import re


def calculate(q):
    # 1. patterns
    num = r"(-?\d+)"
    pats = [
        (f"^What is {num}", r"+_\1"),
        (f"plus {num}", r"+_\1"),
        (f"minus {num}", r"-_\1"),
        (f"multiplied by {num}", r"*_\1"),
        (f"divided by {num}", r"/_\1"),
        (f"raised to the {num}\w+ power/", r"**_\1"),
        ("\?$", ""),
    ]

    # 2. normalize
    for pat, repl in pats:
        q = re.sub(pat, repl, q)

    # 3. ???
    total = 0
    for do in q.split(" "):
        operator, val = do.split("_")
        val = int(val)
        total = {
            '+': lambda t: t + val,
            '-': lambda t: t - val,
            '*': lambda t: t * val,
            '/': lambda t: t / val,
            '**': lambda t: t ** val
        }[operator](total)

    # 4. Profit
    return total
