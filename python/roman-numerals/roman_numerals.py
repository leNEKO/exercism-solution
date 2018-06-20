<<<<<<< HEAD
#  litteral translation of my php solution
def numeral(number):
    system = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I",
    }

    roman = ""

    for val, k in system.items():
        while(number - val) >= 0:
            roman += k
            number -= val

    return roman
=======
def numeral(number):
    pass
>>>>>>> 5c4e5fe1434ee93824e05fb37c28789faf19f46c
