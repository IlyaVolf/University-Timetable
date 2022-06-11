from pyswip import Prolog
import datetime

import addManTests
from DatabaseManager import DatabaseManager

# NB:
# пока штраф будет храниться как 0-й!
from entities.Subject import Subject

# число попыток, если это значение не задано явно
attempts = 1

def buildPrologList(elements, brackets, prefix, postfix):
    res = "["
    for i in range(0, len(elements), 1):
        res += prefix
        if brackets:
            res += "\""
        res += elements[i]
        if brackets:
            res += "\""
        res += postfix
        if i < len(elements) - 1:
            res += ", "
    res += "]"

    return res


# 0 - generate
# 1 - remove manually one subject
# 2 - add manually one subject
# 3 - add one subject


def create_pl(mode, classToAdd=None):
    with open("fit_new_department_db.pl", "w") as file:
        file.write(":- module(fit_new_department_db, [ \n\
	      teacher/1, \n\
	      type_of_class/1, \n\
		  classroom/3, \n\
		  faculty/1, \n\
		  ed_program/2, \n\
		  specialization/2, \n\
          getSpecialization/3, \n\
		  subject/4, \n\
		  group_of_students/4, \n\
		  first_class_starts/2, \n\
		  class_duration/1, \n\
		  short_brake_duration/1, \n\
		  long_brake_duration/1, \n\
		  study_days_in_week/1, \n\
		  study_days_in_week_students/1, \n\
		  study_days_in_week_teachers/1, \n\
		  classes_in_day/1, \n\
		  classes_in_day_students/1, \n\
		  classes_in_day_teachers/1, \n\
		  days_teacher_can_work/2, \n\
		  c_lunch_break/1, \n\
		  c_gaps/2, \n\
		  days_teacher_want_work/3, \n\
		  semester/1, \n\
		  list_groups_of_students/3, \n\
		  attempts/1, \n\
		  classroom_fillness/3]). \n")

        file.write("\n")
        file.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n\
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% DATABASE %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n\
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n")
        file.write("\n")

        file.write("attempts(2). \n")

        file.write("\n")

        allTeachers = dbManager.getAllTeachers()
        for teacher in allTeachers:
            file.write("teacher(\"" + teacher.name + "\"). \n")

        file.write("\n")

        allTypesOfClasses = dbManager.getAllTypesOfClasses()
        for typeOfClass in allTypesOfClasses:
            file.write("type_of_class(\"" + typeOfClass + "\"). \n")

        file.write("\n")

        allAuditories = dbManager.getAuditories()
        for auditory in allAuditories:
            typeOfClass = auditory.typesOfClass.split(", ")
            file.write(
                "classroom(\"" + auditory.number + "\", " + buildPrologList(typeOfClass, True, "type_of_class(", ")")
                + ", " + auditory.capacity + "). \n")

        file.write("\n")
        file.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n\
