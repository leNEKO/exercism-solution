from string import ascii_lowercase as ASCII
import random


class Cipher:
    def __init__(self, key: str=None):
        if key is None:
            key = "".join(random.choice(ASCII)
                          for _ in range(128))  # a default random key
        # check for invalid keys
        elif key == '' or sum(not (c.isalpha() and c.islower()) for c in key):
            raise ValueError("Bad key")
        self.key = key

    def codec(self, text: str, dir: int=1) -> str:
        encoded = ""
        for i, char in enumerate(text):
            k = self.key[i % len(self.key)]  # key char
            pos = ASCII.find(char)  # char position in ascii
            offset = ASCII.find(k)  # key char position "
            encoded += ASCII[(pos + offset * dir) % len(ASCII)]  # nu char
        return encoded

    def encode(self, text: str) -> str:
        return self.codec(text, 1)

    def decode(self, text: str) -> str:
        return self.codec(text, -1)
