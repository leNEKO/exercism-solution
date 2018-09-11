def is_leap_year(year):
    mod4 = (year % 4) == 0
    mod100 = (year % 100) != 0
    mod400 = (year % 400) == 0
    is_leap = mod4 and (mod100 or mod400)
    return is_leap