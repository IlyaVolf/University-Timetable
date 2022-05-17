from dataclasses import fields
import imp
from rest_framework import serializers
from TimetableApp.models import Auditories, Constraints,  EducationalPrograms, Faculties, GeneratedEntities, Groups, Subjects, Teachers, entries

class AuditorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Auditories
        fields=('AuditoryId','TypeOfClass', 'Capacity', 'Number')


class ConstraintsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Constraints
        fields=('FirstClassStarts', 'ClassDuration', 'ShortBrakeDuration', 
        'LargeBrakeDuration', 'StudyDaysInWeek', 'StudyDaysInWeekForStudents',
        'StudyDaysInWeekForTeachers', 'ClassesPerDay', 'ClassesPerDayStudents',
        'ClassesPerDayTeachers', 'LunchBrake', 'Gaps', 'ClassroonFillness')


class EducationalProgramsSerializer(serializers.ModelSerializer):
    class Meta:
        model=EducationalPrograms
        fields=('Faculty', 'EducationalProgram', 'Specialization')

class FacultiesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Faculties
        fields=('Faculty', 'EducationalProgram')

class GeneratedEntitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model=GeneratedEntities
        fields=('Specialization', 'Day', 'Subject', 'Teacher', 'Auditory', 'Groups', 'NumberOfClass', 'TypeOfClass')


class GeneratedScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model=GeneratedEntities
        fields=('id', 'Faculty', 'EducationalProgram', 'Specialization', 'Subject', 'Semester', 'Teacher', 
        'TypeOfClass', 'Auditory', 'Groups', 'Day', 'ClassNumber')

class GroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Groups
        fields=('Specialization', 'Number', 'AmountOfStudetns', 'YearOfStudy')

class SubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Subjects
        fields=('Specialization', 'Name', 'Semesters', 'TypeOfClass', 'Frequency', 'Teacher', 'AmountOfGroups')

class TeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teachers
        fields=('Subject', 'Name', 'DaysCanWork', 'DaysWantWork', 'Weight')

class EntriesSerializer(serializers.ModelSerializer):
    class Meta:
        model=entries
        fields=('id', 'Faculty', 'EducationalProgram', 'Specialization', 'Subject', 'Teacher', 
        'TypeOfClass', 'Auditory', 'Groups', 'Day', 'ClassNumber')



'''
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields=('DepartmentId', 'DepartmentName')

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields=('TeacherId', 'TeacherName', 'Department', 'Preferencies')

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model=Group
        fields=('GroupId', 'GroupNumber', 'Department')

class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model=Classroom
        fields=('ClassroomId', 'ClassroomNumber')
'''