from operator import ge
import os
from webbrowser import get
from flask import Flask, jsonify, make_response, request
from flask_cors import CORS
import generator
from entities import GeneratedClass, User

from EntitySerializer import serialiseTeacher, serialiseUser, serialiseClassroom, serialiseEducationalProgram, serialiseFaculty, serialiseGroup, serialiseSubject,serialiseSpecialization, serialiseConstraints, serialiseGeneratedClass, serialiseSchedule, serialiseGeneratedClass
from DatabaseManager import DatabaseManager

import random
import string

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from flask_login import LoginManager
from flask_mail import Mail, Message

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)


app.config['MAIL_SERVER'] = 'smtp.rambler.ru'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'timetablensu@rambler.ru'  # введите свой адрес электронной почты здесь
app.config['MAIL_DEFAULT_SENDER'] = 'timetablensu@rambler.ru'  # и здесь
app.config['MAIL_PASSWORD'] = 'yGj-iK2-skz-US7'  # введите пароль
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

# enable CORS
CORS(app)

currentUser = User.User(role=3)

mail = Mail(app)

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
    if (currentUser.role != 0 and currentUser.role != 1):
        return jsonify(error = str("Only dispatcher has access")), 401

    response_object = {'response': 'success'}
    if (currentUser.role != 3):
        if (currentUser.role == 0 or currentUser.role == 1):
            return jsonify(error = str("Only dispatcher has access")), 401

    if request.method == 'GET':
        dbManager = DatabaseManager()
        try:
            teacher = dbManager.getTeacher(id)
        except ValueError as e:
                return jsonify(error = str(e)), 400
        dbManager.close()
        response_object['teacher'] = serialiseTeacher(teacher)
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
        if weight is None:
            weight = 5
        if name is not None and daysCanWork is not None and daysWantWork is not None and weight is not None:
            dbManager = DatabaseManager()
            try:
                dbManager.updateTeacher(id, name, daysCanWork, daysWantWork, int(weight))
            except ValueError as e:
                return jsonify(error = str(e)), 400
            dbManager.close()
            return jsonify({'response': 'success'})
        return jsonify({'response': 'failure'})
    return jsonify({'response': 'failure'})

@app.route('/teachers', methods=['POST','GET'])
def addTeacher():
    if (currentUser.role != 0 and currentUser.role != 1):
        return jsonify(error = str("Only dispatcher has access")), 401
    response_object = {'response': 'success'}
    if request.method == 'POST':
        name = request.args.get('name')
        daysCanWork = request.args.get('daysCanWork').replace(" ", ",").replace("_", ";")
        daysWantWork = request.args.get('daysWantWork').replace(" ", ",").replace("_", ";")
        weight = request.args.get('weight')
        if weight is None:
            weight = 5
        if name is not None and daysCanWork is not None and daysWantWork is not None and weight is not None:
            dbManager = DatabaseManager()
            try:
                dbManager.addTeacher(name, daysCanWork, daysWantWork, int(weight))
            except ValueError as e:
                return jsonify(error = str(e)), 400
            dbManager.close()
            return jsonify({'response': 'success'})
        return jsonify({'response': 'failure'})
    dbManager = DatabaseManager()
    teachers = dbManager.getAllTeacher()
    dbManager.close()
    response_object['teachers'] = list(map(lambda x: serialiseTeacher(x), teachers))
    return jsonify(response_object)

# только интересуют вес и даты
@app.route('/teacherconstraints', methods=['GET','PUT'])
def teacher_constraints():
    if (currentUser.role != 2):
        return jsonify(error = str("Only teacher has access")), 401

    response_object = {'response': 'success'}
    if request.method == 'GET':
        dbManager = DatabaseManager()
        teacher = dbManager.getTeacher(currentUser.teacherId)
        dbManager.close()
        response_object['teacher'] = serialiseTeacher(teacher)
        return jsonify(response_object)
    if request.method == 'PUT':
        dbManager = DatabaseManager()
        name = dbManager.getTeacher(currentUser.teacherId).name
        daysCanWork = request.args.get('daysCanWork').replace(" ", ",").replace("_", ";")
        daysWantWork = request.args.get('daysWantWork').replace(" ", ",").replace("_", ";")
        weight = request.args.get('weight')
        if name is not None and daysCanWork is not None and daysWantWork is not None and weight is not None:
            dbManager = DatabaseManager()
            dbManager.updateTeacher(currentUser.teacherId, name, daysCanWork, daysWantWork, int(weight))
            dbManager.close()
            return jsonify({'response': 'success'})
        dbManager.close()
        return jsonify({'response': 'failure'})
    dbManager.close()
    return jsonify({'response': 'failure'})

