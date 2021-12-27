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
teacher('Пермяков Руслан Анатольевич').
teacher('Злыгостев Антон Игоревич').
teacher('Букшев Иван Евгеньевич').
teacher('Васкевич Владимир Леонтьевич').
teacher('Адаманский Антон Валентинович').
teacher('Ситнов Владимир Евгеньевич').
teacher('Мигинский Дмитрий Сергеевич').
teacher('Терентьева Татьяна Александровна').
teacher('Постовалов Сергей Николаевич').
teacher('Балабанов Артем Андреевич').
teacher('Антонец Денис Викторович').
teacher('Шваб Ирина Васильевна').
teacher('Авдеев Роман Русланович').
teacher('Горчаков Константин Михайлович').
teacher('Пузаренко Вадим Григорьевич').

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% PART ONE - TYPES OF CLASSES AND CLASSROOMS %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%
% Type of classes
% type_of_class(Name_of_type_of_class).
type_of_class('pr').
type_of_class('lec').
type_of_class('lab').
type_of_class('pe').
type_of_class('misc').

%
% Classrooms
% type_of_classroom(Code_of_classroom, Type_of_class[], INT Capacity_of_classroom)
% classroom(Name_of_classroom, Types_of_class, INT Capacity_of_classroom))
%
type_of_classroom('huge for lectures and practices', [type_of_class('lec'), type_of_class('pr')], 200).
% type_of_classroom('huge for lectures', [type_of_class('lec')], 200).
type_of_classroom('big for lectures and practices', [type_of_class('lec'), type_of_class('pr')], 80).
type_of_classroom('medium for lectures and practices', [type_of_class('lec'), type_of_class('pr')], 40).
type_of_classroom('small for lectures and practices', [type_of_class('lec'), type_of_class('pr')], 20).
type_of_classroom('terminals', [type_of_class('pr'), type_of_class('lab')], 20).
type_of_classroom('room for pe', [type_of_class('pe')], 500).


classroom('1156', Types_of_class, Capacity_of_classroom) :- type_of_classroom('huge for lectures and pratices', Types_of_class, Capacity_of_classroom).
classroom('т3213', Types_of_class, Capacity_of_classroom) :- type_of_classroom('terminals', Types_of_class, Capacity_of_classroom).
classroom('402 ГК', Types_of_class, Capacity_of_classroom) :- type_of_classroom('huge for lectures and practices', Types_of_class, Capacity_of_classroom).
classroom('СК', Types_of_class, Capacity_of_classroom) :- type_of_classroom('room for pe', Types_of_class, Capacity_of_classroom).
classroom('т2266', Types_of_class, Capacity_of_classroom) :- type_of_classroom('terminals', Types_of_class, Capacity_of_classroom).
classroom('2128', Types_of_class, Capacity_of_classroom) :- type_of_classroom('big for lectures and practices', Types_of_class, Capacity_of_classroom).
classroom('т3220', Types_of_class, Capacity_of_classroom) :- type_of_classroom('terminals', Types_of_class, Capacity_of_classroom).
classroom('1154', Types_of_class, Capacity_of_classroom) :- type_of_classroom('small for lectures and practices', Types_of_class, Capacity_of_classroom).
classroom('406 ГК', Types_of_class, Capacity_of_classroom) :- type_of_classroom('small for lectures and practices', Types_of_class, Capacity_of_classroom).
classroom('1155', Types_of_class, Capacity_of_classroom) :- type_of_classroom('medium for lectures and practices', Types_of_class, Capacity_of_classroom).
classroom('т2213', Types_of_class, Capacity_of_classroom) :- type_of_classroom('terminals', Types_of_class, Capacity_of_classroom).
classroom('т2221', Types_of_class, Capacity_of_classroom) :- type_of_classroom('terminals', Types_of_class, Capacity_of_classroom).


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% PART TWO - FACS, ED PRS, SPECS %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


%
% Faculties
% faculty(Name_of_faculty)
%
faculty('Faculty of Information Technologies').

%
% Education program
% ed_program(Name_of_faculty, Name_of_ed_program)
%
ed_program('Faculty of Information Technologies', 'BACH, 09.03.01, Computer Science and Engineering').

%
% Specialization or profile
% specialization(Name_of_ed_program, Name_of_specialization)
%
specialization('BACH, 09.03.01, Computer Science and Engineering', 'Computer Science and Systems Engineering').
specialization('BACH, 09.03.01, Computer Science and Engineering', 'Software Engineering and Computer Science').


%%%%%%%%%%%%%%%%%%%%%%%%%
% PART THREE - SUBJECTS %
%%%%%%%%%%%%%%%%%%%%%%%%%

%
% Subjects
% subject(Name_of_ed_program, Name_of_subject, Semesters[], [Type_of_class, INT Frequency_of_class, [Teacher, INT amount_of_groups][]][])
% semesters: semester = [1,2] or [3] or [1,2,3,4,5,6]
%
% subject('Computer Science and Systems Engineering', 'Электротехника и электроника', [3, 4], [[type_of_class('lec'), 1, [[teacher('Горчаков Константин Михайлович'), 2]]], [type_of_class('pr'), 1, [[teacher('Горчаков Константин Михайлович'), 2]]]]).

