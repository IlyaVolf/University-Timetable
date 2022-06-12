import sqlite3

from entities.Faculty import Faculty
from entities.Constraints import Constraints
from entities.EducationalProgram import EducationalProgram
from entities.GeneratedClass import GeneratedClass
from entities.Specialization import Specialization
from entities.Group import Group
from entities.Subject import Subject
from entities.Teacher import Teacher
from entities.Classroom import Classroom


def tupleToList(t):
    lst = []
    for row in t:
        lst.append(row[0])
    return lst


class DatabaseManager:
    studyDaysInWeek = 6

    def __init__(self, dbFileName='timetable.sqlite'):
        try:
            self.sqlite_connection = sqlite3.connect(dbFileName)
        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite", error)

    ########################################################################################################################

    ########################################################################################################################

    # Создать таблицу факультетов
    def initFaculty(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'CREATE TABLE FacultiesNEW(id INTEGER PRIMARY KEY, Faculty TEXT)'
        cursor.execute(sqliteQuery)
        self.sqlite_connection.commit()
        cursor.close()

    # Очистить таблицу факультетов
    def clearFaculty(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'DELETE FROM FacultiesNEW'
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
        sqliteQuery = 'SELECT EXISTS(SELECT 1 FROM FacultiesNEW WHERE Faculty= ? AND id <> ?);'
        cursor.execute(sqliteQuery, (faculty, id,))
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

        # Идём сконца: находим те id образ програм, которые будут удалены следом. И удаляем. Вереница:
        # удаляем Subjects, Groups, Specializations, EducationalPrograms и, окончательно, Faculties.
        sqliteQuery = 'SELECT id FROM EducationalProgramsNEW WHERE FacultyId = ?'
        cursor.execute(sqliteQuery, (id,))
        rows = cursor.fetchall()
        dbManager = DatabaseManager()
        for row in rows:
            dbManager.removeEducationalProgram(row[0])

        sqliteQuery = 'DELETE FROM FacultiesNEW WHERE id = ?'
        cursor.execute(sqliteQuery, (id,))
        self.sqlite_connection.commit()
        cursor.close()

    # Получить все факультеты
    def getAllFaculty(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT * FROM FacultiesNEW'
        cursor.execute(sqliteQuery)
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append(Faculty(row[0], row[1]))
        return lst

    # Получить все факультеты
    # id - id факультета
    def getFaculty(self, id):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT * FROM FacultiesNEW WHERE id = ?'
        cursor.execute(sqliteQuery, (id,))
        row = cursor.fetchall()[0]
        cursor.close()

        return Faculty(row[0], row[1])

    ########################################################################################################################

    # Создать таблицу образовательных программ
    def initEducationalProgram(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'CREATE TABLE EducationalProgramsNEW(id INTEGER PRIMARY KEY, FacultyId INTEGER, ' \
                      'EducationalProgram TEXT) '
        cursor.execute(sqliteQuery)
        self.sqlite_connection.commit()
        cursor.close()

    # Очистить таблицу образовательных программ
    def clearEducationalProgram(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'DELETE FROM EducationalProgramsNEW'
        cursor.execute(sqliteQuery)
        self.sqlite_connection.commit()
        cursor.close()

    # Добавить образовательную программу
    # FacultyId - id факультета
    # EducationalProgram - образовательная программа
    def addEducationalProgram(self, facultyId, educationalProgram):
        cursor = self.sqlite_connection.cursor()

        # Проверка на то, что указанный facultyId существует
        sqliteQuery = 'SELECT EXISTS(SELECT 1 FROM FacultiesNEW WHERE id = ?); '
        cursor.execute(sqliteQuery, (facultyId,))
        rows = cursor.fetchall()
        for row in rows:
            if row[0] == 0:
                raise ValueError('This FacultyID does not exist!')

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

        # Проверка на то, что указанный facultyId существует
        sqliteQuery = 'SELECT EXISTS(SELECT 1 FROM FacultiesNEW WHERE id = ?); '
        cursor.execute(sqliteQuery, (facultyId,))
        rows = cursor.fetchall()
        for row in rows:
            if row[0] == 0:
                raise ValueError('This FacultyID does not exist!')

        # Проверка на то, что такая образовательная программа уже не существует в таблице
        sqliteQuery = 'SELECT EXISTS(SELECT 1 FROM EducationalProgramsNEW WHERE FacultyId = ? AND EducationalProgram ' \
                      '= ? AND id <> ?); '
        cursor.execute(sqliteQuery, (facultyId, educationalProgram, id,))
        rows = cursor.fetchall()
        for row in rows:
            if row[0] == 1:
                raise ValueError('This Educational program already exists!')

        sqliteQuery = 'UPDATE EducationalProgramsNEW SET EducationalProgram = ?, FacultyId = ? WHERE id = ?'
        cursor.execute(sqliteQuery, (educationalProgram, facultyId, id,))
        self.sqlite_connection.commit()
        cursor.close()

    # Удалить образовательную программу
    # id - id образовательной программы
    def removeEducationalProgram(self, id):
        cursor = self.sqlite_connection.cursor()

        # Идём сконца: находим те id специализаций, которые будут удалены следом. И удаляем. Вереница:
        # удаляем Subjects, Groups, Specializations, EducationalPrograms
        sqliteQuery = 'SELECT id FROM SpecializationsNEW WHERE EducationalProgramId = ?'
        cursor.execute(sqliteQuery, (id,))
        rows = cursor.fetchall()
        dbManager = DatabaseManager()
        for row in rows:
            dbManager.removeSpecialization(row[0])

        sqliteQuery = 'DELETE FROM EducationalProgramsNEW WHERE id = ?'
        cursor.execute(sqliteQuery, (id,))
        self.sqlite_connection.commit()
        cursor.close()

    # Получить все образовательные программы
    def getAllEducationalProgram(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT * FROM EducationalProgramsNEW'
        cursor.execute(sqliteQuery)
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append(EducationalProgram(row[0], row[1], row[2]))
        return lst

    # Получить образовательную программу
    def getEducationalProgram(self, id):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT * FROM EducationalProgramsNEW WHERE id = ?'
        cursor.execute(sqliteQuery, (id,))
        row = cursor.fetchall()[0]
        cursor.close()

        return EducationalProgram(row[0], row[1], row[2])

    # Получить образовательную программу
    def getAllEducationalProgramByFaculty(self, facultyId):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT * FROM EducationalProgramsNEW WHERE id = ?'
        cursor.execute(sqliteQuery, (facultyId,))
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append(EducationalProgram(row[0], row[1], row[2]))
        return lst

    ########################################################################################################################

    # Создать таблицу специализаций
    def initSpecialization(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'CREATE TABLE SpecializationsNEW(id INTEGER PRIMARY KEY, ' \
                      'EducationalProgramId INTEGER, Specialization TEXT) '
        cursor.execute(sqliteQuery)
        self.sqlite_connection.commit()
        cursor.close()

    # Очистить таблицу специализаций
    def clearSpecialization(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'DELETE FROM SpecializationsNEW'
        cursor.execute(sqliteQuery)
        self.sqlite_connection.commit()
        cursor.close()

    # Добавить специализацию
    # educationalProgramId - id образовательной программы
    # Specialization - специализация
    def addSpecialization(self, educationalProgramId, specialization):
        cursor = self.sqlite_connection.cursor()

        # Проверка на то, что указанный educationalProgramId существует
        sqliteQuery = 'SELECT EXISTS(SELECT 1 FROM EducationalProgramsNEW WHERE id = ?); '
        cursor.execute(sqliteQuery, (educationalProgramId,))
        rows = cursor.fetchall()
        for row in rows:
            if row[0] == 0:
                raise ValueError('This EducationalProgramId does not exist!')

        # Проверка на то, что такая специализация уже не существует в таблице
        sqliteQuery = 'SELECT EXISTS(SELECT 1 FROM SpecializationsNEW WHERE EducationalProgramId = ? AND ' \
                      'Specialization = ?);'
        cursor.execute(sqliteQuery, (educationalProgramId, specialization,))
        rows = cursor.fetchall()
        for row in rows:
            if row[0] == 1:
                raise ValueError('This Specialization already exists!')

        sqliteQuery = 'INSERT INTO SpecializationsNEW(`EducationalProgramId`, `Specialization`) ' \
                      'VALUES(?, ?)'
        cursor.execute(sqliteQuery, (educationalProgramId, specialization,))
        self.sqlite_connection.commit()
        cursor.close()

    # Изменить специализацию
    # id - id специализации
    # educationalProgramId - id образовательной программы
    # Specialization - специализация
    def updateSpecialization(self, id, educationalProgramId, specialization):
        cursor = self.sqlite_connection.cursor()

        # Проверка на то, что указанный educationalProgramId существует
        # sqliteQuery = 'SELECT EXISTS(SELECT 1 FROM EducationalProgramsNEW WHERE id = ?); '
        # cursor.execute(sqliteQuery, (educationalProgramId,))
        # rows = cursor.fetchall()
        # for row in rows:
        #    if row[0] == 0:
        #        raise ValueError('This EducationalProgramId does not exist!')

        # Проверка на то, что такая специализация уже не существует в таблице
        sqliteQuery = 'SELECT EXISTS(SELECT 1 FROM SpecializationsNEW WHERE EducationalProgramId = ? AND' \
                      'Specialization = ? AND id <> ?); '
        cursor.execute(sqliteQuery, (educationalProgramId, specialization, id,))
        rows = cursor.fetchall()
        for row in rows:
            if row[0] == 1:
                raise ValueError('This Specialization already exists!')

        sqliteQuery = 'UPDATE SpecializationsNEW SET Specialization = ?, EducationalProgramId = ? WHERE id = ?'
        cursor.execute(sqliteQuery, (specialization, educationalProgramId, id,))
        self.sqlite_connection.commit()
        cursor.close()

    # Удалить специализацию
    # id - id специализации
    def removeSpecialization(self, id):
        cursor = self.sqlite_connection.cursor()

        # Идём сконца: находим те id групп, которые будут удалены следом. И удаляем. Вереница:
        # удаляем Groups, Subjects, Specializations
        sqliteQuery = 'SELECT id FROM GroupsNEW WHERE SpecializationId = ?'
        cursor.execute(sqliteQuery, (id,))
        rows = cursor.fetchall()
        dbManager = DatabaseManager()
        for row in rows:
            dbManager.removeGroup(row[0])

        sqliteQuery = 'SELECT id FROM SubjectsNEW WHERE SpecializationId = ?'
        cursor.execute(sqliteQuery, (id,))
        rows = cursor.fetchall()
        dbManager = DatabaseManager()
        for row in rows:
            dbManager.removeSubject(row[0])

        sqliteQuery = 'DELETE FROM SpecializationsNEW WHERE id = ?'
        cursor.execute(sqliteQuery, (id,))
        self.sqlite_connection.commit()
        cursor.close()

    # Получить все специализации
    def getAllSpecialization(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT * FROM SpecializationsNEW'
        cursor.execute(sqliteQuery)
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append(Specialization(row[0], row[1], row[2]))
        return lst

    # Получить специализацию
    def getSpecialization(self, id):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT * FROM SpecializationsNEW WHERE id = ?'
        cursor.execute(sqliteQuery, (id,))
        row = cursor.fetchall()[0]
        cursor.close()

        return Specialization(row[0], row[1], row[2])

    # Получить все специализации
    def getAllSpecializationByEdProgram(self, educationalProgramId):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT * FROM SpecializationsNEW WHERE EducationalProgramId = ?'
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
        sqliteQuery = 'SELECT Distinct YearOfStudy FROM GroupsNEW WHERE SpecializationId=? ORDER BY YearOfStudy'
        cursor.execute(sqliteQuery, (specializationId,))
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append(row[0])

        return lst

    ########################################################################################################################

    # Создать таблицу групп
    def initGroup(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'CREATE TABLE GroupsNEW(id INTEGER PRIMARY KEY, SpecializationId INTEGER,' \
                      'Name TEXT, AmountOfStudents INTEGER, YearOfStudy INTEGER) '
        cursor.execute(sqliteQuery)
        self.sqlite_connection.commit()
        cursor.close()

    # Очистить таблицу групп
    def clearGroup(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'DELETE FROM GroupsNEW'
        cursor.execute(sqliteQuery)
        self.sqlite_connection.commit()
        cursor.close()

    # Добавить группу
    # specializationId - id специализации
    # name - имя группы
    # amountOfStudents - число студентов
    # yearOfStudy - од обучения
    def addGroup(self, specializationId, name, amountOfStudents, yearOfStudy):
        if not (type(amountOfStudents) is int):
            raise ValueError("amount of students field must be a number")

        if not (type(yearOfStudy) is int):
            raise ValueError("year of study field must be a number")

        cursor = self.sqlite_connection.cursor()

        # Проверка на то, что указанный SpecializationId существует
        # sqliteQuery = 'SELECT EXISTS(SELECT 1 FROM SpecializationsNEW WHERE id = ?); '
        # cursor.execute(sqliteQuery, (specializationId,))
        # rows = cursor.fetchall()
        # for row in rows:
        #    if row[0] == 0:
        #        raise ValueError('This SpecializationId does not exist!')

        # Проверка на то, что такая группа уже не существует в таблице
        sqliteQuery = 'SELECT EXISTS(SELECT 1 FROM GroupsNEW WHERE SpecializationId = ? AND ' \
                      'name = ? AND id <> ?);'
        cursor.execute(sqliteQuery, (specializationId, name, id))
        rows = cursor.fetchall()
        for row in rows:
            if row[0] == 1:
                raise ValueError('This group already exists!')

        sqliteQuery = 'INSERT INTO GroupsNEW(`SpecializationId`, `Name`, `AmountOfStudents`, `YearOfStudy`) VALUES(' \
                      '?, ?, ?, ?) '
        cursor.execute(sqliteQuery, (specializationId, name, amountOfStudents, yearOfStudy,))
        self.sqlite_connection.commit()
        cursor.close()

    # Изменить группу
    # specializationId - id специализации
    # name - имя группы
    # amountOfStudents - число студентов
    # yearOfStudy - од обучения
    def updateGroup(self, id, specializationId, name, amountOfStudents, yearOfStudy):
        if not (type(amountOfStudents) is int):
            raise ValueError("amount of students field must be a number")

        if not (type(yearOfStudy) is int):
            raise ValueError("year of study field must be a number")

        cursor = self.sqlite_connection.cursor()

        # Проверка на то, что указанный SpecializationId существует
        sqliteQuery = 'SELECT EXISTS(SELECT 1 FROM SpecializationsNEW WHERE id = ?); '
        cursor.execute(sqliteQuery, (specializationId,))
        rows = cursor.fetchall()
        for row in rows:
            if row[0] == 0:
                raise ValueError('This SpecializationId does not exist!')

        # Проверка на то, что такая группа уже не существует в таблице
        sqliteQuery = 'SELECT EXISTS(SELECT 1 FROM GroupsNEW WHERE SpecializationId = ? AND ' \
                      'name = ? AND id <> ?);'
        cursor.execute(sqliteQuery, (specializationId, name, id))
        rows = cursor.fetchall()
        for row in rows:
            if row[0] == 1:
                raise ValueError('This group already exists!')

        sqliteQuery = 'UPDATE GroupsNEW SET Name = ?, AmountOfStudents = ?, YearOfStudy = ?, SpecializationId = ?' \
                      ' WHERE id = ?'
        cursor.execute(sqliteQuery, (name, amountOfStudents, yearOfStudy, specializationId, id))
        self.sqlite_connection.commit()
        cursor.close()

    # Удалить группу
    # id - id группы
    def removeGroup(self, id):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'DELETE FROM GroupsNEW WHERE id = ?'
        cursor.execute(sqliteQuery, (id,))
        self.sqlite_connection.commit()
        cursor.close()

    def getAllGroup(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT * FROM GroupsNEW'
        cursor.execute(sqliteQuery)
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append(Group(row[0], row[1], row[2], row[3], row[4]))
        return lst

    def getGroup(self, id):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT * FROM GroupsNEW WHERE id = ?'
        cursor.execute(sqliteQuery, (id,))
        row = cursor.fetchall()[0]
        cursor.close()

        return Group(row[0], row[1], row[2], row[3], row[4])

    # for prolog
    def getAllSpecializationGroups(self, specializationId, yearOfStudy):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT Name FROM GroupsNEW WHERE SpecializationId=? AND YearOfStudy=? ORDER BY YearOfStudy'
        cursor.execute(sqliteQuery, (specializationId, yearOfStudy,))
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append(row[0])

        return lst

    ########################################################################################################################

    # Создать таблицу предметов
    def initSubject(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'CREATE TABLE SubjectsNEW(id INTEGER PRIMARY KEY, SpecializationId INTEGER,' \
                      'Name TEXT, Semesters TEXT, TypeOfClass TEXT, Frequency INTEGER, TeacherId INTEGER,' \
                      'AmountOfGroups INTEGER) '
        cursor.execute(sqliteQuery)
        self.sqlite_connection.commit()
        cursor.close()

    # Очистить таблицу предметов
    def clearSubject(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'DELETE FROM SubjectsNEW'
        cursor.execute(sqliteQuery)
        self.sqlite_connection.commit()
        cursor.close()

    def addSubject(self, specializationId, name, semesters, typeOfClass, frequency, teacherId, amountOfGroups):
        if not (type(amountOfGroups) is int):
            raise ValueError("amount of groups field must be a number")

        if not (1 <= amountOfGroups <= 100):
            raise ValueError("amount of groups field must be within 1..100")

        if not (type(frequency) is int):
            raise ValueError("frequency field must be a number")

        if not (1 <= frequency <= 100):
            raise ValueError("frequency field must be within 1..100")

        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'INSERT INTO SubjectsNEW(`SpecializationId`, `Name`, `Semesters`, `TypeOfClass`, `Frequency`, ' \
                      '`TeacherId`, `AmountOfGroups`) VALUES(?, ?, ?, ?, ?, ?, ?) '
        cursor.execute(sqliteQuery, (specializationId, name, semesters, typeOfClass,
                                     frequency, teacherId, amountOfGroups))
        self.sqlite_connection.commit()
        cursor.close()

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
        sqliteQuery = 'UPDATE SubjectsNEW SET SpecializationId = ?, Name = ?, Semesters = ?, TypeOfClass = ?,' \
                      'Frequency = ?, TeacherId = ?, AmountOfGroups = ? WHERE id = ?'
        cursor.execute(sqliteQuery, (specializationId, name, semesters, typeOfClass,
                                     frequency, teacherId, amountOfGroups, id))
        self.sqlite_connection.commit()
        cursor.close()

    # Удалить занятие
    # id - id занятия
    def removeSubject(self, id):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'DELETE FROM SubjectsNEW WHERE id = ?'
        cursor.execute(sqliteQuery, (id,))
        self.sqlite_connection.commit()
        cursor.close()

    def getAllSubject(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT * FROM SubjectsNEW'
        cursor.execute(sqliteQuery)
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append(Subject(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
        return lst

    def getSubject(self, id):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT * FROM SubjectsNEW WHERE id = ?'
        cursor.execute(sqliteQuery, (id,))
        row = cursor.fetchall()[0]
        cursor.close()

        return Subject(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])

    # for prolog
    def getAllSubjectsDistinct(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT DISTINCT SpecializationId, Name, Semesters FROM SubjectsNEW'
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
        sqliteQuery = 'SELECT DISTINCT TypeOfClass, Frequency FROM SubjectsNEW WHERE SpecializationId=? AND Name=? ' \
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
        sqliteQuery = 'SELECT TeacherId, AmountOfGroups FROM SubjectsNEW WHERE SpecializationId=? AND Name=? AND ' \
                      'Semesters=? AND TypeOfClass=? AND Frequency=?'
        cursor.execute(sqliteQuery, (specializationId, name, semesters, typeOfClass, Frequency,))
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append([row[0], row[1]])
        return lst

    ########################################################################################################################

    # Создать таблицу учителей
    def initTeacher(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'CREATE TABLE TeachersNEW(id INTEGER PRIMARY KEY, Name TEXT, DaysCanWork, DaysWantWork, Weight)'
        cursor.execute(sqliteQuery)
        self.sqlite_connection.commit()
        cursor.close()

    # Очистить таблицу учителей
    def clearTeacher(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'DELETE FROM TeachersNEW'
        cursor.execute(sqliteQuery)
        self.sqlite_connection.commit()
        cursor.close()

    # Матвей!!! Этот метод вызывается только диспетчером.
    # Уже потом препод сам через updateTeacher может убрать те дни, когда не может или не хочет работать
    def addTeacher(self, name, daysCanWork, daysWantWork, weight):
        if not (type(weight) is int):
            raise ValueError("weight field must be a number")

        if not (0 <= weight <= 10):
            raise ValueError("weight field must be within 0..10")

        # Проверка на то, что учитель хочет работать в тот день, когда он не может
        canTokens = daysCanWork[1:-1].split(",")
        wantTokens = daysWantWork[1:-1].split(",")
        for want in wantTokens:
            if not (want in canTokens):
                raise Exception('Хочет работать в тот день, в который не может работать!')

        # если может и хочет работать в любой день, то вес равен 0
        if len(wantTokens) == studyDaysInWeek:
            weight = 0

        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'INSERT INTO TeachersNEW(`Name`, `DaysCanWork`, `DaysWantWork`, `Weight`) VALUES(?, ' \
                      '?, ?, ?) '

        cursor.execute(sqliteQuery, (name, daysCanWork, daysWantWork, weight,))
        self.sqlite_connection.commit()
        cursor.close()

    # Матвей!!! Этот метод вызывается диспетчером и самим преподом.
    # Препод сам может убрать те дни, когда не может или не хочет работать
    def updateTeacher(self, id, name, daysCanWork, daysWantWork, weight):
        if not (type(weight) is int):
            raise ValueError("weight field must be a number")

        if not (0 <= weight <= 10):
            raise ValueError("weight field must be within 0..10")

        # Проверка на то, что учитель хочет работать в тот день, когда он не может
        canTokens = daysCanWork[1:-1].split(",")
        wantTokens = daysWantWork[1:-1].split(",")
        for want in wantTokens:
            if not (want in canTokens):
                raise Exception('Хочет работать в тот день, в который не может работать!')

        # если может и хочет работать в любой день, то вес равен 0
        if len(wantTokens) == studyDaysInWeek:
            weight = 0

        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'UPDATE TeachersNEW SET Name = ?, DaysCanWork = ?, DaysWantWork = ?, Weight = ? WHERE id = ?'
        cursor.execute(sqliteQuery, (name, daysCanWork, daysWantWork, weight, id))
        self.sqlite_connection.commit()
        cursor.close()

    # Удалить преподавателя
    # id - id преподавателя
    def removeTeacher(self, id):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'DELETE FROM TeachersNEW WHERE id = ?'
        cursor.execute(sqliteQuery, (id,))
        self.sqlite_connection.commit()
        cursor.close()

    def getAllTeacher(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT * FROM TeachersNEW'
        cursor.execute(sqliteQuery)
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append(Teacher(row[0], row[1], row[2], row[3], row[4]))
        return lst

    def getTeacher(self, id):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT * FROM TeachersNEW WHERE id = ?'
        cursor.execute(sqliteQuery, (id,))
        row = cursor.fetchall()[0]
        cursor.close()

        return Teacher(row[0], row[1], row[2], row[3], row[4])

    ########################################################################################################################

    # Создать таблицу аудиторий
    def initClassroom(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'CREATE TABLE ClassroomsNEW(id INTEGER PRIMARY KEY, Number TEXT, TypesOfClass TEXT,' \
                      'Capacity INTEGER) '
        cursor.execute(sqliteQuery)
        self.sqlite_connection.commit()
        cursor.close()

    # Очистить таблицу аудиторий
    def clearClassroom(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'DELETE FROM ClassroomsNEW'
        cursor.execute(sqliteQuery)
        self.sqlite_connection.commit()
        cursor.close()

    def addClassroom(self, number, typesOfClass, capacity):
        if not (type(capacity) is int):
            raise ValueError("capacity field must be a number")

        # Проверка на то, что такая аудитория уже не существует в таблице
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT EXISTS(SELECT 1 FROM ClassroomsNEW WHERE Number= ?);'
        cursor.execute(sqliteQuery, (number,))
        rows = cursor.fetchall()
        for row in rows:
            if row[0] == 1:
                raise ValueError('This Classroom already exists!')

        sqliteQuery = 'INSERT INTO ClassroomsNEW(`Number`, `TypesOfClass`, `Capacity`) VALUES(?, ?, ?)'
        cursor.execute(sqliteQuery, (number, typesOfClass, capacity,))
        self.sqlite_connection.commit()
        cursor.close()

    def updateClassroom(self, id, number, typesOfClass, capacity):
        if not (type(capacity) is int):
            raise ValueError("capacity field must be a number")

        # Проверка на то, что такая аудитория уже не существует в таблице
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT EXISTS(SELECT 1 FROM ClassroomsNEW WHERE Number= ? AND id <> ?);'
        cursor.execute(sqliteQuery, (number, id))
        rows = cursor.fetchall()
        for row in rows:
            if row[0] == 1:
                raise ValueError('This Classroom already exists!')

        sqliteQuery = 'UPDATE ClassroomsNEW SET Number = ?, TypesOfClass = ?, Capacity = ? WHERE id = ?'
        cursor.execute(sqliteQuery, (number, typesOfClass, capacity, id))
        self.sqlite_connection.commit()
        cursor.close()

    def removeClassroom(self, id):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'DELETE FROM ClassroomsNEW WHERE id = ?'
        cursor.execute(sqliteQuery, (id,))
        self.sqlite_connection.commit()
        cursor.close()

    def getAllClassroom(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT * FROM ClassroomsNEW'
        cursor.execute(sqliteQuery)
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append(Classroom(row[0], row[1], row[2], row[3]))
        return lst

    def getClassroom(self, id):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT * FROM ClassroomsNEW WHERE id = ?'
        cursor.execute(sqliteQuery, (id,))
        row = cursor.fetchall()[0]
        cursor.close()

        return Classroom(row[0], row[1], row[2], row[3])

    ########################################################################################################################

    # Создать таблицу ограничений
    def initConstraints(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'CREATE TABLE ConstraintsNEW(id INTEGER PRIMARY KEY, FirstClassStarts TEXT, ' \
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
        sqliteQuery = 'DELETE FROM ConstraintsNEW'
        cursor.execute(sqliteQuery)
        self.sqlite_connection.commit()
        cursor.close()

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
        sqliteQuery = 'INSERT INTO ConstraintsNEW(`FirstClassStarts`, `ClassDuration`, `ShortBrakeDuration`, ' \
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

    def updateConstraints(self, firstClassStarts, classDuration, shortBrakeDuration, largeBrakeDuration,
                          studyDaysInWeek,
                          studyDaysInWeekForStudents, studyDaysInWeekForTeachers, classesPerDay, classesPerDayStudents,
                          classesPerDayTeachers, lunchBrake, gaps, classroomFillness, semester):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'UPDATE ConstraintsNEW SET FirstClassStarts = ?, ClassDuration = ?, ShortBrakeDuration = ?,' \
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

    def removeConstraints(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'DELETE FROM ClassroomsNEW WHERE id = 1'
        cursor.execute(sqliteQuery)
        self.sqlite_connection.commit()
        cursor.close()

    def getConstraints(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT * FROM ConstraintsNEW'
        cursor.execute(sqliteQuery)
        row = cursor.fetchall()[0]
        cursor.close()

        return Constraints(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9],
                           row[10], row[11], row[12], row[13], row[14])

    ########################################################################################################################

    def initGeneratedScheduleTable(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'DROP TABLE IF EXISTS GeneratedSchedule;'
        cursor.execute(sqliteQuery)
        sqliteQuery = 'DROP TABLE IF EXISTS ClassToGroups;'
        cursor.execute(sqliteQuery)
        sqliteQuery = 'create table GeneratedSchedule (id integer primary key autoincrement, `Faculty`, ' \
                      '`EducationalProgram`, `Specialization`, `Subject`, `Semester`, `Teacher`, `TypeOfClass`, ' \
                      '`Auditory`, `Groups`, `Day`, `ClassNumber`)'
        cursor.execute(sqliteQuery)
        sqliteQuery = 'create table ClassToGroups (id integer primary key autoincrement, `ClassId`, ' \
                      '`GroupName`)'
        cursor.execute(sqliteQuery)

        self.sqlite_connection.commit()
        cursor.close()

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

        ############################ GROUPS ARE ADDED SEPERATELY #######################

        for group in groups:
            sqliteQuery = 'INSERT INTO ClassToGroups(`ClassId`, `GroupName`) VALUES(?, ?) '
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
                GeneratedClass(rows[i][0], rows[i][1], rows[i][2], rows[i][3], rows[i][4], rows[i][5], rows[i][6],
                               rows[i][7], rows[i][8], rows[i][9], rows[i][10], rows[i][11]))
        return lst

    # Получить список из всех групп, которые отнесены к конкретному занятию
    def getAllGroupsOfClass(self, classId):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT * FROM ClassToGroups WHERE ClassId = ?'
        cursor.execute(sqliteQuery, (classId,))
        rows = cursor.fetchall()
        cursor.close()

        lst = []
        for row in rows:
            lst.append(row[2])
        return lst

########################################################################################################################

    #def getSchedule

########################################################################################################################

    def yearShiftRight(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT * FROM GroupsNEW'
        cursor.execute(sqliteQuery)
        rows = cursor.fetchall()
        cursor.close()

        for row in rows:
            dbManager = DatabaseManager()
            dbManager.updateGroup(row[0], row[1], row[2], row[3], row[4] + 1)

    def yearShiftLeft(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT * FROM GroupsNEW'
        cursor.execute(sqliteQuery)
        rows = cursor.fetchall()
        cursor.close()

        for row in rows:
            dbManager = DatabaseManager()
            dbManager.updateGroup(row[0], row[1], row[2], row[3], row[4] - 1)

########################################################################################################################

    # TODO functions working with generated timetable will be written later because of new solver
    def clearAll(self):
        cursor = self.sqlite_connection.cursor()
        cursor.execute('DELETE FROM ClassroomsNEW')
        cursor.execute('DELETE FROM ConstraintsNEW')
        cursor.execute('DELETE FROM EducationalProgramsNEW')
        cursor.execute('DELETE FROM FacultiesNEW')
        cursor.execute('DELETE FROM GroupsNEW')
        cursor.execute('DELETE FROM SubjectsNEW')
        cursor.execute('DELETE FROM TeachersNEW')
        self.sqlite_connection.commit()
        cursor.close()

    def getAllTypesOfClasses(self):
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'SELECT DISTINCT TypeOfClass FROM SubjectsNEW'
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


def disassemblePrologList(groupsList):
    prologList2 = groupsList[1:len(groupsList) - 1]
    groups = prologList2.split(",")

    return groups