@app.route('/classrooms/<id>', methods=['GET','DELETE','PUT'])
def classroom(id):
    if (currentUser.role != 0 and currentUser.role != 1):
        return jsonify(error = str("Only dispatcher has access")), 401
    response_object = {'response': 'success'}
    if request.method == 'GET':
        dbManager = DatabaseManager()
        try:
            classroom = dbManager.getClassroom(id)
        except ValueError as e:
            return jsonify(error = str(e)), 400
        dbManager.close()
        response_object['classroom'] = serialiseClassroom(classroom)
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
            try:
                dbManager.updateClassroom(id, number, typesOfClass, int(capacity))
            except ValueError as e:
                return jsonify(error = str(e)), 400
            dbManager.close()
            return jsonify({'response': 'success'})
        return jsonify({'response': 'failure'})
    return jsonify({'response': 'failure'})

@app.route('/classrooms', methods=['POST','GET'])
def addClassroom():
    if (currentUser.role != 0 and currentUser.role != 1):
        return jsonify(error = str("Only dispatcher has access")), 401

    response_object = {'response': 'success'}
    if request.method == 'POST':
        number = request.args.get('number')
        capacity = request.args.get('capacity')
        typesOfClass = request.args.get('typesOfClass').replace(" ", ",")
        if number is not None and capacity is not None and typesOfClass is not None:
            dbManager = DatabaseManager()
            try:
                dbManager.addClassroom(number, typesOfClass, int(capacity))
            except ValueError as e:
                return jsonify(error = str(e)), 400
            dbManager.close()
            return jsonify({'response': 'success'})
        return jsonify({'response': 'failure'})
    dbManager = DatabaseManager()
    teachers = dbManager.getAllClassroom()
    dbManager.close()
    response_object['classrooms'] = list(map(lambda x: serialiseClassroom(x), teachers))
    return jsonify(response_object)

@app.route('/faculties/<id>', methods=['GET','DELETE','PUT'])
def faculty(id):
    if (currentUser.role != 0 and currentUser.role != 1):
        return jsonify(error = str("Only dispatcher has access")), 401

    response_object = {'response': 'success'}
    if request.method == 'GET':
        dbManager = DatabaseManager()
        try:
            faculty = dbManager.getFaculty(id)
        except ValueError as e:
            return jsonify(error = str(e)), 400
        dbManager.close()
        response_object['faculty'] = serialiseFaculty(faculty)
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
            try:
                dbManager.updateFaculty(id, name)
            except ValueError as e:
                return jsonify(error = str(e)), 400
            dbManager.close()
            return jsonify({'response': 'success'})
        return jsonify({'response': 'failure'})
    return jsonify({'response': 'failure'})

@app.route('/faculties', methods=['POST','GET'])
def addFaculty():
    if (currentUser.role != 0 and currentUser.role != 1):
        return jsonify(error = str("Only dispatcher has access")), 401

    response_object = {'response': 'success'}
    if request.method == 'POST':
        name = request.args.get('name')
        if name is not None:
            dbManager = DatabaseManager()
            try:
                dbManager.addFaculty(name)
            except ValueError as e:
                return jsonify(error = str(e)), 400
            dbManager.close()
            return jsonify({'response': 'success'})
        return jsonify({'response': 'failure'})
    dbManager = DatabaseManager()
    faculties = dbManager.getAllFaculty()
    dbManager.close()
    response_object['faculties'] = list(map(lambda x: serialiseFaculty(x), faculties))
    return jsonify(response_object)

