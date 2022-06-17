from werkzeug.security import generate_password_hash, check_password_hash
import DatabaseManager

class User2:
    def __init__(self, id=None, name=None):
        self._id = id
        self._name = None
        self._email = None
        self._password_hash = None
        self._role = None
        self._teacherId = None
        self._status = None
        self._updatedDate = None
        self._createdDate = None
        self._signedUpDate = None

    def getId(self):
        return self._id

    def getName(self):
        return self._name

    def getEmail(self):
        return self._email

    def getRole(self):
        return self._role

    def getTeacherId(self):
        return self._teacherId

    def getStatus(self):
        return self._status

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
