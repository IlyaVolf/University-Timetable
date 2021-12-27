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
teacher('�������� ������ �����������').
teacher('��������� ����� ��������').
teacher('������ ���� ����������').
teacher('�������� �������� ����������').
teacher('���������� ����� ������������').
teacher('������ �������� ����������').
teacher('��������� ������� ���������').
teacher('���������� ������� �������������').
teacher('���������� ������ ����������').
teacher('��������� ����� ���������').
teacher('������� ����� ����������').
teacher('���� ����� ����������').
teacher('������ ����� ����������').
teacher('�������� ���������� ����������').
teacher('��������� ����� �����������').

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
classroom('�3213', Types_of_class, Capacity_of_classroom) :- type_of_classroom('terminals', Types_of_class, Capacity_of_classroom).
classroom('402 ��', Types_of_class, Capacity_of_classroom) :- type_of_classroom('huge for lectures and practices', Types_of_class, Capacity_of_classroom).
classroom('��', Types_of_class, Capacity_of_classroom) :- type_of_classroom('room for pe', Types_of_class, Capacity_of_classroom).
classroom('�2266', Types_of_class, Capacity_of_classroom) :- type_of_classroom('terminals', Types_of_class, Capacity_of_classroom).
classroom('2128', Types_of_class, Capacity_of_classroom) :- type_of_classroom('big for lectures and practices', Types_of_class, Capacity_of_classroom).
classroom('�3220', Types_of_class, Capacity_of_classroom) :- type_of_classroom('terminals', Types_of_class, Capacity_of_classroom).
classroom('1154', Types_of_class, Capacity_of_classroom) :- type_of_classroom('small for lectures and practices', Types_of_class, Capacity_of_classroom).
classroom('406 ��', Types_of_class, Capacity_of_classroom) :- type_of_classroom('small for lectures and practices', Types_of_class, Capacity_of_classroom).
classroom('1155', Types_of_class, Capacity_of_classroom) :- type_of_classroom('medium for lectures and practices', Types_of_class, Capacity_of_classroom).
classroom('�2213', Types_of_class, Capacity_of_classroom) :- type_of_classroom('terminals', Types_of_class, Capacity_of_classroom).
classroom('�2221', Types_of_class, Capacity_of_classroom) :- type_of_classroom('terminals', Types_of_class, Capacity_of_classroom).


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
% subject('Computer Science and Systems Engineering', '�������������� � �����������', [3, 4], [[type_of_class('lec'), 1, [[teacher('�������� ���������� ����������'), 2]]], [type_of_class('pr'), 1, [[teacher('�������� ���������� ����������'), 2]]]]).

subject('Computer Science and Systems Engineering', '������ ����������', [3, 4], [[type_of_class('lec'), 1, [[teacher('��������� ����� �����������'), 3]]], [type_of_class('pr'), 1, [[teacher('��������� ����� �����������'), 2], [teacher('������ ����� ����������'), 1]]]]).
% subject('Computer Science and Systems Engineering', '������ ����������', [5, 6], [[type_of_class('lec'), 1, [[teacher('��������� ����� �����������'), 2]]], [type_of_class('pr'), 1, [[teacher('��������� ����� �����������'), 1], [teacher('������ ����� ����������'), 1]]]]).
subject('Computer Science and Systems Engineering', '������ ��������� ��������', [5], [[type_of_class('lec'), 1, [[teacher('���������� ������ ����������'), 2]]], [type_of_class('pr'), 1, [[teacher('������� ����� ����������'), 2]]]]).
subject('Computer Science and Systems Engineering', '������ ����������� � �������������� ����������', [3], [[type_of_class('lec'), 1, [[teacher('���������� ������ ����������'), 3]]], [type_of_class('pr'), 1, [[teacher('���������� ������ ����������'), 2], [teacher('������� ����� ����������'), 1]]]]).
subject('Computer Science and Systems Engineering', '���������������� ��������� � ������ ������� ������������ �����������', [3], [[type_of_class('lec'), 1, [[teacher('�������� �������� ����������'), 3]]], [type_of_class('pr'), 1, [[teacher('�������� �������� ����������'), 2], [teacher('���� ����� ����������'), 1]]]]).
subject('Computer Science and Systems Engineering', '�������������� ����������', [5], [[type_of_class('lec'), 1, [[teacher('�������� �������� ����������'), 2]]], [type_of_class('pr'), 1, [[teacher('�������� �������� ����������'), 1], [teacher('���� ����� ����������'), 1]]]]).
subject('Computer Science and Systems Engineering', '��������� ���������� �������������������� ����������-����������� ���������', [5], [[type_of_class('lec'), 1, [[teacher('���������� ����� ������������'), 2]]], [type_of_class('pr'), 2, [[teacher('���������� ����� ������������'), 2]]]]).
subject('Software Engineering and Computer Science', '�������������� � �����������', [5], [[type_of_class('lec'), 1, [[teacher('�������� ���������� ����������'), 12]]], [type_of_class('pr'), 1, [[teacher('�������� ���������� ����������'), 4], [teacher('�������� ���������� ����������'), 4], [teacher('�������� ���������� ����������'), 4]]]]).