subject('Computer Science and Systems Engineering', 'Модели вычислений', [3, 4], [[type_of_class('lec'), 1, [[teacher('Пузаренко Вадим Григорьевич'), 3]]], [type_of_class('pr'), 1, [[teacher('Пузаренко Вадим Григорьевич'), 2], [teacher('Авдеев Роман Русланович'), 1]]]]).
% subject('Computer Science and Systems Engineering', 'Модели вычислений', [5, 6], [[type_of_class('lec'), 1, [[teacher('Пузаренко Вадим Григорьевич'), 2]]], [type_of_class('pr'), 1, [[teacher('Пузаренко Вадим Григорьевич'), 1], [teacher('Авдеев Роман Русланович'), 1]]]]).
subject('Computer Science and Systems Engineering', 'Методы машинного обучения', [5], [[type_of_class('lec'), 1, [[teacher('Постовалов Сергей Николаевич'), 2]]], [type_of_class('pr'), 1, [[teacher('Антонец Денис Викторович'), 2]]]]).
subject('Computer Science and Systems Engineering', 'Теория вероятности и математическая статистика', [3], [[type_of_class('lec'), 1, [[teacher('Постовалов Сергей Николаевич'), 3]]], [type_of_class('pr'), 1, [[teacher('Постовалов Сергей Николаевич'), 2], [teacher('Антонец Денис Викторович'), 1]]]]).
subject('Computer Science and Systems Engineering', 'Дифференциальные уравнения и теория функций комплексного переменного', [3], [[type_of_class('lec'), 1, [[teacher('Васкевич Владимир Леонтьевич'), 3]]], [type_of_class('pr'), 1, [[teacher('Васкевич Владимир Леонтьевич'), 2], [teacher('Шваб Ирина Васильевна'), 1]]]]).
subject('Computer Science and Systems Engineering', 'Вычислительная математика', [5], [[type_of_class('lec'), 1, [[teacher('Васкевич Владимир Леонтьевич'), 2]]], [type_of_class('pr'), 1, [[teacher('Васкевич Владимир Леонтьевич'), 1], [teacher('Шваб Ирина Васильевна'), 1]]]]).
subject('Computer Science and Systems Engineering', 'Командная разработка многофункционального программно-аппаратного комплекса', [5], [[type_of_class('lec'), 1, [[teacher('Адаманский Антон Валентинович'), 2]]], [type_of_class('pr'), 2, [[teacher('Адаманский Антон Валентинович'), 2]]]]).
subject('Software Engineering and Computer Science', 'Электротехника и электроника', [5], [[type_of_class('lec'), 1, [[teacher('Горчаков Константин Михайлович'), 12]]], [type_of_class('pr'), 1, [[teacher('Горчаков Константин Михайлович'), 4], [teacher('Горчаков Константин Михайлович'), 4], [teacher('Горчаков Константин Михайлович'), 4]]]]).

% subject('Computer Science and Systems Engineering', 'Методы машинного обучения', [5], [[type_of_class('lec'), 1, [['Постовалов Сергей Николаевич', 2]]], [type_of_class('pr'), 1, [['Антонец Денис Викторович', 2]]]]).
% subject('Computer Science and Systems Engineering', 'Вычислительная математика', [5], [[type_of_class('lec'), 1, [['Васкевич Владимир Леонтьевич', 2]]], [type_of_class('pr'), 1, [['Васкевич Владимир Леонтьевич'), 1], ['Шваб Ирина Васильевна', 1]]]]).
% subject('Computer Science and Systems Engineering', 'Командная разработка многофункционального программно-аппаратного комплекса', [5, 6], [[type_of_class('lec'), 1, [['Адаманский Антон Валентинович', 2]]], [type_of_class('pr'), 2, [['Адаманский Антон Валентинович', 2]]]]).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% PART FOUR - GROUPS OF STUDENTS %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

	
%
% Groups of students
% group_of_students(Name_of_ed_program, Number_of_group, Amount_of_students, Year_of_study)
%
group_of_students('Software Engineering and Computer Science', '20201', 17, 2).
group_of_students('Software Engineering and Computer Science', '20202', 15, 2).
group_of_students('Software Engineering and Computer Science', '20203', 15, 2).
group_of_students('Software Engineering and Computer Science', '20204', 12, 2).
group_of_students('Software Engineering and Computer Science', '20205', 18, 2).
group_of_students('Software Engineering and Computer Science', '20206', 13, 2).
group_of_students('Software Engineering and Computer Science', '20207', 15, 2).
group_of_students('Software Engineering and Computer Science', '20208', 14, 2).
group_of_students('Software Engineering and Computer Science', '20209', 15, 2).
group_of_students('Software Engineering and Computer Science', '20210', 14, 2).
group_of_students('Software Engineering and Computer Science', '20211', 16, 2).
group_of_students('Software Engineering and Computer Science', '20212', 17, 2).
group_of_students('Computer Science and Systems Engineering', '20213', 16, 2).
group_of_students('Computer Science and Systems Engineering', '20214', 16, 2).
group_of_students('Computer Science and Systems Engineering', '20215', 17, 2).

group_of_students('Software Engineering and Computer Science', '19201', 17, 3).
group_of_students('Software Engineering and Computer Science', '19202', 15, 3).
group_of_students('Software Engineering and Computer Science', '19203', 15, 3).
group_of_students('Software Engineering and Computer Science', '19204', 12, 3).
group_of_students('Software Engineering and Computer Science', '19205', 18, 3).
group_of_students('Software Engineering and Computer Science', '19206', 13, 3).
group_of_students('Software Engineering and Computer Science', '19207', 12, 3).
group_of_students('Software Engineering and Computer Science', '19208', 14, 3).
group_of_students('Software Engineering and Computer Science', '19209', 15, 3).
group_of_students('Software Engineering and Computer Science', '19210', 12, 3).
group_of_students('Software Engineering and Computer Science', '19211', 11, 3).
group_of_students('Software Engineering and Computer Science', '19212', 17, 3).
group_of_students('Computer Science and Systems Engineering', '19213', 13, 3).
group_of_students('Computer Science and Systems Engineering', '19214', 12, 3).

%
% A list of groups of students
% list_groups_of_students(Name_of_ed_program, Year_of_study, Groups_of_students)
%
list_groups_of_students('Software Engineering and Computer Science', 3, ['19201', '19202', '19203', '19204', '19205', '19206', '19207', '19208', '19209', '19210', '19211', '19212']).
list_groups_of_students('Computer Science and Systems Engineering', 3, ['19213', '19214']).
list_groups_of_students('Computer Science and Systems Engineering', 2, ['20213', '20214', '20215']).

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
classes_in_day_teachers(1).

