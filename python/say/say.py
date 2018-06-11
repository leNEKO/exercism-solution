from collections import defaultdict

SYSTEM = {
    10 ** 15: "#quadrillion",
    10 ** 12: "#trillion",
    10 ** 9: "#billion",
    10 ** 6: "#million",
    10 ** 3: "#thousand",
    10 ** 2: "#hundred",
    90: "ninety",
    80: "eighty",
    70: "seventy",
    60: "sixty",
    50: "fifty",
    40: "fourty",
    30: "thirty",
    20: "twenty",
    19: "nineteen",
    18: "eighteen",
    17: "seventeen",
    16: "sixteen",
    15: "fifteen",
    14: "fourteen",
    13: "thirteen",
    12: "twelve",
    11: "eleven",
    10: "ten",
    9: "nine",
    8: "eight",
    7: "seven",
    6: "six",
    5: "five",
    4: "four",
    3: "three",
    2: "two",
    1: "one",
}


def say(number):
    out = defaultdict(int)

    if number < 0:
        out["minus"] = 1

    number = abs(number)

    for i, name in SYSTEM.items():
        while (number - i) >= 0:
            out[name] += 1
            number -= i

    p = []

    for name, val in out.items():
        if val > 0 and name[0] == "#":
            p.append(say(val) + " " + name[1::] + ("s" if val > 1 else ""))
        else:
            p.append(name)

    return " ".join(p)


def main():

    for num in {0, 15, 50, 98, -1548, 100, 200}:
        print()
        print(f"{num}: ")
        print(say(num))

    # while True:
    #     number = int(input())
    #     print(say(number))


if __name__ == '__main__':
    main()