% PART TWO - FACS, ED PRS, SPECS % \n\
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n")
        file.write("\n")

        allFaculties = dbManager.getAllFaculties()
        for faculty in allFaculties:
            file.write("faculty(\"" + faculty + "\"). \n")

        file.write("\n")

        for faculty in allFaculties:
            allEdPrograms = dbManager.getEducationalProgramsIlya(faculty)
            for edProgram in allEdPrograms:
                file.write("ed_program(\"" + faculty + "\", \"" + edProgram + "\"). \n")

        file.write("\n")

        for faculty in allFaculties:
            allEdPrograms = dbManager.getEducationalPrograms(faculty)
            for edProgram in allEdPrograms:
                file.write("specialization(\"" + edProgram.name + "\", \"" + edProgram.specialization + "\"). \n")

        file.write("\n")

        file.write("getSpecialization(Specialization, EdProgram, Faculty) :- \n\
	specialization(EdProgram, Specialization), \n\
	ed_program(Faculty, EdProgram). \n")

        file.write("\n")

        file.write("\n")
        file.write("%%%%%%%%%%%%%%%%%%%%%%%%% \n\
% PART THREE - SUBJECTS % \n\
%%%%%%%%%%%%%%%%%%%%%%%%% \n")
        file.write("\n")

        # create
        if mode == 0 or mode == 1:

            allSubjects = dbManager.getAllSubjects()
            for subject in allSubjects:
                file.write("subject(\"" + subject[0] + "\", \"" + subject[1] + "\", [" + subject[2] + "], [")
                allSubjectsTypesOfClass = dbManager.getAllSubjectTypesOfClass(subject[0], subject[1], subject[2])
                for i in range(0, len(allSubjectsTypesOfClass), 1):
                    file.write(
                        "[type_of_class(\"" + allSubjectsTypesOfClass[i][0] + "\"), " + allSubjectsTypesOfClass[i][1]
                        + ", [")
                    allSubjectTeachers = dbManager.getAllSubjectTeachers(subject[0], subject[1], subject[2],
                                                                         allSubjectsTypesOfClass[i][0],
                                                                         allSubjectsTypesOfClass[i][1])
                    for j in range(0, len(allSubjectTeachers), 1):
                        file.write(
                            "[teacher(\"" + allSubjectTeachers[j][0] + "\"), " + allSubjectTeachers[j][1] + "]")
                        if j < len(allSubjectTeachers) - 1:
                            file.write(", ")

                    file.write("]]")
                    if i < len(allSubjectsTypesOfClass) - 1:
                        file.write(", ")
                file.write("]). \n")

        if mode == 2:
            # Это для теста надо! Вообще это не надо будет.
            #file.write("teacher(\"Derzho Marina Anatolievna\"). \n")
            #file.write("days_teacher_can_work(teacher(\"Derzho Marina Anatolievna\"), [1,2,3,4,5,6]). \n")
            #file.write("days_teacher_want_work(teacher(\"Derzho Marina Anatolievna\"), [1,2,3,4,5,6], 0). \n")

            file.write("subject(\"Computer Science and Systems Engineering\", \"Interface design\", [5], "
                       "[[type_of_class(\"lec\"), 1, [[teacher(\"Derzho Marina Anatolievna\"), 2]]]]). \n")

            allSubjects = dbManager.getAllSubjects()
            for subject in allSubjects:
                file.write("subject(\"" + subject[0] + "\", \"" + subject[1] + "\", [" + subject[2] + "], [")
                allSubjectsTypesOfClass = dbManager.getAllSubjectTypesOfClass(subject[0], subject[1], subject[2])
                for i in range(0, len(allSubjectsTypesOfClass), 1):
                    file.write(
                        "[type_of_class(\"" + allSubjectsTypesOfClass[i][0] + "\"), " + allSubjectsTypesOfClass[i][1]
                        + ", [")
                    allSubjectTeachers = dbManager.getAllSubjectTeachers(subject[0], subject[1], subject[2],
                                                                         allSubjectsTypesOfClass[i][0],
                                                                         allSubjectsTypesOfClass[i][1])
                    for j in range(0, len(allSubjectTeachers), 1):
                        file.write(
                            "[teacher(\"" + allSubjectTeachers[j][0] + "\"), " + allSubjectTeachers[j][1] + "]")
                        if j < len(allSubjectTeachers) - 1:
                            file.write(", ")

                    file.write("]]")
                    if i < len(allSubjectsTypesOfClass) - 1:
                        file.write(", ")
                file.write("]). \n")

        if mode == 3:
            # Это для теста надо! Вообще это не надо будет.
            #file.write("teacher(\"Derzho Marina Anatolievna\"). \n")
            #file.write("days_teacher_can_work(teacher(\"Derzho Marina Anatolievna\"), [1,2,3,4,5,6]). \n")
            #file.write("days_teacher_want_work(teacher(\"Derzho Marina Anatolievna\"), [1,2,3,4,5,6], 0). \n")
            ###################################################################################################

            file.write("subject(\"" + classToAdd.specialization + "\", \"" + classToAdd.subjectName + "\", " +
                       buildPrologList(classToAdd.getSemesters(), False, "", "") + ", [[type_of_class(\""
                       + classToAdd.typeOfClass + "\"), " + str(classToAdd.frequency) + ", [[teacher(\"" +
                       classToAdd.teacher + "\"), " + str(classToAdd.amountOfGroups) + "]]]]). \n")

        file.write("\n")

        file.write("\n")
        file.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n\
