class Schedule:
    # type, 0 for students, 1 for teachers
    def __init__(self, type, entity, classesPerDay, studyDaysInWeek, scheduleEntities):
        self.type = type
        self.entity = entity
        self.classesPerDay = classesPerDay
        self.studyDaysInWeek = studyDaysInWeek
        self.scheduleEntities = scheduleEntities
