class Schedule:
    # type, 0 for students, 1 for teachers
    def __init__(self, type, classesPerDay, studyDaysInWeek, scheduleEntities):
        self.type = type
        self.classesPerDay = classesPerDay
        self.studyDaysInWeek = studyDaysInWeek
        self.scheduleEntities = scheduleEntities
