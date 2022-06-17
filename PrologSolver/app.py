from operator import ge
import os
from webbrowser import get
#from PrologSolver.entities.GeneratedClass import GeneratedClass
from flask import Flask, jsonify, request
from flask_cors import CORS
import generator
from entities import GeneratedClass

from EntitySerializer import serialiseTeacher, serialiseClassroom, serialiseEducationalProgram, serialiseFaculty, serialiseGroup, serialiseSubject,serialiseSpecialization, serialiseConstraints, serialiseGeneratedClass, serialiseSchedule, serialiseGeneratedClass
from DatabaseManager import DatabaseManager


from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from flask_login import LoginManager

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)

i = 0
def check():
    print("HI")
    if (i == 1):
        import generator
        print("JU")

login_manager = LoginManager()
#login_manager.login_view = 'auth.login'
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user_id):
    dbManager = DatabaseManager()
    res = dbManager.getUser(user_id)
    dbManager.close()
    return res

@app.route('/teachers/<id>', methods=['GET','DELETE','PUT'])
def teacher(id):
    if request.method == 'GET':
        dbManager = DatabaseManager()
        teacher = dbManager.getTeacher(id)
        dbManager.close()
        response_object = serialiseTeacher(teacher)
        return jsonify(response_object)
    if request.method == 'DELETE':
        dbManager = DatabaseManager()
        dbManager.removeTeacher(id)
        dbManager.close()
        return jsonify({'response': 'success'})
    if request.method == 'PUT':
        name = request.args.get('name')
        daysCanWork = request.args.get('daysCanWork').replace(" ", ",").replace("_", ";")
        daysWantWork = request.args.get('daysWantWork').replace(" ", ",").replace("_", ";")
        weight = request.args.get('weight')
        if name is not None and daysCanWork is not None and daysWantWork is not None and weight is not None:
            dbManager = DatabaseManager()
            dbManager.updateTeacher(id, name, daysCanWork, daysWantWork, int(weight))
            dbManager.close()
            return jsonify({'response': 'success'})
        return jsonify({'response': 'failure'})
    return jsonify({'response': 'failure'})

@app.route('/teachers', methods=['POST','GET'])
def addTeacher():
    if request.method == 'POST':
        name = request.args.get('name')
        daysCanWork = request.args.get('daysCanWork').replace(" ", ",").replace("_", ";")
        daysWantWork = request.args.get('daysWantWork').replace(" ", ",").replace("_", ";")
        weight = request.args.get('weight')
        if name is not None and daysCanWork is not None and daysWantWork is not None and weight is not None:
            dbManager = DatabaseManager()
            dbManager.addTeacher(name, daysCanWork, daysWantWork, int(weight))
            dbManager.close()
            return jsonify({'response': 'success'})
        return jsonify({'response': 'failure'})
    dbManager = DatabaseManager()
    teachers = dbManager.getAllTeacher()
    dbManager.close()
    return jsonify(list(map(lambda x: serialiseTeacher(x), teachers)))

@app.route('/classrooms/<id>', methods=['GET','DELETE','PUT'])
def classroom(id):
    if request.method == 'GET':
        dbManager = DatabaseManager()
        classroom = dbManager.getClassroom(id)
        dbManager.close()
        response_object = serialiseClassroom(classroom)
        return jsonify(response_object)
    if request.method == 'DELETE':
        dbManager = DatabaseManager()
        dbManager.removeClassroom(id)
        dbManager.close()
        return jsonify({'response': 'success'})
    if request.method == 'PUT':
        number = request.args.get('number')
        capacity = request.args.get('capacity')
        typesOfClass = request.args.get('typesOfClass').replace(" ", ",")
        if number is not None and capacity is not None and typesOfClass is not None:
            dbManager = DatabaseManager()
            dbManager.updateClassroom(id, number, typesOfClass, int(capacity))
            dbManager.close()
            return jsonify({'response': 'success'})
        return jsonify({'response': 'failure'})
    return jsonify({'response': 'failure'})

