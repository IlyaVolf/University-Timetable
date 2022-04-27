:- use_module(fit_new_department).

 
main() :-
	clear_all(),
	attempts(Attempts),
	sumOfAllDaysTeachersCanWork(X_can, Y_can, Z_can),
	sumOfAllDaysTeachersWantWork(X_want, Y_want, Z_want),
	asserta(sumOfDaysTeachersCanWork(X_can, Y_can, Z_can)),
	asserta(sumOfDaysTeachersWantWork(X_want, Y_want, Z_want)),
	initiateDijkstraSearch(Attempts, Attempts, 1000000, []), !.
 
main(Attempts) :-
	clear_all(),
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
	((Min == 1000000, write("�� ������� ��������� ����������. ������� ���� �������: "), writeln(Attempts), !);
	(not(Min == 1000000), writeln(""),
	sort(5, @=<, BestState, SortedState),
	sort(3, @=<, SortedState, TwiceSortedState),
	writeln("������ ����������: "),
	printResult(TwiceSortedState),
	write("������� ���� �������: "), writeln(Attempts),
	writeln("����� �������: "),
	writeln(Min), !)).
	
initiateDijkstraSearch(I, Attempts, Min, BestState) :-
	clear(),
	allClassList(VacantClasses),
	Iter is Attempts - I + 1,
	writeln(""),
	write("�������: "), writeln(Iter),
	dijkstraSearch(node([], 0, 0), VacantClasses, Fine, State),
	((State == [], New_BestState = BestState, New_Min is Min, writeln("��������� �������: ���������� ��������� �� �������."));
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
	writeln("����������: "),
	printResult(TwiceSortedState),
	writeln("����� �������: "),
	cost_all(State, Fine),
	X is Fine,
	Y = State,
	writeln(Fine),
	writeln(""), !.

/*
 * ������ ��� ��������� �������� ������� � ����������� ������������
 * �����������. ����� �������� ���� ������ ������������ ������� �
 * ������� ������� � ���������� �������. ���� � ��������.
 */
 
dijkstraSearch(node(State, Length, H), VacantClasses, X, Y) :-
	% sort(5, @=<, State, SortedState),
	% sort(3, @=<, SortedState, TwiceSortedState),
	% writeln(""),
	% writeln("����������: "),
	% printResult(TwiceSortedState),
	% findall(node(NewState, NewLength, 0), (findNeighbors(State, VacantClasses, NewState), NewLength is Length + 1), ListOfNeighbors),
	findall(node(NewState, NewLength, SumH), (findNeighbors(State, VacantClasses, NewState), NewLength is Length + 1, cost_last(NewState, NewH), SumH is NewH + H), ListOfNeighbors),
	lengthList(ListOfNeighbors, Len),
	writeln(Len),
	((Len > 0,
	random_permutation(ListOfNeighbors, RandomListOfNeighbors),
	sort(3, @=<, RandomListOfNeighbors, SortedListOfNeighbors),
	% sort(3, @=<, ListOfNeighbors, SortedListOfNeighbors),
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
printResult([]) :- writeln("").
printResult([event(class(_, Name_of_subject, _, type_of_class(Type_of_class), teacher(Teacher), _, _, _), Classroom, Day, Group, ClassTime) | Other]) :-
	write("���� "), write(Day),write(" "),write(Type_of_class),write(" "),write(Name_of_subject),write(", ������������� "),write(Teacher),write(", ��� "),write(Classroom),write(", ������: "),write(Group),write(", ����� "), writeln(ClassTime),
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
	% write([Name_of_subject, Type_of_class, Semester, X]), writeln(" Error: the subjects require more students than they are"),!,
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
	divmod(Semester, 2, _, Mod),
	((semester(1), Mod =:= 1, (((class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Teacher, Amount_of_groups, Frequency_of_class, I)), New_I is I + 1, asserta(class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Teacher, Amount_of_groups, Frequency_of_class, New_I)));
	(not(class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Teacher, Amount_of_groups, Frequency_of_class, _)), asserta(class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Teacher, Amount_of_groups, Frequency_of_class, 0)))));
	(semester(2), Mod =:= 0, (((class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Teacher, Amount_of_groups, I)), New_I is I + 1, asserta(class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Teacher, Amount_of_groups, Frequency_of_class, New_I)));
	(not(class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Teacher, Amount_of_groups, _)), asserta(class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Teacher, Amount_of_groups, Frequency_of_class, 0)))));
	(semester(1), Mod =:= 0); (semester(2), Mod =:= 1)),
	splitter5(Name_of_ed_program, Name_of_subject, Rest, Type_of_class, Frequency_of_class, Teacher, Amount_of_groups).
	
% �������� taken_groups_in_type_of_class ����������, ����� ������� ���������� � ���, ������� ����� ��� ���� ����� ��� ��� ��� ���� ��� �������.
splitter6(_, _, [], _, _).
splitter6(Name_of_ed_program, Name_of_subject, [Semester | Rest], Type_of_class, Frequency_of_class) :-
	divmod(Semester, 2, Div, Mod),
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
lengthList([], 0).
lengthList([_|Tail],Length) :-
    lengthList(Tail,Tail_Length),
    Length is Tail_Length + 1.
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
	divmod(Classes_in_day, 2, Div, Mod),
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
		write(Teacher), write(" ������������ ��� "), write(Days), write(", �� ���� ������� � ���� "), write(Day), write(". ����� - "), writeln(Weight));
	(member(Day, Days), New_X is X)),
	teacher_want_work_this_day_WHOLE(Other, New_X, Fine).

/*
 * �������� ����, ��� ����������� ��������� �� ������ ���� ����� ���������. ��� �������-���������.  
 */
check_classrooms(event(_, Classroom, _, Groups, _), Fine) :-
	count_amount_of_students(Groups, 0, Amount_of_students),
 	classroom(Classroom, _, Capacity),
 	divmod(Capacity, Amount_of_students, Div, _),
	classroom_fillness(Weight1, Weight2, Weight3),
 	((Div < 2, Fine is Weight1);(Div = 2, Fine is Weight2);(Div > 2, Fine is Weight3)).

/*
 * �������� ����, ��� ����������� ��������� �� ������ ���� ����� ���������. ��� ����� ����������.  
 */	
check_classrooms_WHOLE([], X, Fine) :- Fine is X.
check_classrooms_WHOLE([event(_, Classroom, _, Groups, _) | Other], X, Fine) :-
 	count_amount_of_students(Groups, 0, Amount_of_students),
 	classroom(Classroom, _, Capacity),
 	divmod(Capacity, Amount_of_students, Div, _),
	classroom_fillness(Weight1, Weight2, Weight3),
 	((Div < 2, New_X is X + Weight1);
	(Div = 2, New_X is X + Weight2,
		write("����� ��������� �� ������� "), write(Amount_of_students), write(" , � ����������� ������ "), write(Capacity), write(". ����� - "), writeln(Weight2));
	(Div > 2, New_X is X + Weight3,
		write("����� ��������� �� ������� "), write(Amount_of_students), write(" , � ����������� ������ "), write(Capacity), write(". ����� - "), writeln(Weight3))),
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
		write("������ "), write(GroupOfStudents), write(" � "), write(Day), write( " ���� ����� (����������) ���� �������� � "), write(Max_gap), write(" ���(-�). ����� - "), writeln(F))),
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