@app.route('/educationalPrograms/<id>', methods=['GET','DELETE','PUT'])
def educationalProgram(id):
    if (currentUser.role != 0 and currentUser.role != 1):
        return jsonify(error = str("Only dispatcher has access")), 401

    response_object = {'response': 'success'}
    if request.method == 'GET':
        dbManager = DatabaseManager()
        try:
            educationalProgram = dbManager.getEducationalProgram(id)
        except ValueError as e:
            return jsonify(error = str(e)), 400
        dbManager.close()
        response_object['educationalProgram'] = serialiseEducationalProgram(educationalProgram)
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
            try:
                dbManager.updateEducationalProgram(id, facultyId, name)
            except ValueError as e:
                return jsonify(error = str(e)), 400
            dbManager.close()
            return jsonify({'response': 'success'})
        return jsonify({'response': 'failure'})
    return jsonify({'response': 'failure'})

@app.route('/educationalPrograms', methods=['POST','GET'])
def addEducationalProgram():
    if (currentUser.role != 0 and currentUser.role != 1):
        return jsonify(error = str("Only dispatcher has access")), 401

    response_object = {'response': 'success'}
    if request.method == 'POST':
        facultyId = request.args.get('facultyId')
        name = request.args.get('name').replace("_", ",").replace("-", ".")
        if name is not None and facultyId is not None:
            dbManager = DatabaseManager()
            try:
                dbManager.addEducationalProgram(facultyId, name)
            except ValueError as e:
                return jsonify(error = str(e)), 400
            dbManager.close()
            return jsonify({'response': 'success'})
        return jsonify({'response': 'failure'})
    dbManager = DatabaseManager()
    educationalPrograms = dbManager.getAllEducationalProgram()
    dbManager.close()
    response_object['educationalPrograms'] = list(map(lambda x: serialiseEducationalProgram(x), educationalPrograms))
    return jsonify(response_object)

@app.route('/groups/<id>', methods=['GET','DELETE','PUT'])
def group(id):
    if (currentUser.role != 0 and currentUser.role != 1):
        return jsonify(error = str("Only dispatcher has access")), 401

    response_object = {'response': 'success'}
    if request.method == 'GET':
        dbManager = DatabaseManager()
        try:
            group = dbManager.getGroup(id)
        except ValueError as e:
            return jsonify(error = str(e)), 400
        dbManager.close()
        response_object['group'] = serialiseGroup(group)
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
            try:
                dbManager.updateGroup(id, specializationId, name, int(amountOfStudents), int(yearOfStudy))
            except ValueError as e:
                return jsonify(error = str(e)), 400
            dbManager.close()
            return jsonify({'response': 'success'})
        return jsonify({'response': 'failure'})
    return jsonify({'response': 'failure'})

@app.route('/groups', methods=['POST','GET'])
def addGroup():
    if (currentUser.role != 0 and currentUser.role != 1):
        return jsonify(error = str("Only dispatcher has access")), 401 

    response_object = {'response': 'success'}
    if request.method == 'POST':
        specializationId = request.args.get('specializationId')
        name = request.args.get('name').replace("-", ".")
        amountOfStudents = request.args.get('amountOfStudents')
        yearOfStudy = request.args.get('yearOfStudy')
        if (specializationId is not None and name is not None and 
            amountOfStudents is not None and yearOfStudy is not None):
            dbManager = DatabaseManager()
            try:
                dbManager.addGroup(specializationId, name, int(amountOfStudents), int(yearOfStudy))
            except ValueError as e:
                return jsonify(error = str(e)), 400
            dbManager.close()
            return jsonify({'response': 'success'})
        return jsonify({'response': 'failure'})
    dbManager = DatabaseManager()
    groups = dbManager.getAllGroup()
    dbManager.close()
    response_object['groups'] = list(map(lambda x: serialiseGroup(x), groups))
    return jsonify(response_object)