% subject('Computer Science and Systems Engineering', '������ ��������� ��������', [5], [[type_of_class('lec'), 1, [['���������� ������ ����������', 2]]], [type_of_class('pr'), 1, [['������� ����� ����������', 2]]]]).
% subject('Computer Science and Systems Engineering', '�������������� ����������', [5], [[type_of_class('lec'), 1, [['�������� �������� ����������', 2]]], [type_of_class('pr'), 1, [['�������� �������� ����������'), 1], ['���� ����� ����������', 1]]]]).
% subject('Computer Science and Systems Engineering', '��������� ���������� �������������������� ����������-����������� ���������', [5, 6], [[type_of_class('lec'), 1, [['���������� ����� ������������', 2]]], [type_of_class('pr'), 2, [['���������� ����� ������������', 2]]]]).

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
days_teacher_can_work(teacher('��������� ����� �����������'),[4,5,6]).
days_teacher_can_work(teacher('������ ����� ����������'),[1]).
days_teacher_can_work(teacher('�������� ������ �����������'),[1,2,3,4,5,6]).
days_teacher_can_work(teacher('��������� ����� ��������'),[1,2,3,4,5,6]).
days_teacher_can_work(teacher('������ ���� ����������'),[1,2,3,4,5,6]).
days_teacher_can_work(teacher('�������� �������� ����������'),[3,4,5,6]).
days_teacher_can_work(teacher('���������� ����� ������������'),[1,2,3,4,5,6]).
days_teacher_can_work(teacher('������ �������� ����������'),[1,2,3,4,5,6]).
days_teacher_can_work(teacher('��������� ������� ���������'),[1,2,3,4,5,6]).
days_teacher_can_work(teacher('���������� ������� �������������'),[1,2,3,4,5,6]).
days_teacher_can_work(teacher('���������� ������ ����������'),[1,2,3,4,5,6]).
days_teacher_can_work(teacher('��������� ����� ���������'),[1,2,3,4,5,6]).
days_teacher_can_work(teacher('������� ����� ����������'),[1,2,3,4,5,6]).
days_teacher_can_work(teacher('���� ����� ����������'),[1,2,3]).
days_teacher_can_work(teacher('�������� ���������� ����������'),[1,2,3,4,5,6]).


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
days_teacher_want_work(teacher('��������� ����� �����������'),[4,5,6], 10).
days_teacher_want_work(teacher('������ ����� ����������'),[1], 10).
days_teacher_want_work(teacher('�������� ������ �����������'),[1,3,5], 5).
days_teacher_want_work(teacher('��������� ����� ��������'),[1,2,3,4,5], 2).
days_teacher_want_work(teacher('������ ���� ����������'),[1,2,3,4,5], 5).
days_teacher_want_work(teacher('�������� �������� ����������'),[1,2,3,4,5,6], 0).
days_teacher_want_work(teacher('���������� ����� ������������'),[3,4,6], 4).
days_teacher_want_work(teacher('������ �������� ����������'),[1,2,3,4,5], 2).
days_teacher_want_work(teacher('��������� ������� ���������'),[1,2,3,4,5,6], 0).
days_teacher_want_work(teacher('���������� ������� �������������'),[3,5], 5).
days_teacher_want_work(teacher('���������� ������ ����������'),[1,2,3,4,5], 2).
days_teacher_want_work(teacher('��������� ����� ���������'),[1,2,3,4,5], 1).
days_teacher_want_work(teacher('������� ����� ����������'),[1,2,3,4,5], 3).
days_teacher_want_work(teacher('���� ����� ����������'),[1,3], 1).
days_teacher_want_work(teacher('�������� ���������� ����������'),[1,2,3,4,5,6], 0).




