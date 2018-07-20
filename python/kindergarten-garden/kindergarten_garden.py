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
        zone = {}
        for student in students:
            zone.update({student: []})

        for row in diagram.split("\n"):
            for k, cup in enumerate(row):
                try:
                    student = students[int(k*.5)]
                    zone[student].append(self.PLANTS[cup])
                except:
                    pass

        self.zone = zone

    def plants(self, student):
        return self.zone[student]
