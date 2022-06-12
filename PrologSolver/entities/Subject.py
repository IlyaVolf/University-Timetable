class Subject:
    def __init__(self, id, specializationId, name, semesters,
                 typeOfClass, frequency, teacherId, amountOfGroups):
        self.id = id
        self.specializationId = specializationId
        self.name = name
        self.semesters = semesters
        self.typeOfClass = typeOfClass
        self.frequency = frequency
        self.teacherId = teacherId
        self.amountOfGroups = amountOfGroups

    def getSemesters(self):
        tokens = self.semesters.split(",")

        return tokens
