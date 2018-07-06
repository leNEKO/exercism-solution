import gc
import random


class Robot(object):
    def __init__(self):
        self.name = self.give_name()

    def give_name(self):
        if not hasattr(self, "name"):
            self.name = "AA000"
        chars = []
        digit = [("00" + str(i))[-3:] for i in range(1000)]
        for i in range(26):
            for k in range(26):
                chars.append(chr(i + 65) + chr(k + 65))
        for obj in gc.get_objects():
            if isinstance(obj, Robot):
                chars.remove(obj.name[:2])
                digit.remove(obj.name[2:])
        return chars[random.randrange(len(chars))] + digit[random.randrange(1000)]

    def reset(self):
        self.name = self.give_name()


# check if all robots can be created
MAX = 26**2*10**3
total = len(set([Robot().name for _ in range(MAX)]))
assert(
    total == MAX), f":O collision happened {total} / {MAX}"
# randomness sample
print([Robot().name for _ in range(100)])
