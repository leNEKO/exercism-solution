SUBLIST = "sublist"
EQUAL = "equal"
SUPERLIST = "superlist"
UNEQUAL = "unequal"


def check_lists(first_list, second_list):
    fl = "_".join(str(x) for x in first_list)
    sl = "_".join(str(x) for x in second_list)

    if fl == sl:
        return EQUAL
    elif fl.find(sl) != -1:
        return SUPERLIST
    elif sl.find(fl) != -1:
        return SUBLIST

    return UNEQUAL
