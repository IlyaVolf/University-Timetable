from pyswip import Prolog

from DatabaseManager import DatabaseManager
from entities.GeneratedClass import GeneratedClass

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


def create_pl(mode):
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

        allTeachers = dbManager.getAllTeacher()
        for teacher in allTeachers:
            file.write("teacher(\"" + teacher.name + "\"). \n")

        file.write("\n")

        allTypesOfClasses = dbManager.getAllTypesOfClasses()
        for typeOfClass in allTypesOfClasses:
            file.write("type_of_class(\"" + typeOfClass + "\"). \n")

        file.write("\n")

        allClassrooms = dbManager.getAllClassroom()
        for classroom in allClassrooms:
            typeOfClass = classroom.typesOfClass.split(", ")
            file.write(
                "classroom(\"" + classroom.number + "\", " + buildPrologList(typeOfClass, True, "type_of_class(", ")")
                + ", " + str(classroom.capacity) + "). \n")

        file.write("\n")
        file.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n\
% PART TWO - FACS, ED PRS, SPECS % \n\
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n")
        file.write("\n")

        allFaculties = dbManager.getAllFaculty()
        for faculty in allFaculties:
            file.write("faculty(\"" + faculty.faculty + "\"). \n")

        file.write("\n")

        for faculty in allFaculties:
            allEdPrograms = dbManager.getAllEducationalProgramByFaculty(faculty.id)
            for edProgram in allEdPrograms:
                file.write("ed_program(\"" + faculty.faculty + "\", \"" + edProgram.educationalProgram + "\"). \n")
                allSpecializations = dbManager.getAllSpecializationByEdProgram(edProgram.id)
                for specialization in allSpecializations:
                    file.write("specialization(\"" + edProgram.educationalProgram + "\", \"" +
                               specialization.specialization + "\"). \n")

        file.write("\n")

        # for faculty in allFaculties:
        #    allEdPrograms = dbManager.getEducationalPrograms(faculty)
        #    for edProgram in allEdPrograms:
        #        file.write("specialization(\"" + edProgram.name + "\", \"" + edProgram.specialization + "\"). \n")

        # file.write("\n")

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

            allSubjects = dbManager.getAllSubjectsDistinct()
            for subject in allSubjects:
                spec = dbManager.getSpecialization(subject[0])
                file.write("subject(\"" + spec.specialization + "\", \"" + subject[1] + "\", [" + subject[2] + "], [")
                allSubjectsTypesOfClass = dbManager.getAllSubjectTypesOfClass(subject[0], subject[1], subject[2])
                for i in range(0, len(allSubjectsTypesOfClass), 1):
                    file.write(
                        "[type_of_class(\"" + allSubjectsTypesOfClass[i][0] + "\"), " +
                        str(allSubjectsTypesOfClass[i][1]) + ", [")
                    allSubjectTeachers = dbManager.getAllSubjectTeachers(subject[0], subject[1], subject[2],
                                                                         allSubjectsTypesOfClass[i][0],
                                                                         allSubjectsTypesOfClass[i][1])
                    for j in range(0, len(allSubjectTeachers), 1):
                        subjectTeacher = dbManager.getTeacher(allSubjectTeachers[j][0])
                        file.write(
                            "[teacher(\"" + subjectTeacher.name + "\"), " + str(allSubjectTeachers[j][1]) + "]")
                        if j < len(allSubjectTeachers) - 1:
                            file.write(", ")

                    file.write("]]")
                    if i < len(allSubjectsTypesOfClass) - 1:
                        file.write(", ")
                file.write("]). \n")

        if mode == 2:
            # Это для теста надо! Вообще это не надо будет.
            # file.write("teacher(\"Derzho Marina Anatolievna\"). \n")
            # file.write("days_teacher_can_work(teacher(\"Derzho Marina Anatolievna\"), [1,2,3,4,5,6]). \n")
            # file.write("days_teacher_want_work(teacher(\"Derzho Marina Anatolievna\"), [1,2,3,4,5,6], 0). \n")

            # file.write("subject(\"Computer Science and Systems Engineering\", \"Interface design\", [5], "
            #           "[[type_of_class(\"lec\"), 1, [[teacher(\"Derzho Marina Anatolievna\"), 2]]]]). \n")

            allSubjects = dbManager.getAllSubject()
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
            # file.write("teacher(\"Derzho Marina Anatolievna\"). \n")
            # file.write("days_teacher_can_work(teacher(\"Derzho Marina Anatolievna\"), [1,2,3,4,5,6]). \n")
            # file.write("days_teacher_want_work(teacher(\"Derzho Marina Anatolievna\"), [1,2,3,4,5,6], 0). \n")
            ###################################################################################################

            subjectsToAdd = dbManager.getAllUngeneratedSubjects()

            for subjectToAdd in subjectsToAdd:
                spec = dbManager.getSpecialization(subjectToAdd.specializationId)
                teac = dbManager.getTeacher(subjectToAdd.teacherId)
                file.write("subject(\"" + spec.specialization + "\", \"" + subjectToAdd.name + "\", " +
                           buildPrologList(subjectToAdd.getSemesters(), False, "", "") + ", [[type_of_class(\""
                           + subjectToAdd.typeOfClass + "\"), " + str(subjectToAdd.frequency) + ", [[teacher(\"" +
                           teac.name + "\"), " + str(subjectToAdd.amountOfGroups) + "]]]]). \n")

        file.write("\n")

        file.write("\n")
        file.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n\