%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

/*
 * ������� ������ ���� �������. ��� �������� � �����
 * �������, ��������� class ������������ ������� ����� ������� �� ������.
 * �������� ��������� �� ��� ���, ���� �������� ��������������� ������.
 * Attempts - ���������� ������� �� ���������, �������� �������������.
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
	((Min == 1000000, write('�� ������� ��������� ����������. ������� ���� �������: '), writeln(Attempts), !);
	(not(Min == 1000000), writeln(''),
	sort(5, @=<, BestState, SortedState),
	sort(3, @=<, SortedState, TwiceSortedState),
	writeln('������ ����������: '),
	printResult(TwiceSortedState),
	write('������� ���� �������: '), writeln(Attempts),
	writeln('����� �������: '),
	writeln(Min), !)).
	
initiateDijkstraSearch(I, Attempts, Min, BestState) :-
	clear,
	allClassList(VacantClasses),
	Iter is Attempts - I + 1,
	writeln(''),
	write('�������: '), writeln(Iter),
	dijkstraSearch(node([], 0, 0), VacantClasses, Fine, State),
	((State == [], New_BestState = BestState, New_Min is Min, writeln('��������� �������: ���������� ��������� �� �������.'));
	(not(State == []), Min > Fine, New_BestState = State, New_Min is Fine);
	(not(State == []), Min =< Fine, New_BestState = BestState, New_Min is Min)),
	New_I is I - 1,
	initiateDijkstraSearch(New_I, Attempts, New_Min, New_BestState).
	
	
/*
 * ��� �������� � ����������. �������� � ������ ��� ���������� � �����.
 */ 

dijkstraSearch(node(State, _, _), [], X, Y) :-
	sort(5, @=<, State, SortedState),
	sort(3, @=<, SortedState, TwiceSortedState),
	writeln('����������: '),
	printResult(TwiceSortedState),
	writeln('����� �������: '),
	cost_all(State, Fine),
	X is Fine,
	Y = State,
	writeln(Fine),
	writeln(''), !.

/*
 * ������ ��� ��������� �������� ������� � ����������� ������������
 * �����������. ����� �������� ���� ������ ������������ ������� �
 * ������� ������� � ���������� �������. ���� � ��������.
 */
 
dijkstraSearch(node(State, Length, H), VacantClasses, X, Y) :-
	% sort(5, @=<, State, SortedState),
	% sort(3, @=<, SortedState, TwiceSortedState),
	% writeln(''),
	% writeln('����������: '),
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
 * ������ �������, �����, ��� ��� �� ������������ ������������
 * ������������. ���� �� � �������, �� ����� - ����� State.
 * �� ������ ������� �������, ������� �� ������� �
 * ������� ����������.
 * ����� ������ ���� ����������������� �������� ��������� ��������.
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
 * ��������, ��� ��� �������� �� ����� ���������� ������������ ������
 * ������� � ��������� �������� ����������. �� ���� � ����� ��������
 * �� ����� 2 ������� ������������. � ���� ��, ������������� � �������
 * � ���� ����� �� ����� ������������� ����� �� ���� ��������.
 */
dateIsOk([],_) :- !.
% ���� ������� ���������� �� � ���� �����, �� ��������� �� ��������
% �������������� � �������� ���� ��� ������.
dateIsOk([event(_, Classroom, Day, _, ClassTime) | Other], event(NewClass, Classroom, Day, NewGroupsOfStudents, NewClassTime)) :-
	%% ?? ���� �� ����������, ��� Classroom = NewClassroom ��� � ��������� ??
	ClassTime \= NewClassTime,
	dateIsOk(Other, event(NewClass, Classroom, Day, NewGroupsOfStudents, NewClassTime)).
	