% PART FOUR - GROUPS OF STUDENTS % \n\
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n")
        file.write("\n")

        allGroups = dbManager.getAllGroups()
        for group in allGroups:
            file.write("group_of_students(\"" + group.specialization + "\", \"" + group.numberOfGroup + "\", " +
                       group.amountOfStudents + ", " + group.yearOfStudy + "). \n")

        file.write("\n")

        for faculty in allFaculties:
            allEdPrograms = dbManager.getEducationalProgramsIlya(faculty)
            for edProgram in allEdPrograms:
                allSpecializations = dbManager.getSpecializations(faculty, edProgram)
                for specialization in allSpecializations:
                    allUniqueYears = dbManager.getAllSpecializationUniqueYears(specialization)
                    for year in allUniqueYears:
                        allSpecializationGroups = dbManager.getAllSpecializationGroups(specialization, year)
                        file.write(
                            "list_groups_of_students(\"" + specialization + "\", " + str(year) + ", " +
                            buildPrologList(allSpecializationGroups, True, "", "") + "). \n")

        file.write("\n")

        file.write("\n")
        file.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n\
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% CONSTRAINTS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n\
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n")
        file.write("\n")

        file.write("\n")
        file.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n\
% PART FIVE - HARD CONSTRAINTS % \n\
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n")
        file.write("\n")

        constraints = dbManager.getConstraints()

        file.write("semester(" + constraints[0].semester + "). \n")
        file.write("first_class_starts(" + constraints[0].firstClassStarts + "). \n")
        file.write("class_duration(" + constraints[0].classDuration + "). \n")
        file.write("short_brake_duration(" + constraints[0].shortBrakeDuration + "). \n")
        file.write("long_brake_duration(" + constraints[0].largeBrakeDuration + "). \n")
        file.write("study_days_in_week(" + constraints[0].studyDaysInWeek + "). \n")
        file.write("study_days_in_week_students(" + constraints[0].studyDaysInWeekForStudents + "). \n")
        file.write("study_days_in_week_teachers(" + constraints[0].studyDaysInWeekForTeachers + "). \n")
        file.write("classes_in_day(" + constraints[0].classesPerDay + "). \n")
        file.write("classes_in_day_students(" + constraints[0].classesPerDayStudents + "). \n")
        file.write("classes_in_day_teachers(" + constraints[0].classesPerDayTeachers + "). \n")

        file.write("\n")

        for teacher in allTeachers:
            file.write(
                "days_teacher_can_work(teacher(\"" + teacher.name + "\"), " + teacher.daysTeacherCanWork + "). \n")

        file.write("\n")

        file.write("\n")
        file.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n\
% PART SIX - SOFT CONSTRAINTS         % \n\
%                                     % \n\
% WEIGHTS (PENALTY POINTS)            % \n\
% Penalty points are accounted if a   % \n\
% constraint is not satisfied         % \n\
% 0 - TURN OFF                        % \n\
% 1-9 - PREFERABLE BUT NOT OBLIGATORY % \n\
% 10 - OBLIGATORY TO SATISFY          % \n\
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n")
        file.write("\n")

        file.write("c_lunch_break(" + constraints[0].lunchBrake + "). \n")
        file.write("c_gaps(0,0). \n")
        file.write("c_gaps(1,2). \n")
        file.write("c_gaps(2,6). \n")
        file.write("c_gaps(3,9). \n")
        file.write("c_gaps(Amount_of_gaps, 10) :- Amount_of_gaps > 3. \n")
        file.write("classroom_fillness(0, 10, 10). \n")

        file.write("\n")

        for teacher in allTeachers:
            file.write(
                "days_teacher_want_work(teacher(\"" + teacher.name + "\"), " + teacher.daysTeacherWantWork + ", " +
                teacher.weight + "). \n")

        file.write("\n")


