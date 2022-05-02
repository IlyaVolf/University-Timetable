class GeneratedClass:
    def __init__(self, faculty, edProgram, specialization, subject, semester, teacher, typeOfClass, auditory, groups,
                 day, classNumber):
        self.faculty = faculty
        self.edProgram = edProgram
        self.specialization = specialization
        self.subject = subject
        self.semester = semester
        self.teacher = teacher
        self.typeOfClass = typeOfClass
        self.auditory = auditory
        self.groups = groups
        self.day = day
        self.classNumber = classNumber

    def getGroups(self):
        groupsString = self.groups[1:-1]

        tokens = groupsString.split(",")

        return tokens

    def getAmountOfGroups(self):
        if self.groups == "[]":
            return 0

        tokens = self.getGroups()

        return len(tokens)