@app.route('/classrooms', methods=['POST','GET'])
def addClassroom():
    if request.method == 'POST':
        number = request.args.get('number')
        capacity = request.args.get('capacity')
        typesOfClass = request.args.get('typesOfClass').replace(" ", ",")
        if number is not None and capacity is not None and typesOfClass is not None:
            dbManager = DatabaseManager()
            dbManager.addClassroom(number, typesOfClass, int(capacity))
            dbManager.close()
            return jsonify({'response': 'success'})
        return jsonify({'response': 'failure'})
    dbManager = DatabaseManager()
    teachers = dbManager.getAllClassroom()
    dbManager.close()
    return jsonify(list(map(lambda x: serialiseClassroom(x), teachers)))

@app.route('/faculties/<id>', methods=['GET','DELETE','PUT'])
@login_required
def faculty(id):
    response_object = {'id': 'null', 'faculty': 'null'}
    if request.method == 'GET':
        dbManager = DatabaseManager()
        faculty = dbManager.getFaculty(id)
        dbManager.close()
        response_object = serialiseFaculty(faculty)
        return jsonify(response_object)
    if request.method == 'DELETE':
        dbManager = DatabaseManager()
        dbManager.removeFaculty(id)
        dbManager.close()
        return jsonify({'response': 'success'})
    if request.method == 'PUT':
        name = request.args.get('name')
        if name is not None:
            dbManager = DatabaseManager()
            dbManager.updateFaculty(id, name)
            dbManager.close()
            return jsonify({'response': 'success'})
        return jsonify({'response': 'failure'})
    return jsonify({'response': 'failure'})

@app.route('/faculties', methods=['POST','GET'])
def addFaculty():
    if request.method == 'POST':
        name = request.args.get('name')
        if name is not None:
            dbManager = DatabaseManager()
            dbManager.addFaculty(name)
            dbManager.close()
            return jsonify({'response': 'success'})
        return jsonify({'response': 'failure'})
    dbManager = DatabaseManager()
    faculties = dbManager.getAllFaculty()
    dbManager.close()
    return jsonify(list(map(lambda x: serialiseFaculty(x), faculties)))

@app.route('/educationalPrograms/<id>', methods=['GET','DELETE','PUT'])
def educationalProgram(id):
    if request.method == 'GET':
        dbManager = DatabaseManager()
        educationalProgram = dbManager.getEducationalProgram(id)
        dbManager.close()
        response_object = serialiseEducationalProgram(educationalProgram)
        return jsonify(response_object)
    if request.method == 'DELETE':
        dbManager = DatabaseManager()
        dbManager.removeEducationalProgram(id)
        dbManager.close()
        return jsonify({'response': 'success'})
    if request.method == 'PUT':
        facultyId = request.args.get('facultyId')
        name = request.args.get('name').replace("_", ",").replace("-", ".")
        if facultyId is not None and name is not None:
            dbManager = DatabaseManager()
            dbManager.updateEducationalProgram(id, facultyId, name)
            dbManager.close()
            return jsonify({'response': 'success'})
        return jsonify({'response': 'failure'})
    return jsonify({'response': 'failure'})

@app.route('/educationalPrograms', methods=['POST','GET'])
def addEducationalProgram():
    if request.method == 'POST':
        facultyId = request.args.get('facultyId')
        name = request.args.get('name').replace("_", ",").replace("-", ".")
        if name is not None and facultyId is not None:
            dbManager = DatabaseManager()
            dbManager.addEducationalProgram(facultyId, name)
            dbManager.close()
            return jsonify({'response': 'success'})
        return jsonify({'response': 'failure'})
    dbManager = DatabaseManager()
    educationalPrograms = dbManager.getAllEducationalProgram()
    dbManager.close()
    return jsonify(list(map(lambda x: serialiseEducationalProgram(x), educationalPrograms)))

@app.route('/groups/<id>', methods=['GET','DELETE','PUT'])
def group(id):
    response_object = {'id': 'null', 'specializationId': 'null', 'name': 'null',
    'amountOfStudents': 'null', 'yearOfStudy': 'null'}
    if request.method == 'GET':
        dbManager = DatabaseManager()
        group = dbManager.getGroup(id)
        dbManager.close()
        response_object = serialiseGroup(group)
        return jsonify(response_object)
    if request.method == 'DELETE':
        dbManager = DatabaseManager()
        dbManager.removeGroup(id)
        dbManager.close()
        return jsonify({'response': 'success'})
    if request.method == 'PUT':
        specializationId = request.args.get('specializationId')
        name = request.args.get('name').replace("-", ".")
        amountOfStudents = request.args.get('amountOfStudents')
        yearOfStudy = request.args.get('yearOfStudy')
        if specializationId is not None and name is not None and amountOfStudents is not None and yearOfStudy is not None:
            dbManager = DatabaseManager()
            dbManager.updateGroup(id, specializationId, name, int(amountOfStudents), int(yearOfStudy))
            dbManager.close()
            return jsonify({'response': 'success'})
        return jsonify({'response': 'failure'})
    return jsonify({'response': 'failure'})