def save():
    dbManager.clearGeneratedScheduleTable()

    with open("query.txt", "r") as file:
        data = file.read()

    strings = data.split("\n")

    dbManager.clearClassToGroupTable()
    for i in range(1, len(strings) - 1, 1):
        elements = strings[i].split(";")
        dbManager.addGeneratedClass(i, elements[0], elements[1].replace(',', ':'), elements[2], elements[3], elements[4],
                                    elements[5], elements[6], elements[7], elements[8], elements[9], elements[10])


# Функция рассчитывает время начала пары
def calculateTimeStart(classNumber):
    constraints = dbManager.getConstraints()
    classesPerDay = int(constraints.classesPerDay)
    startTime = constraints.firstClassStarts
    classDuration = int(constraints.classDuration)
    shortBrake = int(constraints.shortBrakeDuration)
    longBrake = int(constraints.largeBrakeDuration)

    inMinutes = (classNumber - 1) * (classDuration + shortBrake + longBrake)

    if classNumber > classesPerDay:
        return -1, -1

    time = datetime.datetime(2000, 1, 1, int(startTime.split(",")[0]), int(startTime.split(",")[1]), 0) + \
           datetime.timedelta(minutes=inMinutes)

    return time.hour, time.minute


# Функция рассчитывает время конца пары
def calculateTimeEnd(classNumber):
    constraints = dbManager.getConstraints()
    classesPerDay = int(constraints.classesPerDay)
    startTime = constraints.firstClassStarts
    classDuration = int(constraints.classDuration)
    shortBrake = int(constraints.shortBrakeDuration)
    longBrake = int(constraints.largeBrakeDuration)

    inMinutes = (classNumber - 1) * (classDuration + shortBrake + longBrake) + classDuration + shortBrake

    if classNumber > classesPerDay:
        return -1, -1

    time = datetime.datetime(2000, 1, 1, int(startTime.split(",")[0]), int(startTime.split(",")[1]), 0) + \
           datetime.timedelta(minutes=inMinutes)

    return time.hour, time.minute


def fromClassToEvent(classToTransform):
    res = "event(class(\"" + classToTransform.specialization + "\", \"" + classToTransform.subject + "\", " + \
          str(classToTransform.semester) + ", type_of_class(\"" + classToTransform.typeOfClass + "\"), teacher(\"" + \
          classToTransform.teacher + "\"), " + str(classToTransform.getAmountOfGroups()) + ", 1, 0), \"" + \
          classToTransform.auditory + "\", " + \
          str(classToTransform.day) + ", " + \
          buildPrologList(classToTransform.getGroups(), True, "", "") + \
          ", " + str(classToTransform.classNumber) + ")"

    return res


def fromClassesToSchedule(wrapper):
    res = ""

    if wrapper:
        res += "currentSchedule("

    classes = dbManager.getAllGeneratedClasses()
    res += "["
    for i in range(0, len(classes), 1):
        res += fromClassToEvent(classes[i])
        if i < len(classes) - 1:
            res += ", "

    res += "]"

    if wrapper:
        res += ", 0)"

    return res


# генерация расписания с 0. Предыдущее расписание, если было, удаляется
def generate():
    create_pl(0)
    prolog = Prolog()
    prolog.consult("fit_new_department_db.pl")
    prolog.consult("main.pl")
    print(list(prolog.query("main(" + str(attempts) + ").")))
    save()


# Добавление одного предмета с неполным указанием характеристик - система к текущему расписанию сама добавит
# новое занятие самым оптимальным образом, если это возможно.
# Требуется подать на вход элемент таблицы Subjects (класс Subject).
# TODO Нужно как-то заполучить занятие - объект класса Subject
def add(classToAdd):
    schedule = fromClassesToSchedule(True)
    create_pl(3, classToAdd)
    prolog = Prolog()
    prolog.consult("fit_new_department_db.pl")
    prolog.consult("main.pl")
    print(list(prolog.query("add(" + schedule + ", " + str(attempts) + ").")))
    save()


