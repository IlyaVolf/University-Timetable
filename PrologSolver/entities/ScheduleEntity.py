class ScheduleEntity:
    def __init__(self, subject, typeOfClass, teacher, auditory, groups, classNumber, time):
        self.subject = subject
        self.typeOfClass = typeOfClass
        self.teacher = teacher
        self.auditory = auditory
        self.groups = groups[1:-1]
        self.classNumber = classNumber
        self.time = time