% For EACH (for correct work) teacher: possible days for teaching. Monday - 1, Sunday - 7.
% days_teacher_can_work(teacher(Teacher), Number_of_days[]).
days_teacher_can_work(teacher('Пузаренко Вадим Григорьевич'),[4,5,6]).
days_teacher_can_work(teacher('Авдеев Роман Русланович'),[1]).
days_teacher_can_work(teacher('Пермяков Руслан Анатольевич'),[1,2,3,4,5,6]).
days_teacher_can_work(teacher('Злыгостев Антон Игоревич'),[1,2,3,4,5,6]).
days_teacher_can_work(teacher('Букшев Иван Евгеньевич'),[1,2,3,4,5,6]).
days_teacher_can_work(teacher('Васкевич Владимир Леонтьевич'),[3,4,5,6]).
days_teacher_can_work(teacher('Адаманский Антон Валентинович'),[1,2,3,4,5,6]).
days_teacher_can_work(teacher('Ситнов Владимир Евгеньевич'),[1,2,3,4,5,6]).
days_teacher_can_work(teacher('Мигинский Дмитрий Сергеевич'),[1,2,3,4,5,6]).
days_teacher_can_work(teacher('Терентьева Татьяна Александровна'),[1,2,3,4,5,6]).
days_teacher_can_work(teacher('Постовалов Сергей Николаевич'),[1,2,3,4,5,6]).
days_teacher_can_work(teacher('Балабанов Артем Андреевич'),[1,2,3,4,5,6]).
days_teacher_can_work(teacher('Антонец Денис Викторович'),[1,2,3,4,5,6]).
days_teacher_can_work(teacher('Шваб Ирина Васильевна'),[1,2,3]).
days_teacher_can_work(teacher('Горчаков Константин Михайлович'),[1,2,3,4,5,6]).


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
days_teacher_want_work(teacher('Пузаренко Вадим Григорьевич'),[4,5,6], 10).
days_teacher_want_work(teacher('Авдеев Роман Русланович'),[1], 10).
days_teacher_want_work(teacher('Пермяков Руслан Анатольевич'),[1,3,5], 5).
days_teacher_want_work(teacher('Злыгостев Антон Игоревич'),[1,2,3,4,5], 2).
days_teacher_want_work(teacher('Букшев Иван Евгеньевич'),[1,2,3,4,5], 5).
days_teacher_want_work(teacher('Васкевич Владимир Леонтьевич'),[1,2,3,4,5,6], 0).
days_teacher_want_work(teacher('Адаманский Антон Валентинович'),[3,4,6], 4).
days_teacher_want_work(teacher('Ситнов Владимир Евгеньевич'),[1,2,3,4,5], 2).
days_teacher_want_work(teacher('Мигинский Дмитрий Сергеевич'),[1,2,3,4,5,6], 0).
days_teacher_want_work(teacher('Терентьева Татьяна Александровна'),[3,5], 5).
days_teacher_want_work(teacher('Постовалов Сергей Николаевич'),[1,2,3,4,5], 2).
days_teacher_want_work(teacher('Балабанов Артем Андреевич'),[1,2,3,4,5], 1).
days_teacher_want_work(teacher('Антонец Денис Викторович'),[1,2,3,4,5], 3).
days_teacher_want_work(teacher('Шваб Ирина Васильевна'),[1,3], 1).
days_teacher_want_work(teacher('Горчаков Константин Михайлович'),[1,2,3,4,5,6], 0).




%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

/*
 * Получаю список всех занятий. При переходе в новую
 * вершину, структура class добавленного занятия будет удалена из списка.
 * Выполняю процедуру до тех пор, пока остались нераспределённые задачи.
 * Attempts - количество попыток на генерацию, заданное пользователем.
 */
 
main :-
	clear_all,
	attempts(Attempts),
	sumOfAllDaysTeachersCanWork(X_can, Y_can, Z_can),
	sumOfAllDaysTeachersWantWork(X_want, Y_want, Z_want),
	asserta(sumOfDaysTeachersCanWork(X_can, Y_can, Z_can)),
	asserta(sumOfDaysTeachersWantWork(X_want, Y_want, Z_want)),
	initiateDijkstraSearch(Attempts, Attempts, 1000000, []), !.
 
main(Attempts) :-
	clear_all,
	sumOfAllDaysTeachersCanWork(X_can, Y_can, Z_can),
	sumOfAllDaysTeachersWantWork(X_want, Y_want, Z_want),
	asserta(sumOfDaysTeachersCanWork(X_can, Y_can, Z_can)),
	asserta(sumOfDaysTeachersWantWork(X_want, Y_want, Z_want)),
	initiateDijkstraSearch(Attempts, Attempts, 1000000, []), !.
	
:- dynamic class/8.
:- dynamic taken_groups_in_type_of_class/6.
:- dynamic group_day_time/3.
:- dynamic teacher_day_time/3.
:- dynamic sumOfDaysTeachersCanWork/3.
:- dynamic sumOfDaysTeachersWantWork/3.
%

initiateDijkstraSearch(0, Attempts, Min, BestState) :-
	((Min == 1000000, write('Не удалось составить расписание. Попыток было сделано: '), writeln(Attempts), !);
	(not(Min == 1000000), writeln(''),
	sort(5, @=<, BestState, SortedState),
	sort(3, @=<, SortedState, TwiceSortedState),
	writeln('Лучшее расписание: '),
	printResult(TwiceSortedState),
	write('Попыток было сделано: '), writeln(Attempts),
	writeln('Сумма штрафов: '),
	writeln(Min), !)).
	
initiateDijkstraSearch(I, Attempts, Min, BestState) :-
	clear,
	allClassList(VacantClasses),
	Iter is Attempts - I + 1,
	writeln(''),
	write('Попытка: '), writeln(Iter),
	dijkstraSearch(node([], 0, 0), VacantClasses, Fine, State),
	((State == [], New_BestState = BestState, New_Min is Min, writeln('Неудачная попытка: расписание составить не удалось.'));
	(not(State == []), Min > Fine, New_BestState = State, New_Min is Fine);
	(not(State == []), Min =< Fine, New_BestState = BestState, New_Min is Min)),
	New_I is I - 1,
	initiateDijkstraSearch(New_I, Attempts, New_Min, New_BestState).
	
	
/*
 * Все экзамены в расписании. Сортирую и вывожу это расписание и штраф.
 */ 

dijkstraSearch(node(State, _, _), [], X, Y) :-
	sort(5, @=<, State, SortedState),
	sort(3, @=<, SortedState, TwiceSortedState),
	writeln('Расписание: '),
	printResult(TwiceSortedState),
	writeln('Сумма штрафов: '),
	cost_all(State, Fine),
	X is Fine,
	Y = State,
	writeln(Fine),
	writeln(''), !.

/*
 * Нахожу все возможные соседние вершины с сохранением обязательных
 * ограничений. Далее сортирую этот список всевозможных соседей и
 * выбираю вершину с наименьшим штрафом. Туда и перехожу.
 */
 
