from entities.Teacher import Teacher
from entities.Classroom import Classroom
from entities.Faculty import Faculty
from entities.EducationalProgram import EducationalProgram
from entities.Group import Group
from entities.Subject import Subject
from entities.Specialization import Specialization
from entities.Constraints import Constraints
from entities.GeneratedClass import GeneratedClass
from entities.Schedule import Schedule
from entities.User import User

def serialiseTeacher(teacher: Teacher):
    return {
        'id': teacher.id,
        'name': teacher.name,
        'daysCanWork': teacher.daysCanWork,
        'daysWantWork': teacher.daysWantWork,
        'weight': teacher.weight
    }

def serialiseClassroom(classroom: Classroom):
    return {
        'id': classroom.id,
        'capacity': classroom.capacity,
        'number': classroom.number,
        'typesOfClass': classroom.typesOfClass
    }

def serialiseFaculty(faculty: Faculty):
    return {
        'id': faculty.id,
        'faculty': faculty.faculty
    }

def serialiseEducationalProgram(educationalProgram: EducationalProgram):
    return {
        'id': educationalProgram.id,
        'facultyId': educationalProgram.facultyId,
        'educationalProgram': educationalProgram.educationalProgram
    }

def serialiseGroup(group: Group):
    return {
        'id': group.id,
        'specializationId': group.specializationId,
        'name': group.name,
        'amountOfStudents': group.amountOfStudents,
        'yearOfStudy': group.yearOfStudy
    }

def serialiseUser(user: User):
    return {
        'id': user.id,
        'name': user.name,
        'email': user.email,
        'passwordHash': user.passwordHash,
        'role': user.role,
        'teacherId': user.teacherId,
        'status': user.status
    }

def serialiseSubject(subject: Subject):
    return {
        'id': subject.id,
        'specializationId': subject.specializationId,
        'name': subject.name,
        'semesters': subject.semesters,
        'typeOfClass': subject.typeOfClass,
        'frequency': subject.frequency,
        'teacherId': subject.teacherId,
        'amountOfGroups': subject.amountOfGroups,
        'generated': subject.generated
    }

def serialiseSpecialization(specialization: Specialization):
    return {
        'id': specialization.id,
        'educationalProgramId': specialization.educationalProgramId,
        'specialization': specialization.specialization 
    }

def serialiseConstraints(constraints: Constraints):
    return {
        'firstClassStarts': constraints.firstClassStarts, 
        'classDuration': constraints.classDuration,
        'shortBrakeDuration': constraints.shortBrakeDuration, 
        'largeBrakeDuration': constraints.largeBrakeDuration, 
        'studyDaysInWeek': constraints.studyDaysInWeek,
        'studyDaysInWeekForStudents': constraints.studyDaysInWeekForStudents, 
        'studyDaysInWeekForTeachers': constraints.studyDaysInWeekForTeachers, 
        'classesPerDay': constraints.classesPerDay, 
        'classesPerDayStudents': constraints.classesPerDayStudents, 
        'classesPerDayTeachers': constraints.classesPerDayTeachers,
        'lunchBrake': constraints.lunchBrake, 
        'gaps': constraints.gaps, 
        'classroomFillness': constraints.classroomFillness, 
        'semester': constraints.semester
    }

def serialiseGeneratedClass(generatedClass: GeneratedClass):
    return {
        'id': generatedClass.id,
        'faculty': generatedClass.faculty,
        'educationalProgram': generatedClass.educationalProgram,
        'specialization': generatedClass.specialization,
        'subject': generatedClass.subject,
        'semester': generatedClass.semester,
        'teacher': generatedClass.teacher,
        'typeOfClass': generatedClass.typeOfClass,
        'auditory': generatedClass.auditory,
        'groups': generatedClass.groups,
        'day': generatedClass.day,
        'classNumber': generatedClass.classNumber,
        'teacherId': generatedClass.teacherId
    }

def serialiseScheduleEntity(scheduleEntity):
    if scheduleEntity is not None:
        return [{
            'subject': scheduleEntity.subject,
            'typeOfClass': scheduleEntity.typeOfClass,
            'teacher': scheduleEntity.teacher,
            'auditory': scheduleEntity.auditory,
            'groups': scheduleEntity.groups,
            'classNumber': scheduleEntity.classNumber,
            'time': scheduleEntity.time
        }]
    return [{
            'subject': 'null',
            'typeOfClass': 'null',
            'teacher': 'null',
            'auditory': 'null',
            'groups': 'null',
            'classNumber': 'null',
            'time': 'null'
        }]

def serialiseSchedule(schedule: Schedule):
    entities = [[serialiseScheduleEntity(schedule.scheduleEntities[i][j]) for i in range(schedule.studyDaysInWeek)] for j in range(schedule.classesPerDay)]
    return {
        'type': schedule.type,
        'classesPerDay': schedule.classesPerDay,
        'studyDaysInWeek': schedule.studyDaysInWeek,
        'scheduleEntities': entities
    }

def serialiseSchedule2(schedule: Schedule):
    entities = [[serialiseScheduleEntity(schedule.scheduleEntities[i][j]) for i in range(schedule.studyDaysInWeek)] for j in range(schedule.classesPerDay)]
    return {
        'type': schedule.type,
        'classesPerDay': schedule.classesPerDay,
        'studyDaysInWeek': schedule.studyDaysInWeek,
        'scheduleEntities': entities
    }
