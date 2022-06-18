from werkzeug.security import generate_password_hash, check_password_hash
from DatabaseManager import DatabaseManager
import sqlite3
import datetime

# id - string!
class User:
    def __init__(self, id=None, name=None, email=None, passwordHash=None, role=None, teacherId=None, status=None,
                 updatedDate=None, createdDate=None, SignedUpDate=None):
        self.id = id
        self.name = name
        self.email = email
        self.passwordHash = passwordHash
        self.role = role
        self.teacherId = teacherId
        self.status = status
        self.updatedDate = updatedDate
        self.createdDate = createdDate
        self.SignedUpDate = SignedUpDate

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def addUser(name, email, role, teacherId=None):
        sqlite_connection = sqlite3.connect('timetable.sqlite')

        if role == 0:
            raise ValueError("chief dispatcher can be only one!")

        if role != 1 and role != 2 and role != 3:
            raise ValueError("No such role!")

        if role == 2:
            dbManager = DatabaseManager()
            if teacherId is None:
                raise ValueError("Teacher was not specified!")
            teacher = dbManager.getTeacher(teacherId)
            if teacher is None:
                raise ValueError("No such teacher id!")
            if teacher.name != name:
                raise ValueError("Names do not coincide!")

        cursor = sqlite_connection.cursor()

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
        id = cursor.fetchall()[0][0]

        sqliteQuery = 'SELECT * FROM Users WHERE id = ?'
        cursor.execute(sqliteQuery, (int(id),))
        row = cursor.fetchall()[0]

        sqlite_connection.commit()
        cursor.close()

        return User(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