@app.route('/groups', methods=['POST','GET'])
def addGroup():
    if request.method == 'POST':
        specializationId = request.args.get('specializationId')
        name = request.args.get('name').replace("-", ".")
        amountOfStudents = request.args.get('amountOfStudents')
        yearOfStudy = request.args.get('yearOfStudy')
        if (specializationId is not None and name is not None and 
            amountOfStudents is not None and yearOfStudy is not None):
            dbManager = DatabaseManager()
            dbManager.addGroup(specializationId, name, int(amountOfStudents), int(yearOfStudy))
            dbManager.close()
            return jsonify({'response': 'success'})
        return jsonify({'response': 'failure'})
    dbManager = DatabaseManager()
    groups = dbManager.getAllGroup()
    dbManager.close()
    return jsonify(list(map(lambda x: serialiseGroup(x), groups)))

@app.route('/subjects/<id>', methods=['GET','DELETE','PUT'])
def subject(id):
    if request.method == 'GET':
        dbManager = DatabaseManager()
        subject = dbManager.getSubject(id)
        dbManager.close()
        response_object = serialiseSubject(subject)
        return jsonify(response_object)
    if request.method == 'DELETE':
        dbManager = DatabaseManager()
        dbManager.removeSubject(id)
        dbManager.close()
        return jsonify({'response': 'success'})
    if request.method == 'PUT':
        specializationId = request.args.get('specializationId')
        name = request.args.get('name')
        semesters = request.args.get('semesters').replace("_", ",")
        typeOfClass = request.args.get('typeOfClass')
        frequency = request.args.get('frequency')
        teacherId = request.args.get('teacherId')
        amountOfGroups = request.args.get('amountOfGroups')
        if (specializationId is not None and name is not None and semesters is not None 
            and typeOfClass is not None and frequency is not None and teacherId is not None
            and amountOfGroups is not None):
            dbManager = DatabaseManager()
            dbManager.updateSubject(id, specializationId, name, semesters, typeOfClass,
                int(frequency), teacherId, int(amountOfGroups))
            dbManager.close()
            return jsonify({'response': 'success'})
        return jsonify({'response': 'failure'})
    return jsonify({'response': 'failure'})

@app.route('/subjects', methods=['POST','GET'])
def addSubject():
    if request.method == 'POST':
        specializationId = request.args.get('specializationId')
        name = request.args.get('name')
        semesters = request.args.get('semesters').replace("_", ",")
        typeOfClass = request.args.get('typeOfClass')
        frequency = request.args.get('frequency')
        teacherId = request.args.get('teacherId')
        amountOfGroups = request.args.get('amountOfGroups')
        if (specializationId is not None and name is not None and semesters is not None 
            and typeOfClass is not None and frequency is not None and teacherId is not None
            and amountOfGroups is not None):
            dbManager = DatabaseManager()
            dbManager.addSubject(specializationId, name, semesters, typeOfClass,
                int(frequency), teacherId, int(amountOfGroups))
            dbManager.close()
            return jsonify({'response': 'success'})
        return jsonify({'response': 'failure'})
    dbManager = DatabaseManager()
    subjects = dbManager.getAllSubject()
    dbManager.close()
    return jsonify(list(map(lambda x: serialiseSubject(x), subjects)))

@app.route('/specializations/<id>', methods=['GET','DELETE','PUT'])
def specialization(id):
    if request.method == 'GET':
        dbManager = DatabaseManager()
        specialization = dbManager.getSpecialization(id)
        dbManager.close()
        response_object = serialiseSpecialization(specialization)
        return jsonify(response_object)
    if request.method == 'DELETE':
        dbManager = DatabaseManager()
        dbManager.removeSpecialization(id)
        dbManager.close()
        return jsonify({'response': 'success'})
    if request.method == 'PUT':
        educationalProgramId = request.args.get('educationalProgramId')
        name = request.args.get('name')
        if educationalProgramId is not None and name is not None:
            dbManager = DatabaseManager()
            dbManager.updateSpecialization(id, educationalProgramId, name)
            dbManager.close()
            return jsonify({'response': 'success'})
        return jsonify({'response': 'failure'})
    return jsonify({'response': 'failure'})