% ������� ���������� � ������ ��� - ��������� �� ��������
% �������������� � �������� ��� ������.
dateIsOk([event(_, Classroom, Day, _, _) | Other], event(NewClass, NewClassroom, NewDay, NewGroupsOfStudents, NewClassTime)) :-
	Day \= NewDay,
	Classroom \= NewClassroom,
	dateIsOk(Other, event(NewClass, NewClassroom, NewDay, NewGroupsOfStudents, NewClassTime)).
	
% ������� � ������ ����������, �� � ���� ���� � � ���� �����. ���� ���������, ���
% �������� �� �������������� � �������� ���.
dateIsOk([event(Class, Classroom, Day, GroupsOfStudents, ClassTime) | Other], event(NewClass, NewClassroom, Day, NewGroupsOfStudents, NewClassTime)) :-
	Classroom \= NewClassroom,
	noTeacherOverruns(Class, ClassTime, NewClass, NewClassTime),
	noStudentOverruns(ClassTime, GroupsOfStudents, NewClassTime, NewGroupsOfStudents),
	dateIsOk(Other, event(NewClass, NewClassroom, Day, NewGroupsOfStudents, NewClassTime)).
	
% ������� ���������� � ������ ��� - ��������� �� ��������
% �������������� � �������� ��� ������.
dateIsOk([event(_, Classroom, Day, _, _) | Other], event(NewClass, Classroom, NewDay, NewGroupsOfStudents, NewClassTime)) :-
	Day \= NewDay,
	dateIsOk(Other, event(NewClass, Classroom, NewDay, NewGroupsOfStudents, NewClassTime)).

/* 
 * ��������, ��� � ���� ���� � ��� ����� ������� �� ���� �������.
 */
% ������� ������ ������.
noTeacherOverruns(class(_, _, _, _, Teacher, _, _, _), _, class(_, _, _, _, NewTeacher, _, _, _), _) :-
	Teacher \= NewTeacher.

% ������� ����, �� ����� ������.	
noTeacherOverruns(class(_, _, _, _, Teacher, _, _, _), ClassTime, class(_, _, _, _, NewTeacher, _, _, _), NewClassTime) :-
	Teacher = NewTeacher,
	ClassTime \= NewClassTime.

/* 
 * ��������, ��� � ���� ���� � ��� ����� � ������ ��������� ��� �������.
 */
% ��� ������ ��������� ������������ ����� ������.
noStudentOverruns(_, GroupsOfStudents, _, NewGroupsOfStudents) :-
	not(have_common_item(GroupsOfStudents, NewGroupsOfStudents)).

% ���� ����������� � �������, ���������� ���������� �� �������������� �������.	
noStudentOverruns(ClassTime, GroupsOfStudents, NewClassTime, NewGroupsOfStudents) :-
	have_common_item(GroupsOfStudents, NewGroupsOfStudents),
	noStudentOverruns2(ClassTime, GroupsOfStudents, NewClassTime, NewGroupsOfStudents).

% ���������������� ������� ���� �� �������-����������.
noStudentOverruns2(_, [], _, _).
noStudentOverruns2(ClassTime, [GroupOfStudents | Rest], NewClassTime, NewGroupsOfStudents) :-
	noStudentOverruns3(ClassTime, GroupOfStudents, NewClassTime, NewGroupsOfStudents),
	noStudentOverruns2(ClassTime, Rest, NewClassTime, NewGroupsOfStudents).

% ��������� ����������� ������-��������� � ������ �����.
noStudentOverruns3(_, _, _, []).
noStudentOverruns3(ClassTime, GroupOfStudents, NewClassTime, [NewGroupOfStudents | Rest]) :-
	((GroupOfStudents \= NewGroupOfStudents); (GroupOfStudents = NewGroupOfStudents, ClassTime \= NewClassTime)),
	noStudentOverruns3(ClassTime, GroupOfStudents, NewClassTime, Rest).

