from flask import Flask, jsonify, request
from flask_cors import CORS

from EntitySerializer import serialiseTeacher, serialiseClassroom, serialiseEducationalProgram, serialiseFaculty, serialiseGroup, serialiseSubject, serialiseSpecialization, serialiseConstraints
from DatabaseManager import DatabaseManager

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)

@app.route('/teachers/<id>', methods=['GET','DELETE','PUT'])
def teacher(id):
    response_object = {'id': 'null', 'name': 'null','daysCanWork': 'null',
    'daysWantWork': 'null', 'weight': 'null'}
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
        daysCanWork = "[" + request.args.get('daysCanWork').replace(" ", ",") + "]"
        daysWantWork = "[" + request.args.get('daysWantWork').replace(" ", ",") + "]"
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
        daysCanWork = "[" + request.args.get('daysCanWork').replace(" ", ",") + "]"
        daysWantWork = "[" + request.args.get('daysWantWork').replace(" ", ",") + "]"
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
    response_object = {'id': 'null', 'capacity': 'null','number': 'null',
    'typesOfClass': 'null'}
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
            dbManager.updateFaculty(id, faculty)
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
    response_object = {'id': 'null', 'facultyId': 'null', 'name': 'null'}
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
        name = request.args.get('name')
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
        name = request.args.get('name')
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
        name = request.args.get('name')
        amountOfStudents = request.args.get('amountOfStudents')
        yearOfStudy = request.args.get('yearOfStudy')
        if specializationId is not None and name is not None and amountOfStudents is not None and yearOfStudy is not None:
            dbManager = DatabaseManager()
            dbManager.updateGroup(id, specializationId, name, amountOfStudents, yearOfStudy)
            dbManager.close()
            return jsonify({'response': 'success'})
        return jsonify({'response': 'failure'})
    return jsonify({'response': 'failure'})

@app.route('/groups', methods=['POST','GET'])
def addGroup():
    if request.method == 'POST':
        specializationId = request.args.get('specializationId')
        name = request.args.get('name')
        amountOfStudents = request.args.get('amountOfStudents')
        yearOfStudy = request.args.get('yearOfStudy')
        if (specializationId is not None and name is not None and 
            amountOfStudents is not None and yearOfStudy is not None):
            dbManager = DatabaseManager()
            dbManager.addGroup(specializationId, name, amountOfStudents, yearOfStudy)
            dbManager.close()
            return jsonify({'response': 'success'})
        return jsonify({'response': 'failure'})
    dbManager = DatabaseManager()
    groups = dbManager.getAllGroup()
    dbManager.close()
    return jsonify(list(map(lambda x: serialiseGroup(x), groups)))

@app.route('/subjects/<id>', methods=['GET','DELETE','PUT'])
def subject(id):
    response_object = {'id': 'null', 'specializationId': 'null', 'name': 'null',
    'semesters': 'null', 'typeOfClass': 'null', 'frequency': 'null', 'teacherId': 'null',
    'amountOfGroups': 'null', 'generated': 'null'}
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
        semesters = request.args.get('semesters')
        typeOfClass = request.args.get('typeOfClass')
        frequency = request.args.get('frequency')
        teacherId = request.args.get('teacherId')
        amountOfGroups = request.args.get('amountOfGroups')
        generated = request.args.get('generated')
        if (specializationId is not None and name is not None and semesters is not None 
            and typeOfClass is not None and frequency is not None and teacherId is not None
            and amountOfGroups is not None and generated is not None):
            dbManager = DatabaseManager()
            dbManager.updateSubject(id, specializationId, name, semesters, typeOfClass,
                frequency, teacherId, amountOfGroups)
            dbManager.close()
            return jsonify({'response': 'success'})
        return jsonify({'response': 'failure'})
    return jsonify({'response': 'failure'})

@app.route('/subjects', methods=['POST','GET'])
def addSubject():
    if request.method == 'POST':
        specializationId = request.args.get('specializationId')
        name = request.args.get('name')
        semesters = request.args.get('semesters')
        typeOfClass = request.args.get('typeOfClass')
        frequency = request.args.get('frequency')
        teacherId = request.args.get('teacherId')
        amountOfGroups = request.args.get('amountOfGroups')
        generated = request.args.get('generated')
        if (specializationId is not None and name is not None and semesters is not None 
            and typeOfClass is not None and frequency is not None and teacherId is not None
            and amountOfGroups is not None and generated is not None):
            dbManager = DatabaseManager()
            dbManager.addSubject(specializationId, name, semesters, typeOfClass,
                frequency, teacherId, amountOfGroups)
            dbManager.close()
            return jsonify({'response': 'success'})
        return jsonify({'response': 'failure'})
    dbManager = DatabaseManager()
    subjects = dbManager.getAllSubject()
    dbManager.close()
    return jsonify(list(map(lambda x: serialiseSubject(x), subjects)))

@app.route('/specializations/<id>', methods=['GET','DELETE','PUT'])
def specialization(id):
    response_object = {'id': 'null', 'educationalProgramId': 'null', 'name': 'null'}
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
            dbManager.updateSpecialization(id, educationalProgramId, specialization)
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
    dbManager = DatabaseManager()
    specializations = dbManager.getAllSpecialization()
    dbManager.close()
    return jsonify(list(map(lambda x: serialiseSpecialization(x), specializations)))

@app.route('/constraints', methods=['GET','DELETE','PUT', 'POST'])
def constraints(id):
    response_object = {'firstClassStarts': 'null', 'classDuration': 'null',
    'shortBrakeDuration': 'null', 'largeBrakeDuration': 'null', 'studyDaysInWeek': 'null',
    'studyDaysInWeekForStudents': 'null', 'studyDaysInWeekForTeachers': 'null', 
    'classesPerDay': 'null', 'classesPerDayStudents': 'null', 'classesPerDayTeachers': 'null',
    'lunchBrake': 'null', 'gaps': 'null', 'classroomFillness': 'null', 'semester': 'null'}
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
    
if __name__ == '__main__':
    app.run()