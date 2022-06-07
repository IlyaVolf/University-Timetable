:- module(fit_new_department, [
	      teacher/1,
	      type_of_class/1,
	      type_of_classroom/3,
		  building/1,
		  classroom/3,
		  faculty/1,
		  ed_program/2,
		  specialization/2,
		  subject/4,
		  group_of_students/4,
		  first_class_starts/2,
		  class_duration/1,
		  short_brake_duration/1,
		  long_brake_duration/1,
		  study_days_in_week/1,
		  study_days_in_week_students/1,
		  study_days_in_week_teachers/1,
		  classes_in_day/1,
		  classes_in_day_students/1,
		  classes_in_day_teachers/1,
		  days_teacher_can_work/2,
		  c_lunch_break/1,
		  c_gaps/2,
		  days_teacher_want_work/3,
		  semester/1,
		  list_groups_of_students/3,
		  attempts/1,
		  classroom_fillness/3]).

% Dear prey of the legacy. Faculties hashes are temporarily obtained via SHA-256 algorithm
% https://sha256.online
% All data validity is checked in JAVA!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
% То есть если контрольные суммы не сходятся, списки пустые - всё это должно быть проверено до запуска Пролога.

/*
	ПРАВИЛО СОСТАВЛЕНИЯ ФАЙЛА ДЛЯ НКРЕМЕНТАЛЬНОГО ДОБАВЛЕНИЯ:
	Все данные и ограничения берутся из дб. НО!!!!!! В документ нужно заливать subject(-ы), который хотим добавить к уже
	сгенерированному расписанию. А так всё то же самое. Команда append().
*/

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% DATABASE %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%
% Attemps to build a timetable.
% attempts(0 < Number).
attempts(2).

%
% Current semester
% semester(1<= Number <= 2).
% 1 - autumn semester, 2 - spring semester.
%
semester(1).

%
% Teachers database
% teacher(name_of_teacher).
%
teacher("Пермяков Руслан Анатольевич").
teacher("Злыгостев Антон Игоревич").
teacher("Букшев Иван Евгеньевич").
teacher("Васкевич Владимир Леонтьевич").
teacher("Адаманский Антон Валентинович").
teacher("Ситнов Владимир Евгеньевич").
teacher("Мигинский Дмитрий Сергеевич").
teacher("Терентьева Татьяна Александровна").
teacher("Постовалов Сергей Николаевич").
teacher("Балабанов Артем Андреевич").
teacher("Антонец Денис Викторович").
teacher("Шваб Ирина Васильевна").
teacher("Авдеев Роман Русланович").
teacher("Горчаков Константин Михайлович").
teacher("Пузаренко Вадим Григорьевич").

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% PART ONE - TYPES OF CLASSES AND CLASSROOMS %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%
% Type of classes
% type_of_class(Name_of_type_of_class).
type_of_class("pr").
type_of_class("lec").
type_of_class("lab").
type_of_class("pe").
type_of_class("misc").

%
% Classrooms
% type_of_classroom(Code_of_classroom, Type_of_class[], INT Capacity_of_classroom)
% classroom(Name_of_classroom, Types_of_class, INT Capacity_of_classroom))
%
type_of_classroom("huge for lectures and practices", [type_of_class("lec"), type_of_class("pr")], 200).
% type_of_classroom("huge for lectures", [type_of_class("lec")], 200).
type_of_classroom("big for lectures and practices", [type_of_class("lec"), type_of_class("pr")], 80).
type_of_classroom("medium for lectures and practices", [type_of_class("lec"), type_of_class("pr")], 40).
type_of_classroom("small for lectures and practices", [type_of_class("lec"), type_of_class("pr")], 20).
type_of_classroom("terminals", [type_of_class("pr"), type_of_class("lab")], 20).
type_of_classroom("room for pe", [type_of_class("pe")], 500).
% type_of_classroom("huge for lectures and practices", type_of_class("lec"), 200).
% type_of_classroom("big for lectures and practices", type_of_class("lec"), 80).
% type_of_classroom("big for lectures and practices", type_of_class("pr"), 80).
% type_of_classroom("medium for lectures and practices", type_of_class("lec"), 40).
% type_of_classroom("medium for lectures and practices", type_of_class("pr"), 40).
% type_of_classroom("small for lectures and practices", type_of_class("lec"), 20).
% type_of_classroom("small for lectures and practices", type_of_class("pr"), 20).
% type_of_classroom("terminals", type_of_class("pr"), 20).
% type_of_classroom("terminals", type_of_class("lab"), 20).
% type_of_classroom("room for pe", [type_of_class("pe")], 500).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% BETA   BETA   BETA   BETA   BETA   BETA   BETA   BETA   BETA   BETA   BETA   BETA   BETA   BETA   BETA   BETA   BETA   BETA   BETA   BETA
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% Buildings
% building(Name_of_Building)
%
building("Главный корпус").
building("Новый корпус").
building("Спорткомплекс").

