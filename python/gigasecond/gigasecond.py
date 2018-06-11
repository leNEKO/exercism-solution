import datetime


def add_gigasecond(birth_date):
    gigaseconds = datetime.timedelta(seconds=10**9)
    gigaday = birth_date + gigaseconds
    return gigaday