dijkstraSearch(node(State, Length, H), VacantClasses, X, Y) :-
	% sort(5, @=<, State, SortedState),
	% sort(3, @=<, SortedState, TwiceSortedState),
	% writeln(''),
	% writeln('Расписание: '),
	% printResult(TwiceSortedState),
	% findall(node(NewState, NewLength, 0), (findNeighbors(State, VacantClasses, NewState), NewLength is Length + 1), ListOfNeighbors),
	findall(node(NewState, NewLength, SumH), (findNeighbors(State, VacantClasses, NewState), NewLength is Length + 1, cost_last(NewState, NewH), SumH is NewH + H), ListOfNeighbors),
	writeln('SEX'),
	lengthList(ListOfNeighbors, Len),
	writeln(Len),
	((Len > 0,
	writeln('SEX3'),
	% random_permutation(ListOfNeighbors, RandomListOfNeighbors),
	  RandomListOfNeighbors = ListOfNeighbors,
	% perm(ListOfNeighbors,RandomListOfNeighbors):-
	%
	writeln('SEX4'),
	sort(3, @=<, RandomListOfNeighbors, SortedListOfNeighbors),
	% sort(3, @=<, ListOfNeighbors, SortedListOfNeighbors),
	writeln('SEX3'),
	headOfList(SortedListOfNeighbors, OptimalNeighbor), !,
	getNewClassInfo(OptimalNeighbor, NewClass, NewGroupsOfStudents, NewDay, NewClassTime),
	add_to_taken_groups(NewClass, NewGroupsOfStudents),
	add_to_teacher_day_time(NewClass, NewDay, NewClassTime),
	add_to_group_day_time(NewClass, NewGroupsOfStudents, NewDay, NewClassTime),
	delete(VacantClasses, NewClass, NewVacantClasses),
	dijkstraSearch(OptimalNeighbor, NewVacantClasses, X, Y));
	(Len = 0, !, Y = [], !)).

/*
 * Нахожу соседей, таких, что они не противоречат обязательным
 * ограничениям. Если всё в порядке, на выход - новый State.
 * За основу берутся занятия, которые не состоят в
 * текущем расписании.
 * Поиск ведётся путём последовательного усечения элементов множеств.
 */
 
findNeighbors(State, VacantClasses, NewState) :-
	member(NewClass, VacantClasses),
	study_days_in_week(StudyDaysInAWeek),
	classes_in_day(ClassesInDay),
	between(1, StudyDaysInAWeek, NewDay),
	between(1, ClassesInDay, NewClassTime),
	classroom(NewClassroom, NewTypesOfClass, NewCapacityOfClassrom),
	check_types_of_class_match(NewClass, NewTypesOfClass),
	class_to_group(NewClass, NewGroupsOfStudents),
	count_amount_of_students(NewGroupsOfStudents, 0, AmountOfStudents),
	AmountOfStudents =< NewCapacityOfClassrom,
	dateIsOk(State, event(NewClass, NewClassroom, NewDay, NewGroupsOfStudents, NewClassTime)),
	teacher_can_work_this_day(NewClass, NewDay),
	limit_of_classes(NewClass, NewGroupsOfStudents, NewDay),
	append(State, [event(NewClass, NewClassroom, NewDay, NewGroupsOfStudents, NewClassTime)], NewState).


% get_type_of_class(class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Teacher, Amount_of_groups, Order_in_week, Id), X) :- X = Type_of_class.

/*
 * Проверяю, что нет накладок по датам проведения добавляемого нового
 * занятия с занятиями текущего расписания. То есть в одном кабинете
 * не будет 2 занятия одновременно. К тому же, преподаватели и ученики
 * в одно время не будут задействованы сразу на двух занятиях.
 */
dateIsOk([],_) :- !.
% Если занятия проводятся не в одно время, то проверять на коллизию
% преподавателей и учеников даже нет смысла.
dateIsOk([event(_, Classroom, Day, _, ClassTime) | Other], event(NewClass, Classroom, Day, NewGroupsOfStudents, NewClassTime)) :-
	%% ?? Надо ли утверждать, что Classroom = NewClassroom как в оригинале ??
	ClassTime \= NewClassTime,
	dateIsOk(Other, event(NewClass, Classroom, Day, NewGroupsOfStudents, NewClassTime)).
	
% Занятия проводятся в разные дни - проверять на коллизию
% преподавателей и учеников нет смысла.
dateIsOk([event(_, Classroom, Day, _, _) | Other], event(NewClass, NewClassroom, NewDay, NewGroupsOfStudents, NewClassTime)) :-
	Day \= NewDay,
	Classroom \= NewClassroom,
	dateIsOk(Other, event(NewClass, NewClassroom, NewDay, NewGroupsOfStudents, NewClassTime)).
	
% Занятия в разных аудиториях, но в один день и в одно время. Надо проверить, что
% коллизий по преподавателям и ученикам нет.
dateIsOk([event(Class, Classroom, Day, GroupsOfStudents, ClassTime) | Other], event(NewClass, NewClassroom, Day, NewGroupsOfStudents, NewClassTime)) :-
	Classroom \= NewClassroom,
	noTeacherOverruns(Class, ClassTime, NewClass, NewClassTime),
	noStudentOverruns(ClassTime, GroupsOfStudents, NewClassTime, NewGroupsOfStudents),
	dateIsOk(Other, event(NewClass, NewClassroom, Day, NewGroupsOfStudents, NewClassTime)).
	
% Занятия проводятся в разные дни - проверять на коллизию
% преподавателей и учеников нет смысла.
dateIsOk([event(_, Classroom, Day, _, _) | Other], event(NewClass, Classroom, NewDay, NewGroupsOfStudents, NewClassTime)) :-
	Day \= NewDay,
	dateIsOk(Other, event(NewClass, Classroom, NewDay, NewGroupsOfStudents, NewClassTime)).

/* 
 * Проверяю, что в этот день в это время учитель не ведёт занятие.
 */
% Учителя вообще разные.
noTeacherOverruns(class(_, _, _, _, Teacher, _, _, _), _, class(_, _, _, _, NewTeacher, _, _, _), _) :-
	Teacher \= NewTeacher.

% Учителя одни, но время разное.	
noTeacherOverruns(class(_, _, _, _, Teacher, _, _, _), ClassTime, class(_, _, _, _, NewTeacher, _, _, _), NewClassTime) :-
	Teacher = NewTeacher,
	ClassTime \= NewClassTime.

/* 
 * Проверяю, что в этот день в это время у группы студентов нет занятий.
 */
% Все группы студентов обозреваемых групп разные.
noStudentOverruns(_, GroupsOfStudents, _, NewGroupsOfStudents) :-
	not(have_common_item(GroupsOfStudents, NewGroupsOfStudents)).

% Есть пересечения в группах, сравниваем циклически на пересекаемость занятий.	
noStudentOverruns(ClassTime, GroupsOfStudents, NewClassTime, NewGroupsOfStudents) :-
	have_common_item(GroupsOfStudents, NewGroupsOfStudents),
	noStudentOverruns2(ClassTime, GroupsOfStudents, NewClassTime, NewGroupsOfStudents).

