class Garden(object):
    PLANTS = {
        "R": "Radishes",
        "V": "Violets",
        "C": "Clover",
        "G": "Grass",
    }
    DEFAULT_STUDENTS = "Alice Bob Charlie David Eve Fred Ginny Harriet Ileana Joseph Kincaid Larry".split()

    def __init__(self, diagram, students=DEFAULT_STUDENTS):
        students = sorted(students)
        zone = dict((student, []) for student in students)

        for row in diagram.split():
            for k, cup in enumerate(row):
                student = students[k//2]
                zone[student].append(self.PLANTS[cup])

        self.zone = zone

    def plants(self, student):
        return self.zone[student]
