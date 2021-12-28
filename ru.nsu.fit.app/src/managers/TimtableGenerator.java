package managers;

import entities.*;
import org.projog.api.Projog;
import org.projog.api.QueryResult;
import org.projog.core.term.Term;

import java.io.*;
import java.nio.channels.FileChannel;
import java.sql.SQLException;
import java.util.*;

public class TimtableGenerator {
    public static void copyFile(File sourceFile, File destFile) throws IOException {
        if (!destFile.exists()) {
            destFile.createNewFile();
        }

        FileChannel source = null;
        FileChannel destination = null;

        try {
            source = new FileInputStream(sourceFile).getChannel();
            destination = new FileOutputStream(destFile).getChannel();
            destination.transferFrom(source, 0, source.size());
        } finally {
            if (source != null) {
                source.close();
            }
            if (destination != null) {
                destination.close();
            }
        }
    }

    public static void prepare_prolog(File main_temp) throws IOException, SQLException {
        FileWriter fw = new FileWriter(main_temp, true);
        DatabaseManager dm = DatabaseManager.getInstance();

        fw.write("\n");

        // Число попыток по умолчанию
        // Служебный параметр
        fw.write("attempts(1).\n");

        // Текущий семестр
        // Пока что служебный параметр (зависит от внедрения Матвея)
        fw.write("semester(1).\n");

        // Добавление ограничений
        Constraints constraints = dm.getConstraints();
        fw.write("study_days_in_week(".concat(constraints.studyDaysInWeek).concat(").\n"));
        fw.write("study_days_in_week_students(".concat(constraints.studyDaysInWeekForStudents).concat(").\n"));
        fw.write("study_days_in_week_teachers(".concat(constraints.studyDaysInWeekForTeachers).concat(").\n"));
        fw.write("classes_in_day(".concat(constraints.classesPerDay).concat(").\n"));
        fw.write("classes_in_day_students(".concat(constraints.classesPerDayStudents).concat(").\n"));
        fw.write("classes_in_day_teachers(".concat(constraints.classesPerDayTeachers).concat(").\n"));
        // Пока что служебные параметры (зависят от внедрения Матвея)
        fw.write("c_gaps(0, 0).\n");
        fw.write("c_gaps(1, 2).\n");
        fw.write("c_gaps(2, 6).\n");
        fw.write("c_gaps(3, 9).\n");
        fw.write("c_gaps(Amount_of_gaps, 10) :- Amount_of_gaps > 3.\n");
        fw.write("classroom_fillness(0, 10, 10).\n");

        // Добавление типов занятий
        fw.write("type_of_class('pr').\n");
        fw.write("type_of_class('lec').\n");
        fw.write("type_of_class('lab').\n");
        fw.write("type_of_class('pe').\n");
        fw.write("type_of_class('misc').\n");

        // Добавлен типов аудиторий
        // Пока что служебные параметры (зависят от внедрения Матвея)
        fw.write("type_of_classroom('huge for lectures and practices', [type_of_class('lec'), type_of_class('pr')], 200).\n");
        fw.write("type_of_classroom('big for lectures and practices', [type_of_class('lec'), type_of_class('pr')], 80).\n");
        fw.write("type_of_classroom('medium for lectures and practices', [type_of_class('lec'), type_of_class('pr')], 40).\n");
        fw.write("type_of_classroom('small for lectures and practices', [type_of_class('lec'), type_of_class('pr')], 20).\n");
        fw.write("type_of_classroom('terminals', [type_of_class('pr'), type_of_class('lab')], 20).\n");
        fw.write("type_of_classroom('room for pe', [type_of_class('pe')], 500).\n");

        DatabaseManager manager = DatabaseManager.getInstance();
        manager.deleteTeacher(new Teacher("Vaskevich", "", "", "", ""));

        // Добавление аудиторий
        ArrayList<Auditory> auditories = (ArrayList<Auditory>) dm.getAuditories();
        for (Auditory auditory : auditories) {
            if (auditory.number.equals("")) {
                continue;
            }
            fw.write("classroom(".
                    concat("'").concat(auditory.number).concat("'").
                    concat(", ").
                    concat(buildPrologList((ArrayList<String>) dm.getAuditoryTypes(auditory.number), true,
                            "type_of_class(", ")").
                            concat(", ").
                            concat(auditory.capacity).
                            concat(").\n")));
        }

        // Добавление факультетов
        ArrayList<Faculty> faculties = (ArrayList<Faculty>) dm.getAllFaculties();
        for (Faculty faculty : faculties) {
            fw.write("faculty(".
                    concat("'").concat(faculty.name).concat("'").
                    concat(").\n"));
        }

        // Добавление программ образований
        for (Faculty faculty : faculties) {
            ArrayList<EducationalProgram> educationalPrograms = (ArrayList<EducationalProgram>) dm.getEducationalPrograms(faculty.name);
            Set<String> educationalProgramsNames = new HashSet<String>();
            for (EducationalProgram educationalProgram : educationalPrograms) {
                educationalProgramsNames.add(educationalProgram.name);
            }
            for (EducationalProgram educationalProgram : educationalPrograms) {
                if (educationalProgramsNames.contains(educationalProgram.name)) {
                    fw.write("ed_program(".
                            concat("'").concat(educationalProgram.faculty).concat("'").
                            concat(", ").
                            concat("'").concat(educationalProgram.name).concat("'").
                            concat(").\n"));
                    educationalProgramsNames.remove(educationalProgram.name);
                }
            }
        }

        // Добавление специализаций
        for (Faculty faculty : faculties) {
            ArrayList<EducationalProgram> educationalPrograms = (ArrayList<EducationalProgram>) dm.getEducationalPrograms(faculty.name);
            for (EducationalProgram educationalProgram : educationalPrograms) {
                fw.write("specialization(".
                        concat("'").concat(educationalProgram.name).concat("'").
                        concat(", ").
                        concat("'").concat(educationalProgram.specialization).concat("'").
                        concat(").\n"));
            }
        }

        // Добавление учителей
        ArrayList<Teacher> teachers = (ArrayList<Teacher>) dm.getAllTeachers();
        for (Teacher teacher : teachers) {
            fw.write("teacher(".
                    concat("'").concat(teacher.name).concat("'").
                    concat(").\n"));
        }

        // Добавление групп студентов
        for (Faculty faculty : faculties) {
            ArrayList<EducationalProgram> educationalPrograms = (ArrayList<EducationalProgram>) dm.getEducationalPrograms(faculty.name);
            for (EducationalProgram educationalProgram : educationalPrograms) {
                ArrayList<Group> groups = (ArrayList<Group>) dm.getGroups(educationalProgram.specialization);
                for (Group group : groups) {
                    fw.write("group_of_students(".
                            concat("'").concat(group.specialization).concat("'").
                            concat(",").
                            concat("'").concat(group.numberOfGroup).concat("'").
                            concat(",").
                            concat(group.amountOfStudents).
                            concat(",").
                            concat(group.yearOfStudy).
                            concat(").\n"));
                }
            }
        }

        // Добавление списка групп студентов
        for (Faculty faculty : faculties) {
            ArrayList<EducationalProgram> educationalPrograms = (ArrayList<EducationalProgram>)
                    dm.getEducationalPrograms(faculty.name);
            for (EducationalProgram educationalProgram : educationalPrograms) {
                Map<Integer, List<String>> allSpecializationGroups =
                        dm.getAllSpecializationGroups(educationalProgram.specialization);
                for (int year : allSpecializationGroups.keySet()) {
                    fw.write("list_groups_of_students(".
                            concat("'").concat(educationalProgram.specialization).concat("'").
                            concat(",").
                            concat(String.valueOf(year)).
                            concat(",").
                            concat(buildPrologList((ArrayList<String>) allSpecializationGroups.get(year),
                                    true, "", "")).
                            concat(").\n"));
                }
            }
        }

        // Это временная мера, поскольку на данный момент БД не умеет в иерархию дубликатов предметов. Зависит от Матвея
        // Как БД будет исправлена, тотчас будет реализован эффективный алгоритм. Клянёмся!!!!
        // Добавление предмета
        for (Faculty faculty : faculties) {
            ArrayList<EducationalProgram> educationalPrograms = (ArrayList<EducationalProgram>)
                    dm.getEducationalPrograms(faculty.name);

            for (EducationalProgram educationalProgram : educationalPrograms) {
                List<String> subjectNames = dm.getSubjectNames(educationalProgram.specialization);
                for (String subjectName : subjectNames) {
                    List<String> allSemestersOfSubject = dm.getSemestersOfSubject(educationalProgram.specialization,
                            subjectName);
                    for (String semestersOfSubject : allSemestersOfSubject) {
                        List<String> typesOfClass = dm.getTypesOfClasses(educationalProgram.specialization,
                                subjectName, semestersOfSubject);
                        fw.write("subject(".
                                concat("'").concat(educationalProgram.specialization).concat("'").
                                concat(",").
                                concat("'").concat(subjectName).concat("'").
                                concat(",").
                                concat("[").concat(semestersOfSubject).concat("]").
                                concat(",").
                                concat("["));
                        for (int i = 0; i < typesOfClass.size(); i++) {
                            List<Subject> subjects = dm.getSubjectsDuplicates(educationalProgram.specialization,
                                    subjectName, semestersOfSubject, typesOfClass.get(i));

                            fw.write("[type_of_class(".
                                    concat("'").concat(typesOfClass.get(i)).concat("'").concat(")").
                                    concat(",").
                                    concat(subjects.get(0).frequency).
                                    concat(",").
                                    concat("["));

                            for (int j = 0; j < subjects.size(); j++) {
                                fw.write("[".
                                        concat("teacher(").
                                        concat("'").concat(subjects.get(j).teacher).concat("'").
                                        concat("),").
                                        concat(subjects.get(j).amountOfGroups).
                                        concat("]"));
                                if (j < subjects.size() - 1) {
                                    fw.write(",");
                                }
                            }

                            fw.write("]]");

                            if (i < typesOfClass.size() - 1) {
                                fw.write(",");
                            }
                        }

                        fw.write("]).\n");
                    }
                }
            }
        }

        // Добавление дней, когда преподователь МОЖЕТ работать
        for (Teacher teacher : teachers) {
            fw.write("days_teacher_can_work(".
                    concat("teacher('").concat(teacher.name).concat("')").
                    concat(",").
                    concat(teacher.daysTeacherCanWork).
                    concat(").\n"));
        }

        // Добавление дней, когда преподователь ХОЧЕТ работать
        for (Teacher teacher : teachers) {
            fw.write("days_teacher_want_work(".
                    concat("teacher('").concat(teacher.name).concat("')").
                    concat(",").
                    concat(teacher.daysTeacherWantWork).
                    concat(",").
                    concat(teacher.weight).
                    concat(").\n"));
        }

        fw.close();
    }

