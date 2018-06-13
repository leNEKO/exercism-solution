
plants = {
    "R": "Radishes",
    "V": "Violets",
    "C": "Clover",
    "G": "Grass",
}


class Garden(object):
    def __init__(self, diagram, students="Alice Bob Charlie David Eve Fred Ginny Harriet Ileana Joseph Kincaid Larry".split()):
        students = sorted(students)
        zone = {}
        for student in students:
            zone.update({student: []})

        for row in diagram.split("\n"):
            for k, cup in enumerate(row):
                try:
                    student = students[int(k*.5)]
                    zone[student].append(plants[cup])
                except:
                    pass

        self.zone = zone

    def plants(self, student):
        return self.zone[student]
