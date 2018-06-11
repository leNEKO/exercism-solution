def decode(string):
    decoded = ""
    digit = ""

    for char in string:
        if char.isdigit():
            digit += char
        else:
            if not digit:
                digit = "1"
            qte = int(digit)
            digit = ""
            decoded += char * qte
    return decoded


def encode(string):
    encoded = ""

    last_char = ""
    counter = 1
    for char in string:
        if (char == last_char):
            counter += 1
        elif last_char != "":
            if counter > 1:
                encoded += str(counter)
            encoded += last_char
            counter = 1
        last_char = char
        print(char, counter)
    if counter > 1:
        encoded += str(counter)
    encoded += last_char

    return encoded