/*
 * �������� ���������� � �������: ��������� class, ������ ���������, ���� ������� � ����� �������.
 * ��� ����� ������������� ������ �����, ���� ��������� ���� � ��������� ����������.
 */
getNewClassInfo(node(State, _, _), NewClass, NewGroupsOfStudents, NewDay, NewClassTime) :-
	reverse(State, [NewEvent | _]),
	getNewClassInfo2(NewEvent, NewClass, NewGroupsOfStudents, NewDay, NewClassTime).

% ���������������� ���������.
getNewClassInfo2(event(Class, _, Day, GroupsOfStudents, ClassTime), NewClass, NewGroupsOfStudents, NewDay, NewClassTime) :-
	NewClass = Class,
	NewGroupsOfStudents = GroupsOfStudents,
	NewDay = Day,
	NewClassTime = ClassTime.

/*
 * �������
 */
stateToClassConverter([], List, Classes) :- Classes = List.
stateToClassConverter([event(Class, _, _, _) | Other], List, Classes) :-
	append(List, [Class], NewList),
	stateToClassConverter(Other, NewList, Classes).

/*
 * �������� ���������� �� ����������.
 */
printResult([]) :- writeln('').
printResult([event(class(_, Name_of_subject, _, type_of_class(Type_of_class), teacher(Teacher), _, _, _), Classroom, Day, Group, ClassTime) | Other]) :-
	write('���� '), write(Day),write(' '),write(Type_of_class),write(' '),write(Name_of_subject),write(', ������������� '),write(Teacher),write(', ��� '),write(Classroom),write(', ������: '),write(Group),write(', ����� '), writeln(ClassTime),
	printResult(Other).


/*
 * ������� ��������� ��������� ���������������� ����� �� �������� ��� ������� ���� ��������.
 */
add_to_taken_groups(class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, _, _, Order_in_week, _), Groups) :-
	taken_groups_in_type_of_class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Current_groups, Order_in_week),
	% append(Current_groups, Groups, New_groups),
	subtract(Current_groups, Groups, New_groups),
	retract(taken_groups_in_type_of_class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, _, Order_in_week)),
	asserta(taken_groups_in_type_of_class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, New_groups, Order_in_week)).
	% writeln(taken_groups_in_type_of_class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, New_groups)).

/*
 * ������� ��������� ��������� ���������: ������ ���������, ����, ����� �������.
 */
add_to_group_day_time(_, [], _, _).
add_to_group_day_time(class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Teacher, Amount_of_groups, Order_in_week, Id), [GroupOfStudents | Rest], Day, ClassTime) :-
	asserta(group_day_time(GroupOfStudents, Day, ClassTime)),
	add_to_group_day_time(class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Teacher, Amount_of_groups, Order_in_week, Id), Rest, Day, ClassTime).

/*
 * ������� ��������� ��������� ���������: �������������, ����, ����� �������.
 */
add_to_teacher_day_time(class(_, _, _, _, Teacher, _, _, _), Day, ClassTime) :-
	asserta(teacher_day_time(Teacher, Day, ClassTime)).

/*
 * �� �������� �������������, �������� � ��������� �������� �������� �������� ���������� ������, ������� ����� � ���������� ����������� � ����������� �������������.
 */
class_to_group(class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, _, Amount_of_groups, Order_in_week, _), Groups_of_Students) :- 
	taken_groups_in_type_of_class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Vacant_groups, Order_in_week),
	class_to_group2(Name_of_subject, Semester, Type_of_class, [], Groups_of_Students, Amount_of_groups, Vacant_groups).

% ��������� ������������� �� ��������������� �����	�������, ������� �������� ��� ���������.
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
 * ������������ ����� ����� ����� ���������, ������� ����� �������� �������.
 */
count_amount_of_students([], X, Sum) :- Sum is X.
count_amount_of_students([Group_of_Students | Rest], X, Sum) :-
	group_of_students(_, Group_of_Students, Amount_of_students, _),
	NewX is X + Amount_of_students,
	count_amount_of_students(Rest, NewX, Sum).
	
/*
 * ���������, ��� � �������� ����� �������� ��������� ��� �������.
 */
check_types_of_class_match(class(_, _, _, X, _, _, _, _), Y) :-
	have_common_item([X], Y).