% PART FOUR - GROUPS OF STUDENTS % \n\
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n")
        file.write("\n")

        allGroups = dbManager.getAllGroup()
        for group in allGroups:
            spec = dbManager.getSpecialization(group.specializationId)
            file.write("group_of_students(\"" + spec.specialization + "\", \"" + group.name + "\", " +
                       str(group.amountOfStudents) + ", " + str(group.yearOfStudy) + "). \n")

        file.write("\n")

        for faculty in allFaculties:
            allEdPrograms = dbManager.getAllEducationalProgramByFaculty(faculty.id)
            for edProgram in allEdPrograms:
                allSpecializations = dbManager.getAllSpecializationByEdProgram(edProgram.id)
                for specialization in allSpecializations:
                    allUniqueYears = dbManager.getAllSpecializationUniqueYears(specialization.id)
                    for year in allUniqueYears:
                        allSpecializationGroups = dbManager.getAllSpecializationGroups(specialization.id, year)
                        file.write(
                            "list_groups_of_students(\"" + specialization.specialization + "\", " + str(year) + ", " +
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

        file.write("semester(" + str(constraints.semester) + "). \n")
        file.write("first_class_starts(" + constraints.firstClassStarts + "). \n")
        file.write("class_duration(" + str(constraints.classDuration) + "). \n")
        file.write("short_brake_duration(" + str(constraints.shortBrakeDuration) + "). \n")
        file.write("long_brake_duration(" + str(constraints.largeBrakeDuration) + "). \n")
        file.write("study_days_in_week(" + str(constraints.studyDaysInWeek) + "). \n")
        file.write("study_days_in_week_students(" + str(constraints.studyDaysInWeekForStudents) + "). \n")
        file.write("study_days_in_week_teachers(" + str(constraints.studyDaysInWeekForTeachers) + "). \n")
        file.write("classes_in_day(" + str(constraints.classesPerDay) + "). \n")
        file.write("classes_in_day_students(" + str(constraints.classesPerDayStudents) + "). \n")
        file.write("classes_in_day_teachers(" + str(constraints.classesPerDayTeachers) + "). \n")

        file.write("\n")

        for teacher in allTeachers:
            file.write(
                "days_teacher_can_work(teacher(\"" + teacher.name + "\"), " + teacher.daysCanWork + "). \n")

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

        file.write("c_lunch_break(" + str(constraints.lunchBrake) + "). \n")
        file.write("c_gaps(0,0). \n")
        file.write("c_gaps(1,2). \n")
        file.write("c_gaps(2,6). \n")
        file.write("c_gaps(3,9). \n")
        file.write("c_gaps(Amount_of_gaps, 10) :- Amount_of_gaps > 3. \n")
        file.write("classroom_fillness(0, 10, 10). \n")

        file.write("\n")

        for teacher in allTeachers:
            file.write(
                "days_teacher_want_work(teacher(\"" + teacher.name + "\"), " + str(teacher.daysWantWork) + ", " +
                str(teacher.weight) + "). \n")

        file.write("\n")


# Сохраняем результат в БД
def save():
    dbManager.initGeneratedScheduleTable()

    with open("query.txt", "r") as file:
        data = file.read()

    strings = data.split("\n")

    for i in range(1, len(strings) - 1, 1):
        elements = strings[i].split(";")
        dbManager.addGeneratedClass(i, elements[0], elements[1].replace(',', ':'), elements[2], elements[3],
                                    elements[4],
                                    elements[5], elements[6], elements[7], elements[8], elements[9], elements[10],
                                    dbManager.getTeacherByName(elements[5]).id)


def fromClassToEvent(classToTransform):
    res = "event(class(\"" + classToTransform.specialization + "\", \"" + classToTransform.subject + "\", " + \
          str(classToTransform.semester) + ", type_of_class(\"" + classToTransform.typeOfClass + "\"), teacher(\"" + \
          classToTransform.teacher + "\"), " + str(classToTransform.getAmountOfGroups()) + ", 1, 0), \"" + \
          classToTransform.auditory + "\", " + \
          str(classToTransform.day) + ", " + \
          buildPrologList(classToTransform.getGroupsAsString(), True, "", "") + \
          ", " + str(classToTransform.classNumber) + ")"

    return res


# возвращаем текущее расписание
def fromClassesToSchedule(wrapper):
    res = ""

    if wrapper:
        res += "currentSchedule("

    classes = dbManager.getAllGeneratedClass()
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
    dbManager.markAsGeneratedSubject()
    save()
    return dbManager.getAllGeneratedClass()


# догенерация расписания, используя текущее сгенерированное расписание
def overgenerate():
    schedule = fromClassesToSchedule(True)
    create_pl(3)
    prolog = Prolog()
    prolog.consult("fit_new_department_db.pl")
    prolog.consult("main.pl")
    print(list(prolog.query("add(" + schedule + ", " + str(attempts) + ").")))
    dbManager.markAsGeneratedSubject()
    save()
    return dbManager.getAllGeneratedClass()


# удаление одного предмета из текущего расписания. Требуется подать на вход элемент таблицы GeneratedSchedule
# (класс GeneratedClass).
# TODO Если fail, то размер списка 0?
def remove_man(id):
    classToDelete = dbManager.getGeneratedClass(id)
    event = fromClassToEvent(classToDelete)
    schedule = fromClassesToSchedule(False)
    create_pl(0)
    prolog = Prolog()
    prolog.consult("fit_new_department_db.pl")
    prolog.consult("main.pl")
    print(list(prolog.query("remove(" + schedule + ", " + event + ")")))
    save()
    return dbManager.getAllGeneratedClass()


# добавление одного предмета с полным указанием параметров вручную. Если противоречий нет с текущим расписанием, то
# предмет добавится. Требуется подать на вход элемент таблицы GeneratedSchedule (класс GeneratedClass).
# TODO Если fail, то размер списка 0?
def add_man(classToAdd):
    event = fromClassToEvent(classToAdd)
    schedule = fromClassesToSchedule(False)
    create_pl(0)
    prolog = Prolog()
    prolog.consult("fit_new_department_db.pl")
    prolog.consult("main.pl")
    print(list(prolog.query("addManually(" + schedule + ", " + event + ")")))
    save()
    return dbManager.getAllGeneratedClass()


# ВНУТРЕННИЕ ТЕСТЫ

# Проверка простой генерации
def test0():
    generate()


# Проверка инкрементального добавления: авто добавления предмета
def test1():
    generate()
    dbManager.addSubject(1, "Interface design", "5", "lec", 1, 16, 2)
    overgenerate()
    dbManager.removeSubject(23)


# Тут я провожу тест: генерирую расписание с нуля, затем удаляю пердмет вручную и возвращаю его обратно вручную,
# удаляю интерфейсы Держо на всякий и добавляю вновь. Предметов после генерации с 0 - 23, в конце - 23 или 24 в
# зависимости от того, заняты ли 19213 и 19214 группы 4-й парой в субботу или нет.
def test2():
    generate()
    a = dbManager.getGeneratedClass(1)
    remove_man(1)
    add_man(a)

    # Заполняется диспетчером вручную!
    clazz = GeneratedClass(
        a.id,
        a.faculty,
        a.educationalProgram,
        "Computer Science and Systems Engineering",
        "Interface design",
        5,
        "Derzho Marina Anatolievna",
        "lec",
        "1156",
        "[19213,19214]",
        6,
        4,
        16
    )

    add_man(clazz)


dbManager = DatabaseManager()

# test0, test1, test2
dbManager.updateConstraints("9,0", 90, 5, 15, 6, 6, 5, 7, 3, 3, 5, 3, 6, 1)

# простая генерация
generate()

# TODO штраф может быть из-за больших окон. Это нормально!

# test2()

res = dbManager.getScheduleStudents("20213").scheduleEntities
# res = dbManager.getScheduleTeachers("Puzarenko Vadim Grigorievich").scheduleEntities
for i in range(6):
    for j in range(len(res[i])):
        print(i + 1, res[i][j].subject, res[i][j].teacher, res[i][j].typeOfClass,
              res[i][j].auditory, res[i][j].groups, res[i][j].time)

# dbManager.initGeneratedScheduleTable()
# dbManager.yearShiftLeft()
# dbManager.initFaculty()
# dbManager.addFaculty("Department of Information Technologies")
# dbManager.addFaculty("Department of Natural Science")
# dbManager.addEducationalProgram(1, "BACH, 09.03.01, Computer Science and Engineering")
# dbManager.removeEducationalProgram(2)
# dbManager.removeFaculty(2)
# dbManager.clearSpecialization()
# dbManager.addSpecialization(1, "Computer Science and Systems Engineering")
# dbManager.addSpecialization(1, "Software Engineering and Computer Science")
# dbManager.clearGroup()
# dbManager.addGroup(2, "20212", 17, 2)
# print(dbManager.getGroup(1).name)
# dbManager.addTeacher("Derzho Marina Anatolievna","[1,2,3,4,5,6]","[1,2,3]",5)
# dbManager.addClassroom("t2221", "lab, pr", 20)
# dbManager.addSubject(1, "Electrical engineering and Electronics", "3,4", "pr", 1, 13, 3)
# dbManager.addConstraints("9,0", 90, 5, 15, 6, 6, 5, 7, 3, 3, 5, 3, 6, 1)

dbManager.close()

# вам надо: generate, remove_man, add, add_man, calculateTimeEnd, calculateTimeStart