@app.route('/specializations', methods=['POST','GET'])
def addSpecialization():
    if request.method == 'POST':
        educationalProgramId = request.args.get('educationalProgramId')
        name = request.args.get('name')
        if name is not None and educationalProgramId is not None:
            dbManager = DatabaseManager()
            dbManager.addSpecialization(educationalProgramId, name)
            dbManager.close()
            return jsonify({'response': 'success'})
        return jsonify({'response': 'failure'})
    if request.method == 'GET' and request.args.get('educationalProgramId') is not None:
        educationalProgramId = request.args.get('educationalProgramId')
        dbManager = DatabaseManager()
        specializations = dbManager.getAllSpecializationByEdProgram(educationalProgramId)
        dbManager.close()
        return jsonify(list(map(lambda x: serialiseSpecialization(x), specializations)))
    dbManager = DatabaseManager()
    specializations = dbManager.getAllSpecialization()
    dbManager.close()
    return jsonify(list(map(lambda x: serialiseSpecialization(x), specializations)))

@app.route('/constraints', methods=['GET','DELETE','PUT', 'POST'])
def constraints():
    if request.method == 'GET':
        dbManager = DatabaseManager()
        constraints = dbManager.getConstraints()
        dbManager.close()
        response_object = serialiseConstraints(constraints)
        return jsonify(response_object)
    if request.method == 'DELETE':
        dbManager = DatabaseManager()
        dbManager.removeConstraints()
        dbManager.close()
        return jsonify({'response': 'success'})
    firstClassStarts = request.args.get('firstClassStarts')
    classDuration = request.args.get('classDuration')
    shortBrakeDuration = request.args.get('shortBrakeDuration')
    largeBrakeDuration = request.args.get('largeBrakeDuration')
    studyDaysInWeek = request.args.get('studyDaysInWeek')
    studyDaysInWeekForStudents = request.args.get('studyDaysInWeekForStudents')
    studyDaysInWeekForTeachers = request.args.get('studyDaysInWeekForTeachers')
    classesPerDay = request.args.get('classesPerDay')
    classesPerDayStudents = request.args.get('classesPerDayStudents')
    classesPerDayTeachers = request.args.get('classesPerDayTeachers')
    lunchBrake = request.args.get('lunchBrake')
    gaps = request.args.get('gaps')
    classroomFillness = request.args.get('classroomFillness')
    semester = request.args.get('semester')
    if (firstClassStarts is not None and classDuration is not None and 
        shortBrakeDuration is not None and largeBrakeDuration is not None and 
        studyDaysInWeek is not None and studyDaysInWeekForStudents is not None and 
        studyDaysInWeekForTeachers is not None and classesPerDay is not None and
        classesPerDayStudents is not None and classesPerDayTeachers is not None and
        lunchBrake is not None and gaps is not None and 
        classroomFillness is not None and semester is not None):
        dbManager = DatabaseManager()
        if request.method == 'PUT':
            dbManager.updateConstraints(firstClassStarts, classDuration,
                shortBrakeDuration, largeBrakeDuration, studyDaysInWeek,
                studyDaysInWeekForStudents, studyDaysInWeekForTeachers,
                classesPerDay, classesPerDayStudents, classesPerDayTeachers,
                lunchBrake, gaps, classroomFillness, semester)
        if request.method == 'POST':
            dbManager.addConstraints(firstClassStarts, int(classDuration),
                int(shortBrakeDuration), int(largeBrakeDuration), int(studyDaysInWeek),
                int(studyDaysInWeekForStudents), int(studyDaysInWeekForTeachers),
                int(classesPerDay), int(classesPerDayStudents), int(classesPerDayTeachers),
                int(lunchBrake), int(gaps), int(classroomFillness), int(semester))
        dbManager.close()
        return jsonify({'response': 'success'})
    return jsonify({'response': 'failure'})