% classroom(building("Новый корпус"), "1156", Types_of_class, Capacity_of_classroom) :- type_of_classroom("huge for lectures and pratices", Types_of_class, Capacity_of_classroom).
% classroom(building("Новый корпус"), "т3213", Types_of_class, Capacity_of_classroom) :- type_of_classroom("terminals", Types_of_class, Capacity_of_classroom).
% classroom(building("Главный корпус"), "402 ГК", Types_of_class, Capacity_of_classroom) :- type_of_classroom("huge for lectures and practices", Types_of_class, Capacity_of_classroom).
% classroom(building("Спорткомплекс"), "СК", Types_of_class, Capacity_of_classroom) :- type_of_classroom("room for pe", Types_of_class, Capacity_of_classroom).
% classroom(building("Новый корпус"), "т2266", Types_of_class, Capacity_of_classroom) :- type_of_classroom("terminals", Types_of_class, Capacity_of_classroom).
% classroom(building("Новый корпус"), "2128", Types_of_class, Capacity_of_classroom) :- type_of_classroom("big for lectures and practices", Types_of_class, Capacity_of_classroom).
% classroom(building("Новый корпус"), "т3220", Types_of_class, Capacity_of_classroom) :- type_of_classroom("terminals", Types_of_class, Capacity_of_classroom).
% classroom(building("Новый корпус"), "1154", Types_of_class, Capacity_of_classroom) :- type_of_classroom("small for lectures and practices", Types_of_class, Capacity_of_classroom).
% classroom(building("Главный корпус"), "406 ГК", Types_of_class, Capacity_of_classroom) :- type_of_classroom("small for lectures and practices", Types_of_class, Capacity_of_classroom).
% classroom(building("Новый корпус"), "т2266", Types_of_class, Capacity_of_classroom) :- type_of_classroom("terminals", Types_of_class, Capacity_of_classroom).
% classroom(building("Новый корпус"), "1155", Types_of_class, Capacity_of_classroom) :- type_of_classroom("medium for lectures and practices", Types_of_class, Capacity_of_classroom).
% classroom(building("Новый корпус"), "т2213", Types_of_class, Capacity_of_classroom) :- type_of_classroom("terminals", Types_of_class, Capacity_of_classroom).
% classroom(building("Новый корпус"), "т2221", Types_of_class, Capacity_of_classroom) :- type_of_classroom("terminals", Types_of_class, Capacity_of_classroom).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% BETA   BETA   BETA   BETA   BETA   BETA   BETA   BETA   BETA   BETA   BETA   BETA   BETA   BETA   BETA   BETA   BETA   BETA   BETA   BETA
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

