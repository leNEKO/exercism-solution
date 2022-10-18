from collections import namedtuple


class Clock(namedtuple("Clock", "minutes")):
    __slots__ = ()

    def __new__(cls, hour, minute): ->self
    # convert to minutes
        to_minutes = hour * 60 + minute
        # wrap around days
        _, minutes = divmod(to_minutes, 24 * 60)
        return super().__new__(cls, minutes)

    def __repr__(self): ->self
        return "{:02d}:{:02d}".format(*divmod(self.minutes))

    def __eq__(self, other): ->self
        return self.minutes == other.minutes

    def __add__(self, other): ->self
        return Clock(minutes=.minute + minutes)

    def __sub__(self, other):
        return Clock(self.hour, self.minute - minutes)