/*
 * ������� ���������, ��� ������������� ����� �������� � �������������� ����.
 */
teacher_can_work_this_day(class(_, _, _, _, Teacher, _, _, _), Day) :-
	days_teacher_can_work(Teacher, Days),
	member(Day, Days).

/*
 * ������� ���������, ��� ����� ��� � ��������� � �������������� �� ���������.
 */
limit_of_classes(class(_, _, _, _, Teacher, _, _, _), GroupOfStudents, Day) :-
	limit_of_classes_stundents(GroupOfStudents, Day),
	limit_of_classes_teachers(Teacher, Day).

% ������� ���������, ��� ����� ��� � ��������� �� ���������.	
limit_of_classes_stundents([], _).
limit_of_classes_stundents([GroupOfStudent | Other], Day) :-
	findall(group_day_time(GroupOfStudent, Day, X), group_day_time(GroupOfStudent, Day, X), List),
	lengthList(List, Len),
	classes_in_day_students(Classes_limit_students),
	% + 1 - ��������� �������-���������, ������� ���� ��� �� ����������� � group_day_time.
	Len + 1 =< Classes_limit_students,
	limit_of_classes_stundents(Other, Day).

% ������� ���������, ��� ����� ��� � �������������� �� ���������.	
limit_of_classes_teachers(Teacher, Day) :-
	findall(teacher_day_time(Teacher, Day, X), teacher_day_time(Teacher, Day, X), List),
	lengthList(List, Len),
	classes_in_day_teachers(Classes_limit_teachers),
	Len + 1 =< Classes_limit_teachers.

% ������� ������ ��������� ���� ���������, ������� ������ ���� ��������� �� ������.
% ���� ������ � �������� ������ �� ��������������.
allClassList(List_of_all_classes) :-
	findall(subject(Name_of_ed_program, Name_of_subject, Semesters, Type_of_class_description), subject(Name_of_ed_program, Name_of_subject, Semesters, Type_of_class_description), List_of_names_of_all_subjects),
	splitter(List_of_names_of_all_subjects),
	writeln('OKAY222'),
	findall(class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Teacher, Amount_of_groups, Order_in_week, Id), class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Teacher, Amount_of_groups, Order_in_week, Id), List_of_all_classes),
	lengthList(List_of_all_classes, X),
	writeln(List_of_all_classes),
	writeln(X).
	
% ������������� ���������� ������ subject �� ������.
splitter([]).
splitter([Subject | Rest]) :-
	splitter2(Subject),
	splitter(Rest).
	
% ������������� ���������� ������ ��� ������� ������-�� ������������ ��������.
splitter2(subject(_, _, _, [])).
splitter2(subject(Name_of_ed_program, Name_of_subject, Semesters, [Type_of_class_description | Other])) :-
	splitter3(Name_of_ed_program, Name_of_subject, Semesters, Type_of_class_description),
	splitter2(subject(Name_of_ed_program, Name_of_subject, Semesters, Other)).

% ������������� ���������� ������ �������� ������-�� ������������ ���� ������� ������-�� ������������ ��������.
splitter3(_, _, _, [_, _, []]).
splitter3(Name_of_ed_program, Name_of_subject, Semesters, [Type_of_class, Frequency_of_class, [[Teacher, Amount_of_groups] | Rest]]) :-
	splitter4(Name_of_ed_program, Name_of_subject, Semesters, Type_of_class, Frequency_of_class, Teacher, Amount_of_groups),
	splitter3(Name_of_ed_program, Name_of_subject, Semesters, [Type_of_class, Frequency_of_class, Rest]).

% ��������� class ���������� �������� �������� ��������� ������-�� ������������ ���� ������� ������-�� ������������ ��������
% ������� ���, ������� ��� � ������ ���� ������� ������ ���������.
splitter4(_, _, _, _, 0, _, _).
splitter4(Name_of_ed_program, Name_of_subject, Semesters, Type_of_class, Frequency_of_class, Teacher, Amount_of_groups) :-
	splitter6(Name_of_ed_program, Name_of_subject, Semesters, Type_of_class, Frequency_of_class),
	splitter5(Name_of_ed_program, Name_of_subject, Semesters, Type_of_class, Frequency_of_class, Teacher, Amount_of_groups),
	New_frequency_of_class is Frequency_of_class - 1,
	splitter4(Name_of_ed_program, Name_of_subject, Semesters, Type_of_class, New_frequency_of_class, Teacher, Amount_of_groups).
	
