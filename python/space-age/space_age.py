class SpaceAge(object):
    EARTH_YEAR = 31557600  # seconds.
    RATIOS = {
        "earth": 1, "mercury": 0.2408467, "venus": 0.61519726,
        "mars": 1.8808158, "jupiter": 11.862615, "saturn": 29.447498,
        "uranus": 84.016846, "neptune": 164.79132
    }

    def __init__(self, seconds):
        self.seconds = seconds

        def add_planet_method(planet, ratio):
            ''' dynamically set SpaceAge on_planet methods '''
            name = f"on_{planet}"

            def _method(self):
                # years
                return round(self.seconds / (self.EARTH_YEAR * ratio), 2)

            setattr(SpaceAge, name, _method)

        # automagically set methods
        for planet, ratio in self.RATIOS.items():
            add_planet_method(planet, ratio)
