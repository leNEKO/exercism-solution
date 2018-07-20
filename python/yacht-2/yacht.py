from collections import defaultdict

# Score categories
# Change the values as you see fit

YACHT = "yacht"
ONES = "ones"
TWOS = "twos"
THREES = "threes"
FOURS = "fours"
FIVES = "fives"
SIXES = "sixes"
FULL_HOUSE = "full_house"
FOUR_OF_A_KIND = "four_of_a_kind"
LITTLE_STRAIGHT = "little_straight"
BIG_STRAIGHT = "big_straight"
CHOICE = "choice"


def score(dice, category):
    myscore = defaultdict(int)
    counter = defaultdict(int)

    dice = sorted(dice)

    for val in dice:
        counter[val] += 1
    # counter = (val in dice)

    # choice
    myscore["choice"] = sum(dice)

    # full house
    if all(v in counter.values() for v in [2, 3]):
        myscore["full_house"] = sum(dice)

    # straights
    if dice == [1, 2, 3, 4, 5]:
        myscore["little_straight"] = 30
    if dice == [2, 3, 4, 5, 6]:
        myscore["big_straight"] = 30

    # 4 of a kind, Yatches
    simple_cat = ["ones", "twos", "threes", "fours", "fives", "sixes", ]
    for k, qty in counter.items():
        varname = simple_cat[k-1]
        myscore[varname] = k * qty
        if qty >= 4:
            myscore["four_of_a_kind"] = k * 4
        if qty == 5:
            myscore["yacht"] = 50

    return myscore[category]