% ��������� class ���������� �������� �������� �������� ������-�� ������������ ���� ������� ������-�� ������������ ��������
% ������� ���, ������� ��� � ������ ���� ������� ������ ���������.
splitter5(_, _, [], _, _, _, _).
splitter5(Name_of_ed_program, Name_of_subject, [Semester | Rest], Type_of_class, Frequency_of_class, Teacher, Amount_of_groups) :-
	Mod is Semester mod 2,
	((semester(1), Mod =:= 1, (((class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Teacher, Amount_of_groups, Frequency_of_class, I)), New_I is I + 1, asserta(class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Teacher, Amount_of_groups, Frequency_of_class, New_I)));
	(not(class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Teacher, Amount_of_groups, Frequency_of_class, _)), asserta(class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Teacher, Amount_of_groups, Frequency_of_class, 0)))));
	(semester(2), Mod =:= 0, (((class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Teacher, Amount_of_groups, I)), New_I is I + 1, asserta(class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Teacher, Amount_of_groups, Frequency_of_class, New_I)));
	(not(class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Teacher, Amount_of_groups, _)), asserta(class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Teacher, Amount_of_groups, Frequency_of_class, 0)))));
	(semester(1), Mod =:= 0); (semester(2), Mod =:= 1)),
	splitter5(Name_of_ed_program, Name_of_subject, Rest, Type_of_class, Frequency_of_class, Teacher, Amount_of_groups).
	
% �������� taken_groups_in_type_of_class ����������, ����� ������� ���������� � ���, ������� ����� ��� ���� ����� ��� ��� ��� ���� ��� �������.
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
 * ����� ���� ����, ����� ������� ����� ��������. � ����� ����� �������� � ����������� ���������� ����.
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
 * ����� ���� ����, ����� ������� ����� ��������. � ����� ����� �������� � ����������� ���������� ����.
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
 * �������� ��� ������������ ������.
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
 * ����� ������.
 */
lengthList(A,B) :- length(A,B).
%lengthList([], 0).
%lengthList([_|Tail],Length) :-
%    lengthList(Tail,Tail_Length),
%    Length is Tail_Length + 1.
%

/*
 * ������ ������� ������.
 */
headOfList([Head | _], Head).


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

cost_all(Events, Cost) :- 
	check_classrooms_WHOLE(Events, 0, Fine1),
	check_gaps_WHOLE(1, 0, Fine2),
	teacher_want_work_this_day_WHOLE(Events, 0, Fine3),
	Cost is Fine1 + Fine2 + Fine3.

/*
 * ������� ���� ������� (�������������� ����������) ������ ��� �������-���������.
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
 * ��������� �� ��������: � ���������� ���� ������� ������ �������� ���.
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
 * ����� ��������� �� ��������: ������ ���� �� �������, ������� ����� �������� � ������� ���� ���������.
 */
teacher_priority_can(event(class(_, _, _, _, Teacher, _, _, _), _, _, _, _), Fine) :-
	sumOfDaysTeachersCanWork(Sum, Amount, Min),
	days_teacher_can_work(Teacher, Days),
	lengthList(Days, Len),
	((Len == Min, Fine is 0);
	(Len > Min, Sum > Len * Amount, Fine is 1);
	(Len > Min, Sum < Len * Amount, Fine is 3)).

/*
 * ����� ��������� �� ��������: ������ ���� �� �������, ������� ����� �������� � ������� ���� ���������.
 */
teacher_priority_want(event(class(_, _, _, _, Teacher, _, _, _), _, _, _, _), Fine) :-
	sumOfDaysTeachersWantWork(Sum, Amount, Min),
	days_teacher_want_work(Teacher, Days, _),
	lengthList(Days, Len),
	((Len == Min, Fine is 0);
	(Len > Min, Sum > Len * Amount, Fine is 0);
	(Len > Min, Sum < Len * Amount, Fine is 1)).	