@app.route('/subjects/<id>', methods=['GET','DELETE','PUT'])
def subject(id):
    if (currentUser.role != 0 and currentUser.role != 1):
        return jsonify(error = str("Only dispatcher has access")), 401

    response_object = {'response': 'success'}
    if request.method == 'GET':
        dbManager = DatabaseManager()
        try:
            subject = dbManager.getSubject(id)
        except ValueError as e:
            return jsonify(error = str(e)), 400
        dbManager.close()
        response_object['subject'] = serialiseSubject(subject)
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
            try:
                dbManager.updateSubject(id, specializationId, name, semesters, typeOfClass,
                    int(frequency), teacherId, int(amountOfGroups))
            except ValueError as e:
                return jsonify(error = str(e)), 400
            dbManager.close()
            return jsonify({'response': 'success'})
        return jsonify({'response': 'failure'})
    return jsonify({'response': 'failure'})

@app.route('/subjects', methods=['POST','GET'])
def addSubject():
    if (currentUser.role != 0 and currentUser.role != 1):
        return jsonify(error = str("Only dispatcher has access")), 401

    response_object = {'response': 'success'}
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
            try:
                dbManager.addSubject(specializationId, name, semesters, typeOfClass,
                    int(frequency), teacherId, int(amountOfGroups))
            except ValueError as e:
                return jsonify(error = str(e)), 400
            dbManager.close()
            return jsonify({'response': 'success'})
        return jsonify({'response': 'failure'})
    dbManager = DatabaseManager()
    subjects = dbManager.getAllSubject()
    dbManager.close()
    response_object['subjects'] = list(map(lambda x: serialiseSubject(x), subjects))
    return jsonify(response_object)

@app.route('/specializations/<id>', methods=['GET','DELETE','PUT'])
def specialization(id):
    if (currentUser.role != 0 and currentUser.role != 1):
        return jsonify(error = str("Only dispatcher has access")), 401

    response_object = {'response': 'success'}
    if request.method == 'GET':
        dbManager = DatabaseManager()
        try:
            specialization = dbManager.getSpecialization(id)
        except ValueError as e:
            return jsonify(error = str(e)), 400
        dbManager.close()
        response_object['specialization'] = serialiseSpecialization(specialization)
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
            try:
                dbManager.updateSpecialization(id, educationalProgramId, name)
            except ValueError as e:
                return jsonify(error = str(e)), 400
            dbManager.close()
            return jsonify({'response': 'success'})
        return jsonify({'response': 'failure'})
    return jsonify({'response': 'failure'})

@app.route('/specializations', methods=['POST','GET'])
def addSpecialization():
    if (currentUser.role != 0 and currentUser.role != 1):
        return jsonify(error = str("Only dispatcher has access")), 401

    response_object = {'response': 'success'}
    if request.method == 'POST':
        educationalProgramId = request.args.get('educationalProgramId')
        name = request.args.get('name')
        if name is not None and educationalProgramId is not None:
            dbManager = DatabaseManager()
            try:
                dbManager.addSpecialization(educationalProgramId, name)
            except ValueError as e:
                return jsonify(error = str(e)), 400
            dbManager.close()
            return jsonify({'response': 'success'})
        return jsonify({'response': 'failure'})
    if request.method == 'GET' and request.args.get('educationalProgramId') is not None:
        educationalProgramId = request.args.get('educationalProgramId')
        dbManager = DatabaseManager()
        try:
            specializations = dbManager.getAllSpecializationByEdProgram(educationalProgramId)
        except ValueError as e:
            return jsonify(error = str(e)), 400
        dbManager.close()
        return jsonify(list(map(lambda x: serialiseSpecialization(x), specializations)))
    dbManager = DatabaseManager()
    specializations = dbManager.getAllSpecialization()
    dbManager.close()
    response_object['specializations'] = list(map(lambda x: serialiseSpecialization(x), specializations))
    return jsonify(response_object)