% Непосредстввенно заводим цикл по группам-кандидатам.
noStudentOverruns2(_, [], _, _).
noStudentOverruns2(ClassTime, [GroupOfStudents | Rest], NewClassTime, NewGroupsOfStudents) :-
	noStudentOverruns3(ClassTime, GroupOfStudents, NewClassTime, NewGroupsOfStudents),
	noStudentOverruns2(ClassTime, Rest, NewClassTime, NewGroupsOfStudents).

% Проверяем пересечение группы-кандидата и других групп.
noStudentOverruns3(_, _, _, []).
noStudentOverruns3(ClassTime, GroupOfStudents, NewClassTime, [NewGroupOfStudents | Rest]) :-
	((GroupOfStudents \= NewGroupOfStudents); (GroupOfStudents = NewGroupOfStudents, ClassTime \= NewClassTime)),
	noStudentOverruns3(ClassTime, GroupOfStudents, NewClassTime, Rest).

/*
 * Получить информацию о занятии: структура class, группы студентов, день занятия и время занятия.
 * Для этого разворачиваем список узлов, берём последний узел и излвекаем информацию.
 */
getNewClassInfo(node(State, _, _), NewClass, NewGroupsOfStudents, NewDay, NewClassTime) :-
	reverse(State, [NewEvent | _]),
	getNewClassInfo2(NewEvent, NewClass, NewGroupsOfStudents, NewDay, NewClassTime).

% Непосредственное получение.
getNewClassInfo2(event(Class, _, Day, GroupsOfStudents, ClassTime), NewClass, NewGroupsOfStudents, NewDay, NewClassTime) :-
	NewClass = Class,
	NewGroupsOfStudents = GroupsOfStudents,
	NewDay = Day,
	NewClassTime = ClassTime.

/*
 * Избыток
 */
stateToClassConverter([], List, Classes) :- Classes = List.
stateToClassConverter([event(Class, _, _, _) | Other], List, Classes) :-
	append(List, [Class], NewList),
	stateToClassConverter(Other, NewList, Classes).

/*
 * Печатаем циклически всё расписание.
 */
printResult([]) :- writeln('').
printResult([event(class(_, Name_of_subject, _, type_of_class(Type_of_class), teacher(Teacher), _, _, _), Classroom, Day, Group, ClassTime) | Other]) :-
	write('День '), write(Day),write(' '),write(Type_of_class),write(' '),write(Name_of_subject),write(', преподаватель '),write(Teacher),write(', ауд '),write(Classroom),write(', группы: '),write(Group),write(', парой '), writeln(ClassTime),
	printResult(Other).


/*
 * Функция обновляет состояние распределенности групп по учителям для каждого типа предмета.
 */
add_to_taken_groups(class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, _, _, Order_in_week, _), Groups) :-
	taken_groups_in_type_of_class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Current_groups, Order_in_week),
	% append(Current_groups, Groups, New_groups),
	subtract(Current_groups, Groups, New_groups),
	retract(taken_groups_in_type_of_class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, _, Order_in_week)),
	asserta(taken_groups_in_type_of_class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, New_groups, Order_in_week)).
	% writeln(taken_groups_in_type_of_class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, New_groups)).

/*
 * Функция обновляет состояние структуры: группа студентов, день, время занятия.
 */
add_to_group_day_time(_, [], _, _).
add_to_group_day_time(class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Teacher, Amount_of_groups, Order_in_week, Id), [GroupOfStudents | Rest], Day, ClassTime) :-
	asserta(group_day_time(GroupOfStudents, Day, ClassTime)),
	add_to_group_day_time(class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Teacher, Amount_of_groups, Order_in_week, Id), Rest, Day, ClassTime).

/*
 * Функция обновляет состояние структуры: преподаватель, день, время занятия.
 */
add_to_teacher_day_time(class(_, _, _, _, Teacher, _, _, _), Day, ClassTime) :-
	asserta(teacher_day_time(Teacher, Day, ClassTime)).

/*
 * По названию специализации, предмета и семестрам обучения предмета получить подходящие группы, которые будут в дальшейшем закреплятся к конкретному преподавателю.
 */
class_to_group(class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, _, Amount_of_groups, Order_in_week, _), Groups_of_Students) :- 
	taken_groups_in_type_of_class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Vacant_groups, Order_in_week),
	class_to_group2(Name_of_subject, Semester, Type_of_class, [], Groups_of_Students, Amount_of_groups, Vacant_groups).

% Извлекаем последователь из нераспределённых групп	столько, сколько требутся для дубликата.
class_to_group2(Name_of_subject, Semester, Type_of_class, X, _, I, []) :-
	I > 0,
	% write([Name_of_subject, Type_of_class, Semester, X]), writeln(' Error: the subjects require more students than they are'),!,
	!, fail, !.
class_to_group2(_, _, _, X, Groups_of_Students, 0, _) :- X = Groups_of_Students.
class_to_group2(Name_of_subject, Semester, Type_of_class, X, Groups_of_Students, I, [Vacant_group | Rest]) :-
	append(X, [Vacant_group], New_X),
	New_I is I - 1,
	class_to_group2(Name_of_subject, Semester, Type_of_class, New_X, Groups_of_Students, New_I, Rest).
	
/*	
 * Подсчитываем число общее число студентов, которое будет посещать занятия.
 */
count_amount_of_students([], X, Sum) :- Sum is X.
count_amount_of_students([Group_of_Students | Rest], X, Sum) :-
	group_of_students(_, Group_of_Students, Amount_of_students, _),
	NewX is X + Amount_of_students,
	count_amount_of_students(Rest, NewX, Sum).
	
/*
 * Проверяем, что в кабинете можно провести требуемый тип занятия.
 */
check_types_of_class_match(class(_, _, _, X, _, _, _, _), Y) :-
	have_common_item([X], Y).

/*
 * Функция проверяет, что преподаватель может работать в предполагаемый день.
 */
teacher_can_work_this_day(class(_, _, _, _, Teacher, _, _, _), Day) :-
	days_teacher_can_work(Teacher, Days),
	member(Day, Days).

/*
 * Функция проверяет, что число пар у студентов и преподавателей не превышено.
 */
limit_of_classes(class(_, _, _, _, Teacher, _, _, _), GroupOfStudents, Day) :-
	limit_of_classes_stundents(GroupOfStudents, Day),
	limit_of_classes_teachers(Teacher, Day).