/*
 * �������� ����, ��� ������� � ���� ���� ����� �������� �������. ��� �������-���������.
 */
teacher_want_work_this_day(event(class(_, _, _, _, Teacher, _, _, _), _, Day, _, _), Fine) :-
	days_teacher_want_work(Teacher, Days, Weight),
	((not(member(Day, Days)), Fine is Weight);(member(Day, Days), Fine is 0)).
	
/*
 * �������� ����, ��� ������� � ���� ���� ����� �������� �������. ��� ����� ����������. 
 */
teacher_want_work_this_day_WHOLE([], X, Fine) :- Fine is X.
teacher_want_work_this_day_WHOLE([event(class(_, _, _, _, Teacher, _, _, _), _, Day, _, _) | Other], X, Fine) :-
	days_teacher_want_work(Teacher, Days, Weight),
	((not(member(Day, Days)), New_X is X + Weight,
		write(Teacher), write(' ������������ ��� '), write(Days), write(', �� ���� ������� � ���� '), write(Day), write('. ����� - '), writeln(Weight));
	(member(Day, Days), New_X is X)),
	teacher_want_work_this_day_WHOLE(Other, New_X, Fine).

/*
 * �������� ����, ��� ����������� ��������� �� ������ ���� ����� ���������. ��� �������-���������.  
 */
check_classrooms(event(_, Classroom, _, Groups, _), Fine) :-
	count_amount_of_students(Groups, 0, Amount_of_students),
 	classroom(Classroom, _, Capacity),
	Div is Capacity // Amount_of_students,
 	% divmod(Capacity, Amount_of_students, Div, _),
	classroom_fillness(Weight1, Weight2, Weight3),
 	((Div < 2, Fine is Weight1);(Div = 2, Fine is Weight2);(Div > 2, Fine is Weight3)).

/*
 * �������� ����, ��� ����������� ��������� �� ������ ���� ����� ���������. ��� ����� ����������.  
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
		write('����� ��������� �� ������� '), write(Amount_of_students), write(' , � ����������� ������ '), write(Capacity), write('. ����� - '), writeln(Weight2));
	(Div > 2, New_X is X + Weight3,
		write('����� ��������� �� ������� '), write(Amount_of_students), write(' , � ����������� ������ '), write(Capacity), write('. ����� - '), writeln(Weight3))),
	check_classrooms_WHOLE(Other, New_X, Fine).

/*
 * �������� ����, ��� ����������� ������� �� �����.
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

% ���������� ����������� ���� ����� ��������-���������� � ��� ������������� ��������� � ���������� � ������ �� �����-����������.
check_gaps3(_, _, _, _, [], X, Min) :- Min is X.
check_gaps3(List, Group, Day, ClassTime, [group_day_time(_, _, Y) | Other], X, Min) :-
	Dif is ClassTime - Y,
	((Dif < 0, New_dif is Dif * (-1)); (Dif >= 0, New_dif is Dif)),
	((X > New_dif, New_X is New_dif); (X =< New_dif, New_X is X)),
	check_gaps3(List, Group, Day, ClassTime, Other, New_X, Min).

% ���������� ������������ ���� ����� ��������-���������� � ��� ������������� ��������� � ���������� � ������ �� �����-����������.
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
		write('������ '), write(GroupOfStudents), write(' � '), write(Day), write( ' ���� ����� (����������) ���� �������� � '), write(Max_gap), write(' ���(-�). ����� - '), writeln(F))),
	check_gaps_WHOLE2(Other, Day, New_X, Fine).

check_gaps_WHOLE3(_, [], X, Max) :- Max is X.
check_gaps_WHOLE3(Left, [Right | Rest], X, Max) :-
	Dif is Right - Left,
	((X < Dif, New_X is Dif); (X >= Dif, New_X is X)),
	check_gaps_WHOLE3(Right, Rest, New_X, Max).

/*
 * � ����� ��� �������� ����������!! ���� ������� 1-2, �� ���� �� ����� ������.
 */

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

/*
 * ����� �� ������ ���� �� ���� ����� �������.
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
