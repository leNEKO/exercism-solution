class Clock(object):
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute
        self.normalize()

    def __repr__(self):
        return "{:02d}:{:02d}".format(self.hour, self.minute)

    def __eq__(self, other):
        return self.__repr__() == other.__repr__()

    def __add__(self, minutes):
        self.minute += minutes
        self.normalize()
        return self

    def __sub__(self, minutes):
        return self.__add__(-minutes)  # … just add negative value

    # all the magic happen here
    def normalize(self):
        # h:m to minutes
        to_minutes = self.hour * 60 + self.minute
        # wrap around days
        days, minutes = divmod(to_minutes, 24 * 60)
        # convert back to h:m
        self.hour, self.minute = divmod(minutes, 60)
