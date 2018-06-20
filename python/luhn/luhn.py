class Luhn(object):
    def __init__(self, card_num):
        # normalizing input
        try:
            self.cn = [int(c) for c in card_num.replace(" ", "")][::-1]
        except ValueError:
            self.cn = [0]

    def is_valid(self):
        if len(self.cn) < 2:
            return False

        # sum of the doubles
        odds = sum(
            sum(divmod(i * 2, 10))
            for i in self.cn[1::2]
        )
        evens = sum(self.cn[0::2])

        return (odds + evens) % 10 == 0
