class School(object):
    def __init__(self, name):
        self.name = name
        self.rooster = {}
        for i in range(1, 9):
            self.rooster.update({i: []})

    def grade(self, n):
        return set(self.rooster[n])

    def add(self, student, n):
        self.rooster[n].append(student)

    def sort(self):
        return list(
            (k, tuple(sorted(v)))  # that's some parenthesis
            for k, v in self.rooster.items()
            if v
        )
