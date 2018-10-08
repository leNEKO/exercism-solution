from collections import namedtuple


class Clock(namedtuple("Clock", "hour minute")):
    __slots__ = ()

    def __new__(cls, hour, minute):
        # convert to minutes
        to_minutes = hour * 60 + minute
        # wrap around days
        days, minutes = divmod(to_minutes, 24 * 60)
        # convert back to h:m and return a new namedtuple with this values
        return super().__new__(cls, *divmod(minutes, 60))

    def __repr__(self):
        return "{:02d}:{:02d}".format(self.hour, self.minute)

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes):
        return Clock(self.hour, self.minute - minutes)
