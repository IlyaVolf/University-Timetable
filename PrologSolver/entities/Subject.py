class Subject:
    def __init__(self, id, specializationId, specialization, name, semesters,
                 typeOfClass, frequency, teacherId, teacher, amountOfGroups, generated):
        self.id = id
        self.specializationId = specializationId
        self.specialization = specialization
        self.name = name
        self.semesters = semesters
        self.typeOfClass = typeOfClass
        self.frequency = frequency
        self.teacherId = teacherId
        self.teacher = teacher
        self.amountOfGroups = amountOfGroups
        self.generated = generated

    def getSemesters(self):
        tokens = self.semesters.split(",")

        return tokens
