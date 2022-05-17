from django.db import models

# Create your models here.


class Auditories(models.Model):  # Faculty - name, only Name field
    AuditoryId = models.AutoField(primary_key=True)
    TypeOfClass = models.CharField(max_length=500)
    Capacity = models.CharField(max_length=500)
    Number = models.CharField(max_length=500)


class Constraints(models.Model):
    FirstClassStarts = models.CharField(max_length=500)
    ClassDuration = models.CharField(max_length=500)
    ShortBrakeDuration = models.CharField(max_length=500)
    LargeBrakeDuration = models.CharField(max_length=500)
    StudyDaysInWeek = models.CharField(max_length=500)
    StudyDaysInWeekForStudents = models.CharField(max_length=500)
    StudyDaysInWeekForTeachers = models.CharField(max_length=500)
    ClassesPerDay = models.CharField(max_length=500)
    ClassesPerDayStudents = models.CharField(max_length=500)
    ClassesPerDayTeachers = models.CharField(max_length=500)
    LunchBrake = models.CharField(max_length=500)
    Gaps = models.CharField(max_length=500)
    ClassroomFillness = models.CharField(max_length=500)


class EducationalPrograms(models.Model):
    Faculty = models.CharField(max_length=500)
    EducationalProgram = models.CharField(max_length=500)
    Specialization = models.CharField(max_length=500)


class Faculties(models.Model):
    Faculty = models.CharField(max_length=500)
    EducationalProgram = models.CharField(max_length=500)


class GeneratedEntities(models.Model):
    Specialization = models.CharField(max_length=500)
    Day = models.CharField(max_length=500)
    Subject = models.CharField(max_length=500)
    Teacher = models.CharField(max_length=500)
    Auditory = models.CharField(max_length=500)
    Groups = models.CharField(max_length=500)
    NumberOfClass = models.CharField(max_length=500)
    TypeOfClass = models.CharField(max_length=500)


class GeneratedSchedule(models.Model):
    id = models.AutoField(primary_key=True)
    Faculty = models.CharField(max_length=500)
    EducationalProgram = models.CharField(max_length=500)
    Specialization = models.CharField(max_length=500)
    Subject = models.CharField(max_length=500)
    Semester = models.CharField(max_length=500)
    Teacher = models.CharField(max_length=500)
    TypeOfClass = models.CharField(max_length=500)
    Auditory = models.CharField(max_length=500)
    Groups = models.CharField(max_length=500)
    Day = models.CharField(max_length=500)
    ClassNumber = models.CharField(max_length=500)


class Groups(models.Model):
    Specialization = models.CharField(max_length=500)
    Number = models.CharField(max_length=500)
    AmountOfStudents = models.CharField(max_length=500)
    YearOfStudy = models.CharField(max_length=500)


class Subjects(models.Model):
    Specialization = models.CharField(max_length=500)
    Name = models.CharField(max_length=500)
    Semesters = models.CharField(max_length=500)
    TypeOfClass = models.CharField(max_length=500)
    Frequency = models.CharField(max_length=500)
    Teacher = models.CharField(max_length=500)
    AmountOfGroups = models.CharField(max_length=500)


class Teachers(models.Model):
    Subject = models.CharField(max_length=500)
    Name = models.CharField(max_length=500)
    DaysCanWork = models.CharField(max_length=500)
    DaysWantWork = models.CharField(max_length=500)
    Weight = models.CharField(max_length=500)


class entries(models.Model):
    id = models.AutoField(primary_key=True)
    Faculty = models.CharField(max_length=500)
    EducationalProgram = models.CharField(max_length=500)
    Specialization = models.CharField(max_length=500)
    Subject = models.CharField(max_length=500)
    Teacher = models.CharField(max_length=500)
    TypeOfClass = models.CharField(max_length=500)
    Auditory = models.CharField(max_length=500)
    Groups = models.CharField(max_length=500)
    Day = models.CharField(max_length=500)
    ClassNumber = models.CharField(max_length=500)

'''
class Department(models.Model): #Faculty - name, only Name field
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=500)

class Teacher(models.Model):
    TeacherId = models.AutoField(primary_key=True)
    TeacherName = models.CharField(max_length=500)
    Department = models.CharField(max_length=500)
    Preferencies = models.CharField(max_length=500)

class Group(models.Model):
    GroupId = models.AutoField(primary_key=True)
    GroupNumber = models.CharField(max_length=500)
    Department = models.CharField(max_length=500)

class Classroom(models.Model):
    ClassroomId = models.AutoField(primary_key=True)
    ClassroomNumber = models.CharField(max_length=500)'''


