import re


class Phone(object):
    def __init__(self, phone_number):
        # check for alpha in phone
        if any(c.isalpha() for c in phone_number):
            raise ValueError("Can't contains letter")

        # normalized
        clean = re.sub("\D", "", phone_number)

        # check for country code
        try:
            country_code = clean[-11]
        except IndexError:
            country_code = 1
        if int(country_code) != 1:
            raise ValueError(
                f"Country code ({country_code}) must be 1 or empty")

        # store the plain number
        self.number = n = clean[-10::]

        # check, store area code
        self.area_code = ac = n[0:3]
        if int(ac[0]) in [0, 1]:
            raise ValueError(f"Area code ({ac}) can't start with 0 or 1")

        # check, store exchange code
        self.exchange_code = ec = n[3:6]
        if int(ec[0]) in [0, 1]:
            raise ValueError(f"Exchange code ({ec}) can't start with 0 or 1")

        # store the station code
        self.station_code = n[6::]

    def pretty(self):
        # format (###) ###-####
        return f"({self.area_code}) {self.exchange_code}-{self.station_code}"