@app.route('/generatedClasses', methods=['GET'])
def generatedClasses():
    dbManager = DatabaseManager()
    generatedClasses = dbManager.getAllGeneratedClass()
    dbManager.close()
    return jsonify(list(map(lambda x: serialiseGeneratedClass(x), generatedClasses)))

@app.route('/generatedClasses/<id>', methods=['GET'])
def generatedClass(id):
    dbManager = DatabaseManager()
    generatedClass = dbManager.getGeneratedClass(id)
    dbManager.close()
    return jsonify(serialiseGeneratedClass(generatedClass))

@app.route('/groupsOfClass/<id>', methods=['GET'])
def groupsOfClass(id):
    dbManager = DatabaseManager()
    groupsOfClass = dbManager.getAllGroupsOfClass(id)
    dbManager.close()
    
    return jsonify(groupsOfClass)

@app.route('/getScheduleStudents/<group>', methods=['GET'])
def scheduleStudents(group):
    dbManager = DatabaseManager()
    schedule = dbManager.getScheduleStudents(group)
    dbManager.close()
    return jsonify(serialiseSchedule(schedule))

@app.route('/getScheduleTeachers/<teacherId>', methods=['GET'])
def scheduleTeachers(teacherId):
    dbManager = DatabaseManager()
    schedule = dbManager.getScheduleTeachers(teacherId)
    dbManager.close()
    return jsonify(serialiseSchedule(schedule))

@app.route('/yearShiftRight', methods=['PUT'])
def doYearShiftRight():
    dbManager = DatabaseManager()
    dbManager.yearShiftRight()
    dbManager.close()
    return jsonify({'response': 'success'})

@app.route('/yearShiftLeft', methods=['PUT'])
def doYearShiftLeft():
    dbManager = DatabaseManager()
    dbManager.yearShiftLeft()
    dbManager.close()
    return jsonify({'response': 'success'})

@app.route('/generate', methods=['GET'])
def generate():
    dbManager = DatabaseManager()
    generator.generate()
    res = dbManager.getAllGeneratedClass()

    dbManager.close()
    return jsonify(list(map(lambda x: serialiseGeneratedClass(x), res)))

@app.route('/overgenerate', methods=['GET'])
def overgenerate():
    dbManager = DatabaseManager()
    generator.overgenerate()
    res = dbManager.getAllGeneratedClass()

    dbManager.close()
    return jsonify(list(map(lambda x: serialiseGeneratedClass(x), res)))

# id не надо!
@app.route('/addman', methods=['GET'])
def add_man():
    faculty = request.args.get('faculty')
    educationalProgram = request.args.get('educationalProgram')
    specialization = request.args.get('specialization')
    subject = request.args.get('subject')
    semester = request.args.get('semester')
    teacher = request.args.get('teacher')
    typeOfClass = request.args.get('typeOfClass')
    auditory = request.args.get('auditory')
    groups = request.args.get('groups')
    day = request.args.get('day')
    classNumber = request.args.get('classNumber')
    teacherId = request.args.get('teacherId')

    dbManager = DatabaseManager()
    generator.add_man(GeneratedClass(0, faculty, educationalProgram, specialization, subject, semester, teacher, typeOfClass, auditory, groups, day, classNumber, teacherId))
    res = dbManager.getAllGeneratedClass()

    dbManager.close()
    return jsonify(list(map(lambda x: serialiseGeneratedClass(x), res)))

@app.route('/removeman/<id>', methods=['GET'])
def remove_man(id):
    dbManager = DatabaseManager()
    generator.remove_man(id)
    res = dbManager.getAllGeneratedClass()

    dbManager.close()
    return jsonify(list(map(lambda x: serialiseGeneratedClass(x), res)))

@app.route('/login')
def login():
    email = request.args.get('email')
    print(email)
    password = request.args.get('password')
    remember = True
    dbManager = DatabaseManager()
    user = dbManager.signInUser(email)

    if not user.checkPassword(password):
        return jsonify({'response': 'failure'})

    login_user(user, remember=remember)

    print("Hello ", current_user.name)

    return jsonify({'response': 'success'})

@app.route('/logout')
@login_required
def logout():
    print(current_user.name)
    logout_user()

    return jsonify({'response': 'success'})
    
if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.run()