@app.route('/constraints', methods=['GET','DELETE','PUT', 'POST'])
def constraints():
    if (currentUser.role != 0 and currentUser.role != 1):
        return jsonify(error = str("Only dispatcher has access")), 401

    response_object = {'response': 'success'}
    if request.method == 'GET':
        dbManager = DatabaseManager()
        try:
            constraints = dbManager.getConstraints()
        except ValueError as e:
            return jsonify(error = str(e)), 400
        dbManager.close()
        response_object['constraints'] = serialiseConstraints(constraints)
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
            try:
                dbManager.updateConstraints(firstClassStarts, classDuration,
                    shortBrakeDuration, largeBrakeDuration, studyDaysInWeek,
                    studyDaysInWeekForStudents, studyDaysInWeekForTeachers,
                    classesPerDay, classesPerDayStudents, classesPerDayTeachers,
                    lunchBrake, gaps, classroomFillness, semester)
            except ValueError as e:
                return jsonify(error = str(e)), 400
        if request.method == 'POST':
            try:
                dbManager.addConstraints(firstClassStarts, int(classDuration),
                    int(shortBrakeDuration), int(largeBrakeDuration), int(studyDaysInWeek),
                    int(studyDaysInWeekForStudents), int(studyDaysInWeekForTeachers),
                    int(classesPerDay), int(classesPerDayStudents), int(classesPerDayTeachers),
                    int(lunchBrake), int(gaps), int(classroomFillness), int(semester))
            except ValueError as e:
                return jsonify(error = str(e)), 400
        dbManager.close()
        return jsonify({'response': 'success'})
    return jsonify({'response': 'failure'})

@app.route('/generatedClasses', methods=['GET'])
def generatedClasses():
    if (currentUser.role != 0 and currentUser.role != 1):
        return jsonify(error = str("Only dispatcher has access")), 401

    response_object = {'response': 'success'}
    dbManager = DatabaseManager()
    generatedClasses = dbManager.getAllGeneratedClass()
    dbManager.close()
    response_object['generatedClasses'] = list(map(lambda x: serialiseGeneratedClass(x), generatedClasses))
    return jsonify(response_object)

@app.route('/generatedClasses/<id>', methods=['GET'])
def generatedClass(id):
    if (currentUser.role != 0 and currentUser.role != 1):
        return jsonify(error = str("Only dispatcher has access")), 401

    response_object = {'response': 'success'}    
    dbManager = DatabaseManager()
    generatedClass = dbManager.getGeneratedClass(id)
    dbManager.close()
    response_object['generatedClass'] = serialiseGeneratedClass(generatedClass)
    return jsonify(response_object)

@app.route('/groupsOfClass/<id>', methods=['GET'])
def groupsOfClass(id):
    if (currentUser.role != 0 and currentUser.role != 1):
        return jsonify(error = str("Only dispatcher has access")), 401

    response_object = {'response': 'success'}
    dbManager = DatabaseManager()
    groupsOfClass = dbManager.getAllGroupsOfClass(id)
    dbManager.close()
    response_object['groupsOfClass'] = groupsOfClass
    return jsonify(response_object)

# Доступ для всех
@app.route('/schedule/faculties', methods=['GET'])
def getFacultiesForSchedule():
    response_object = {'response': 'success'}
    dbManager = DatabaseManager()
    faculties = dbManager.getAllFaculty()
    dbManager.close()
    response_object['facultiesForSchedule'] = list(map(lambda x: serialiseFaculty(x), faculties))
    return jsonify(response_object)

# Доступ для всех
@app.route('/schedule/faculties/<id>', methods=['GET'])
def getGroupsForSchedule(id):
    response_object = {'response': 'success'}
    dbManager = DatabaseManager()
    groups = dbManager.getAllGroupByFaculty(id)
    dbManager.close()
    response_object['groupsForSchedule'] = list(map(lambda x: serialiseGroup(x), groups))
    return jsonify(response_object)

# Доступ для всех
@app.route('/schedule/groups/<group>', methods=['GET'])
def scheduleStudents(group):
    response_object = {'response': 'success'}
    dbManager = DatabaseManager()
    schedule = dbManager.getScheduleStudents(group)
    dbManager.close()
    response_object['scheduleStudents'] = serialiseSchedule(schedule)
    return jsonify(response_object)

# Доступ для всех
@app.route('/schedule/teachers', methods=['GET'])
def getTeachersForSchedule():
    response_object = {'response': 'success'}
    dbManager = DatabaseManager()
    teachers = dbManager.getAllTeacher()
    dbManager.close()
    response_object['teachersForSchedule'] = list(map(lambda x: serialiseTeacher(x), teachers))
    return jsonify(response_object)

