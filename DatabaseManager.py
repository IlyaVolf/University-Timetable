import sqlite3

from entities.Auditory import Auditory
from entities.Constraints import Constraints
from entities.EducationalProgram import EducationalProgram
from entities.Faculty import Faculty
from entities.Group import Group
from entities.Subject import Subject
from entities.Teacher import Teacher


def tupleToList(t):
    lst = []
    for row in t:
        lst.append(row[0])
    return lst


class DatabaseManager:

    def __init__(self, dbFileName='timetable.sqlite'):
        try:
            self.sqlite_connection = sqlite3.connect(dbFileName)
        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite", error)

    def addFaculty(self, faculty):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'INSERT INTO Faculties(`Faculty`) VALUES(?)'
        cursor.execute(sqliteQuery, (faculty.name,))
        self.sqlite_connection.commit()
        cursor.close()

    def getAllFaculties(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT Faculty FROM Faculties'
        cursor.execute(sqliteQuery)
        rows = cursor.fetchall()
        cursor.close()
        return tupleToList(rows)

    def deleteFaculty(self, facultyName):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'DELETE FROM Faculties WHERE Faculty = ?'
        cursor.execute(sqliteQuery, (facultyName,))
        self.sqlite_connection.commit()
        cursor.close()

    def addEducationalProgram(self, educationalProgram):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'INSERT INTO EducationalPrograms(`Faculty`, `EducationalProgram`, `Specialization`) ' \
                      'VALUES(?, ?, ?)'
        cursor.execute(sqliteQuery, (educationalProgram.faculty, educationalProgram.name,
                                     educationalProgram.specialization,))
        self.sqlite_connection.commit()
        cursor.close()

    def getEducationalPrograms(self, facultyName):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT EducationalProgram, Specialization FROM EducationalPrograms WHERE Faculty=?'
        cursor.execute(sqliteQuery, (facultyName,))
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append(EducationalProgram(facultyName, row[0], row[1]))
        return lst

    def deleteEducationalProgram(self, educationalProgram):
        cursor = self.sqlite_connection.cursor()

        sqliteQuery = 'DELETE FROM EducationalPrograms WHERE Faculty = ? AND EducationalProgram = ? AND' \
                      'Specialization = ?'
        cursor.execute(sqliteQuery, (educationalProgram.faculty, educationalProgram.name,
                                     educationalProgram.specialization,))
        sqliteQuery = 'DELETE FROM Faculties WHERE EducationalProgram = ?'
        cursor.execute(sqliteQuery, (educationalProgram.name,))
        sqliteQuery = 'DELETE FROM Groups WHERE EducationalProgram = ?'
        cursor.execute(sqliteQuery, (educationalProgram.name,))
        sqliteQuery = 'DELETE FROM Subjects WHERE EducationalProgram = ?'
        cursor.execute(sqliteQuery, (educationalProgram.name,))
        self.sqlite_connection.commit()
        cursor.close()

    def addGroup(self, group):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'INSERT INTO Groups(`EducationalProgram`, `Number`, `AmountOfStudents`, `YearOfStudy`) VALUES(?, ?, ?, ?)'
        cursor.execute(sqliteQuery, (group.specialization, group.numberOfGroup,
                                     group.amountOfStudents, group.yearOfStudy,))
        self.sqlite_connection.commit()
        cursor.close()

    def getGroups(self, specialization):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT Number, AmountOfStudents, YearOfStudy FROM Groups WHERE EducationalProgram=?'
        cursor.execute(sqliteQuery, (specialization,))
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append(Group(specialization, row[0], row[1], row[2]))
        return lst

    def addSubject(self, subject):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'INSERT INTO Subjects(`EducationalProgram`, `Name`, `Semesters`, `TypeOfClass`, `Frequency`, `teacher`, `AmountOfGroups`) VALUES(?, ?, ?, ?, ?, ?, ?)'
        cursor.execute(sqliteQuery, (subject.educationalProgram, subject.subjectName,
                                     subject.semesters, subject.typeOfClass,
                                     subject.frequency, subject.teacher,
                                     subject.amountOfGroups,))
        self.sqlite_connection.commit()
        cursor.close()

    def updateSubject(self, specialization, subject, teacher,
                      semesters, types, frequency, amountOfGroups):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'UPDATE Subjects SET Teacher = ? WHERE EducationalProgram = ? AND Name = ? AND Semesters = ? AND TypeOfClass = ? AND Frequency = ? AND AmountOfGroups = ?'
        cursor.execute(sqliteQuery, (teacher, specialization,
                                     subject, semesters,
                                     types, frequency,
                                     amountOfGroups,))
        self.sqlite_connection.commit()
        cursor.close()

    def getSubjects(self, specialization):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT Name, Semesters, TypeOfClass, Frequency, Teacher, AmountOfGroups FROM Subjects WHERE EducationalProgram=?'
        cursor.execute(sqliteQuery, (specialization,))
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append(Subject(specialization, row[0], row[1], row[2], row[3], row[4], row[5]))
        return lst

    def getSubjectNames(self, specialization):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT DISTINCT Name FROM Subjects WHERE EducationalProgram=?'
        cursor.execute(sqliteQuery, (specialization,))
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append(row[0])
        return lst

    def getSemestersOfSubject(self, specialization, subjectName):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT DISTINCT Semesters FROM Subjects WHERE EducationalProgram=? AND Name=?'
        cursor.execute(sqliteQuery, (specialization, subjectName))
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append(row[0])
        return lst

    def getTypesOfClasses(self, specialization, subjectName, semesters):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT DISTINCT TypeOfClass FROM Subjects WHERE EducationalProgram=? AND Name=? AND Semesters=?'
        cursor.execute(sqliteQuery, (specialization, subjectName, semesters))
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append(row[0])
        return lst

    def getSubjectsDuplicates(self, specialization, subjectName, semesters, typesOfClass):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT Frequency, Teacher, AmountOfGroups FROM Subjects WHERE EducationalProgram=? AND Name=? AND Semesters=? AND TypeOfClass=?'
        cursor.execute(sqliteQuery, (specialization, subjectName, semesters, typesOfClass,))
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append(Subject(specialization, subjectName, semesters, typesOfClass, row[0], row[1], row[2]))
        return lst

    def addTeacher(self, teacher):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'INSERT INTO Teachers(`Subject`, `Name`, `DaysCanWork`, `DaysWantWork`, `Weight`) VALUES(?, ?, ?, ?, ?)'
        cursor.execute(sqliteQuery, (teacher.subject, teacher.name, teacher.daysTeacherCanWork,
                                     teacher.daysTeacherWantWork, teacher.weight,))
        self.sqlite_connection.commit()
        cursor.close()

    def getAllTeachers(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT * FROM Teachers'
        cursor.execute(sqliteQuery)
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append(Teacher(row[0], row[1], row[2], row[3], row[4]))
        return lst

    def addAuditory(self, auditory):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'INSERT INTO Auditories(`TypeOfClass`, `Capacity`, `Number`) VALUES(?, ?, ?)'
        cursor.execute(sqliteQuery, (auditory.typesOfClass, auditory.capacity, auditory.number,))
        self.sqlite_connection.commit()
        cursor.close()

    def getAuditories(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT * FROM Auditories'
        cursor.execute(sqliteQuery)
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append(Auditory(row[0], row[1], row[2]))
        return lst

    def getAuditoryTypes(self, auditoryNumber):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT TypeOfClass FROM Auditories WHERE Number=?'
        cursor.execute(sqliteQuery, (auditoryNumber,))
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append(row[0])
        return lst

    def getAllSpecializationGroups(self, specialization):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT Number, YearOfStudy FROM Groups WHERE EducationalProgram=? ORDER BY YearOfStudy'
        cursor.execute(sqliteQuery, (specialization,))
        rows = cursor.fetchall()
        cursor.close()

        # TODO maybe now it is not needed
        return []

    def addConstraints(self, constraints):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'INSERT INTO Constraints(`FirstClassStarts`, `ClassDuration`, `ShortBrakeDuration`, `LargeBrakeDuration`, `StudyDaysInWeek`, `StudyDaysInWeekForStudents`, `StudyDaysInWeekForTeachers`, `ClassesPerDay`, `ClassesPerDayStudents`, `ClassesPerDayTeachers`, `LunchBrake`, `Gaps`, `ClassroomFillness`) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
        cursor.execute(sqliteQuery, (constraints.firstClassStarts, constraints.classDuration,
                                     constraints.shortBrakeDuration, constraints.largeBrakeDuration,
                                     constraints.studyDaysInWeek, constraints.studyDaysInWeekForStudents,
                                     constraints.studyDaysInWeekForTeachers, constraints.classesPerDay,
                                     constraints.classesPerDayStudents, constraints.classesPerDayTeachers,
                                     constraints.lunchBrake, constraints.classroomFillness,))
        self.sqlite_connection.commit()
        cursor.close()

    def getConstraints(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT FirstClassStarts, ClassDuration, ShortBrakeDuration, LargeBrakeDuration, StudyDaysInWeek, StudyDaysInWeekForStudents, StudyDaysInWeekForTeachers, ClassesPerDay, ClassesPerDayStudents, ClassesPerDayTeachers, LunchBrake, Gaps, ClassroomFillness FROM Constraints'
        cursor.execute(sqliteQuery)
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append(Constraints(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                                   row[10], row[11], row[12]))
        return lst

    def deleteAuditory(self, auditory):
        cursor = self.sqlite_connection.cursor()

        sqliteQuery = 'DELETE FROM Auditories WHERE TypeOfClass = ? AND Capacity = ? AND Number = ?'
        cursor.execute(sqliteQuery, (auditory.typesOfClass, auditory.capacity,
                                     auditory.number,))
        self.sqlite_connection.commit()
        cursor.close()

    def deleteTeacher(self, teacher):
        cursor = self.sqlite_connection.cursor()

        sqliteQuery = 'DELETE FROM Teachers WHERE Name = ? AND DaysCanWork = ? AND DaysWantWork = ? AND Weight = ?'
        cursor.execute(sqliteQuery, (teacher.name, teacher.daysTeacherCanWork,
                                     teacher.daysTeacherWantWork, teacher.weight,))
        sqliteQuery = 'SELECT * FROM Subjects WHERE Teacher = ?'
        cursor.execute(sqliteQuery, (teacher.name,))
        rows = cursor.fetchall()
        sqliteQuery = 'DELETE FROM Subjects WHERE Teacher = ?'
        cursor.execute(sqliteQuery)
        for row in rows:
            self.addSubject(Subject(row[0], row[1], row[2], row[3], row[4], 'Undefined', row[6]))

        self.sqlite_connection.commit()
        cursor.close()

    def deleteSubject(self, subject):
        cursor = self.sqlite_connection.cursor()

        sqliteQuery = 'DELETE FROM Subjects WHERE EducationalProgram = ? AND Name = ? AND Semesters = ? AND TypeOfClass = ? AND Frequency = ? AND Teacher = ? AND AmountOfGroups = ?'
        cursor.execute(sqliteQuery, (subject.educationalProgram, subject.subjectName,
                                     subject.semesters, subject.typeOfClass,
                                     subject.frequency, subject.teacher, subject.amountOfGroups,))

        self.sqlite_connection.commit()
        cursor.close()

    def deleteGroup(self, group):
        cursor = self.sqlite_connection.cursor()

        sqliteQuery = 'DELETE FROM Groups WHERE EducationalProgram = ? AND Number = ? AND AmountOfStudents = ? AND YearOfStudy = ?'
        cursor.execute(sqliteQuery, (group.specialization, group.numberOfGroup,
                                     group.amountOfStudents, group.yearOfStudy,))

        self.sqlite_connection.commit()
        cursor.close()
# TODO functions working with generated timetable will be written later because of new solver
    def clearAll(self):
        cursor = self.sqlite_connection.cursor()
        cursor.execute('DELETE FROM Auditories')
        cursor.execute('DELETE FROM Constraints')
        cursor.execute('DELETE FROM EducationalPrograms')
        cursor.execute('DELETE FROM Faculties')
        cursor.execute('DELETE FROM Groups')
        cursor.execute('DELETE FROM Subjects')
        cursor.execute('DELETE FROM Teachers')
        self.sqlite_connection.commit()
        cursor.close()

    def close(self):
        if self.sqlite_connection:
            self.sqlite_connection.close()


dbManager = DatabaseManager()
ep = EducationalProgram('Test', 'test', 'test')
#  dbManager.addEducationalProgram(ep)
eps = dbManager.getEducationalPrograms('fit')
for e in eps:
    print('F - ' + e.faculty + ', Ep - ' + e.name + ', S - ' + e.specialization)
dbManager.close()
