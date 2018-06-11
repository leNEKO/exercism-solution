import calendar
from datetime import date, timedelta


def days_by_name(year, month, day_of_the_week):
    d = date(year, month, 1)
    dwd = list(calendar.day_name).index(day_of_the_week)

    d += timedelta(days=(dwd - d.weekday()) % 7)
    while (d.year, d.month) == (year, month):
        yield d
        d += timedelta(7)


def meetup_day(year, month, day_of_the_week, which):
    days = list(days_by_name(year, month, day_of_the_week))

    try:
        if which[0].isdigit():
            return days[int(which[0])-1]
        else:
            return {
                "last": days[-1],
                "teenth": list(filter(lambda x: 13 <= x.day <= 19, days))[0]
            }[which]
    except:
        raise MeetupDayException("Ça pas marche")


class MeetupDayException(Exception):
    pass
