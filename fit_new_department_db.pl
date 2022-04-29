:- module(fit_new_department_db, [ 
	      teacher/1, 
	      type_of_class/1, 
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

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% DATABASE %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 

attempts(2). 
semester(1). 

teacher("Permyakov Ruslan Anatolievich"). 
teacher("Zlygostev Anton Igorevich"). 
teacher("Bukshev Ivan Evgenievich"). 
teacher("Adamansky Anton Valentinovich"). 
teacher("Sitnov Vladimir Evgenievich"). 
teacher("Miginsky Dmitry Sergeevich"). 
teacher("Terentyeva Tatyana Alexandrovna"). 
teacher("Postovalov Sergey Nikolaevich"). 
teacher("Balabanov Artem Andreevich"). 
teacher("Antonets Denis Viktorovich"). 
teacher("Shvab Irina Vasilievna"). 
teacher("Avdeev Roman Ruslanovich"). 
teacher("Gorchakov Konstantin Mikhailovich"). 
teacher("Puzarenko Vadim Grigorievich"). 
teacher("Vaskevich Vladimir Leontievich"). 

type_of_class("lec"). 
type_of_class("pr"). 

classroom("t3213", [type_of_class("pr"), type_of_class("lab")], 20). 
classroom("402 MB", [type_of_class("lec"), type_of_class("pr")], 200). 
classroom("t2266", [type_of_class("lab"), type_of_class("pr")], 20). 
classroom("2128", [type_of_class("lec"), type_of_class("pr")], 80). 
classroom("t3220", [type_of_class("lab"), type_of_class("pr")], 20). 
classroom("1154", [type_of_class("lec"), type_of_class("pr")], 20). 
classroom("406 MB", [type_of_class("lec"), type_of_class("pr")], 20). 
classroom("1155", [type_of_class("lec"), type_of_class("pr")], 40). 
classroom("t2213", [type_of_class("lab"), type_of_class("pr")], 20). 
classroom("SB", [type_of_class("pe")], 500). 
classroom("1156", [type_of_class("lec"), type_of_class("pr")], 200). 
classroom("t2221", [type_of_class("lab"), type_of_class("pr")], 20). 

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
% PART TWO - FACS, ED PRS, SPECS % 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 

faculty("Faculty of Information Technologies"). 

ed_program("Faculty of Information Technologies", "BACH, 09.03.01, Computer Science and Engineering"). 

specialization("BACH, 09.03.01, Computer Science and Engineering", "Computer Science and Systems Engineering"). 
specialization("BACH, 09.03.01, Computer Science and Engineering", "Software Engineering and Computer Science"). 


%%%%%%%%%%%%%%%%%%%%%%%%% 
% PART THREE - SUBJECTS % 
%%%%%%%%%%%%%%%%%%%%%%%%% 

subject("Computer Science and Systems Engineering", "Models of Computation", [3,4], [[type_of_class("lec"), 1, [[teacher("Puzarenko Vadim Grigorievich"), 3]]], [type_of_class("pr"), 1, [[teacher("Puzarenko Vadim Grigorievich"), 2], [teacher("Avdeev Roman Ruslanovich"), 1]]]]). 
subject("Computer Science and Systems Engineering", "Machine learning methods", [5], [[type_of_class("lec"), 1, [[teacher("Postovalov Sergey Nikolaevich"), 2]]], [type_of_class("pr"), 1, [[teacher("Antonets Denis Viktorovich"), 2]]]]). 
subject("Computer Science and Systems Engineering", "Probability theory and mathematical statistics", [3], [[type_of_class("lec"), 1, [[teacher("Postovalov Sergey Nikolaevich"), 3]]], [type_of_class("pr"), 1, [[teacher("Postovalov Sergey Nikolaevich"), 2], [teacher("Antonets Denis Viktorovich"), 1]]]]). 
subject("Computer Science and Systems Engineering", "Team development of a multifunctional software and hardware complex", [5], [[type_of_class("lec"), 1, [[teacher("Adamansky Anton Valentinovich"), 2]]], [type_of_class("pr"), 2, [[teacher("Adamansky Anton Valentinovich"), 2]]]]). 
subject("Software Engineering and Computer Science", "Electrical engineering and Electronics", [5], [[type_of_class("lec"), 1, [[teacher("Gorchakov Konstantin Mikhailovich"), 12]]], [type_of_class("pr"), 1, [[teacher("Gorchakov Konstantin Mikhailovich"), 4], [teacher("Gorchakov Konstantin Mikhailovich"), 4], [teacher("Gorchakov Konstantin Mikhailovich"), 4]]]]). 
subject("Computer Science and Systems Engineering", "Differential equations and the theory of functions of a complex variable", [3], [[type_of_class("lec"), 1, [[teacher("Vaskevich Vladimir Leontievich"), 3]]], [type_of_class("pr"), 1, [[teacher("Vaskevich Vladimir Leontievich"), 2], [teacher("Shvab Irina Vasilievna"), 1]]]]). 
subject("Computer Science and Systems Engineering", "Computational Mathematics", [5], [[type_of_class("pr"), 1, [[teacher("Shvab Irina Vasilievna"), 1], [teacher("Vaskevich Vladimir Leontievich"), 1]]], [type_of_class("lec"), 1, [[teacher("Vaskevich Vladimir Leontievich"), 2]]]]). 
subject("Computer Science and Systems Engineering", "Electrical engineering and Electronics", [3,4], [[type_of_class("lec"), 1, [[teacher("Gorchakov Konstantin Mikhailovich"), 3]]], [type_of_class("pr"), 1, [[teacher("Gorchakov Konstantin Mikhailovich"), 3]]]]). 


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
% PART FOUR - GROUPS OF STUDENTS % 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 

group_of_students("Computer Science and Systems Engineering", "19213", 13, 3). 
group_of_students("Computer Science and Systems Engineering", "19214", 12, 3). 
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

list_groups_of_students("Computer Science and Systems Engineering", 2, ["20213", "20214", "20215"]). 
list_groups_of_students("Computer Science and Systems Engineering", 3, ["19213", "19214"]). 
list_groups_of_students("Software Engineering and Computer Science", 2, ["20201", "20202", "20203", "20204", "20205", "20206", "20207", "20208", "20209", "20210", "20211", "20212"]). 
list_groups_of_students("Software Engineering and Computer Science", 3, ["19201", "19202", "19203", "19204", "19205", "19206", "19207", "19208", "19209", "19210", "19211", "19212"]). 


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% CONSTRAINTS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
% PART FIVE - HARD CONSTRAINTS % 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 

first_class_starts(9,0). 
class_duration(90). 
short_brake_duration(5). 
long_brake_duration(15). 
study_days_in_week(6). 
study_days_in_week_students(6). 
study_days_in_week_teachers(5). 
classes_in_day(7). 
classes_in_day_students(2). 
classes_in_day_teachers(3). 

days_teacher_can_work(teacher("Permyakov Ruslan Anatolievich"), [1,2,3,4,5,6]). 
days_teacher_can_work(teacher("Zlygostev Anton Igorevich"), [1,2,3,4,5,6]). 
days_teacher_can_work(teacher("Bukshev Ivan Evgenievich"), [1,2,3,4,5,6]). 
days_teacher_can_work(teacher("Adamansky Anton Valentinovich"), [1,2,3,4,5,6]). 
days_teacher_can_work(teacher("Sitnov Vladimir Evgenievich"), [1,2,3,4,5,6]). 
days_teacher_can_work(teacher("Miginsky Dmitry Sergeevich"), [1,2,3,4,5,6]). 
days_teacher_can_work(teacher("Terentyeva Tatyana Alexandrovna"), [1,2,3,4,5,6]). 
days_teacher_can_work(teacher("Postovalov Sergey Nikolaevich"), [1,2,3,4,5,6]). 
days_teacher_can_work(teacher("Balabanov Artem Andreevich"), [1,2,3,4,5,6]). 
days_teacher_can_work(teacher("Antonets Denis Viktorovich"), [1,2,3,4,5,6]). 
days_teacher_can_work(teacher("Shvab Irina Vasilievna"), [1,2,3]). 
days_teacher_can_work(teacher("Avdeev Roman Ruslanovich"), [1]). 
days_teacher_can_work(teacher("Gorchakov Konstantin Mikhailovich"), [1,2,3,4,5,6]). 
days_teacher_can_work(teacher("Puzarenko Vadim Grigorievich"), [4,5,6]). 
days_teacher_can_work(teacher("Vaskevich Vladimir Leontievich"), [3,4,5,6]). 


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

c_lunch_break(5). 
c_gaps(0,0). 
c_gaps(1,2). 
c_gaps(2,6). 
c_gaps(3,9). 
c_gaps(Amount_of_gaps, 10) :- Amount_of_gaps > 3. 
classroom_fillness(0, 10, 10). 

days_teacher_want_work(teacher("Permyakov Ruslan Anatolievich"), [1,3,5], 5). 
days_teacher_want_work(teacher("Zlygostev Anton Igorevich"), [1,2,3,4,5], 2). 
days_teacher_want_work(teacher("Bukshev Ivan Evgenievich"), [1,2,3,4,5], 5). 
days_teacher_want_work(teacher("Adamansky Anton Valentinovich"), [3,4,6], 4). 
days_teacher_want_work(teacher("Sitnov Vladimir Evgenievich"), [1,2,3,4,5], 2). 
days_teacher_want_work(teacher("Miginsky Dmitry Sergeevich"), [1,2,3,4,5,6], 0). 
days_teacher_want_work(teacher("Terentyeva Tatyana Alexandrovna"), [3,5], 5). 
days_teacher_want_work(teacher("Postovalov Sergey Nikolaevich"), [1,2,3,4,5], 2). 
days_teacher_want_work(teacher("Balabanov Artem Andreevich"), [1,2,3,4,5], 1). 
days_teacher_want_work(teacher("Antonets Denis Viktorovich"), [1,2,3,4,5], 3). 
days_teacher_want_work(teacher("Shvab Irina Vasilievna"), [1,2,3], 1). 
days_teacher_want_work(teacher("Avdeev Roman Ruslanovich"), [1], 10). 
days_teacher_want_work(teacher("Gorchakov Konstantin Mikhailovich"), [1,2,3,4,5,6], 0). 
days_teacher_want_work(teacher("Puzarenko Vadim Grigorievich"), [4,5,6], 10). 
days_teacher_want_work(teacher("Vaskevich Vladimir Leontievich"), [3,4,5,6], 10). 

