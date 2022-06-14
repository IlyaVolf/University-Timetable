import sqlite3
import datetime

from entities.Faculty import Faculty
from entities.Constraints import Constraints
from entities.EducationalProgram import EducationalProgram
from entities.GeneratedClass import GeneratedClass
from entities.Specialization import Specialization
from entities.Group import Group
from entities.Subject import Subject
from entities.Teacher import Teacher
from entities.Classroom import Classroom
from entities.Schedule import Schedule
from entities.ScheduleEntity import ScheduleEntity
from entities.ScheduleTeacher import ScheduleTeacher
from entities.User import User


def tupleToList(t):
    lst = []
    for row in t:
        lst.append(row[0])
    return lst


studyDaysInWeek = 6


class DatabaseManager:
    def __init__(self, dbFileName='timetable.sqlite'):
        try:
            self.sqlite_connection = sqlite3.connect(dbFileName)
        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite", error)

    ####################################################################################################################

    ####################################################################################################################

    # Создать таблицу факультетов
    def initFaculty(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'CREATE TABLE Faculties(id INTEGER PRIMARY KEY, Faculty TEXT)'
        cursor.execute(sqliteQuery)
        self.sqlite_connection.commit()
        cursor.close()

    # Очистить таблицу факультетов
    def clearFaculty(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'DELETE FROM Faculties'
        cursor.execute(sqliteQuery)
        self.sqlite_connection.commit()
        cursor.close()

    # Добавить факультет
    # faculty - имя факультета
    # TODO МАТВЕЙ
    def addFaculty(self, faculty):
        cursor = self.sqlite_connection.cursor()

        # Проверка на то, что такой факультет уже не существует в таблице
        sqliteQuery = 'SELECT EXISTS(SELECT 1 FROM Faculties WHERE Faculty= ?);'
        cursor.execute(sqliteQuery, (faculty,))
        rows = cursor.fetchall()
        for row in rows:
            if row[0] == 1:
                raise ValueError('This Faculty already exists!')

        sqliteQuery = 'INSERT INTO Faculties(`Faculty`) VALUES(?)'
        cursor.execute(sqliteQuery, (faculty,))
        self.sqlite_connection.commit()
        cursor.close()

    # Редактировать факультет
    # id - id факультета
    # faculty - имя факультета
    # TODO МАТВЕЙ
    def updateFaculty(self, id, faculty):
        cursor = self.sqlite_connection.cursor()

        # Проверка на то, что такой факультет уже не существует в таблице
        sqliteQuery = 'SELECT EXISTS(SELECT 1 FROM Faculties WHERE Faculty= ? AND id <> ?);'
        cursor.execute(sqliteQuery, (faculty, id,))
        rows = cursor.fetchall()
        for row in rows:
            if row[0] == 1:
                raise ValueError('This Faculty already exists!')

        sqliteQuery = 'UPDATE Faculties SET Faculty = ? WHERE id = ?'
        cursor.execute(sqliteQuery, (faculty, id,))
        self.sqlite_connection.commit()
        cursor.close()

    # Удалить факультет
    # id - id факультета
    # TODO МАТВЕЙ
    def removeFaculty(self, id):
        cursor = self.sqlite_connection.cursor()

        # Идём сконца: находим те id образ програм, которые будут удалены следом. И удаляем. Вереница:
        # удаляем Subjects, Groups, Specializations, EducationalPrograms и, окончательно, Faculties.
        sqliteQuery = 'SELECT id FROM EducationalPrograms WHERE FacultyId = ?'
        cursor.execute(sqliteQuery, (id,))
        rows = cursor.fetchall()
        dbManager = DatabaseManager()
        for row in rows:
            dbManager.removeEducationalProgram(row[0])

        sqliteQuery = 'DELETE FROM Faculties WHERE id = ?'
        cursor.execute(sqliteQuery, (id,))
        self.sqlite_connection.commit()
        cursor.close()

    # Получить все факультеты
    # TODO МАТВЕЙ
    def getAllFaculty(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT * FROM Faculties'
        cursor.execute(sqliteQuery)
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append(Faculty(row[0], row[1]))
        return lst

    # Получить все факультеты
    # id - id факультета
    # TODO МАТВЕЙ
    def getFaculty(self, id):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT * FROM Faculties WHERE id = ?'
        cursor.execute(sqliteQuery, (id,))
        row = cursor.fetchall()[0]
        cursor.close()

        return Faculty(row[0], row[1])

    ####################################################################################################################

    # Создать таблицу образовательных программ
    def initEducationalProgram(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'CREATE TABLE EducationalPrograms(id INTEGER PRIMARY KEY, FacultyId INTEGER, ' \
                      'EducationalProgram TEXT) '
        cursor.execute(sqliteQuery)
        self.sqlite_connection.commit()
        cursor.close()

    # Очистить таблицу образовательных программ
    def clearEducationalProgram(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'DELETE FROM EducationalPrograms'
        cursor.execute(sqliteQuery)
        self.sqlite_connection.commit()
        cursor.close()

    # Добавить образовательную программу
    # FacultyId - id факультета
    # EducationalProgram - образовательная программа
    # TODO МАТВЕЙ
    def addEducationalProgram(self, facultyId, educationalProgram):
        cursor = self.sqlite_connection.cursor()

        # Проверка на то, что указанный facultyId существует
        sqliteQuery = 'SELECT EXISTS(SELECT 1 FROM Faculties WHERE id = ?); '
        cursor.execute(sqliteQuery, (facultyId,))
        rows = cursor.fetchall()
        for row in rows:
            if row[0] == 0:
                raise ValueError('This FacultyID does not exist!')

        # Проверка на то, что такая образовательная программа уже не существует в таблице
        sqliteQuery = 'SELECT EXISTS(SELECT 1 FROM EducationalPrograms WHERE FacultyId = ? AND EducationalProgram ' \
                      '= ?); '
        cursor.execute(sqliteQuery, (facultyId, educationalProgram,))
        rows = cursor.fetchall()
        for row in rows:
            if row[0] == 1:
                raise ValueError('This Educational program already exists!')

        sqliteQuery = 'INSERT INTO EducationalPrograms(`FacultyId`, `EducationalProgram`) ' \
                      'VALUES(?, ?)'
        cursor.execute(sqliteQuery, (facultyId, educationalProgram,))
        self.sqlite_connection.commit()
        cursor.close()

    # Изменить образовательную программу
    # id - id образовательной программы
    # FacultyId - id факультета
    # EducationalProgram - образовательная программа
    # TODO МАТВЕЙ
    def updateEducationalProgram(self, id, facultyId, educationalProgram):
        cursor = self.sqlite_connection.cursor()

        # Проверка на то, что указанный facultyId существует
        sqliteQuery = 'SELECT EXISTS(SELECT 1 FROM Faculties WHERE id = ?); '
        cursor.execute(sqliteQuery, (facultyId,))
        rows = cursor.fetchall()
        for row in rows:
            if row[0] == 0:
                raise ValueError('This FacultyID does not exist!')

        # Проверка на то, что такая образовательная программа уже не существует в таблице
        sqliteQuery = 'SELECT EXISTS(SELECT 1 FROM EducationalPrograms WHERE FacultyId = ? AND EducationalProgram ' \
                      '= ? AND id <> ?); '
        cursor.execute(sqliteQuery, (facultyId, educationalProgram, id,))
        rows = cursor.fetchall()
        for row in rows:
            if row[0] == 1:
                raise ValueError('This Educational program already exists!')

        sqliteQuery = 'UPDATE EducationalPrograms SET EducationalProgram = ?, FacultyId = ? WHERE id = ?'
        cursor.execute(sqliteQuery, (educationalProgram, facultyId, id,))
        self.sqlite_connection.commit()
        cursor.close()

    # Удалить образовательную программу
    # id - id образовательной программы
    # TODO МАТВЕЙ
    def removeEducationalProgram(self, id):
        cursor = self.sqlite_connection.cursor()

        # Идём сконца: находим те id специализаций, которые будут удалены следом. И удаляем. Вереница:
        # удаляем Subjects, Groups, Specializations, EducationalPrograms
        sqliteQuery = 'SELECT id FROM Specializations WHERE EducationalProgramId = ?'
        cursor.execute(sqliteQuery, (id,))
        rows = cursor.fetchall()
        dbManager = DatabaseManager()
        for row in rows:
            dbManager.removeSpecialization(row[0])

        sqliteQuery = 'DELETE FROM EducationalPrograms WHERE id = ?'
        cursor.execute(sqliteQuery, (id,))
        self.sqlite_connection.commit()
        cursor.close()

    # Получить все образовательные программы
    # TODO МАТВЕЙ
    def getAllEducationalProgram(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT * FROM EducationalPrograms'
        cursor.execute(sqliteQuery)
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append(EducationalProgram(row[0], row[1], row[2]))
        return lst

    # Получить образовательную программу
    # TODO МАТВЕЙ
    def getEducationalProgram(self, id):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT * FROM EducationalPrograms WHERE id = ?'
        cursor.execute(sqliteQuery, (id,))
        row = cursor.fetchall()[0]
        cursor.close()

        return EducationalProgram(row[0], row[1], row[2])

    # Получить образовательную программу
    # TODO МАТВЕЙ
    def getAllEducationalProgramByFaculty(self, facultyId):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT * FROM EducationalPrograms WHERE FacultyId = ?'
        cursor.execute(sqliteQuery, (facultyId,))
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append(EducationalProgram(row[0], row[1], row[2]))
        return lst

    ####################################################################################################################

    # Создать таблицу специализаций
    def initSpecialization(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'CREATE TABLE Specializations(id INTEGER PRIMARY KEY, ' \
                      'EducationalProgramId INTEGER, Specialization TEXT) '
        cursor.execute(sqliteQuery)
        self.sqlite_connection.commit()
        cursor.close()

    # Очистить таблицу специализаций
    def clearSpecialization(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'DELETE FROM Specializations'
        cursor.execute(sqliteQuery)
        self.sqlite_connection.commit()
        cursor.close()

    # Добавить специализацию
    # educationalProgramId - id образовательной программы
    # Specialization - специализация
    # TODO МАТВЕЙ
    def addSpecialization(self, educationalProgramId, specialization):
        cursor = self.sqlite_connection.cursor()

        # Проверка на то, что указанный educationalProgramId существует
        sqliteQuery = 'SELECT EXISTS(SELECT 1 FROM EducationalPrograms WHERE id = ?); '
        cursor.execute(sqliteQuery, (educationalProgramId,))
        rows = cursor.fetchall()
        for row in rows:
            if row[0] == 0:
                raise ValueError('This EducationalProgramId does not exist!')

        # Проверка на то, что такая специализация уже не существует в таблице
        sqliteQuery = 'SELECT EXISTS(SELECT 1 FROM Specializations WHERE EducationalProgramId = ? AND ' \
                      'Specialization = ?);'
        cursor.execute(sqliteQuery, (educationalProgramId, specialization,))
        rows = cursor.fetchall()
        for row in rows:
            if row[0] == 1:
                raise ValueError('This Specialization already exists!')

        sqliteQuery = 'INSERT INTO Specializations(`EducationalProgramId`, `Specialization`) ' \
                      'VALUES(?, ?)'
        cursor.execute(sqliteQuery, (educationalProgramId, specialization,))
        self.sqlite_connection.commit()
        cursor.close()

    # Изменить специализацию
    # id - id специализации
    # educationalProgramId - id образовательной программы
    # Specialization - специализация
    # TODO МАТВЕЙ
    def updateSpecialization(self, id, educationalProgramId, specialization):
        cursor = self.sqlite_connection.cursor()

        # Проверка на то, что указанный educationalProgramId существует
        # sqliteQuery = 'SELECT EXISTS(SELECT 1 FROM EducationalPrograms WHERE id = ?); '
        # cursor.execute(sqliteQuery, (educationalProgramId,))
        # rows = cursor.fetchall()
        # for row in rows:
        #    if row[0] == 0:
        #        raise ValueError('This EducationalProgramId does not exist!')

        # Проверка на то, что такая специализация уже не существует в таблице
        sqliteQuery = 'SELECT EXISTS(SELECT 1 FROM Specializations WHERE EducationalProgramId = ? AND' \
                      'Specialization = ? AND id <> ?); '
        cursor.execute(sqliteQuery, (educationalProgramId, specialization, id,))
        rows = cursor.fetchall()
        for row in rows:
            if row[0] == 1:
                raise ValueError('This Specialization already exists!')

        sqliteQuery = 'UPDATE Specializations SET Specialization = ?, EducationalProgramId = ? WHERE id = ?'
        cursor.execute(sqliteQuery, (specialization, educationalProgramId, id,))
        self.sqlite_connection.commit()
        cursor.close()

    # Удалить специализацию
    # id - id специализации
    # TODO МАТВЕЙ
    def removeSpecialization(self, id):
        cursor = self.sqlite_connection.cursor()

        # Идём сконца: находим те id групп, которые будут удалены следом. И удаляем. Вереница:
        # удаляем Groups, Subjects, Specializations
        sqliteQuery = 'SELECT id FROM Groups WHERE SpecializationId = ?'
        cursor.execute(sqliteQuery, (id,))
        rows = cursor.fetchall()
        dbManager = DatabaseManager()
        for row in rows:
            dbManager.removeGroup(row[0])

        sqliteQuery = 'SELECT id FROM Subjects WHERE SpecializationId = ?'
        cursor.execute(sqliteQuery, (id,))
        rows = cursor.fetchall()
        dbManager = DatabaseManager()
        for row in rows:
            dbManager.removeSubject(row[0])

        sqliteQuery = 'DELETE FROM Specializations WHERE id = ?'
        cursor.execute(sqliteQuery, (id,))
        self.sqlite_connection.commit()
        cursor.close()

    # Получить все специализации
    # TODO МАТВЕЙ
    def getAllSpecialization(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT * FROM Specializations'
        cursor.execute(sqliteQuery)
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append(Specialization(row[0], row[1], row[2]))
        return lst

    # Получить специализацию
    # TODO МАТВЕЙ
    def getSpecialization(self, id):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT * FROM Specializations WHERE id = ?'
        cursor.execute(sqliteQuery, (id,))
        row = cursor.fetchall()[0]
        cursor.close()

        return Specialization(row[0], row[1], row[2])

    # Получить все специализации
    # TODO МАТВЕЙ
    def getAllSpecializationByEdProgram(self, educationalProgramId):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT * FROM Specializations WHERE EducationalProgramId = ?'
        cursor.execute(sqliteQuery, (educationalProgramId,))
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append(Specialization(row[0], row[1], row[2]))
        return lst

    # for prolog
    def getAllSpecializationUniqueYears(self, specializationId):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT Distinct YearOfStudy FROM Groups WHERE SpecializationId=? ORDER BY YearOfStudy'
        cursor.execute(sqliteQuery, (specializationId,))
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append(row[0])

        return lst

    ####################################################################################################################

    # Создать таблицу групп
    def initGroup(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'CREATE TABLE Groups(id INTEGER PRIMARY KEY, SpecializationId INTEGER,' \
                      'Name TEXT, AmountOfStudents INTEGER, YearOfStudy INTEGER) '
        cursor.execute(sqliteQuery)
        self.sqlite_connection.commit()
        cursor.close()

    # Очистить таблицу групп
    def clearGroup(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'DELETE FROM Groups'
        cursor.execute(sqliteQuery)
        self.sqlite_connection.commit()
        cursor.close()

    # Добавить группу
    # specializationId - id специализации
    # name - имя группы
    # amountOfStudents - число студентов
    # yearOfStudy - од обучения
    # TODO МАТВЕЙ
    def addGroup(self, specializationId, name, amountOfStudents, yearOfStudy):
        if not (type(amountOfStudents) is int):
            raise ValueError("amount of students field must be a number")

        if not (type(yearOfStudy) is int):
            raise ValueError("year of study field must be a number")

        cursor = self.sqlite_connection.cursor()

        # Проверка на то, что указанный SpecializationId существует
        # sqliteQuery = 'SELECT EXISTS(SELECT 1 FROM Specializations WHERE id = ?); '
        # cursor.execute(sqliteQuery, (specializationId,))
        # rows = cursor.fetchall()
        # for row in rows:
        #    if row[0] == 0:
        #        raise ValueError('This SpecializationId does not exist!')

        # Проверка на то, что такая группа уже не существует в таблице
        sqliteQuery = 'SELECT EXISTS(SELECT 1 FROM Groups WHERE SpecializationId = ? AND ' \
                      'name = ? AND id <> ?);'
        cursor.execute(sqliteQuery, (specializationId, name, id))
        rows = cursor.fetchall()
        for row in rows:
            if row[0] == 1:
                raise ValueError('This group already exists!')

        sqliteQuery = 'INSERT INTO Groups(`SpecializationId`, `Name`, `AmountOfStudents`, `YearOfStudy`) VALUES(' \
                      '?, ?, ?, ?) '
        cursor.execute(sqliteQuery, (specializationId, name, amountOfStudents, yearOfStudy,))
        self.sqlite_connection.commit()
        cursor.close()

    # Изменить группу
    # specializationId - id специализации
    # name - имя группы
    # amountOfStudents - число студентов
    # yearOfStudy - од обучения
    # TODO МАТВЕЙ
    def updateGroup(self, id, specializationId, name, amountOfStudents, yearOfStudy):
        if not (type(amountOfStudents) is int):
            raise ValueError("amount of students field must be a number")

        if not (type(yearOfStudy) is int):
            raise ValueError("year of study field must be a number")

        cursor = self.sqlite_connection.cursor()

        # Проверка на то, что указанный SpecializationId существует
        sqliteQuery = 'SELECT EXISTS(SELECT 1 FROM Specializations WHERE id = ?); '
        cursor.execute(sqliteQuery, (specializationId,))
        rows = cursor.fetchall()
        for row in rows:
            if row[0] == 0:
                raise ValueError('This SpecializationId does not exist!')

        # Проверка на то, что такая группа уже не существует в таблице
        sqliteQuery = 'SELECT EXISTS(SELECT 1 FROM Groups WHERE SpecializationId = ? AND ' \
                      'name = ? AND id <> ?);'
        cursor.execute(sqliteQuery, (specializationId, name, id))
        rows = cursor.fetchall()
        for row in rows:
            if row[0] == 1:
                raise ValueError('This group already exists!')

        sqliteQuery = 'UPDATE Groups SET Name = ?, AmountOfStudents = ?, YearOfStudy = ?, SpecializationId = ?' \
                      ' WHERE id = ?'
        cursor.execute(sqliteQuery, (name, amountOfStudents, yearOfStudy, specializationId, id))
        self.sqlite_connection.commit()
        cursor.close()

    # Удалить группу
    # id - id группы
    # TODO МАТВЕЙ
    def removeGroup(self, id):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'DELETE FROM Groups WHERE id = ?'
        cursor.execute(sqliteQuery, (id,))
        self.sqlite_connection.commit()
        cursor.close()

    # TODO МАТВЕЙ
    def getAllGroup(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT * FROM Groups'
        cursor.execute(sqliteQuery)
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append(Group(row[0], row[1], row[2], row[3], row[4]))
        return lst

    # TODO МАТВЕЙ
    def getGroup(self, id):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT * FROM Groups WHERE id = ?'
        cursor.execute(sqliteQuery, (id,))
        row = cursor.fetchall()[0]
        cursor.close()

        return Group(row[0], row[1], row[2], row[3], row[4])

    # for prolog
    def getAllSpecializationGroups(self, specializationId, yearOfStudy):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT Name FROM Groups WHERE SpecializationId=? AND YearOfStudy=? ORDER BY YearOfStudy'
        cursor.execute(sqliteQuery, (specializationId, yearOfStudy,))
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append(row[0])

        return lst

    ####################################################################################################################

    # Создать таблицу предметов
    def initSubject(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'CREATE TABLE Subjects(id INTEGER PRIMARY KEY, SpecializationId INTEGER,' \
                      'Name TEXT, Semesters TEXT, TypeOfClass TEXT, Frequency INTEGER, TeacherId INTEGER,' \
                      'AmountOfGroups INTEGER, Generated INTEGER) '
        cursor.execute(sqliteQuery)
        self.sqlite_connection.commit()
        cursor.close()

    # Очистить таблицу предметов
    def clearSubject(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'DELETE FROM Subjects'
        cursor.execute(sqliteQuery)
        self.sqlite_connection.commit()
        cursor.close()

    # TODO МАТВЕЙ
    def addSubject(self, specializationId, name, semesters, typeOfClass, frequency, teacherId, amountOfGroups):
        generated = 0

        if not (type(amountOfGroups) is int):
            raise ValueError("amount of groups field must be a number")

        if not (1 <= amountOfGroups <= 100):
            raise ValueError("amount of groups field must be within 1..100")

        if not (type(frequency) is int):
            raise ValueError("frequency field must be a number")

        if not (1 <= frequency <= 100):
            raise ValueError("frequency field must be within 1..100")

        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'INSERT INTO Subjects(`SpecializationId`, `Name`, `Semesters`, `TypeOfClass`, `Frequency`, ' \
                      '`TeacherId`, `AmountOfGroups`, `Generated`) VALUES(?, ?, ?, ?, ?, ?, ?, ?) '
        cursor.execute(sqliteQuery, (specializationId, name, semesters, typeOfClass,
                                     frequency, teacherId, amountOfGroups, generated))
        self.sqlite_connection.commit()
        cursor.close()

    # TODO МАТВЕЙ
    def updateSubject(self, id, specializationId, name, semesters, typeOfClass, frequency, teacherId, amountOfGroups):
        if not (type(amountOfGroups) is int):
            raise ValueError("amount of groups field must be a number")

        if not (1 <= amountOfGroups <= 100):
            raise ValueError("amount of groups field must be within 1..100")

        if not (type(frequency) is int):
            raise ValueError("frequency field must be a number")

        if not (1 <= frequency <= 100):
            raise ValueError("frequency field must be within 1..100")

        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'UPDATE Subjects SET SpecializationId = ?, Name = ?, Semesters = ?, TypeOfClass = ?,' \
                      'Frequency = ?, TeacherId = ?, AmountOfGroups = ? WHERE id = ?'
        cursor.execute(sqliteQuery, (specializationId, name, semesters, typeOfClass,
                                     frequency, teacherId, amountOfGroups, id))
        self.sqlite_connection.commit()
        cursor.close()

    # Удалить занятие
    # id - id занятия
    # TODO МАТВЕЙ
    def removeSubject(self, id):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'DELETE FROM Subjects WHERE id = ?'
        cursor.execute(sqliteQuery, (id,))
        self.sqlite_connection.commit()
        cursor.close()

    # TODO МАТВЕЙ
    def getAllSubject(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT * FROM Subjects'
        cursor.execute(sqliteQuery)
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append(Subject(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
        return lst

    # TODO МАТВЕЙ
    def getSubject(self, id):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT * FROM Subjects WHERE id = ?'
        cursor.execute(sqliteQuery, (id,))
        row = cursor.fetchall()[0]
        cursor.close()

        return Subject(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])

    # for prolog
    def getAllSubjectsDistinct(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT DISTINCT SpecializationId, Name, Semesters FROM Subjects'
        cursor.execute(sqliteQuery)
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append([row[0], row[1], row[2]])
        return lst

    # for prolog
    def getAllSubjectTypesOfClass(self, specializationId, name, semesters):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT DISTINCT TypeOfClass, Frequency FROM Subjects WHERE SpecializationId=? AND Name=? ' \
                      'AND Semesters=? '
        cursor.execute(sqliteQuery, (specializationId, name, semesters,))
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append([row[0], row[1]])
        return lst

    # for prolog
    def getAllSubjectTeachers(self, specializationId, name, semesters, typeOfClass, Frequency):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT TeacherId, AmountOfGroups FROM Subjects WHERE SpecializationId=? AND Name=? AND ' \
                      'Semesters=? AND TypeOfClass=? AND Frequency=?'
        cursor.execute(sqliteQuery, (specializationId, name, semesters, typeOfClass, Frequency,))
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append([row[0], row[1]])
        return lst

    # for prolog
    def markAsGeneratedSubject(self):
        generated = 1
        dbManager = DatabaseManager()

        cursor = self.sqlite_connection.cursor()
        subjects = dbManager.getAllSubject()

        for subject in subjects:
            semesters = subject.getSemesters()
            currentSemester = dbManager.getConstraints().semester

            for semester in semesters:
                if int(semester) % 2 == currentSemester % 2:
                    sqliteQuery = 'UPDATE Subjects SET Generated = ? WHERE id = ?'
                    cursor.execute(sqliteQuery, (generated, subject.id,))

        self.sqlite_connection.commit()
        cursor.close()

    # for prolog (incremental adding)
    def getAllUngeneratedSubjects(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT * FROM Subjects WHERE Generated = 0'
        cursor.execute(sqliteQuery)
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append(Subject(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
        return lst

    ####################################################################################################################

    # Создать таблицу учителей
    def initTeacher(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'CREATE TABLE Teachers(id INTEGER PRIMARY KEY, Name TEXT, DaysCanWork, DaysWantWork, Weight)'
        cursor.execute(sqliteQuery)
        self.sqlite_connection.commit()
        cursor.close()

    # Очистить таблицу учителей
    def clearTeacher(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'DELETE FROM Teachers'
        cursor.execute(sqliteQuery)
        self.sqlite_connection.commit()
        cursor.close()

    # Матвей!!! Этот метод вызывается только диспетчером.
    # Уже потом препод сам через updateTeacher может убрать те дни, когда не может или не хочет работать
    # TODO МАТВЕЙ
    def addTeacher(self, name, daysCanWork, daysWantWork, weight):
        dbManager = DatabaseManager()
        constraints = dbManager.getConstraints()

        if not (type(weight) is int):
            raise ValueError("weight field must be a number")

        if not (0 <= weight <= 10):
            raise ValueError("weight field must be within 0..10")

        # Проверка на то, что учитель хочет работать в тот день, когда он не может
        canDays = daysCanWork[1:-1].split(";")
        wantDays = daysWantWork[1:-1].split(";")

        for i in range(len(canDays)):
            canTokens = canDays[i][1:-1].split(",")
            wantTokens = wantDays[i][1:-1].split(",")
            for j in range(len(wantTokens)):
                if (wantTokens[j] > constraints.classesPerDay) or (canTokens[j] > constraints.classesPerDay):
                    raise Exception('Пар в день может быть меньше, чем одно из указанных значений')
                if not (wantTokens[j] in canTokens) and wantTokens[j] != '':
                    raise Exception('Хочет работать в тот день, в который не может работать!')

        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'INSERT INTO Teachers(`Name`, `DaysCanWork`, `DaysWantWork`, `Weight`) VALUES(?, ' \
                      '?, ?, ?) '

        cursor.execute(sqliteQuery, (name, daysCanWork.replace(';', ','), daysWantWork.replace(';', ','), weight,))
        self.sqlite_connection.commit()
        cursor.close()

    # Матвей!!! Этот метод вызывается диспетчером и самим преподом.
    # Препод сам может убрать те дни, когда не может или не хочет работать
    # TODO МАТВЕЙ
    def updateTeacher(self, id, name, daysCanWork, daysWantWork, weight):
        if not (type(weight) is int):
            raise ValueError("weight field must be a number")

        if not (0 <= weight <= 10):
            raise ValueError("weight field must be within 0..10")

        # Проверка на то, что учитель хочет работать в тот день, когда он не может
        canDays = daysCanWork[1:-1].split(";")
        wantDays = daysWantWork[1:-1].split(";")

        for i in range(len(canDays)):
            canTokens = canDays[i][1:-1].split(",")
            wantTokens = wantDays[i][1:-1].split(",")
            for want in wantTokens:
                if not (want in canTokens) and want != '':
                    raise Exception('Хочет работать в тот день, в который не может работать!')

        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'UPDATE Teachers SET Name = ?, DaysCanWork = ?, DaysWantWork = ?, Weight = ? WHERE id = ?'
        cursor.execute(sqliteQuery, (name, daysCanWork.replace(';', ','), daysWantWork.replace(';', ','), weight, id))
        self.sqlite_connection.commit()
        cursor.close()

    # Удалить преподавателя
    # id - id преподавателя
    # TODO МАТВЕЙ
    def removeTeacher(self, id):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'DELETE FROM Teachers WHERE id = ?'
        cursor.execute(sqliteQuery, (id,))
        self.sqlite_connection.commit()
        cursor.close()

    # TODO МАТВЕЙ
    def getAllTeacher(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT * FROM Teachers'
        cursor.execute(sqliteQuery)
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append(Teacher(row[0], row[1], row[2], row[3], row[4]))
        return lst

    # TODO МАТВЕЙ
    def getTeacher(self, id):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT * FROM Teachers WHERE id = ?'
        cursor.execute(sqliteQuery, (id,))
        rows = cursor.fetchall()
        if len(rows) < 1:
            return
            # raise ValueError("No such teacher id!")
        row = rows[0]
        cursor.close()

        return Teacher(row[0], row[1], row[2], row[3], row[4])

    ####################################################################################################################

    # Создать таблицу аудиторий
    def initClassroom(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'CREATE TABLE Classrooms(id INTEGER PRIMARY KEY, Number TEXT, TypesOfClass TEXT,' \
                      'Capacity INTEGER) '
        cursor.execute(sqliteQuery)
        self.sqlite_connection.commit()
        cursor.close()

    # Очистить таблицу аудиторий
    def clearClassroom(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'DELETE FROM Classrooms'
        cursor.execute(sqliteQuery)
        self.sqlite_connection.commit()
        cursor.close()

    # TODO МАТВЕЙ
    def addClassroom(self, number, typesOfClass, capacity):
        if not (type(capacity) is int):
            raise ValueError("capacity field must be a number")

        # Проверка на то, что такая аудитория уже не существует в таблице
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT EXISTS(SELECT 1 FROM Classrooms WHERE Number= ?);'
        cursor.execute(sqliteQuery, (number,))
        rows = cursor.fetchall()
        for row in rows:
            if row[0] == 1:
                raise ValueError('This Classroom already exists!')

        sqliteQuery = 'INSERT INTO Classrooms(`Number`, `TypesOfClass`, `Capacity`) VALUES(?, ?, ?)'
        cursor.execute(sqliteQuery, (number, typesOfClass, capacity,))
        self.sqlite_connection.commit()
        cursor.close()

    # TODO МАТВЕЙ
    def updateClassroom(self, id, number, typesOfClass, capacity):
        if not (type(capacity) is int):
            raise ValueError("capacity field must be a number")

        # Проверка на то, что такая аудитория уже не существует в таблице
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT EXISTS(SELECT 1 FROM Classrooms WHERE Number= ? AND id <> ?);'
        cursor.execute(sqliteQuery, (number, id))
        rows = cursor.fetchall()
        for row in rows:
            if row[0] == 1:
                raise ValueError('This Classroom already exists!')

        sqliteQuery = 'UPDATE Classrooms SET Number = ?, TypesOfClass = ?, Capacity = ? WHERE id = ?'
        cursor.execute(sqliteQuery, (number, typesOfClass, capacity, id))
        self.sqlite_connection.commit()
        cursor.close()

    # TODO МАТВЕЙ
    def removeClassroom(self, id):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'DELETE FROM Classrooms WHERE id = ?'
        cursor.execute(sqliteQuery, (id,))
        self.sqlite_connection.commit()
        cursor.close()

    # TODO МАТВЕЙ
    def getAllClassroom(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT * FROM Classrooms'
        cursor.execute(sqliteQuery)
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append(Classroom(row[0], row[1], row[2], row[3]))
        return lst

    # TODO МАТВЕЙ
    def getClassroom(self, id):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT * FROM Classrooms WHERE id = ?'
        cursor.execute(sqliteQuery, (id,))
        row = cursor.fetchall()[0]
        cursor.close()

        return Classroom(row[0], row[1], row[2], row[3])

    ####################################################################################################################

    # Создать таблицу ограничений
    def initConstraints(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'CREATE TABLE Constraints(id INTEGER PRIMARY KEY, FirstClassStarts TEXT, ' \
                      'ClassDuration INTEGER, ShortBrakeDuration INTEGER, LargeBrakeDuration INTEGER, ' \
                      'StudyDaysInWeek INTEGER, StudyDaysInWeekForStudents INTEGER, ' \
                      'StudyDaysInWeekForTeachers INTEGER, ClassesPerDay INTEGER, ClassesPerDayStudents INTEGER,' \
                      'ClassesPerDayTeachers INTEGER, LunchBrake INTEGER, Gaps INTEGER, ClassroomFillness INTEGER,' \
                      'Semester INTEGER) '
        cursor.execute(sqliteQuery)
        self.sqlite_connection.commit()
        cursor.close()

    # Очистить таблицу ограничений
    def clearConstraints(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'DELETE FROM Constraints'
        cursor.execute(sqliteQuery)
        self.sqlite_connection.commit()
        cursor.close()

    # TODO МАТВЕЙ
    def addConstraints(self, firstClassStarts, classDuration, shortBrakeDuration, largeBrakeDuration, studyDaysInWeek,
                       studyDaysInWeekForStudents, studyDaysInWeekForTeachers, classesPerDay, classesPerDayStudents,
                       classesPerDayTeachers, lunchBrake, gaps, classroomFillness, semester):
        if not (type(classDuration) is int):
            raise ValueError("class duration field must be a number")

        if not (type(classesPerDay) is int):
            raise ValueError("classes per day field must be a number")

        if not (1 <= classDuration <= ((24 * 60) / classesPerDay)):
            raise ValueError("class duration field must be within 1..", ((24 * 60) / classesPerDay))

        if not (type(shortBrakeDuration) is int):
            raise ValueError("short brake duration field must be a number")

        if not (0 <= shortBrakeDuration <= ((24 * 60) / classesPerDay)):
            raise ValueError("short brake duration field must be within 1..", ((24 * 60) / classesPerDay))

        if not (type(largeBrakeDuration) is int):
            raise ValueError("large brake duration field must be a number")

        if not (0 <= largeBrakeDuration <= ((24 * 60) / classesPerDay)):
            raise ValueError("large brake duration field must be within 1..", ((24 * 60) / classesPerDay))

        if not (type(studyDaysInWeek) is int):
            raise ValueError("study days in week field must be a number")

        if not (1 <= studyDaysInWeek <= 7):
            raise ValueError("study days in week field must be within 1..7")

        if not (type(studyDaysInWeekForStudents) is int):
            raise ValueError("study days in week for students field must be a number")

        if not (studyDaysInWeekForStudents <= studyDaysInWeek):
            raise ValueError("study days in week for students field must be less than study days in week field")

        if not (1 <= studyDaysInWeekForStudents <= 7):
            raise ValueError("study days in week for students field must be within 1..7")

        if not (type(studyDaysInWeekForTeachers) is int):
            raise ValueError("study days in week for teachers field must be a number")

        if not (studyDaysInWeekForTeachers <= studyDaysInWeek):
            raise ValueError("study days in week for teachers field must be less than study days in week field")

        if not (1 <= studyDaysInWeekForTeachers <= 7):
            raise ValueError("study days in week for teachers field must be within 1..7")

        if not (type(classesPerDayTeachers) is int):
            raise ValueError("classes per day for teachers field must be a number")

        if not (classesPerDayTeachers <= classesPerDay):
            raise ValueError("classes per day for teachers field must be less than classes per day field")

        if not (1 <= classesPerDayTeachers <= ((24 * 60) / classDuration)):
            raise ValueError("study days in week for teachers field must be within 1..", ((24 * 60) / classDuration))

        if not (type(classesPerDayStudents) is int):
            raise ValueError("classes per day for students field must be a number")

        if not (classesPerDayStudents <= classesPerDay):
            raise ValueError("classes per day for students field must be less than classes per day field")

        if not (1 <= classesPerDayStudents <= ((24 * 60) / classDuration)):
            raise ValueError("study days in week for students field must be within 1..", ((24 * 60) / classDuration))

        if not (type(lunchBrake) is int):
            raise ValueError("lunch brake duration field must be a number")

        if not (0 <= lunchBrake <= ((24 * 60) / classesPerDay)):
            raise ValueError("lunch brake duration field must be within 0..", ((24 * 60) / classesPerDay))

        if not (type(gaps) is int):
            raise ValueError("gaps field must be a number")

        if not (0 <= gaps <= 10):
            raise ValueError("gaps field must be within 0..10")

        if not (type(classroomFillness) is int):
            raise ValueError("lunch brake duration field must be a number")

        if not (0 <= classroomFillness <= 10):
            raise ValueError("lunch brake duration field must be within 0..10")

        if not (type(semester) is int):
            raise ValueError("semester field must be a number")

        if not (1 <= semester <= 2):
            raise ValueError("semester field must be 1 or 2")

        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'INSERT INTO Constraints(`FirstClassStarts`, `ClassDuration`, `ShortBrakeDuration`, ' \
                      '`LargeBrakeDuration`, `StudyDaysInWeek`, `StudyDaysInWeekForStudents`, ' \
                      '`StudyDaysInWeekForTeachers`, `ClassesPerDay`, `ClassesPerDayStudents`, ' \
                      '`ClassesPerDayTeachers`, `LunchBrake`, `Gaps`, `ClassroomFillness`, `Semester`)' \
                      'VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) '
        cursor.execute(sqliteQuery, (firstClassStarts, classDuration,
                                     shortBrakeDuration, largeBrakeDuration,
                                     studyDaysInWeek, studyDaysInWeekForStudents,
                                     studyDaysInWeekForTeachers, classesPerDay,
                                     classesPerDayStudents, classesPerDayTeachers,
                                     lunchBrake, classroomFillness, gaps, semester))
        self.sqlite_connection.commit()
        cursor.close()

    # TODO МАТВЕЙ
    def updateConstraints(self, firstClassStarts, classDuration, shortBrakeDuration, largeBrakeDuration,
                          studyDaysInWeek,
                          studyDaysInWeekForStudents, studyDaysInWeekForTeachers, classesPerDay, classesPerDayStudents,
                          classesPerDayTeachers, lunchBrake, gaps, classroomFillness, semester):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'UPDATE Constraints SET FirstClassStarts = ?, ClassDuration = ?, ShortBrakeDuration = ?,' \
                      'LargeBrakeDuration = ?, StudyDaysInWeek = ?, StudyDaysInWeekForStudents = ?, ' \
                      'StudyDaysInWeekForTeachers = ?, ClassesPerDay = ?, ClassesPerDayStudents = ?,' \
                      'ClassesPerDayTeachers = ?, LunchBrake = ?, Gaps = ?, ClassroomFillness = ?, Semester = ?' \
                      'WHERE id = 1'
        cursor.execute(sqliteQuery, (firstClassStarts, classDuration,
                                     shortBrakeDuration, largeBrakeDuration,
                                     studyDaysInWeek, studyDaysInWeekForStudents,
                                     studyDaysInWeekForTeachers, classesPerDay,
                                     classesPerDayStudents, classesPerDayTeachers,
                                     lunchBrake, classroomFillness, gaps, semester))
        self.sqlite_connection.commit()
        cursor.close()

    # TODO МАТВЕЙ
    def removeConstraints(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'DELETE FROM Classrooms WHERE id = 1'
        cursor.execute(sqliteQuery)
        self.sqlite_connection.commit()
        cursor.close()

    # TODO МАТВЕЙ
    def getConstraints(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT * FROM Constraints'
        cursor.execute(sqliteQuery)
        row = cursor.fetchall()[0]
        cursor.close()

        return Constraints(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                           row[10], row[11], row[12], row[13], row[14])

    ####################################################################################################################

    def initGeneratedScheduleTable(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'DROP TABLE IF EXISTS GeneratedSchedule;'
        cursor.execute(sqliteQuery)
        sqliteQuery = 'DROP TABLE IF EXISTS ClassToGroups;'
        cursor.execute(sqliteQuery)
        sqliteQuery = 'CREATE TABLE GeneratedSchedule(id INTEGER PRIMARY KEY, Faculty TEXT, ' \
                      'EducationalProgram TEXT, Specialization TEXT, Subject TEXT, Semester INTEGER, Teacher TEXT, ' \
                      'TypeOfClass TEXT, Auditory TEXT, Groups TEXT, Day INTEGER, ClassNumber INTEGER, ' \
                      'TeacherId INTEGER)'
        cursor.execute(sqliteQuery)
        sqliteQuery = 'CREATE TABLE ClassToGroups (id INTEGER PRIMARY KEY, ClassId INTEGER, ' \
                      'GroupName TEXT)'
        cursor.execute(sqliteQuery)

        self.sqlite_connection.commit()
        cursor.close()

    def addGeneratedClass(self, classId, faculty, edProgram, specialization, subject, semester, teacher, typeOfClass,
                          auditory, groupsList, day, classNumber, teacherId):

        groups = disassemblePrologList(groupsList)

        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'INSERT INTO GeneratedSchedule(`Faculty`, `EducationalProgram`, `Specialization`, `Subject`,' \
                      '`Semester`, `Teacher`, `TypeOfClass`, `Auditory`, `Groups`, `Day`, `ClassNumber`, `TeacherId`' \
                      ') VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) '
        cursor.execute(sqliteQuery, (faculty, edProgram, specialization, subject, semester, teacher, typeOfClass,
                                     auditory, groupsList, day, classNumber, teacherId,))

        ############################ GROUPS ARE ADDED SEPERATELY #######################

        for group in groups:
            sqliteQuery = 'INSERT INTO ClassToGroups(`ClassId`, `GroupName`) VALUES(?, ?) '
            cursor.execute(sqliteQuery, (classId, group,))

        self.sqlite_connection.commit()
        cursor.close()

    # Возвращаем все сгенерированные занятия
    # TODO МАТВЕЙ
    def getAllGeneratedClass(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT * FROM GeneratedSchedule'
        cursor.execute(sqliteQuery)
        rows = cursor.fetchall()
        self.sqlite_connection.commit()
        cursor.close()

        lst = []
        for i in range(len(rows)):
            lst.append(
                GeneratedClass(rows[i][0], rows[i][1], rows[i][2], rows[i][3], rows[i][4], rows[i][5], rows[i][6],
                               rows[i][7], rows[i][8], rows[i][9], rows[i][10], rows[i][11], rows[i][12]))
        return lst

    # Возвращаем все сгенерированное занятие по id
    # TODO МАТВЕЙ
    def getGeneratedClass(self, id):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT * FROM GeneratedSchedule WHERE id = ?'
        cursor.execute(sqliteQuery, (id,))
        row = cursor.fetchall()[0]
        self.sqlite_connection.commit()
        cursor.close()

        return GeneratedClass(row[0], row[1], row[2], row[3], row[4], row[5], row[6],
                              row[7], row[8], row[9], row[10], row[11], row[12])

    # Получить список из всех групп, которые отнесены к конкретному занятию
    # TODO МАТВЕЙ
    def getAllGroupsOfClass(self, classId):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT * FROM ClassToGroups WHERE ClassId = ?'
        cursor.execute(sqliteQuery, (classId,))
        rows = cursor.fetchall()
        self.sqlite_connection.commit()
        cursor.close()

        lst = []
        for row in rows:
            lst.append(row[2])
        return lst

    # TODO МАТВЕЙ
    def getAllGeneratedTeachers(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT DISTINCT Teacher, TeacherId FROM GeneratedSchedule'
        cursor.execute(sqliteQuery)
        rows = cursor.fetchall()
        self.sqlite_connection.commit()
        cursor.close()

        lst = []
        for row in rows:
            lst.append(ScheduleTeacher(row[12], row[6], shortenName(row[6])))
        return lst

    ####################################################################################################################

    # Формат - объект класса Schedule, который содержит:
    # 1) Теоретическое число пар
    # 2) Число учебных дней
    # 3) список из 6 элементов - объектов класса ScheduleEntity, который содержит:
    #       String: название предмета
    #       String: тип занятия
    #       String: преподаватель
    #       String: аудитория
    #       String: группы
    #       String: номер пары
    #       String: время
    # TODO МАТВЕЙ
    def getScheduleStudents(self, groupName):
        dbManager = DatabaseManager()

        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT * FROM ClassToGroups WHERE GroupName = ?'
        cursor.execute(sqliteQuery, (groupName,))
        rows = cursor.fetchall()

        schedule = []
        for day in range(studyDaysInWeek):
            scheduleDay = []
            for row in rows:
                sqliteQuery = 'SELECT * FROM GeneratedSchedule WHERE id = ?'
                cursor.execute(sqliteQuery, (row[1],))
                rows2 = cursor.fetchall()
                for row2 in rows2:
                    if day == (int(row2[10]) - 1):
                        hours, minutes = calculateTimeStart(int(row2[11]))
                        h = str(hours)
                        if minutes < 10:
                            m = "0" + str(minutes)
                        else:
                            m = str(minutes)
                        time = h + ":" + m
                        scheduleDay.append(
                            ScheduleEntity(row2[4], row2[7], row2[6], row2[8], row2[9], row2[11], time))
            schedule.append(scheduleDay)

        self.sqlite_connection.commit()
        cursor.close()

        return Schedule(dbManager.getConstraints().classesPerDay, dbManager.getConstraints().studyDaysInWeek,
                        schedule)

    # Формат - объект класса Schedule, который содержит:
    # 1) Теоретическое число пар
    # 2) Число учебных дней
    # 3) список из 6 элементов - объектов класса ScheduleEntity, который содержит:
    #       String: название предмета
    #       String: тип занятия
    #       String: преподаватель
    #       String: аудитория
    #       String: группы
    #       String: номер пары
    #       String: время
    # TODO МАТВЕЙ
    def getScheduleTeachers(self, teacherName):
        dbManager = DatabaseManager()

        schedule = []
        cursor = self.sqlite_connection.cursor()
        for day in range(studyDaysInWeek):
            scheduleDay = []
            sqliteQuery = 'SELECT * FROM GeneratedSchedule WHERE Teacher = ?'
            cursor.execute(sqliteQuery, (teacherName,))
            rows = cursor.fetchall()
            for row in rows:
                if day == (int(row[10]) - 1):
                    hours, minutes = calculateTimeStart(int(row[11]))
                    h = str(hours)
                    if minutes < 10:
                        m = "0" + str(minutes)
                    else:
                        m = str(minutes)
                    time = h + ":" + m
                    scheduleDay.append(
                        ScheduleEntity(row[4], row[7], row[6], row[8], row[9], row[11], time))
            schedule.append(scheduleDay)

        self.sqlite_connection.commit()
        cursor.close()

        return Schedule(dbManager.getConstraints().classesPerDay, dbManager.getConstraints().studyDaysInWeek,
                        schedule)

    ####################################################################################################################

    ####################################################################################################################

    # TODO МАТВЕЙ
    def yearShiftRight(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT * FROM Groups'
        cursor.execute(sqliteQuery)
        rows = cursor.fetchall()
        cursor.close()

        for row in rows:
            dbManager = DatabaseManager()
            dbManager.updateGroup(row[0], row[1], row[2], row[3], row[4] + 1)

    # TODO МАТВЕЙ
    def yearShiftLeft(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT * FROM Groups'
        cursor.execute(sqliteQuery)
        rows = cursor.fetchall()
        cursor.close()

        for row in rows:
            dbManager = DatabaseManager()
            dbManager.updateGroup(row[0], row[1], row[2], row[3], row[4] - 1)

    ####################################################################################################################

    # TODO functions working with generated timetable will be written later because of new solver
    def clearAll(self):
        cursor = self.sqlite_connection.cursor()
        cursor.execute('DELETE FROM Classrooms')
        cursor.execute('DELETE FROM Constraints')
        cursor.execute('DELETE FROM EducationalPrograms')
        cursor.execute('DELETE FROM Faculties')
        cursor.execute('DELETE FROM Groups')
        cursor.execute('DELETE FROM Subjects')
        cursor.execute('DELETE FROM Teachers')
        self.sqlite_connection.commit()
        cursor.close()

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

    def close(self):
        if self.sqlite_connection:
            self.sqlite_connection.close()

    ####################################################################################################################
    # УЧЕТКИ
    ####################################################################################################################

    # Создать таблицу пользователей с админом
    # role:
    # 0 - главный диспетчер (его нельзя удалить)
    # 1 - диспетчер
    # 2 - преподаватель
    # 3 - простой юзер
    # status:
    # 0 - приглашение отправлено, но не принято
    # 1 - приглашение принято, пользователь зарегистрирован
    def initUsers(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'CREATE TABLE Users(id INTEGER PRIMARY KEY, Name TEXT, Email TEXT, PasswordHash TEXT, ' \
                      'Role INTEGER, TeacherId INTEGER, Status INTEGER, UpdatedDate TEXT, CreatedDate TEXT,' \
                      'SignedUpDate TEXT)'
        cursor.execute(sqliteQuery)
        sqliteQuery = 'INSERT INTO Users(`Name`, `Email`, `PasswordHash`, `Role`, `Status`, ' \
                      '`UpdatedDate`, `CreatedDate`, `SignedUpDate`) ' \
                      'VALUES(?, ?, ?, ?, ?, ?, ?, ?)'
        date = datetime.datetime.now()
        cursor.execute(sqliteQuery, ("Admin", "volfilya@gmail.com", "1234", 0, 1, date, date, date))
        self.sqlite_connection.commit()
        cursor.close()

    # Очистить таблицу факультетов
    def clearUsers(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'DELETE FROM Faculties WHERE id <> 1'
        cursor.execute(sqliteQuery)
        self.sqlite_connection.commit()
        cursor.close()

    # TODO Матвей
    def addUser(self, name, role, email=None, teacherId=None):
        if role == 0:
            raise ValueError("chief dispatcher can be only one!")

        if role != 1 and role != 2 and role != 3:
            raise ValueError("No such role!")

        if role == 2:
            dbManager = DatabaseManager()
            teacher = dbManager.getTeacher(teacherId)
            if teacher is None:
                raise ValueError("No such teacher id!")
            if teacher.name != name:
                raise ValueError("Names do not coincide!")

        cursor = self.sqlite_connection.cursor()

        if email is not None:
            # Проверка на то, что такая образовательная программа уже не существует в таблице
            sqliteQuery = 'SELECT EXISTS(SELECT 1 FROM Users WHERE Email = ?); '
            cursor.execute(sqliteQuery, (email,))
            rows = cursor.fetchall()
            for row in rows:
                if row[0] == 1:
                    raise ValueError('A user with this email already exists!')

        sqliteQuery = 'INSERT INTO Users(`Name`, `Email`, `Role`, `TeacherId`, `Status`, `UpdatedDate`,' \
                      '`CreatedDate`) ' \
                      'VALUES(?, ?, ?, ?, ?, ?, ?)'
        date = datetime.datetime.now()
        cursor.execute(sqliteQuery, (name, email, role, teacherId, 0, date, date))

        sqliteQuery = 'SELECT MAX(id) FROM Users'
        cursor.execute(sqliteQuery)
        row = cursor.fetchall()[0]

        self.sqlite_connection.commit()
        cursor.close()

        return row[0]

    # TODO Матвей
    def updateUser(self, id, name, role, email=None, teacherId=None):
        if role == 0:
            raise ValueError("chief dispatcher can be only one!")

        if role != 1 and role != 2 and role != 3:
            raise ValueError("No such role!")

        if role == 2:
            dbManager = DatabaseManager()
            teacher = dbManager.getTeacher(teacherId)
            if teacher is None:
                raise ValueError("No such teacher id!")
            if teacher.name != name:
                raise ValueError("Names do not coincide!")

        cursor = self.sqlite_connection.cursor()

        if email is not None:
            # Проверка на то, что такая образовательная программа уже не существует в таблице
            sqliteQuery = 'SELECT EXISTS(SELECT 1 FROM Users WHERE Email = ?); '
            cursor.execute(sqliteQuery, (email,))
            rows = cursor.fetchall()
            for row in rows:
                if row[0] == 1:
                    raise ValueError('A user with this email already exists!')

        sqliteQuery = 'UPDATE Users SET Name = ?, Email = ?, Role = ?, TeacherId = ?, UpdatedDate = ? WHERE id = ?'
        date = datetime.datetime.now()
        cursor.execute(sqliteQuery, (name, email, role, teacherId, date, id))

        sqliteQuery = 'SELECT MAX(id) FROM Users'
        cursor.execute(sqliteQuery)
        row = cursor.fetchall()[0]

        self.sqlite_connection.commit()
        cursor.close()

        return row[0]

    # TODO Матвей
    def removeUser(self, id):
        dbManager = DatabaseManager()
        if (dbManager.getUser(id).role == 0):
            raise ValueError("Cannot remove the chief dispatcher!")

        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'DELETE FROM Users WHERE id = ?'
        cursor.execute(sqliteQuery, (id,))
        self.sqlite_connection.commit()
        cursor.close()

    # TODO МАТВЕЙ
    def getAllUser(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT * FROM Users'
        cursor.execute(sqliteQuery)
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append(User(row[0], row[1], row[2], row[4], row[5], row[6], row[7], row[8], row[9]))
        return lst

    # TODO МАТВЕЙ
    def getUser(self, id):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT * FROM Users WHERE id = ?'
        cursor.execute(sqliteQuery, (id,))
        row = cursor.fetchall()[0]
        cursor.close()

        return User(row[0], row[1], row[2], row[4], row[5], row[6], row[7], row[8], row[9])

    # когда через почту подтверждает свое участие + когда уже задал пароль:
    # TODO МАТВЕЙ
    def signUpUser(self, id, passwordHash):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'UPDATE Users SET PasswordHash = ?, Status = 1, UpdatedDate = ?, SignedUpDate = ? WHERE id = ?'
        date = datetime.datetime.now()
        cursor.execute(sqliteQuery, (passwordHash, date, date, id))
        self.sqlite_connection.commit()
        cursor.close()

    # во время входа: для сверки, которая происходит у Матвея, нужно вернуть хеш пароля. По уникальной почте
    # TODO МАТВЕЙ
    def getPasswordByEmailHashUser(self, email):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT PasswordHash FROM Users WHERE email = ?'
        cursor.execute(sqliteQuery, (email,))
        row = cursor.fetchall()[0]
        cursor.close()

        return row[0]

    # во время входа: для сверки, которая происходит у Матвея, нужно вернуть хеш пароля. По уникальной почте
    # TODO МАТВЕЙ
    def getIdByEmailUser(self, email):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT id FROM Users WHERE email = ?'
        cursor.execute(sqliteQuery, (email,))
        row = cursor.fetchall()[0]
        cursor.close()

        return row[0]


# Функция рассчитывает время начала пары
def calculateTimeStart(classNumber):
    dbManager = DatabaseManager()
    constraints = dbManager.getConstraints()
    classesPerDay = int(constraints.classesPerDay)
    startTime = constraints.firstClassStarts
    classDuration = int(constraints.classDuration)
    shortBrake = int(constraints.shortBrakeDuration)
    longBrake = int(constraints.largeBrakeDuration)

    inMinutes = (classNumber - 1) * (classDuration + shortBrake + longBrake)

    if classNumber > classesPerDay:
        return -1, -1

    time = datetime.datetime(2000, 1, 1, int(startTime.split(",")[0]), int(startTime.split(",")[1]), 0) + \
           datetime.timedelta(minutes=inMinutes)

    return time.hour, time.minute


# Функция рассчитывает время конца пары
def calculateTimeEnd(classNumber):
    dbManager = DatabaseManager()
    constraints = dbManager.getConstraints()
    classesPerDay = int(constraints.classesPerDay)
    startTime = constraints.firstClassStarts
    classDuration = int(constraints.classDuration)
    shortBrake = int(constraints.shortBrakeDuration)
    longBrake = int(constraints.largeBrakeDuration)

    inMinutes = (classNumber - 1) * (classDuration + shortBrake + longBrake) + classDuration + shortBrake

    if classNumber > classesPerDay:
        return -1, -1

    time = datetime.datetime(2000, 1, 1, int(startTime.split(",")[0]), int(startTime.split(",")[1]), 0) + \
           datetime.timedelta(minutes=inMinutes)

    return time.hour, time.minute


def disassemblePrologList(groupsList):
    prologList2 = groupsList[1:len(groupsList) - 1]
    groups = prologList2.split(",")

    return groups


def shortenName(name):
    token = name.split(" ")
    return token[0] + token[1][0] + ". " + token[2][0] + "."