classroom("1156", Types_of_class, Capacity_of_classroom) :- type_of_classroom("huge for lectures and pratices", Types_of_class, Capacity_of_classroom).
classroom("т3213", Types_of_class, Capacity_of_classroom) :- type_of_classroom("terminals", Types_of_class, Capacity_of_classroom).
classroom("402 ГК", Types_of_class, Capacity_of_classroom) :- type_of_classroom("huge for lectures and practices", Types_of_class, Capacity_of_classroom).
classroom("СК", Types_of_class, Capacity_of_classroom) :- type_of_classroom("room for pe", Types_of_class, Capacity_of_classroom).
classroom("т2266", Types_of_class, Capacity_of_classroom) :- type_of_classroom("terminals", Types_of_class, Capacity_of_classroom).
classroom("2128", Types_of_class, Capacity_of_classroom) :- type_of_classroom("big for lectures and practices", Types_of_class, Capacity_of_classroom).
classroom("т3220", Types_of_class, Capacity_of_classroom) :- type_of_classroom("terminals", Types_of_class, Capacity_of_classroom).
classroom("1154", Types_of_class, Capacity_of_classroom) :- type_of_classroom("small for lectures and practices", Types_of_class, Capacity_of_classroom).
classroom("406 ГК", Types_of_class, Capacity_of_classroom) :- type_of_classroom("small for lectures and practices", Types_of_class, Capacity_of_classroom).
classroom("1155", Types_of_class, Capacity_of_classroom) :- type_of_classroom("medium for lectures and practices", Types_of_class, Capacity_of_classroom).
classroom("т2213", Types_of_class, Capacity_of_classroom) :- type_of_classroom("terminals", Types_of_class, Capacity_of_classroom).
classroom("т2221", Types_of_class, Capacity_of_classroom) :- type_of_classroom("terminals", Types_of_class, Capacity_of_classroom).


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% PART TWO - FACS, ED PRS, SPECS %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%
% Faculties
% faculty(Name_of_faculty)
%
faculty("Faculty of Information Technologies").

%
% Education program
% ed_program(Name_of_faculty, Name_of_ed_program)
%
ed_program("Faculty of Information Technologies", "BACH, 09.03.01, Computer Science and Engineering").

%
% Specialization or profile
% specialization(Name_of_ed_program, Name_of_specialization)
%
specialization("BACH, 09.03.01, Computer Science and Engineering", "Computer Science and Systems Engineering").
specialization("BACH, 09.03.01, Computer Science and Engineering", "Software Engineering and Computer Science").


%%%%%%%%%%%%%%%%%%%%%%%%%
% PART THREE - SUBJECTS %
%%%%%%%%%%%%%%%%%%%%%%%%%

%
% Subjects
% subject(Name_of_ed_program, Name_of_subject, Semesters[], [Type_of_class, INT Frequency_of_class, [Teacher, INT amount_of_groups][]][])
% semesters: semester = [1,2] or [3] or [1,2,3,4,5,6]
%
% subject("Computer Science and Systems Engineering", "Электротехника и электроника", [3, 4], [[type_of_class("lec"), 1, [[teacher("Горчаков Константин Михайлович"), 2]]], [type_of_class("pr"), 1, [[teacher("Горчаков Константин Михайлович"), 2]]]]).

