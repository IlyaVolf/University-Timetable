import pandas as pd
from pyswip import Prolog

from DatabaseManager import DatabaseManager


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


# TODO функция для рассчёта начала и конца занятий


def create():
    dbManager = DatabaseManager()

    with open("fit_new_department_db.pl", "w") as file:
        file.write(":- module(fit_new_department_db, [ \n\
	      teacher/1, \n\
	      type_of_class/1, \n\
		  classroom/3, \n\
		  faculty/1, \n\
		  ed_program/2, \n\
		  specialization/2, \n\
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
        file.write("semester(1). \n")

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

        file.write("\n")
        file.write("%%%%%%%%%%%%%%%%%%%%%%%%% \n\
% PART THREE - SUBJECTS % \n\
%%%%%%%%%%%%%%%%%%%%%%%%% \n")
        file.write("\n")

        allSubjects = dbManager.getAllSubjects()
        for subject in allSubjects:
            file.write("subject(\"" + subject[0] + "\", \"" + subject[1] + "\", [" + subject[2] + "], [")
            allSubjectsTypesOfClass = dbManager.getAllSubjectTypesOfClass(subject[0], subject[1], subject[2])
            for i in range(0, len(allSubjectsTypesOfClass), 1):
                file.write("[type_of_class(\"" + allSubjectsTypesOfClass[i][0] + "\"), " + allSubjectsTypesOfClass[i][1]
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

    dbManager.close()


create()
prolog = Prolog()
prolog.consult("main.pl")
print(list(prolog.query("main(1).")))
