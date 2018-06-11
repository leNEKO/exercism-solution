ALLERGENE = {
    "cats": 128,
    "pollen": 64,
    "chocolate": 32,
    "tomatoes": 16,
    "strawberries": 8,
    "shellfish": 4,
    "peanuts": 2,
    "eggs": 1,
}


class Allergies(object):

    def __init__(self, score: int):
        score %= (sum(ALLERGENE.values()) + 1)

        self.allergies: list = []
        for k, v in ALLERGENE.items():
            if v <= score:
                self.allergies.append(k)
                score -= v

    def is_allergic_to(self, item: str):
        return item in self.allergies

    @property
    def lst(self) -> list:
        return self.allergies