% Функция проверяет, что число пар у студентов не превышено.	
limit_of_classes_stundents([], _).
limit_of_classes_stundents([GroupOfStudent | Other], Day) :-
	findall(group_day_time(GroupOfStudent, Day, X), group_day_time(GroupOfStudent, Day, X), List),
	lengthList(List, Len),
	classes_in_day_students(Classes_limit_students),
	% + 1 - прибавляю занятие-кандидата, который пока что не сохранянлся в group_day_time.
	Len + 1 =< Classes_limit_students,
	limit_of_classes_stundents(Other, Day).

% Функция проверяет, что число пар у преподавателей не превышено.	
limit_of_classes_teachers(Teacher, Day) :-
	findall(teacher_day_time(Teacher, Day, X), teacher_day_time(Teacher, Day, X), List),
	lengthList(List, Len),
	classes_in_day_teachers(Classes_limit_teachers),
	Len + 1 =< Classes_limit_teachers.

% Находим список абсолютно всех предметов, которые должны быть проведены на неделе.
% Пока чётные и нечётные недели не поддерживаются.
allClassList(List_of_all_classes) :-
	findall(subject(Name_of_ed_program, Name_of_subject, Semesters, Type_of_class_description), subject(Name_of_ed_program, Name_of_subject, Semesters, Type_of_class_description), List_of_names_of_all_subjects),
	splitter(List_of_names_of_all_subjects),
	writeln('OKAY222'),
	findall(class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Teacher, Amount_of_groups, Order_in_week, Id), class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Teacher, Amount_of_groups, Order_in_week, Id), List_of_all_classes),
	lengthList(List_of_all_classes, X),
	writeln(List_of_all_classes),
	writeln(X).
	
% Рассматриваем рекурсивно каждый subject из списка.
splitter([]).
splitter([Subject | Rest]) :-
	splitter2(Subject),
	splitter(Rest).
	
% Рассматриваем рекурсивно каждый тип занятия какого-то определённого предмета.
splitter2(subject(_, _, _, [])).
splitter2(subject(Name_of_ed_program, Name_of_subject, Semesters, [Type_of_class_description | Other])) :-
	splitter3(Name_of_ed_program, Name_of_subject, Semesters, Type_of_class_description),
	splitter2(subject(Name_of_ed_program, Name_of_subject, Semesters, Other)).

% Рассматриваем рекурсивно каждый дубликат какого-то определённого типа занятия какого-то определённого предмета.
splitter3(_, _, _, [_, _, []]).
splitter3(Name_of_ed_program, Name_of_subject, Semesters, [Type_of_class, Frequency_of_class, [[Teacher, Amount_of_groups] | Rest]]) :-
	splitter4(Name_of_ed_program, Name_of_subject, Semesters, Type_of_class, Frequency_of_class, Teacher, Amount_of_groups),
	splitter3(Name_of_ed_program, Name_of_subject, Semesters, [Type_of_class, Frequency_of_class, Rest]).

% Добавляем class рекурсивно описание какждого дубликата какого-то определённого типа занятия какого-то определённого предмета
% столько раз, сколько раз в неделю этот предмет должен изучаться.
splitter4(_, _, _, _, 0, _, _).
splitter4(Name_of_ed_program, Name_of_subject, Semesters, Type_of_class, Frequency_of_class, Teacher, Amount_of_groups) :-
	splitter6(Name_of_ed_program, Name_of_subject, Semesters, Type_of_class, Frequency_of_class),
	splitter5(Name_of_ed_program, Name_of_subject, Semesters, Type_of_class, Frequency_of_class, Teacher, Amount_of_groups),
	New_frequency_of_class is Frequency_of_class - 1,
	splitter4(Name_of_ed_program, Name_of_subject, Semesters, Type_of_class, New_frequency_of_class, Teacher, Amount_of_groups).
	
% Добавляем class рекурсивно описание какждого дубликат какого-то определённого типа занятия какого-то определённого предмета
% столько раз, сколько раз в неделю этот предмет должен изучаться.
splitter5(_, _, [], _, _, _, _).
splitter5(Name_of_ed_program, Name_of_subject, [Semester | Rest], Type_of_class, Frequency_of_class, Teacher, Amount_of_groups) :-
	Mod is Semester mod 2,
	((semester(1), Mod =:= 1, (((class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Teacher, Amount_of_groups, Frequency_of_class, I)), New_I is I + 1, asserta(class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Teacher, Amount_of_groups, Frequency_of_class, New_I)));
	(not(class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Teacher, Amount_of_groups, Frequency_of_class, _)), asserta(class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Teacher, Amount_of_groups, Frequency_of_class, 0)))));
	(semester(2), Mod =:= 0, (((class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Teacher, Amount_of_groups, I)), New_I is I + 1, asserta(class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Teacher, Amount_of_groups, Frequency_of_class, New_I)));
	(not(class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Teacher, Amount_of_groups, _)), asserta(class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Teacher, Amount_of_groups, Frequency_of_class, 0)))));
	(semester(1), Mod =:= 0); (semester(2), Mod =:= 1)),
	splitter5(Name_of_ed_program, Name_of_subject, Rest, Type_of_class, Frequency_of_class, Teacher, Amount_of_groups).
	
% Добавляю taken_groups_in_type_of_class рекурсивно, чтобы хранить информацию о том, сколько групп уже было взято под тот или иной тип занятия.
splitter6(_, _, [], _, _).
splitter6(Name_of_ed_program, Name_of_subject, [Semester | Rest], Type_of_class, Frequency_of_class) :-
	Div is Semester // 2,
	Mod is Semester mod 2,
	%%%%%%% divmod(Semester, 2, Div, Mod),
	Year_of_students is (Div + Mod),
	list_groups_of_students(Name_of_ed_program, Year_of_students, Groups_of_students),
	% ((taken_groups_in_type_of_class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Groups_of_students, I), New_I is I + 1, asserta(taken_groups_in_type_of_class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Groups_of_students, New_I)));
	% (not(taken_groups_in_type_of_class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Groups_of_students, _)), asserta(taken_groups_in_type_of_class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Groups_of_students, 0)))),
	((semester(1), Mod =:= 1, asserta(taken_groups_in_type_of_class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Groups_of_students, Frequency_of_class)));
	(semester(2), Mod =:= 0, asserta(taken_groups_in_type_of_class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Groups_of_students, Frequency_of_class)));
	(semester(1), Mod =:= 0); (semester(2), Mod =:= 1)),
	% asserta(taken_groups_in_type_of_class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Groups_of_students)),
	% asserta(taken_groups_in_type_of_class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, [])),
	splitter6(Name_of_ed_program, Name_of_subject, Rest, Type_of_class, Frequency_of_class).

/*
 * Сумма всех дней, когда учителя МОГУТ работать. А также сумма учителей и минимальное количество дней.
 */
