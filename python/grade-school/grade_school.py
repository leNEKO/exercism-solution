from collections import defaultdict


class School(object):
    def __init__(self):
        self._db = defaultdict(set)

    def grade(self, n):
        return sorted(list(self._db[n])) or []

    def add_student(self, name, grade):
        self._db[grade].add(name)

    def roster(self):
        return [name
                for k, v in sorted(self._db.items())
                for name in sorted(v)
                ]
