from collections import defaultdict


class School(object):
    def __init__(self, name):
        self.name = name
        # with a default dict instead of initializing empty sets
        self.rooster = defaultdict(set)

    def grade(self, n):
        return self.rooster[n]

    def add(self, student, n):
        self.rooster[n].add(student)

    def sort(self):
        return list(
            (k, tuple(sorted(v)))  # acute parenthesism occuring here
            for k, v in sorted(self.rooster.items())
        )
