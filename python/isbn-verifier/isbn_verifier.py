def verify(isbn):
    isbn = isbn.replace("-", "")

    if len(isbn) != 10:
        return False
        #raise Exception("Invalid ISBN 10 length")

    # check 9 first digits
    isbn_9 = isbn[0:9]
    mult = 10
    vals = []
    for char in isbn_9:
        if not char.isdigit():
            return False
            #raise Exception(f"Invalid Digit : {char}")
        else:
            val = int(char) * mult
            vals.append(val)
            mult -= 1

    # check the check
    isbn_check = isbn[-1]
    if isbn_check.upper() == "X":
        isbn_check = "10"
    if not isbn_check.isdigit():
        return False
        #raise Exception(f"Invalid check character: {isbn_check}")
    val = int(isbn_check) * mult
    vals.append(val)

    # check the sum
    checksum = sum(vals) % 11

    if checksum != 0:
        return False
        #raise Exception(f"Invalid checksum")

    return True