    public static String buildPrologList(ArrayList<String> elements, boolean brackets, String prefix, String postfix) {
        String res = "[";
        for (int i = 0; i < elements.size(); i++) {
            res = res.concat(prefix);
            if (brackets) {
                res = res.concat("'");
            }
            res = res.concat(elements.get(i));
            if (brackets) {
                res = res.concat("'");
            }
            res = res.concat(postfix);
            if (i < elements.size() - 1) {
                res = res.concat(", ");
            }
        }
        res = res.concat("]");

        return res;
    }

    public static String buildPrologList(String element, boolean brackets, String prefix, String postfix) {
        String[] elements = element.split(" ");
        String res = "[";
        for (int i = 0; i < elements.length; i++) {
            res = res.concat(prefix);
            if (brackets) {
                res = res.concat("'");
            }
            res = res.concat(elements[i]);
            if (brackets) {
                res = res.concat("'");
            }
            res = res.concat(postfix);
            if (i < elements.length - 1) {
                res = res.concat(", ");
            }
        }
        res = res.concat("]");

        return res;
    }

    private static boolean isEq(String a, String b) {
        return Objects.equals(a, b);
    }

    private static boolean isMatch(String sym, String str) {
        return str.contains(sym);
    }

    public static List<GeneratedEntity> getGeneratedEntities(String timetableTerm) {
        List<GeneratedEntity> entities = new ArrayList<>();
        String[] term = timetableTerm.split("");
        for (int i = 0; i < term.length; i++) {
            if (i + 3 < term.length && isEq(term[i], ".") && isEq(term[i + 1], "(") && isEq(term[i + 2], "e")) {
                // Читаем ивент
                while(isMatch(term[i], ".(event(class(")) {
                    i++;
                }
                String specialization = "";
                while(!isEq(term[i], ",")) {
                    specialization = specialization.concat(term[i]);
                    i++;
                }
                i+=2;
                String subject = "";
                while (!isEq(term[i], ",")) {
                    subject = subject.concat(term[i]);
                    i++;
                }
                i++;
                while (!isEq(term[i], ",")) {
                    i++;
                }
                i+=2;
                while(isMatch(term[i], "type_of_class")) {
                    i++;
                }
                i++;
                String typeOfClass = "";
                while (!isEq(term[i], ")")) {
                    typeOfClass = typeOfClass.concat(term[i]);
                    i++;
                }
                while(isMatch(term[i], "), teacher")) {
                    i++;
                }
                i++;
                String teacher = "";
                while (!isEq(term[i], ")")) {
                    teacher = teacher.concat(term[i]);
                    i++;
                }
                i++;
                while(!isMatch(term[i], ")")) {
                    i++;
                }
                i+=2;
                String auditory = "";
                while (!isEq(term[i], ",")) {
                    auditory = auditory.concat(term[i]);
                    i++;
                }
                i+= 2;
                String day = term[i];
                i++;
                while(isMatch(term[i], ", .(")) {
                    i++;
                }
                String groups = "";
                while (!isEq(term[i], "[")) {
                    groups = groups.concat(term[i]);
                    i++;
                }
                i++;
                while(isMatch(term[i], "]), ")) {
                    i++;
                }
                String numberOfClass = term[i];

                GeneratedEntity entity = new GeneratedEntity(specialization, day, subject,
                        teacher, auditory, groups, numberOfClass, typeOfClass);
                entities.add(entity);
            }
            i++;
        }
        return entities;
    }