sumOfAllDaysTeachersCanWork(Sum, Amount, Min) :-
	findall(days_teacher_can_work(Teacher, DaysList), days_teacher_can_work(Teacher, DaysList), List),
	sumOfAllDaysTeachersCanWork2(List, 0, 0, 100, X, Y, Z),
	Sum is X,
	Amount is Y,
	Min is Z.

sumOfAllDaysTeachersCanWork2([], X, Y, Z, Sum, Amount, Min)	:- Sum is X, Amount is Y, Min is Z.
sumOfAllDaysTeachersCanWork2([days_teacher_can_work(_, DaysList) | Other], X, Y, Z, Sum, Amount, Min) :-
	lengthList(DaysList, Len),
	New_X is X + Len,
	New_Y is Y + 1,
	((Len < Z, New_Z is Len);
	(Len >= Z, New_Z is Z)),
	sumOfAllDaysTeachersCanWork2(Other, New_X, New_Y, New_Z, Sum, Amount, Min).
	
	
/*
 * Сумма всех дней, когда учителя ХОТЯТ работать. А также сумма учителей и минимальное количество дней.
 */
sumOfAllDaysTeachersWantWork(Sum, Amount, Min) :-
	findall(days_teacher_want_work(Teacher, DaysList, Weight), days_teacher_want_work(Teacher, DaysList, Weight), List),
	sumOfAllDaysTeachersWantWork2(List, 0, 0, 100, X, Y, Z),
	Sum is X,
	Amount is Y,
	Min is Z.
	
sumOfAllDaysTeachersWantWork2([], X, Y, Z, Sum, Amount, Min)	:- Sum is X, Amount is Y, Min is Z.
sumOfAllDaysTeachersWantWork2([days_teacher_want_work(_, DaysList, _) | Other], X, Y, Z, Sum, Amount, Min) :-
	lengthList(DaysList, Len),
	New_X is X + Len,
	New_Y is Y + 1,
	((Len < Z, New_Z is Len);
	(Len >= Z, New_Z is Z)),
	sumOfAllDaysTeachersWantWork2(Other, New_X, New_Y, New_Z, Sum, Amount, Min).

/*
 * Очистить все динамические списки.
 */
clear :-
	retractall(class(_,_,_,_,_,_,_,_)),
	retractall(taken_groups_in_type_of_class(_,_,_,_,_,_)),
	retractall(group_day_time(_, _, _)),
	retractall(teacher_day_time(_, _, _)).
	
clear_all :-
	retractall(class(_,_,_,_,_,_,_,_)),
	retractall(taken_groups_in_type_of_class(_,_,_,_,_,_)),
	retractall(group_day_time(_, _, _)),
	retractall(teacher_day_time(_, _, _)),
	retractall(sumOfDaysTeachersCanWork(_, _, _)),
	retractall(sumOfDaysTeachersWantWork(_, _, _)).

/*
 * Длина списка.
 */
lengthList(A,B) :- length(A,B).
%lengthList([], 0).
%lengthList([_|Tail],Length) :-
%    lengthList(Tail,Tail_Length),
%    Length is Tail_Length + 1.
%

/*
 * Первый элемент списка.
 */
headOfList([Head | _], Head).


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

cost_all(Events, Cost) :- 
	check_classrooms_WHOLE(Events, 0, Fine1),
	check_gaps_WHOLE(1, 0, Fine2),
	teacher_want_work_this_day_WHOLE(Events, 0, Fine3),
	Cost is Fine1 + Fine2 + Fine3.

/*
 * Подсчёт всех штрафов (необязательных требований) только для занятия-кандидата.
 */
cost_last(Events, Cost) :- 
	reverse(Events, [LastEvent | _]),
	check_classrooms(LastEvent, Fine1),
	check_gaps(LastEvent, Fine2),
	teacher_want_work_this_day(LastEvent, Fine3),
	teacher_priority_can(LastEvent, Fine4),
	teacher_priority_want(LastEvent, Fine5),
	class_in_morning(LastEvent, Fine6),
	Cost is Fine1 + Fine2 + Fine3 + Fine4 + Fine5 + Fine6.

/*
 * Приоритет по занятиям: в приоритете идут занятия первой половины дня.
 */
class_in_morning(event(class(_, _, _, _, _, _, _, _), _, _, _, ClassTime), Fine) :-
	classes_in_day(Classes_in_day),
	Div is Classes_in_day // 2,
	Mod is Classes_in_day mod 2,
	% divmod(Classes_in_day, 2, Div, Mod),
	Coef is Div + Mod,
	((ClassTime > Coef, Fine is 2);
	(ClassTime =< Coef, Fine is 0)).

/*
 * Некий приоритет по учителям: сперва идут те учителя, которые МОГУТ работать в среднем реже остальных.
 */
teacher_priority_can(event(class(_, _, _, _, Teacher, _, _, _), _, _, _, _), Fine) :-
	sumOfDaysTeachersCanWork(Sum, Amount, Min),
	days_teacher_can_work(Teacher, Days),
	lengthList(Days, Len),
	((Len == Min, Fine is 0);
	(Len > Min, Sum > Len * Amount, Fine is 1);
	(Len > Min, Sum < Len * Amount, Fine is 3)).

/*
 * Некий приоритет по учителям: сперва идут те учителя, которые ХОТЯТ работать в среднем реже остальных.
 */
teacher_priority_want(event(class(_, _, _, _, Teacher, _, _, _), _, _, _, _), Fine) :-
	sumOfDaysTeachersWantWork(Sum, Amount, Min),
	days_teacher_want_work(Teacher, Days, _),
	lengthList(Days, Len),
	((Len == Min, Fine is 0);
	(Len > Min, Sum > Len * Amount, Fine is 0);
	(Len > Min, Sum < Len * Amount, Fine is 1)).	


/*
 * Проверка того, что учитель в этот день хочет провести занятие. Для занятия-кандидата.
 */
teacher_want_work_this_day(event(class(_, _, _, _, Teacher, _, _, _), _, Day, _, _), Fine) :-
	days_teacher_want_work(Teacher, Days, Weight),
	((not(member(Day, Days)), Fine is Weight);(member(Day, Days), Fine is 0)).
	
/*
 * Проверка того, что учитель в этот день хочет провести занятие. Для всего расписания. 
 */
