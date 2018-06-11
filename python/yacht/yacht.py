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
    simple_cat = [
        "ones",
        "twos",
        "threes",
        "fours",
        "fives",
        "sixes",
    ]

    myscore = {
        "yacht": 0,
        "ones": 0,
        "twos": 0,
        "threes": 0,
        "fours": 0,
        "fives": 0,
        "sixes": 0,
        "full_house": 0,
        "four_of_a_kind": 0,
        "little_straight": 0,
        "big_straight": 0,
        "choice": 0,
    }

    dice = sorted(dice)
    counter = defaultdict(int)
    for val in dice:
        counter[val] += 1

    # choice
    myscore["choice"] = sum(dice)

    # full house
    if 3 in counter.values() and 2 in counter.values():
        myscore["full_house"] = sum(dice)

    # straights
    if dice == [1, 2, 3, 4, 5]:
        myscore["little_straight"] = 30
    if dice == [2, 3, 4, 5, 6]:
        myscore["big_straight"] = 30

    # 4 of a kind, Yathces
    for k, qty in counter.items():
        varname = simple_cat[k-1]
        myscore[varname] = k * qty
        if qty >= 4:
            myscore["four_of_a_kind"] = k * 4
        if qty == 5:
            myscore["yacht"] = 50

    return myscore[category]