    public static List<GeneratedEntity> generate() throws IOException, SQLException, InterruptedException {
        Projog projog = new Projog();

        File main = new File("main_empty.pl");
        File main_temp = new File("main_mod.pl");
        copyFile(main, main_temp);

        prepare_prolog(main_temp);

        projog.consultFile(main_temp);

        Term timetable = null;

        QueryResult result = projog.executeQuery("main(1, Res, Fine).");
        while (result.next()) {
            Term res = result.getTerm("Res");
            if(Objects.equals(res.toString(), "[]")) {
                //System.out.println("error");
            } else {
                //System.out.println(res.toString());
            }
            timetable = res;
        }
        main_temp.delete();
        assert timetable != null;
        String t = timetable.toString();
        System.out.println(t);
        projog = null;
        timetable = null;
        //List<GeneratedEntity> entities = null;
        List<GeneratedEntity> entities = TimtableGenerator.getGeneratedEntities(t);
        for (GeneratedEntity entity: entities) {
            System.out.println("---------------------");
            System.out.println(entity.specialization);
            System.out.println(entity.subjectName);
            System.out.println(entity.typeOfClass);
            System.out.println(entity.teacherName);
            System.out.println(entity.auditory);
            System.out.println(entity.day);
            System.out.println(entity.groups);
            System.out.println(entity.numberOfClass);
        }
        return entities;
    }
}
