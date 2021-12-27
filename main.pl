% На стороне Матвея: сдвиги годов вперёд и назад, контрольная сумма: число групп всех дубликатов и число групп обр программы совпадают
% (ну как минимум не больше), время расписания (вся инфа для этого будет в БД) -- просто арифметика.
% class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Teacher, Amount_of_groups, Order_in_week, Id)

% :- use_module(fit_new_departmentllll).

/*
 * Получаю список всех занятий. При переходе в новую
 * вершину, структура class добавленного занятия будет удалена из списка.
 * Выполняю процедуру до тех пор, пока остались нераспределённые задачи.
 * Attempts - количество попыток на генерацию, заданное пользователем.
 */
 
main :-
	writeln('ХУЙы').
	clear_all.
%	attempts(Attempts),
%	sumOfAllDaysTeachersCanWork(X_can, Y_can, Z_can),
%	sumOfAllDaysTeachersWantWork(X_want, Y_want, Z_want),
%	asserta(sumOfDaysTeachersCanWork(X_can, Y_can, Z_can)),
%	asserta(sumOfDaysTeachersWantWork(X_want, Y_want, Z_want)),
%	initiateDijkstraSearch(Attempts, Attempts, 1000000, []), !.
 
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
	((Min == 1000000, write('LOL'), writeln(Attempts), !);
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
	divmod(Semester, 2, _, Mod),
	((semester(1), Mod =:= 1, (((class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Teacher, Amount_of_groups, Frequency_of_class, I)), New_I is I + 1, asserta(class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Teacher, Amount_of_groups, Frequency_of_class, New_I)));
	(not(class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Teacher, Amount_of_groups, Frequency_of_class, _)), asserta(class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Teacher, Amount_of_groups, Frequency_of_class, 0)))));
	(semester(2), Mod =:= 0, (((class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Teacher, Amount_of_groups, I)), New_I is I + 1, asserta(class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Teacher, Amount_of_groups, Frequency_of_class, New_I)));
	(not(class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Teacher, Amount_of_groups, _)), asserta(class(Name_of_ed_program, Name_of_subject, Semester, Type_of_class, Teacher, Amount_of_groups, Frequency_of_class, 0)))));
	(semester(1), Mod =:= 0); (semester(2), Mod =:= 1)),
	splitter5(Name_of_ed_program, Name_of_subject, Rest, Type_of_class, Frequency_of_class, Teacher, Amount_of_groups).
	
% Добавляю taken_groups_in_type_of_class рекурсивно, чтобы хранить информацию о том, сколько групп уже было взято под тот или иной тип занятия.
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
lengthList([], 0).
lengthList([_|Tail],Length) :-
    lengthList(Tail,Tail_Length),
    Length is Tail_Length + 1.
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
	divmod(Classes_in_day, 2, Div, Mod),
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
 	divmod(Capacity, Amount_of_students, Div, _),
	classroom_fillness(Weight1, Weight2, Weight3),
 	((Div < 2, Fine is Weight1);(Div = 2, Fine is Weight2);(Div > 2, Fine is Weight3)).

/*
 * Проверка того, что вместимость аудитории не сильно выше числа студентов. Для всего расписания.  
 */	
check_classrooms_WHOLE([], X, Fine) :- Fine is X.
check_classrooms_WHOLE([event(_, Classroom, _, Groups, _) | Other], X, Fine) :-
 	count_amount_of_students(Groups, 0, Amount_of_students),
 	classroom(Classroom, _, Capacity),
 	divmod(Capacity, Amount_of_students, Div, _),
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
