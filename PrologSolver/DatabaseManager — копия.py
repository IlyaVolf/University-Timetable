import sqlite3

from entities.Constraints import Constraints
from entities.EducationalProgram import EducationalProgram
from entities.GeneratedClass import GeneratedClass
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


    # Создать таблицу факультетов
    def initFaculty(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'CREATE TABLE FacultiesNEW(id INTEGER PRIMARY KEY, Faculty TEXT)'
        cursor.execute(sqliteQuery)
        self.sqlite_connection.commit()
        cursor.close()

    # Добавить факультет
    # faculty - имя факультета
    def addFaculty(self, faculty):
        cursor = self.sqlite_connection.cursor()

        # Проверка на то, что такой факультет уже не существует в таблице
        sqliteQuery = 'SELECT EXISTS(SELECT 1 FROM FacultiesNEW WHERE Faculty= ?);'
        cursor.execute(sqliteQuery, (faculty,))
        rows = cursor.fetchall()
        for row in rows:
            if row[0] == 1:
                raise ValueError('This Faculty already exists!')

        sqliteQuery = 'INSERT INTO FacultiesNEW(`Faculty`) VALUES(?)'
        cursor.execute(sqliteQuery, (faculty,))
        self.sqlite_connection.commit()
        cursor.close()

    # Редактировать факультет
    # id - id факультета
    # faculty - имя факультета
    def updateFaculty(self, id, faculty):
        cursor = self.sqlite_connection.cursor()

        # Проверка на то, что такой факультет уже не существует в таблице
        sqliteQuery = 'SELECT EXISTS(SELECT 1 FROM FacultiesNEW WHERE Faculty= ?);'
        cursor.execute(sqliteQuery, (faculty,))
        rows = cursor.fetchall()
        for row in rows:
            if row[0] == 1:
                raise ValueError('This Faculty already exists!')

        sqliteQuery = 'UPDATE FacultiesNEW SET Faculty = ? WHERE id = ?'
        cursor.execute(sqliteQuery, (faculty, id,))
        self.sqlite_connection.commit()
        cursor.close()

    # Удалить факультет
    # id - id факультета
    def removeFaculty(self, id):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'DELETE FROM FacultiesNEW WHERE id = ?'
        cursor.execute(sqliteQuery, (id,))
        self.sqlite_connection.commit()
        cursor.close()

    # Получить все факультеты
    def getAllFaculties(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT * FROM TEXT'
        cursor.execute(sqliteQuery)
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append(Faculty(row[0], row[1]))
        return lst

########################################################################################################################

    # Создать таблицу факультетов
    def initEducationalProgram(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'CREATE TABLE EducationalProgramsNEW(id INTEGER PRIMARY KEY, FacultyId INTEGER, ' \
                      'EducationalProgram TEXT) '
        cursor.execute(sqliteQuery)
        self.sqlite_connection.commit()
        cursor.close()

    # Добавить образовательную программу
    # FacultyId - id факультета
    # EducationalProgram - образовательная программа
    def addEducationalProgram(self, facultyId, educationalProgram):
        cursor = self.sqlite_connection.cursor()

        # Проверка на то, что такая образовательная программа уже не существует в таблице
        sqliteQuery = 'SELECT EXISTS(SELECT 1 FROM EducationalProgramsNEW WHERE FacultyId = ? AND EducationalProgram ' \
                      '= ?); '
        cursor.execute(sqliteQuery, (facultyId, educationalProgram,))
        rows = cursor.fetchall()
        for row in rows:
            if row[0] == 1:
                raise ValueError('This Educational program already exists!')

        sqliteQuery = 'INSERT INTO EducationalProgramsNEW(`FacultyId`, `EducationalProgram`) ' \
                      'VALUES(?, ?)'
        cursor.execute(sqliteQuery, (facultyId, educationalProgram,))
        self.sqlite_connection.commit()
        cursor.close()

    # Изменить образовательную программу
    # id - id образовательной программы
    # FacultyId - id факультета
    # EducationalProgram - образовательная программа
    def updateEducationalProgram(self, id, facultyId, educationalProgram):
        cursor = self.sqlite_connection.cursor()

        # Проверка на то, что такая образовательная программа уже не существует в таблице
        sqliteQuery = 'SELECT EXISTS(SELECT 1 FROM EducationalProgramsNEW WHERE FacultyId = ? AND EducationalProgram ' \
                      '= ?); '
        cursor.execute(sqliteQuery, (facultyId, educationalProgram,))
        rows = cursor.fetchall()
        for row in rows:
            if row[0] == 1:
                raise ValueError('This Educational program already exists!')

        sqliteQuery = 'UPDATE EducationalProgramsNEW SET EducationalProgram = ? WHERE id = ? AND FacultyId = ?'
        cursor.execute(sqliteQuery, (educationalProgram, id, facultyId, ))
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

    def getEducationalProgramsIlya(self, facultyName):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT DISTINCT EducationalProgram FROM EducationalPrograms WHERE Faculty=?'
        cursor.execute(sqliteQuery, (facultyName,))
        rows = cursor.fetchall()
        cursor.close()

        return tupleToList(rows)

    def getSpecializations(self, faculty, educationalProgram):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT Specialization FROM EducationalPrograms WHERE Faculty=? AND EducationalProgram=?'
        cursor.execute(sqliteQuery, (faculty, educationalProgram))
        rows = cursor.fetchall()
        cursor.close()
        return tupleToList(rows)

    def deleteEducationalProgram(self, educationalProgram):
        cursor = self.sqlite_connection.cursor()

        sqliteQuery = 'DELETE FROM EducationalPrograms WHERE Faculty = ? AND EducationalProgram = ? AND' \
                      'Specialization = ?'
        cursor.execute(sqliteQuery, (educationalProgram.faculty, educationalProgram.name,
                                     educationalProgram.specialization,))
        sqliteQuery = 'DELETE FROM Faculties WHERE EducationalProgram = ?'
        cursor.execute(sqliteQuery, (educationalProgram.name,))
        sqliteQuery = 'DELETE FROM Groups WHERE Specialization = ?'
        cursor.execute(sqliteQuery, (educationalProgram.name,))
        sqliteQuery = 'DELETE FROM Subjects WHERE Specialization = ?'
        cursor.execute(sqliteQuery, (educationalProgram.name,))
        self.sqlite_connection.commit()
        cursor.close()

    def addGroup(self, group):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'INSERT INTO Groups(`Specialization`, `Number`, `AmountOfStudents`, `YearOfStudy`) VALUES(' \
                      '?, ?, ?, ?) '
        cursor.execute(sqliteQuery, (group.specialization, group.numberOfGroup,
                                     group.amountOfStudents, group.yearOfStudy,))
        self.sqlite_connection.commit()
        cursor.close()

    def getGroups(self, specialization):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT Number, AmountOfStudents, YearOfStudy FROM Groups WHERE Specialization=?'
        cursor.execute(sqliteQuery, (specialization,))
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append(Group(specialization, row[0], row[1], row[2]))
        return lst

    def getAllGroups(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT Specialization, Number, AmountOfStudents, YearOfStudy FROM Groups'
        cursor.execute(sqliteQuery)
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append(Group(row[0], row[1], row[2], row[3]))
        return lst

    def addSubject(self, subject):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'INSERT INTO Subjects(`Specialization`, `Name`, `Semesters`, `TypeOfClass`, `Frequency`, ' \
                      '`teacher`, `AmountOfGroups`) VALUES(?, ?, ?, ?, ?, ?, ?) '
        cursor.execute(sqliteQuery, (subject.educationalProgram, subject.subjectName,
                                     subject.semesters, subject.typeOfClass,
                                     subject.frequency, subject.teacher,
                                     subject.amountOfGroups,))
        self.sqlite_connection.commit()
        cursor.close()

    def updateSubject(self, specialization, subject, teacher,
                      semesters, types, frequency, amountOfGroups):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'UPDATE Subjects SET Teacher = ? WHERE Specialization = ? AND Name = ? AND Semesters = ? ' \
                      'AND TypeOfClass = ? AND Frequency = ? AND AmountOfGroups = ? '
        cursor.execute(sqliteQuery, (teacher, specialization,
                                     subject, semesters,
                                     types, frequency,
                                     amountOfGroups,))
        self.sqlite_connection.commit()
        cursor.close()

    def getAllSubjects(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT DISTINCT Specialization, Name, Semesters FROM Subjects'
        cursor.execute(sqliteQuery)
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append([row[0], row[1], row[2]])
        return lst

    def getAllSubjectTypesOfClass(self, specialization, name, semesters):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT DISTINCT TypeOfClass, Frequency FROM Subjects WHERE Specialization=? AND Name=? AND Semesters=?'
        cursor.execute(sqliteQuery, (specialization, name, semesters,))
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append([row[0], row[1]])
        return lst

    def getAllSubjectTeachers(self, specialization, name, semesters, typeOfClass, Frequency):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT Teacher, AmountOfGroups FROM Subjects WHERE Specialization=? AND Name=? AND Semesters=?' \
                      'AND TypeOfClass=? AND Frequency=?'
        cursor.execute(sqliteQuery, (specialization, name, semesters, typeOfClass, Frequency,))
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append([row[0], row[1]])
        return lst

    def getSubjects(self, specialization):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT Name, Semesters, TypeOfClass, Frequency, Teacher, AmountOfGroups FROM Subjects WHERE ' \
                      'Specialization=? '
        cursor.execute(sqliteQuery, (specialization,))
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append(Subject(specialization, row[0], row[1], row[2], row[3], row[4], row[5]))
        return lst

    def getSubjectNames(self, specialization):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT DISTINCT Name FROM Subjects WHERE Specialization=?'
        cursor.execute(sqliteQuery, (specialization,))
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append(row[0])
        return lst

    def getSemestersOfSubject(self, specialization, subjectName):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT DISTINCT Semesters FROM Subjects WHERE Specialization=? AND Name=?'
        cursor.execute(sqliteQuery, (specialization, subjectName))
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append(row[0])
        return lst

    def getAllTypesOfClasses(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT DISTINCT TypeOfClass FROM Subjects'
        cursor.execute(sqliteQuery)
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append(row[0])
        return lst

    def getTypesOfClasses(self, specialization, subjectName, semesters):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT DISTINCT TypeOfClass FROM Subjects WHERE Specialization=? AND Name=? AND Semesters=?'
        cursor.execute(sqliteQuery, (specialization, subjectName, semesters))
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append(row[0])
        return lst

    def getSubjectsDuplicates(self, specialization, subjectName, semesters, typesOfClass):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT Frequency, Teacher, AmountOfGroups FROM Subjects WHERE Specialization=? AND Name=? ' \
                      'AND Semesters=? AND TypeOfClass=? '
        cursor.execute(sqliteQuery, (specialization, subjectName, semesters, typesOfClass,))
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append(Subject(specialization, subjectName, semesters, typesOfClass, row[0], row[1], row[2]))
        return lst

    def addTeacher(self, teacher):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'INSERT INTO Teachers(`Subject`, `Name`, `DaysCanWork`, `DaysWantWork`, `Weight`) VALUES(?, ?, ' \
                      '?, ?, ?) '

        wantTokens = teacher.daysTeacherWantWork[1:-1].split(",")
        canTokens = teacher.daysTeacherCanWork[1:-1].split(",")
        for want in wantTokens:
            if not (want in canTokens):
                raise Exception('Хочет работать в тот день, в который не может работать!')

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

    def getAllSpecializationGroups(self, specialization, yearOfStudy):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT Number FROM Groups WHERE Specialization=? AND YearOfStudy=? ORDER BY YearOfStudy'
        cursor.execute(sqliteQuery, (specialization, yearOfStudy,))
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append(row[0])

        return lst

    def getAllSpecializationUniqueYears(self, specialization):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT Distinct YearOfStudy FROM Groups WHERE Specialization=? ORDER BY YearOfStudy'
        cursor.execute(sqliteQuery, (specialization,))
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append(row[0])

        return lst

    def addConstraints(self, constraints):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'INSERT INTO Constraints(`FirstClassStarts`, `ClassDuration`, `ShortBrakeDuration`, ' \
                      '`LargeBrakeDuration`, `StudyDaysInWeek`, `StudyDaysInWeekForStudents`, ' \
                      '`StudyDaysInWeekForTeachers`, `ClassesPerDay`, `ClassesPerDayStudents`, ' \
                      '`ClassesPerDayTeachers`, `LunchBrake`, `Gaps`, `ClassroomFillness`) VALUES(?, ?, ?, ?, ?, ?, ' \
                      '?, ?, ?, ?, ?, ?, ?) '
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
        sqliteQuery = 'SELECT FirstClassStarts, ClassDuration, ShortBrakeDuration, LargeBrakeDuration, ' \
                      'StudyDaysInWeek, StudyDaysInWeekForStudents, StudyDaysInWeekForTeachers, ClassesPerDay, ' \
                      'ClassesPerDayStudents, ClassesPerDayTeachers, LunchBrake, Gaps, ClassroomFillness FROM ' \
                      'Constraints '
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

        sqliteQuery = 'DELETE FROM Subjects WHERE Specialization = ? AND Name = ? AND Semesters = ? AND ' \
                      'TypeOfClass = ? AND Frequency = ? AND Teacher = ? AND AmountOfGroups = ? '
        cursor.execute(sqliteQuery, (subject.educationalProgram, subject.subjectName,
                                     subject.semesters, subject.typeOfClass,
                                     subject.frequency, subject.teacher, subject.amountOfGroups,))

        self.sqlite_connection.commit()
        cursor.close()

    def deleteGroup(self, group):
        cursor = self.sqlite_connection.cursor()

        sqliteQuery = 'DELETE FROM Groups WHERE Specialization = ? AND Number = ? AND AmountOfStudents = ? AND ' \
                      'YearOfStudy = ? '
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

    def clearGeneratedScheduleTable(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'DROP TABLE IF EXISTS GeneratedSchedule;'
        cursor.execute(sqliteQuery)
        sqliteQuery = 'create table GeneratedSchedule (id integer primary key autoincrement, `Faculty`, ' \
                      '`EducationalProgram`, `Specialization`, `Subject`, `Semester`, `Teacher`, `TypeOfClass`, ' \
                      '`Auditory`, `Groups`, `Day`, `ClassNumber`)'
        cursor.execute(sqliteQuery)

    def clearClassToGroupTable(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'DELETE From ClassToGroups'
        cursor.execute(sqliteQuery, ())
        self.sqlite_connection.commit()

    def addGeneratedClass(self, classId, faculty, edProgram, specialization, subject, semester, teacher, typeOfClass,
                          auditory, groupsList, day, classNumber):

        groups = disassemblePrologList(groupsList)

        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'INSERT INTO GeneratedSchedule(`Faculty`, `EducationalProgram`, `Specialization`, `Subject`,' \
                      '`Semester`, `Teacher`, `TypeOfClass`, `Auditory`, `Groups`, `Day`, `ClassNumber`) VALUES(?, ?,' \
                      ' ?, ?, ?, ?, ?, ?, ?, ?, ?) '
        cursor.execute(sqliteQuery, (faculty, edProgram, specialization, subject, semester, teacher, typeOfClass,
                                     auditory, groupsList, day, classNumber,))
        self.sqlite_connection.commit()

        ############################ GROUPS SEPARATE ADDED #######################

        for group in groups:
            sqliteQuery = 'INSERT INTO ClassToGroups(`ClassId`, `GroupNumber`) VALUES(?, ?) '
            cursor.execute(sqliteQuery, (classId, group,))

        self.sqlite_connection.commit()
        cursor.close()

    # Возвращаем все сгенерированные занятия
    def getAllGeneratedClasses(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT * FROM GeneratedSchedule'
        cursor.execute(sqliteQuery)
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for i in range(len(rows)):
            lst.append(
                GeneratedClass(i, rows[i][1], rows[i][2], rows[i][3], rows[i][4], rows[i][5], rows[i][6], rows[i][7],
                               rows[i][8], rows[i][9], rows[i][10], rows[i][11]))
        return lst


def disassemblePrologList(groupsList):
    prologList2 = groupsList[1:len(groupsList) - 1]
    groups = prologList2.split(",")

    return groups


dbManager = DatabaseManager()
ep = EducationalProgram('Test', 'test', 'test')
#  dbManager.addEducationalProgram(ep)
eps = dbManager.getEducationalPrograms('fit')
for e in eps:
    print('F - ' + e.faculty + ', Ep - ' + e.name + ', S - ' + e.specialization)
dbManager.close()
