def is_isogram(string):
    chars = set()
    for char in string.lower():
        if char in chars:
            return False
        elif char.isalnum():
            chars.add(char)
    return True
