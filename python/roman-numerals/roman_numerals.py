def numeral(number):
    return RomanNumerals.to_roman(number)


class RomanNumerals:
    SYSTEM = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    @classmethod
    def to_roman(cls, i):
        roman = ""

        for val, k in cls.SYSTEM:
            while(i - val) >= 0:
                roman += k
                i -= val

        return roman

    @classmethod
    def from_roman(cls, s):
        i = 0
        for val, k in cls.SYSTEM[::-1]:
            l = len(k)
            while True:
                if s[-l:] == k:
                    i += val
                    s = s[:-l]
                else:
                    break
        return i


def main():
    for i in range(99):
        r = RomanNumerals.to_roman(i)
        ri = RomanNumerals.from_roman(r)
        print(i, r, ri)


if __name__ == '__main__':
    main()
