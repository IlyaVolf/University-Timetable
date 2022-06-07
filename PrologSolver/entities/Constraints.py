class Constraints:
    def __init__(self, firstClassStarts, classDuration, shortBrakeDuration,
                 largeBrakeDuration, studyDaysInWeek, studyDaysInWeekForStudents,
                 studyDaysInWeekForTeachers, classesPerDay, classesPerDayStudents,
                 classesPerDayTeachers, lunchBrake, gaps, classroomFillness):
        self.firstClassStarts = firstClassStarts
        self.classDuration = classDuration
        self.shortBrakeDuration = shortBrakeDuration
        self.largeBrakeDuration = largeBrakeDuration
        self.studyDaysInWeek = studyDaysInWeek
        self.studyDaysInWeekForStudents = studyDaysInWeekForStudents
        self.studyDaysInWeekForTeachers = studyDaysInWeekForTeachers
        self.classesPerDay = classesPerDay
        self.classesPerDayStudents = classesPerDayStudents
        self.classesPerDayTeachers = classesPerDayTeachers
        self.lunchBrake = lunchBrake
        self.gaps = gaps
        self.classroomFillness = classroomFillness
