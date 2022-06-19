class GeneratedClass:
    def __init__(self, id, faculty, educationalProgram, specialization, subject, semester, teacher, typeOfClass,
                 auditory, groups, day, classNumber, teacherId):
        mapp = {1: "Mon", 2: "Tue", 3: "Wen", 4: "Thu", 5: "Fri", 6: "Sat"}

        self.id = id
        self.faculty = faculty
        self.educationalProgram = educationalProgram
        self.specialization = specialization
        self.subject = subject
        self.semester = semester
        self.teacher = teacher
        self.typeOfClass = typeOfClass
        self.auditory = auditory
        self.groups = disassemblePrologList(groups)
        self.groupsStr = groups.replace('[','').replace(']','').replace(",", ", ")
        self.day = day
        self.dayStr = mapp[day]
        self.classNumber = classNumber
        self.teacherId = teacherId

    # ПОЛУЧИТЬ ГРУППЫ МОЖНОИ НАЧЕ, ЧЕРЕЗ: dbManager.getAllGroupsOfClass(id)

    def getGroupsAsString(self):
        return self.groups

    def getAmountOfGroups(self):
        if self.groups == "[]":
            return 0

        tokens = self.getGroupsAsString()

        return len(tokens)


def disassemblePrologList(groupsList):
    prologList2 = groupsList[1:len(groupsList) - 1]
    groups = prologList2.split(",")

    return groups
