from collections import deque

ACTIONS = [
    (0b10000, "REVERSE"),
    (0b01000, "jump"),
    (0b00100, "close your eyes"),
    (0b00010, "double blink"),
    (0b00001, "wink")
]


def handshake(code):
    l = deque()
    reverse = False
    for action in ACTIONS:
        i, a = action
        while (code - i) >= 0:
            if a == "REVERSE":
                reverse = not reverse
            else:
                if(reverse):
                    l.append(a)
                else:
                    l.appendleft(a)
            code -= i
    return list(l)


def secret_code(actions):
    # actions to values
    m = dict()
    for action in ACTIONS:
        i, a = action
        m.update({a: i})

    code = 0
    last = 0
    for a in actions:
        reverse = m[a] < last  # check if reversed
        last = m[a]
        code += m[a]
    code += m["REVERSE"] if reverse else 0
    return code


def main():
    print(secret_code(['jump', 'double blink']))


if __name__ == '__main__':
    main()