subject("Computer Science and Systems Engineering", "Модели вычислений", [3, 4], [[type_of_class("lec"), 1, [[teacher("Пузаренко Вадим Григорьевич"), 3]]], [type_of_class("pr"), 1, [[teacher("Пузаренко Вадим Григорьевич"), 2], [teacher("Авдеев Роман Русланович"), 1]]]]).
% subject("Computer Science and Systems Engineering", "Модели вычислений", [5, 6], [[type_of_class("lec"), 1, [[teacher("Пузаренко Вадим Григорьевич"), 2]]], [type_of_class("pr"), 1, [[teacher("Пузаренко Вадим Григорьевич"), 1], [teacher("Авдеев Роман Русланович"), 1]]]]).
subject("Computer Science and Systems Engineering", "Методы машинного обучения", [5], [[type_of_class("lec"), 1, [[teacher("Постовалов Сергей Николаевич"), 2]]], [type_of_class("pr"), 1, [[teacher("Антонец Денис Викторович"), 2]]]]).
subject("Computer Science and Systems Engineering", "Теория вероятности и математическая статистика", [3], [[type_of_class("lec"), 1, [[teacher("Постовалов Сергей Николаевич"), 3]]], [type_of_class("pr"), 1, [[teacher("Постовалов Сергей Николаевич"), 2], [teacher("Антонец Денис Викторович"), 1]]]]).
subject("Computer Science and Systems Engineering", "Дифференциальные уравнения и теория функций комплексного переменного", [3], [[type_of_class("lec"), 1, [[teacher("Васкевич Владимир Леонтьевич"), 3]]], [type_of_class("pr"), 1, [[teacher("Васкевич Владимир Леонтьевич"), 2], [teacher("Шваб Ирина Васильевна"), 1]]]]).
subject("Computer Science and Systems Engineering", "Вычислительная математика", [5], [[type_of_class("lec"), 1, [[teacher("Васкевич Владимир Леонтьевич"), 2]]], [type_of_class("pr"), 1, [[teacher("Васкевич Владимир Леонтьевич"), 1], [teacher("Шваб Ирина Васильевна"), 1]]]]).
subject("Computer Science and Systems Engineering", "Командная разработка многофункционального программно-аппаратного комплекса", [5], [[type_of_class("lec"), 1, [[teacher("Адаманский Антон Валентинович"), 2]]], [type_of_class("pr"), 2, [[teacher("Адаманский Антон Валентинович"), 2]]]]).
subject("Software Engineering and Computer Science", "Электротехника и электроника", [5], [[type_of_class("lec"), 1, [[teacher("Горчаков Константин Михайлович"), 12]]], [type_of_class("pr"), 1, [[teacher("Горчаков Константин Михайлович"), 4], [teacher("Горчаков Константин Михайлович"), 4], [teacher("Горчаков Константин Михайлович"), 4]]]]).

% subject("Computer Science and Systems Engineering", "Методы машинного обучения", [5], [[type_of_class("lec"), 1, [["Постовалов Сергей Николаевич", 2]]], [type_of_class("pr"), 1, [["Антонец Денис Викторович", 2]]]]).
% subject("Computer Science and Systems Engineering", "Вычислительная математика", [5], [[type_of_class("lec"), 1, [["Васкевич Владимир Леонтьевич", 2]]], [type_of_class("pr"), 1, [["Васкевич Владимир Леонтьевич"), 1], ["Шваб Ирина Васильевна", 1]]]]).
% subject("Computer Science and Systems Engineering", "Командная разработка многофункционального программно-аппаратного комплекса", [5, 6], [[type_of_class("lec"), 1, [["Адаманский Антон Валентинович", 2]]], [type_of_class("pr"), 2, [["Адаманский Антон Валентинович", 2]]]]).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% PART FOUR - GROUPS OF STUDENTS %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%
% Groups of students
% group_of_students(Name_of_ed_program, Number_of_group, Amount_of_students, Year_of_study)
%
group_of_students("Software Engineering and Computer Science", "20201", 17, 2).
group_of_students("Software Engineering and Computer Science", "20202", 15, 2).
group_of_students("Software Engineering and Computer Science", "20203", 15, 2).
group_of_students("Software Engineering and Computer Science", "20204", 12, 2).
group_of_students("Software Engineering and Computer Science", "20205", 18, 2).
group_of_students("Software Engineering and Computer Science", "20206", 13, 2).
group_of_students("Software Engineering and Computer Science", "20207", 15, 2).
group_of_students("Software Engineering and Computer Science", "20208", 14, 2).
group_of_students("Software Engineering and Computer Science", "20209", 15, 2).
group_of_students("Software Engineering and Computer Science", "20210", 14, 2).
group_of_students("Software Engineering and Computer Science", "20211", 16, 2).
group_of_students("Software Engineering and Computer Science", "20212", 17, 2).
group_of_students("Computer Science and Systems Engineering", "20213", 16, 2).
group_of_students("Computer Science and Systems Engineering", "20214", 16, 2).
group_of_students("Computer Science and Systems Engineering", "20215", 17, 2).

