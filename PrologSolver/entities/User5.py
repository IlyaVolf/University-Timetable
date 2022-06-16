from werkzeug.security import generate_password_hash, check_password_hash
#from flask_login import UserMixin, login_user, logout_user, login_required
import sqlite3
import datetime


# Извне:
# @login_manager.user_loader
#    def load_user(user_id):
#       return dbManager.getUser(user_id)

# Примерно так:
# from flask_login import UserMixin, login_user, logout_user, login_required
#
# @auth.route('/login', methods=['POST'])
# def login_post():
#     email = request.form.get('email')
#     password = request.form.get('password')
#     remember = True
#
#     sqlite_connection = sqlite3.connect('timetable.sqlite')
#
#     cursor = self.sqlite_connection.cursor()
#     sqliteQuery = 'SELECT * FROM Users WHERE email = ?'
#     cursor.execute(sqliteQuery, (email,))
#     rows = cursor.fetchall()
#     if len(rows) < 1:
#        raise ValueError("No account with this email!")
#     cursor.close()
#
#     row = rows[0]
#
#     user = User(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
#
#     if check_password_hash(user.passwordHash, password):
#         flash('Please check your login details and try again.')
#         return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page
#
#     login_user(user, remember=remember)!!!!!!!!!!
#     return redirect(url_for('main.profile'))

# @auth.route('/logout')
# @login_required
# def logout():
#     logout_user()!!!!!!!!!
#     return redirect(url_for('main.index'))

#class User(UserMixin):
class User:
    def __init__(self, id=None, name=None, email=None, passwordHash=None, role=None, teacherId=None, status=None,
                 updatedDate=None, createdDate=None, signedUpDate=None):
        self.id = id
        self.name = name
        self.email = email
        self.passwordHash = passwordHash
        self.role = role
        self.teacherId = teacherId
        self.status = status
        self.updatedDate = updatedDate
        self.createdDate = createdDate
        self.signedUpDate = signedUpDate
        self.sqlite_connection = sqlite3.connect('timetable.sqlite')

    def initUser(self, name, email, role, teacherId=None):
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
        id = cursor.fetchall()[0][0]

        self.id = id
        self.name = name
        self.email = email
        self.role = role
        self.teacherId = teacherId

        return self

    def updateUser(self, name, email, role, teacherId=None):
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
        cursor.execute(sqliteQuery, (name, email, role, teacherId, date, self.id))

        self.name = name
        self.email = email
        self.role = role
        self.teacherId = teacherId

        return self

    # когда через почту подтверждает свое участие: задаём пароль
    def signUpUser(self, password):
        passwordHash = generate_password_hash(password)
        cursor = self.sqlite_connection.cursor()
        sqliteQuery = 'UPDATE Users SET PasswordHash = ?, Status = 1, UpdatedDate = ?, SignedUpDate = ? WHERE id = ?'
        date = datetime.datetime.now()
        cursor.execute(sqliteQuery, (passwordHash, date, date, self.id))
        self.sqlite_connection.commit()
        cursor.close()

        self.passwordHash = passwordHash
        self.status = 1
        self.updatedDate = date
        self.signedUpDate = date

        return self

    def checkPassword(self, password):
        return check_password_hash(self.passwordHash, password)