teacher_want_work_this_day_WHOLE([], X, Fine) :- Fine is X.
teacher_want_work_this_day_WHOLE([event(class(_, _, _, _, Teacher, _, _, _), _, Day, _, _) | Other], X, Fine) :-
	days_teacher_want_work(Teacher, Days, Weight),
	((not(member(Day, Days)), New_X is X + Weight,
		write(Teacher), write(' предпочитает дни '), write(Days), write(', но ведёт занятия в день '), write(Day), write('. Штраф - '), writeln(Weight));
	(member(Day, Days), New_X is X)),
	teacher_want_work_this_day_WHOLE(Other, New_X, Fine).

/*
 * Проверка того, что вместимость аудитории не сильно выше числа студентов. Для занятия-кандидата.  
 */
check_classrooms(event(_, Classroom, _, Groups, _), Fine) :-
	count_amount_of_students(Groups, 0, Amount_of_students),
 	classroom(Classroom, _, Capacity),
	Div is Capacity // Amount_of_students,
 	% divmod(Capacity, Amount_of_students, Div, _),
	classroom_fillness(Weight1, Weight2, Weight3),
 	((Div < 2, Fine is Weight1);(Div = 2, Fine is Weight2);(Div > 2, Fine is Weight3)).

/*
 * Проверка того, что вместимость аудитории не сильно выше числа студентов. Для всего расписания.  
 */	
check_classrooms_WHOLE([], X, Fine) :- Fine is X.
check_classrooms_WHOLE([event(_, Classroom, _, Groups, _) | Other], X, Fine) :-
 	count_amount_of_students(Groups, 0, Amount_of_students),
 	classroom(Classroom, _, Capacity),
	Div is Capacity // Amount_of_students,
 	% divmod(Capacity, Amount_of_students, Div, _),
	classroom_fillness(Weight1, Weight2, Weight3),
 	((Div < 2, New_X is X + Weight1);
	(Div = 2, New_X is X + Weight2,
		write('Число студентов на занятии '), write(Amount_of_students), write(' , а вместимость класса '), write(Capacity), write('. Штраф - '), writeln(Weight2));
	(Div > 2, New_X is X + Weight3,
		write('Число студентов на занятии '), write(Amount_of_students), write(' , а вместимость класса '), write(Capacity), write('. Штраф - '), writeln(Weight3))),
	check_classrooms_WHOLE(Other, New_X, Fine).

/*
 * Проверка того, что соблюдаются правила по окнам.
 */	
check_gaps(event(_, _, Day, Groups, ClassTime), Fine) :-
	check_gaps2(Groups, Day, ClassTime, 0, X),
	Fine is X.
	
check_gaps2([], _, _, X, Fine) :- Fine is X.
check_gaps2([Group | Other], Day, ClassTime, X, Fine) :-
	findall(Y, group_day_time(Group, Day, Y), ClassTimeList),
	append(ClassTimeList, [ClassTime], NewClassTimeList),
	sort(NewClassTimeList, [Head | Tail]),
	InitMax is 0,
	check_gaps4(Head, Tail, InitMax, Max),
	Max_gap is Max - 1,
	((Max_gap - InitMax =< 0, New_X is X);
	(not(Max_gap - InitMax =< 0), c_gaps(Max_gap, F), New_X is X + F)),
	check_gaps2(Other, Day, ClassTime, New_X, Fine).

% Определяем минимальное окно между занятием-кандидатом и уже существующими занятиями в расписании у каждой из групп-кандидатов.
check_gaps3(_, _, _, _, [], X, Min) :- Min is X.
check_gaps3(List, Group, Day, ClassTime, [group_day_time(_, _, Y) | Other], X, Min) :-
	Dif is ClassTime - Y,
	((Dif < 0, New_dif is Dif * (-1)); (Dif >= 0, New_dif is Dif)),
	((X > New_dif, New_X is New_dif); (X =< New_dif, New_X is X)),
	check_gaps3(List, Group, Day, ClassTime, Other, New_X, Min).

% Определяем максимальное окно между занятием-кандидатом и уже существующими занятиями в расписании у каждой из групп-кандидатов.
check_gaps4(_, [], X, Max) :- Max is X.
check_gaps4(Left, [Right | Rest], X, Max) :-
	Dif is Right - Left,
	((X < Dif, New_X is Dif); (X >= Dif, New_X is X)),
	check_gaps4(Right, Rest, New_X, Max).

check_gaps_WHOLE(Day, X, Fine) :- study_days_in_week(D), Day == D, Fine is X.
check_gaps_WHOLE(Day, X, Fine) :- 
	findall(GroupOfStudents, group_day_time(GroupOfStudents, Day, _), GroupsList),
	sort(GroupsList, GroupsSet),
	check_gaps_WHOLE2(GroupsSet, Day, 0, F),
	New_X is X + F,
	New_Day is Day + 1,
	check_gaps_WHOLE(New_Day, New_X, Fine).
	
check_gaps_WHOLE2([], _, X, Fine) :- Fine is X.
check_gaps_WHOLE2([GroupOfStudents | Other], Day, X, Fine) :-
	findall(ClassTime, group_day_time(GroupOfStudents, Day, ClassTime), ClassTimeList),
	sort(ClassTimeList, [Head | Tail]),
	InitMax is 0,
	check_gaps_WHOLE3(Head, Tail, InitMax, Max),
	Max_gap is Max - 1,
	((Max_gap - InitMax =< 0, New_X is X);
	(not(Max_gap - InitMax =< 0), c_gaps(Max_gap, F), New_X is X + F,
		write('Группа '), write(GroupOfStudents), write(' в '), write(Day), write( ' день имеет (наибольшее) окно размером в '), write(Max_gap), write(' пар(-ы). Штраф - '), writeln(F))),
	check_gaps_WHOLE2(Other, Day, New_X, Fine).

check_gaps_WHOLE3(_, [], X, Max) :- Max is X.
check_gaps_WHOLE3(Left, [Right | Rest], X, Max) :-
	Dif is Right - Left,
	((X < Dif, New_X is Dif); (X >= Dif, New_X is X)),
	check_gaps_WHOLE3(Right, Rest, New_X, Max).

/*
 * С окном для перекуса осторожнее!! Если занятия 1-2, то окно не нужно вообще.
 */

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

/*
 * Имеют ли списки хотя бы один общий элемент.
 */
have_common_item([], _) :- false.
have_common_item([First|_],OtherList) :-
	member(First, OtherList),
	!.
have_common_item([_|Rest],OtherList) :-
	have_common_item(Rest,OtherList).

perm([H|T],Permutation):-
	findall(A,permutation([H|T],A),List),
	length(List,Length),
	random(1,Length,Random),
	nth1(Random,List,Permutation),!.