group_of_students("Software Engineering and Computer Science", "19201", 17, 3).
group_of_students("Software Engineering and Computer Science", "19202", 15, 3).
group_of_students("Software Engineering and Computer Science", "19203", 15, 3).
group_of_students("Software Engineering and Computer Science", "19204", 12, 3).
group_of_students("Software Engineering and Computer Science", "19205", 18, 3).
group_of_students("Software Engineering and Computer Science", "19206", 13, 3).
group_of_students("Software Engineering and Computer Science", "19207", 12, 3).
group_of_students("Software Engineering and Computer Science", "19208", 14, 3).
group_of_students("Software Engineering and Computer Science", "19209", 15, 3).
group_of_students("Software Engineering and Computer Science", "19210", 12, 3).
group_of_students("Software Engineering and Computer Science", "19211", 11, 3).
group_of_students("Software Engineering and Computer Science", "19212", 17, 3).
group_of_students("Computer Science and Systems Engineering", "19213", 13, 3).
group_of_students("Computer Science and Systems Engineering", "19214", 12, 3).

%
% A list of groups of students
% list_groups_of_students(Name_of_ed_program, Year_of_study, Groups_of_students)
%
list_groups_of_students("Software Engineering and Computer Science", 3, ["19201", "19202", "19203", "19204", "19205", "19206", "19207", "19208", "19209", "19210", "19211", "19212"]).
list_groups_of_students("Computer Science and Systems Engineering", 3, ["19213", "19214"]).
list_groups_of_students("Computer Science and Systems Engineering", 2, ["20213", "20214", "20215"]).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% CONSTRAINTS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% PART FIVE - HARD CONSTRAINTS %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


% Time when the first class begins.
% class_duration(0 <= Hour < 24, 0 <= Minutes < 60)
first_class_starts(9, 0).

% The duration of classes.
% class_duration(0 < Minutes)
class_duration(90).

% Short brakes duration in-between a class.
% short_brake_duration(0 <= Minutes)
short_brake_duration(5).

% Long brakes duration between classes.
% long_brake_duration(0 <= Minutes)
long_brake_duration(15).

% Amount of possible days of studying in a week (starting with Monday).
% study_days_in_week(Amount_of_days)
study_days_in_week(6).

% ?
% Limit on days of studying in a week for a student.
% study_days_in_week_students(Amount_of_days)
study_days_in_week_students(6).

% ?
% Limit on days of studying in a week for a teacher.
% study_days_in_week_teachers(Amount_of_days)
study_days_in_week_teachers(5).

% Amount of possible classes in a day
% classes_in_day(Amount of classes)
classes_in_day(7).

% Limit on amount classes in a day for students
% classes_in_day_students(Amount of classes)
classes_in_day_students(2).

% Limit on amount classes in a day for teachers
% classes_in_day_teachers(Amount of classes)
classes_in_day_teachers(2).