# Доступ для всех
@app.route('/schedule/teachers/<teacherId>', methods=['GET'])
def scheduleTeachers(teacherId):
    response_object = {'response': 'success'}
    dbManager = DatabaseManager()
    schedule = dbManager.getScheduleTeachers(teacherId)
    dbManager.close()
    response_object['scheduleTeachers'] = serialiseSchedule(schedule)
    return jsonify(response_object)

@app.route('/yearShiftRight', methods=['PUT'])
def doYearShiftRight():
    if (currentUser.role != 0 and currentUser.role != 1):
        return jsonify(error = str("Only dispatcher has access")), 401    
    
    dbManager = DatabaseManager()
    dbManager.yearShiftRight()
    dbManager.close()
    return jsonify({'response': 'success'})

@app.route('/yearShiftLeft', methods=['PUT'])
def doYearShiftLeft():
    if (currentUser.role != 0 and currentUser.role != 1):
        return jsonify(error = str("Only dispatcher has access")), 401  
    
    dbManager = DatabaseManager()
    dbManager.yearShiftLeft()
    dbManager.close()
    return jsonify({'response': 'success'})

@app.route('/generate', methods=['GET'])
def generate():
    if (currentUser.role != 0 and currentUser.role != 1):
        return jsonify(error = str("Only dispatcher has access")), 401

    response_object = {'response': 'success'}    
    dbManager = DatabaseManager()
    generator.generate()
    res = dbManager.getAllGeneratedClass()

    dbManager.close()
    response_object['generate'] = list(map(lambda x: serialiseGeneratedClass(x), res))
    return jsonify(response_object)

@app.route('/overgenerate', methods=['GET'])
def overgenerate():
    if (currentUser.role != 0 and currentUser.role != 1):
        return jsonify(error = str("Only dispatcher has access")), 401    

    response_object = {'response': 'success'}
    dbManager = DatabaseManager()
    generator.overgenerate()
    res = dbManager.getAllGeneratedClass()

    dbManager.close()
    response_object['overgenerate'] = list(map(lambda x: serialiseGeneratedClass(x), res))
    return jsonify(response_object)

# id не надо!
@app.route('/addman', methods=['GET'])
def add_man():
    if (currentUser.role != 0 and currentUser.role != 1):
        return jsonify(error = str("Only dispatcher has access")), 401

    response_object = {'response': 'success'}
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
    response_object['addman'] = list(map(lambda x: serialiseGeneratedClass(x), res))
    return jsonify(response_object)

@app.route('/removeman/<id>', methods=['GET'])
def remove_man(id):
    if (currentUser.role != 0 and currentUser.role != 1):
        return jsonify(error = str("Only dispatcher has access")), 401     

    response_object = {'response': 'success'}
    dbManager = DatabaseManager()
    generator.remove_man(id)
    res = dbManager.getAllGeneratedClass()

    dbManager.close()
    response_object['removeman'] = list(map(lambda x: serialiseGeneratedClass(x), res))
    return jsonify(response_object)


@app.route('/users/<id>', methods=['GET','DELETE','PUT'])
def user(id):
    if (currentUser.role != 0 and currentUser.role != 1):
        return jsonify(error = str("Only dispatcher has access")), 401
        
    response_object = {'response': 'success'}
    if request.method == 'GET':
        dbManager = DatabaseManager()
        try:
            user = dbManager.getUser(id)
        except ValueError as e:
            return jsonify(error = str(e)), 400
        dbManager.close()
        response_object['user'] = serialiseUser(user)
        return jsonify(response_object)
    if request.method == 'DELETE':
        dbManager = DatabaseManager()
        try:
            dbManager.removeUser(id)
        except ValueError as e:
            return jsonify(error = str(e)), 400
        dbManager.close()
        return jsonify({'response': 'success'})
    if request.method == 'PUT':
        name = request.args.get('name')
        email = request.args.get('email')
        role = int(request.args.get('role'))
        teacherId = int(request.args.get('teacherId'))
        if name is not None and email is not None and role is not None:
            dbManager = DatabaseManager()
            try:
                dbManager.updateUser(id, name, email, role, teacherId)
            except ValueError as e:
                return jsonify({'error': str(e)})
            dbManager.close()
            return jsonify({'response': 'success'})
        return jsonify({'response': 'failure'})
    return jsonify({'response': 'failure'})

