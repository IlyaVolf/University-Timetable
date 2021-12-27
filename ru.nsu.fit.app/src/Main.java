import entities.*;
import managers.DatabaseManager;
import org.projog.api.Projog;
import org.projog.api.QueryResult;
import org.projog.core.term.Term;

import java.io.*;
import java.nio.ByteBuffer;
import java.nio.channels.FileChannel;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

import static java.nio.charset.StandardCharsets.UTF_8;


public class Main {
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
        fw.write("attempts(1)");

        // Текущий семестр
        fw.write("semester(1)");

        // Добавление ограничений
        Constraints constraints = dm.getConstraints();
        fw.write("study_days_in_week(".concat(constraints.studyDaysInWeek).concat(").\n"));
        fw.write("study_days_in_week_students(".concat(constraints.studyDaysInWeekForStudents).concat(").\n"));
        fw.write("study_days_in_week_teachers(".concat(constraints.studyDaysInWeekForTeachers).concat(").\n"));
        fw.write("classes_in_day(".concat(constraints.classesPerDay).concat(").\n"));
        fw.write("classes_in_day_students(".concat(constraints.classesPerDayStudents).concat(").\n"));
        fw.write("classes_in_day_teachers(".concat(constraints.classesPerDayTeachers).concat(").\n"));

        // Добавление типов занятий
        fw.write("type_of_class('pr').");
        fw.write("type_of_class('lec').");
        fw.write("type_of_class('lab').");
        fw.write("type_of_class('misc').");

        // Добавлен типов аудиторий
        fw.write("type_of_classroom('huge for lectures and practices', [type_of_class('lec'), type_of_class('pr')], 200).");
        fw.write("type_of_classroom('big for lectures and practices', [type_of_class('lec'), type_of_class('pr')], 80).");
        fw.write("type_of_classroom('medium for lectures and practices', [type_of_class('lec'), type_of_class('pr')], 40).");
        fw.write("type_of_classroom('small for lectures and practices', [type_of_class('lec'), type_of_class('pr')], 20).");
        fw.write("type_of_classroom('terminals', [type_of_class('pr'), type_of_class('lab')], 20).");
        fw.write("type_of_classroom('room for pe', [type_of_class('pe')], 500).");

        // Добавление аудиторий
        ArrayList<Auditory> auditories = (ArrayList<Auditory>) dm.getAuditories();
        /*for (int i = 0; i < auditories.size(); i++) {
            fw.write("classroom(".
                    concat("'").concat(auditories.get(i).number).concat("'").
                    concat(", ");
                    concat(buildPrologList(auditories.get(i).typesOfClass, true)).
                    concat(", ");
                    concat(auditories.get(i).capacity).
                    concat(").\n"));
        }*/

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
            for (EducationalProgram educationalProgram : educationalPrograms) {
                fw.write("ed_program(".
                        concat("'").concat(educationalProgram.faculty).concat("'").
                        concat(", ").
                        concat("'").concat(educationalProgram.name).concat("'").
                        concat(").\n"));
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
        /*ArrayList<Teacher> teachers = (ArrayList<Teacher>) dm.getTeachers();
        for (Teacher teacher : teachers) {
            fw.write("specialization(".
                    concat("'").concat(teacher.name).concat("'").
                    concat(").\n"));
        }*/

        // Добавление групп студентов
        /*for (Faculty faculty : faculties) {
            ArrayList<EducationalProgram> educationalPrograms = (ArrayList<EducationalProgram>) dm.getEducationalPrograms(faculty.name);
            for (EducationalProgram educationalProgram : educationalPrograms) {
                ArrayList<Group> groups = (ArrayList<Group>) dm.getGroups(educationalProgram.specialization);
                for (Group group : groups) {
                    fw.write("group(".
                            concat("'").concat(group.specialization).concat("'").
                            concat(",").
                            concat("'").concat(group.numberOfGroup).concat("'").
                            concat(",").
                            concat(group.amountOfStudents).
                            concat(",").
                            concat(group.yearOfStudy).
                            concat(").\n"));
                }
            }*/

        // Добавление списка групп студентов
        /*for (Faculty faculty : faculties) {
            ArrayList<EducationalProgram> educationalPrograms = (ArrayList<EducationalProgram>) dm.getEducationalPrograms(faculty.name);
            for (EducationalProgram educationalProgram : educationalPrograms) {
                ArrayList<Group> groups = (ArrayList<Group>) dm.getGroups(educationalProgram.specialization);
                fw.write("list_groups_of_students(".
                        concat("'").concat(educationalProgram.specialization).concat("'").
                        concat(",").
                        concat(group.yearOfStudy).
                        concat(",").
                        concat(",").
                ДОДЕЛАТЬ
                }
            }*/

        // Добавление предмета

            fw.close();
        }

        public static String buildPrologList (ArrayList < String > elements,boolean brackets){
            String res = "[";
            for (int i = 0; i < elements.size(); i++) {
                if (brackets) {
                    res = res.concat("'");
                }
                res = res.concat(elements.get(i));
                if (brackets) {
                    res = res.concat("'");
                }
                if (i < elements.size() - 1) {
                    res = res.concat(", ");
                }
            }
            res = res.concat("]");

            return res;
        }

        public static void main (String[]args) throws IOException, SQLException {
            Projog projog = new Projog();

            File main = new File("main_j.pl");
            // File main_temp = File.createTempFile("main_mod", ".pl");
            File main_temp = new File("main_temp.pl");
            //main_temp.createNewFile();
            copyFile(main, main_temp);

            prepare_prolog(main_temp);


            projog.consultFile(main);

            QueryResult result = projog.executeQuery("main(1, Res).");
            while (result.next()) {
                Term res = result.getTerm("Res");
                System.out.println(res);
            }

        }
    }
