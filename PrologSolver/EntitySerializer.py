from entities.Teacher import Teacher
from entities.Classroom import Classroom
from entities.Faculty import Faculty
from entities.EducationalProgram import EducationalProgram
from entities.Group import Group
from entities.Subject import Subject
from entities.Specialization import Specialization
from entities.Constraints import Constraints

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
        'firstClassStarts': 'null', 
        'classDuration': 'null',
        'shortBrakeDuration': 'null', 
        'largeBrakeDuration': 'null', 
        'studyDaysInWeek': 'null',
        'studyDaysInWeekForStudents': 'null', 
        'studyDaysInWeekForTeachers': 'null', 
        'classesPerDay': 'null', 
        'classesPerDayStudents': 'null', 
        'classesPerDayTeachers': 'null',
        'lunchBrake': 'null', 
        'gaps': 'null', 
        'classroomFillness': 'null', 
        'semester': 'null'
    }