@app.route('/currentuser', methods=['GET'])
def current_user():
    response_object = {'response': 'success'}
    user = User.User(role = 3)
    response_object['currentuser'] = serialiseUser(user)
    return jsonify(response_object)

import random
@app.route('/users', methods=['POST','GET'])
def addUser():
    if (currentUser.role != 0 and currentUser.role != 1):
        return jsonify(error = str("Only dispatcher has access")), 401

    response_object = {'response': 'success'}
    if request.method == 'POST':
        name = request.args.get('name')
        email = request.args.get('email')
        role = int(request.args.get('role'))
        if role == 1:
            roleString = "Dispatcher"
        if role == 2:
            roleString = "Teacher"
        teacherId = request.args.get('teacherId')
        if teacherId is not None:
            teacherId = int(teacherId)
        if name is not None and email is not None and role is not None:
            dbManager = DatabaseManager()
            password = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(12))
            passwordHash = generate_password_hash(password)
            try:
                dbManager.addUser(name, email, passwordHash, role, teacherId)
                msg = Message("NSU Timetable Membership", recipients=[email])
                msg.body = "Dear " + name + "!\n\nYou are now a member of NSU Timetable.\nYour role is: " + roleString + "\n\nYour automatically generated password is:\n" + password + "\nYou can change it later."
                mail.send(msg)
            except ValueError as e:
                return jsonify(error = str(e)), 400
            dbManager.close()
            return jsonify({'response': 'success'})
        return jsonify({'response': 'failure'})
    dbManager = DatabaseManager()
    try:
        users = dbManager.getAllUser()
    except ValueError as e:
        return jsonify(error = str(e)), 400
    dbManager.close()
    response_object['users'] = list(map(lambda x: serialiseUser(x), users))
    return jsonify(response_object)

"""
@app.route('/signUp', methods=['POST','GET'])
def signUpUser():
    if request.method == 'POST':
        id = request.args.get('id')
        password = request.args.get('password')
        if id is not None and password is not None:
            dbManager = DatabaseManager()
            try:
                dbManager.signUpUser(id, password)
            except ValueError as e:
                return jsonify({'error': str(e)})
            dbManager.close()
            return jsonify({'response': 'success'})
        return jsonify({'response': 'failure'})
    return jsonify({'response': 'failure'})
"""

@app.route('/login', methods=['POST'])
def login():
    if (currentUser.role != 0 and currentUser.role != 1):
        return jsonify(error = str("Already logged in")), 401

    email = request.args.get('email')
    password = request.args.get('password')
    remember = True
    dbManager = DatabaseManager()
    try:
        user = dbManager.getUserByEmail(email)
    except ValueError as e:
        return jsonify(error = str(e)), 400
    dbManager.close()

    if not user.checkPassword(password):
        return jsonify(error = "wrong password"), 400

    login_user(user, remember=remember)
    global currentUser
    currentUser = user

    return jsonify({'response': 'success'})

@app.route('/changePassword', methods=['POST'])
def changePassword():
    if (currentUser.role == 3):
        return jsonify(error = str("You need to log in first")), 401

    oldPassword = request.args.get('oldPassword')
    newPassword = request.args.get('newPassword')
    newPasswordHash = generate_password_hash(newPassword)
    user = currentUser
    dbManager = DatabaseManager()

    if not user.checkPassword(oldPassword):
        return  jsonify({'error': str("wrong password")})

    dbManager.changePassword(user.id, newPasswordHash)

    return jsonify({'response': 'success'})

@app.route('/logout', methods=['POST'])
def logout():
    global currentUser

    if (currentUser.role == 3):
        return jsonify(error = str("You need to log in first")), 401
        
    logout_user()
    currentUser = User.User(role=3)

    return jsonify({'response': 'success'})
    
if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.run()