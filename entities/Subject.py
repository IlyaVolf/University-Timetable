class Subject:
    def __init__(self, specialization, subjectName, semesters,
                 typeOfClass, frequency, teacher, amountOfGroups):
        self.specialization = specialization
        self.subjectName = subjectName
        self.semesters = semesters
        self.typeOfClass = typeOfClass
        self.frequency = frequency
        self.teacher = teacher
        self.amountOfGroups = amountOfGroups

    def getSemesters(self):
        tokens = self.semesters.split(",")

        return tokens
