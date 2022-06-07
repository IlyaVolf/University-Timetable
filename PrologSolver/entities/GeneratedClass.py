class GeneratedClass:
    def __init__(self, classId, faculty, edProgram, specialization, subject, semester, teacher, typeOfClass, auditory, groups,
                 day, classNumber):
        self.classId = classId
        self.faculty = faculty
        self.edProgram = edProgram
        self.specialization = specialization
        self.subject = subject
        self.semester = semester
        self.teacher = teacher
        self.typeOfClass = typeOfClass
        self.auditory = auditory
        self.groups = disassemblePrologList(groups)
        self.day = day
        self.classNumber = classNumber

    def getGroups(self):
        return self.groups

    def getAmountOfGroups(self):
        if self.groups == "[]":
            return 0

        tokens = self.getGroups()

        return len(tokens)


def disassemblePrologList(groupsList):
    prologList2 = groupsList[1:len(groupsList) - 1]
    groups = prologList2.split(",")

    return groups