# удаление одного предмета из текущего расписания. Требуется подать на вход элемент таблицы GeneratedSchedule
# (класс GeneratedClass).
# TODO Нужно как-то заполучить занятие - объект класса GeneratedClass (написать метод извлечения по id из dbManager,
# TODO например)
def remove_man(classToDelete):
    event = fromClassToEvent(classToDelete)
    schedule = fromClassesToSchedule(False)
    create_pl(1)
    prolog = Prolog()
    prolog.consult("fit_new_department_db.pl")
    prolog.consult("main.pl")
    print(list(prolog.query("remove(" + schedule + ", " + event + ")")))
    save()


# добавление одного предмета с полным указанием параметров вручную. Если противоречий нет с текущим расписанием, то
# предмет добавится. Требуется подать на вход элемент таблицы GeneratedSchedule (класс GeneratedClass).
# TODO Нужно как-то заполучить занятие - объект класса GeneratedClass (написать метод извлечения по id из dbManager,
# TODO например)
def add_man(classToAdd):
    event = fromClassToEvent(classToAdd)
    schedule = fromClassesToSchedule(False)
    create_pl(2)
    prolog = Prolog()
    prolog.consult("fit_new_department_db.pl")
    prolog.consult("main.pl")
    print(list(prolog.query("addManually(" + schedule + ", " + event + ")")))
    save()


# ВНУТРЕННИЕ ТЕСТЫ

# Проверка простой генерации
def test0():
    generate()


# Проверка инкрементального добавления: авто добавления предмета
def test1():
    generate()
    add(Subject(
        "Computer Science and Systems Engineering",
        "Interface design",
        "5",
        "lec",
        1,
        "Derzho Marina Anatolievna",
        2
    ))


# Тут я провожу тест: генерирую расписание с нуля, затем удаляю пердмет вручную и возвращаю его обратно вручную,
# удаляю интерфейсы Держо на всякий и добавляю вновь. Предметов после генерации с 0 - 23, в конце - 23 или 24 в
# зависимости от того, заняты ли 19213 и 19214 группы 4-й парой в субботу или нет.
def test2():
    generate()
    a = dbManager.getAllGeneratedClasses()[0]
    remove_man(a)
    add_man(a)
    remove_man(addManTests.test4(a))
    add_man(addManTests.test4(a))


dbManager = DatabaseManager()

# test0, test1, test2
#test2()
#dbManager.initFaculty()
#dbManager.addFaculty("Department of Information Technologies")
#dbManager.addFaculty("Department of Natural Science")
#dbManager.addEducationalProgram(1, "BACH, 09.03.01, Computer Science and Engineering")
#dbManager.removeEducationalProgram(2)
#dbManager.removeFaculty(2)
#dbManager.clearSpecialization()
#dbManager.addSpecialization(1, "Computer Science and Systems Engineering")
#dbManager.addSpecialization(1, "Software Engineering and Computer Science")
#dbManager.clearGroup()
#dbManager.addGroup(2, "20212", 17, 2)
#print(dbManager.getGroup(1).name)
#dbManager.addTeacher("Derzho Marina Anatolievna","[1,2,3,4,5,6]","[1,2,3]",5)
#dbManager.addClassroom("t2221", "lab, pr", 20)
#dbManager.addSubject(1, "Electrical engineering and Electronics", "3,4", "pr", 1, 13, 3)
dbManager.addConstraints("9,0", 90, 5, 15, 6, 6, 5, 7, 3, 3, 5, 3, 6, 1)

print(calculateTimeStart(3))
print(calculateTimeEnd(3))

dbManager.close()

# вам надо: generate, remove_man, add, add_man, calculateTimeEnd, calculateTimeStart