% For EACH (for correct work) teacher: possible days for teaching. Monday - 1, Sunday - 7.
% days_teacher_can_work(teacher(Teacher), Number_of_days[]).
days_teacher_can_work(teacher("Пузаренко Вадим Григорьевич"),[4,5,6]).
days_teacher_can_work(teacher("Авдеев Роман Русланович"),[1]).
days_teacher_can_work(teacher("Пермяков Руслан Анатольевич"),[1,2,3,4,5,6]).
days_teacher_can_work(teacher("Злыгостев Антон Игоревич"),[1,2,3,4,5,6]).
days_teacher_can_work(teacher("Букшев Иван Евгеньевич"),[1,2,3,4,5,6]).
days_teacher_can_work(teacher("Васкевич Владимир Леонтьевич"),[3,4,5,6]).
days_teacher_can_work(teacher("Адаманский Антон Валентинович"),[1,2,3,4,5,6]).
days_teacher_can_work(teacher("Ситнов Владимир Евгеньевич"),[1,2,3,4,5,6]).
days_teacher_can_work(teacher("Мигинский Дмитрий Сергеевич"),[1,2,3,4,5,6]).
days_teacher_can_work(teacher("Терентьева Татьяна Александровна"),[1,2,3,4,5,6]).
days_teacher_can_work(teacher("Постовалов Сергей Николаевич"),[1,2,3,4,5,6]).
days_teacher_can_work(teacher("Балабанов Артем Андреевич"),[1,2,3,4,5,6]).
days_teacher_can_work(teacher("Антонец Денис Викторович"),[1,2,3,4,5,6]).
days_teacher_can_work(teacher("Шваб Ирина Васильевна"),[1,2,3]).
days_teacher_can_work(teacher("Горчаков Константин Михайлович"),[1,2,3,4,5,6]).


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% PART SIX - SOFT CONSTRAINTS         %
%                                     %
% WEIGHTS (PENALTY POINTS)            %
% Penalty points are accounted if a   %
% constraint is not satisfied         %
% 0 - TURN OFF                        %
% 1-9 - PREFERABLE BUT NOT OBLIGATORY %
% 10 - OBLIGATORY TO SATISFY          %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% All students prefer a gap between classes for a lunch break.
% c_lunch_break(0 <= Weight <= 10)
c_lunch_break(5).

% Amount of possible consecutive gaps between classes.
% c_gaps(Amount_of_gaps, 0 <= Weight <= 10)
c_gaps(0, 0).
c_gaps(1, 2).
c_gaps(2, 6).
c_gaps(3, 9).
c_gaps(Amount_of_gaps, 10) :- Amount_of_gaps > 3.

% Amount of students - classroom capacity correlaation. Ratio is: (classroom capacity correlation / Amount of students)
% fillness(0 <= Weight <= 10 - if ratio < 2, 0 <= Weight <= 10 - if ratio = 2, 0 <= Weight <= 10 - if ratio > 2).
classroom_fillness(0, 10, 10).

% For EACH (for correct work) teacher: desirable days for teaching. Monday - 1, Sunday - 7.
% CHECK that desirable Number_of_days[] is strictly a subset of possible Number_of_days[] from days_teacher_can_work.
% days_teacher_want_work(teacher(Teacher), Number_of_days[], 0 <= Weight <= 10).
days_teacher_want_work(teacher("Пузаренко Вадим Григорьевич"),[4,5,6], 10).
days_teacher_want_work(teacher("Авдеев Роман Русланович"),[1], 10).
days_teacher_want_work(teacher("Пермяков Руслан Анатольевич"),[1,3,5], 5).
days_teacher_want_work(teacher("Злыгостев Антон Игоревич"),[1,2,3,4,5], 2).
days_teacher_want_work(teacher("Букшев Иван Евгеньевич"),[1,2,3,4,5], 5).
days_teacher_want_work(teacher("Васкевич Владимир Леонтьевич"),[1,2,3,4,5,6], 0).
days_teacher_want_work(teacher("Адаманский Антон Валентинович"),[3,4,6], 4).
days_teacher_want_work(teacher("Ситнов Владимир Евгеньевич"),[1,2,3,4,5], 2).
days_teacher_want_work(teacher("Мигинский Дмитрий Сергеевич"),[1,2,3,4,5,6], 0).
days_teacher_want_work(teacher("Терентьева Татьяна Александровна"),[3,5], 5).
days_teacher_want_work(teacher("Постовалов Сергей Николаевич"),[1,2,3,4,5], 2).
days_teacher_want_work(teacher("Балабанов Артем Андреевич"),[1,2,3,4,5], 1).
days_teacher_want_work(teacher("Антонец Денис Викторович"),[1,2,3,4,5], 3).
days_teacher_want_work(teacher("Шваб Ирина Васильевна"),[1,3], 1).
days_teacher_want_work(teacher("Горчаков Константин Михайлович"),[1,2,3,4,5,6], 0).
