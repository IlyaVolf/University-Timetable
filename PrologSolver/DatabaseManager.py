import sqlite3

from entities.Faculty import Faculty
from entities.Auditory import Auditory
from entities.Constraints import Constraints
from entities.EducationalProgram import EducationalProgram
from entities.Specialization import Specialization
from entities.GeneratedClass import GeneratedClass
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
        sqliteQuery = 'SELECT EXISTS(SELECT 1 FROM EducationalProgramsNEW WHERE id = ?); '
        cursor.execute(sqliteQuery, (educationalProgramId,))
        rows = cursor.fetchall()
        for row in rows:
            if row[0] == 0:
                raise ValueError('This EducationalProgramId does not exist!')

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
        sqliteQuery = 'SELECT EXISTS(SELECT 1 FROM SpecializationsNEW WHERE id = ?); '
        cursor.execute(sqliteQuery, (specializationId,))
        rows = cursor.fetchall()
        for row in rows:
            if row[0] == 0:
                raise ValueError('This SpecializationId does not exist!')

        # Проверка на то, что такая группа уже не существует в таблице
        sqliteQuery = 'SELECT EXISTS(SELECT 1 FROM GroupsNEW WHERE SpecializationId = ? AND ' \
                      'name = ?);'
        cursor.execute(sqliteQuery, (specializationId, name,))
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

    # Матвей!!! Этот метод вызывается только диспетчером. daysCanWork и daysWantWork ОБЯЗАНЫ быть равны [1,2,3,4,5,6],
    # weight = 0.
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
        sqliteQuery = 'SELECT EXISTS(SELECT 1 FROM ClassroomsNEW WHERE Number= ?);'
        cursor.execute(sqliteQuery, (number,))
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

    """
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
    """

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

    """
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
    """

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
