package managers;

import entities.*;
import org.sqlite.JDBC;

import java.sql.*;
import java.util.*;
import java.util.stream.Collectors;

public class DatabaseManager {
    private static final String DB = "jdbc:sqlite:timetable.sqlite";

    private static DatabaseManager instance = null;

    public static synchronized DatabaseManager getInstance() throws SQLException {
        if (instance == null) {
            instance = new DatabaseManager();
        }
        return instance;
    }

    private Connection connection;

    private DatabaseManager() throws SQLException {
        DriverManager.registerDriver(new JDBC());
        this.connection = DriverManager.getConnection(DB);
    }

    public void addFaculty(Faculty faculty) {
        try (PreparedStatement statement = this.connection.prepareStatement(
                "INSERT INTO Faculties(`Faculty`)" +
                        "VALUES(?)")) {
            statement.setObject(1, faculty.name);
            statement.execute();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public List<Faculty> getAllFaculties() {
        try (Statement statement = this.connection.createStatement()) {
            List<Faculty> faculties = new ArrayList<>();
            ResultSet resultSet = statement.executeQuery("SELECT Faculty FROM Faculties");
            while (resultSet.next()) {
                faculties.add(new Faculty(resultSet.getString("Faculty")));
            }
            return faculties;
        } catch (SQLException e) {
            e.printStackTrace();
            return Collections.emptyList();
        }
    }

    public void deleteFaculty(String name) {
        try (PreparedStatement statement = this.connection.prepareStatement(
                "DELETE FROM Faculties WHERE Faculty = ?")) {
            statement.setObject(1, name);
            statement.execute();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void addEducationalProgram(EducationalProgram educationalProgram) {
        try (PreparedStatement statement = this.connection.prepareStatement(
                "INSERT INTO EducationalPrograms(`Faculty`, `EducationalProgram`, `Specialization`)" +
                        "VALUES(?, ?, ?)")) {
            statement.setObject(1, educationalProgram.faculty);
            statement.setObject(2, educationalProgram.name);
            statement.setObject(3, educationalProgram.specialization);
            statement.execute();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public List<EducationalProgram> getEducationalPrograms(String faculty) {
        try (PreparedStatement statement = this.connection.prepareStatement(
                "SELECT EducationalProgram, Specialization FROM EducationalPrograms WHERE Faculty = ?")) {
            statement.setObject(1, faculty);
            List<EducationalProgram> educationalPrograms = new ArrayList<>();
            ResultSet resultSet = statement.executeQuery();
            while (resultSet.next()) {
                educationalPrograms.add(new EducationalProgram(faculty, resultSet.getString("EducationalProgram"),
                        resultSet.getString("Specialization")));
            }
            return educationalPrograms;
        } catch (SQLException e) {
            e.printStackTrace();
            return Collections.emptyList();
        }
    }

    public void addGroup(Group group) {
        try (PreparedStatement statement = this.connection.prepareStatement(
                "INSERT INTO Groups(`EducationalProgram`, `Number`, `AmountOfStudents`, `YearOfStudy`)" +
                        "VALUES(?, ?, ?, ?)")) {
            statement.setObject(1, group.specialization);
            statement.setObject(2, group.numberOfGroup);
            statement.setObject(3, group.amountOfStudents);
            statement.setObject(4, group.yearOfStudy);
            statement.execute();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public List<Group> getGroups(String specialization) {
        try (PreparedStatement statement = this.connection.prepareStatement(
                "SELECT Number, AmountOfStudents, YearOfStudy FROM Groups WHERE EducationalProgram = ?")) {
            statement.setObject(1, specialization);
            List<Group> groups = new ArrayList<>();
            ResultSet resultSet = statement.executeQuery();
            while (resultSet.next()) {
                groups.add(new Group(specialization, resultSet.getString("Number"),
                        resultSet.getString("AmountOfStudents"), resultSet.getString("YearOfStudy")));
            }
            return groups;
        } catch (SQLException e) {
            e.printStackTrace();
            return Collections.emptyList();
        }
    }

    public void addSubject(Subject subject) {
        try (PreparedStatement statement = this.connection.prepareStatement(
                "INSERT INTO Subjects(`EducationalProgram`, `Name`, `Semesters`, `TypeOfClass`, `Frequency`, `teacher`, `AmountOfGroups`)" +
                        "VALUES(?, ?, ?, ?, ?, ?, ?)")) {
            statement.setObject(1, subject.educationalProgram);
            statement.setObject(2, subject.subjectName);
            statement.setObject(3, subject.semesters);
            statement.setObject(4, subject.typeOfClass);
            statement.setObject(5, subject.frequency);
            statement.setObject(6, subject.teacher);
            statement.setObject(7, subject.amountOfGroups);
            statement.execute();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void updateSubject(String specialization, String subject, String teacher,
                              String semesters, String types, String frequency, String amountOfGroups) {
        try {
            PreparedStatement statement = this.connection.prepareStatement(
                    "UPDATE Subjects SET Teacher = ? WHERE EducationalProgram = ? AND Name = ? AND Semesters = ? AND TypeOfClass = ? AND Frequency = ? AND AmountOfGroups = ?");
            statement.setObject(1, teacher);
            statement.setObject(2, specialization);
            statement.setObject(3, subject);
            statement.setObject(4, semesters);
            statement.setObject(5, types);
            statement.setObject(6, frequency);
            statement.setObject(7, amountOfGroups);
            statement.execute();

            /*PreparedStatement statement1 = this.connection.prepareStatement(
                    "UPDATE Teachers SET Subject = ? WHERE Name = ?");
            statement1.setObject(1, subject);
            statement1.setObject(2, teacher);
            statement1.execute();*/
        } catch (SQLException e) {
            e.printStackTrace();
            System.out.println("Exception in update");
        }
    }

    public List<Subject> getSubjects(String specialization) {
        try (PreparedStatement statement = this.connection.prepareStatement(
                "SELECT Name, Semesters, TypeOfClass, Frequency, Teacher, AmountOfGroups FROM Subjects WHERE EducationalProgram = ?")) {
            statement.setObject(1, specialization);
            List<Subject> subjects = new ArrayList<>();
            ResultSet resultSet = statement.executeQuery();
            while (resultSet.next()) {
                subjects.add(new Subject(specialization, resultSet.getString("Name"),
                        resultSet.getString("Semesters"), resultSet.getString("TypeOfClass"),
                        resultSet.getString("Frequency"), resultSet.getString("teacher"),
                        resultSet.getString("AmountOfGroups")));
            }
            return subjects;
        } catch (SQLException e) {
            e.printStackTrace();
            return Collections.emptyList();
        }
    }

    public List<String> getSubjectNames(String specialization) {
        try {
            PreparedStatement statement = this.connection.prepareStatement(
                    "SELECT DISTINCT Name FROM Subjects WHERE EducationalProgram = ?");
            statement.setObject(1, specialization);
            List<String> names = new ArrayList<>();
            ResultSet resultSet = statement.executeQuery();
            while (resultSet.next()) {
                names.add(resultSet.getString("Name"));
            }
            return names;
        } catch (SQLException e) {
            return null;
        }
    }

    public List<String> getSemestersOfSubject(String specialization, String subject) {
        try {
            PreparedStatement statement = this.connection.prepareStatement(
                    "SELECT DISTINCT Semesters FROM Subjects WHERE EducationalProgram = ? AND Name = ?");
            statement.setObject(1, specialization);
            statement.setObject(2, subject);
            List<String> semesters = new ArrayList<>();
            ResultSet resultSet = statement.executeQuery();
            while (resultSet.next()) {
                semesters.add(resultSet.getString("Semesters"));
            }
            return semesters;
        } catch (SQLException e) {
            return null;
        }
    }

    public List<String> getTypesOfClasses(String specialization, String subject, String semesters) {
        try {
            PreparedStatement statement = this.connection.prepareStatement(
                    "SELECT DISTINCT TypeOfClass FROM Subjects WHERE EducationalProgram = ? AND Name = ? AND Semesters = ?");
            statement.setObject(1, specialization);
            statement.setObject(2, subject);
            statement.setObject(3, semesters);
            List<String> types = new ArrayList<>();
            ResultSet resultSet = statement.executeQuery();
            while (resultSet.next()) {
                types.add(resultSet.getString("TypeOfClass"));
            }
            return types;
        } catch (SQLException e) {
            return null;
        }
    }

    public List<Subject> getSubjectsDuplicates(String specialization, String subjectName, String semesters, String typesOfClass) {
        try {
            PreparedStatement statement = this.connection.prepareStatement(
                    "SELECT Frequency, Teacher, AmountOfGroups FROM Subjects WHERE EducationalProgram = ? AND Name = ? AND Semesters = ? AND TypeOfClass = ?");
            statement.setObject(1, specialization);
            statement.setObject(2, subjectName);
            statement.setObject(3, semesters);
            statement.setObject(4, typesOfClass);
            List<Subject> subjects = new ArrayList<>();
            ResultSet resultSet = statement.executeQuery();
            while (resultSet.next()) {
                subjects.add(new Subject(specialization, subjectName, semesters,
                        typesOfClass, resultSet.getString("Frequency"),
                        resultSet.getString("Teacher"), resultSet.getString("AmountOfGroups")));
            }
            return subjects;
        } catch (SQLException e) {
            return null;
        }
    }

    public void addTeacher(Teacher teacher) {
        try (PreparedStatement statement = this.connection.prepareStatement(
                "INSERT INTO Teachers(`Subject`, `Name`, `DaysCanWork`, `DaysWantWork`, `Weight`)" +
                        "VALUES(?, ?, ?, ?, ?)")) {
            statement.setObject(1, teacher.subject);
            statement.setObject(2, teacher.name);
            statement.setObject(3, teacher.daysTeacherCanWork);
            statement.setObject(4, teacher.daysTeacherWantWork);
            statement.setObject(5, teacher.weight);
            statement.execute();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public List<Teacher> getTeachers(String subject) {
        try (PreparedStatement statement = this.connection.prepareStatement(
                "SELECT Subject, Name, DaysCanWork, DaysWantWork, Weight FROM Teachers WHERE Subject = ?")) {
            statement.setObject(1, subject);
            List<Teacher> teachers = new ArrayList<>();
            ResultSet resultSet = statement.executeQuery();
            while (resultSet.next()) {
                teachers.add(new Teacher(subject, resultSet.getString("Name"),
                        resultSet.getString("DaysCanWork"), resultSet.getString("DaysWantWork"),
                        resultSet.getString("Weight")));
            }
            return teachers;
        } catch (SQLException e) {
            e.printStackTrace();
            return Collections.emptyList();
        }
    }

    public String getTeacherName(String specialization, String subject) {
        //System.out.println("In method: spec = " + specialization + " subject = " + subject);
        try (PreparedStatement statement = this.connection.prepareStatement(
                "SELECT Teacher FROM Subjects WHERE EducationalProgram = ? AND Name = ?")) {
            statement.setObject(1, specialization);
            statement.setObject(2, subject);
            ResultSet resultSet = statement.executeQuery();
            return resultSet.getString("Teacher");

        } catch (SQLException e) {
            return "Exception";
        }
    }

    public List<Teacher> getAllTeachers() {
        try (Statement statement = this.connection.createStatement()) {
            List<Teacher> teachers = new ArrayList<>();
            ResultSet resultSet = statement.executeQuery("SELECT * FROM Teachers");
            while (resultSet.next()) {
                teachers.add(new Teacher(resultSet.getString("Subject"),
                        resultSet.getString("Name"),
                        resultSet.getString("DaysCanWork"),
                        resultSet.getString("DaysWantWork"),
                        resultSet.getString("Weight")));
            }
            return teachers;
        } catch (SQLException e) {
            e.printStackTrace();
            return Collections.emptyList();
        }
    }

    public void addAuditory(Auditory auditory) {
        try (PreparedStatement statement = this.connection.prepareStatement(
                "INSERT INTO Auditories(`TypeOfClass`, `Capacity`, `Number`)" +
                        "VALUES(?, ?, ?)")) {
            statement.setObject(1, auditory.typesOfClass);
            statement.setObject(2, auditory.capacity);
            statement.setObject(3, auditory.number);
            statement.execute();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public List<Auditory> getAuditories() {
        try (PreparedStatement statement = this.connection.prepareStatement(
                "SELECT TypeOfClass, Capacity, Number FROM Auditories")) {
            List<Auditory> auditories = new ArrayList<>();
            ResultSet resultSet = statement.executeQuery();
            while (resultSet.next()) {
                auditories.add(new Auditory(resultSet.getString("TypeOfClass"),
                        resultSet.getString("Capacity"), resultSet.getString("Number")));
            }
            return auditories;
        } catch (SQLException e) {
            e.printStackTrace();
            return Collections.emptyList();
        }
    }

    public List<String> getAuditoryTypes(String auditoryNumber) {
        try {
            PreparedStatement statement = this.connection.prepareStatement(
                    "SELECT TypeOfClass FROM Auditories WHERE Number = ?");
            statement.setObject(1, auditoryNumber);
            String result = statement.executeQuery().getString("TypeOfClass");
            String[] types = result.replaceAll("\\s+", "").split(",");
            return Arrays.stream(types).collect(Collectors.toList());
        } catch (SQLException e) {
            e.printStackTrace();
            return Collections.emptyList();
        }
    }

    public Map<Integer, List<String>> getAllSpecializationGroups(String specialization) {
        try {
            PreparedStatement statement = this.connection.prepareStatement(
                    "SELECT Number, YearOfStudy FROM Groups WHERE EducationalProgram = ? ORDER BY YearOfStudy");
            statement.setObject(1, specialization);
            ResultSet resultSet = statement.executeQuery();
            Map<Integer, List<String>> groups = new HashMap<>();
            while (resultSet.next()) {
                int key = Integer.parseInt(resultSet.getString("YearOfStudy"));
                List<String> values = groups.get(key);
                if (values == null) {
                    values = new ArrayList<>();
                }
                values.add(resultSet.getString("Number"));
                groups.put(key, values);
            }
            for (Integer i : groups.keySet()) {
                List<String> v = groups.get(i);
            }
            return groups;
        } catch (SQLException e) {
            return null;
        }
    }

    public void addConstraints(Constraints constraints) {
        try (PreparedStatement statement = this.connection.prepareStatement(
                "INSERT INTO Constraints(`FirstClassStarts`, `ClassDuration`, `ShortBrakeDuration`, `LargeBrakeDuration`, `StudyDaysInWeek`, `StudyDaysInWeekForStudents`, `StudyDaysInWeekForTeachers`, `ClassesPerDay`, `ClassesPerDayStudents`, `ClassesPerDayTeachers`, `LunchBrake`, `Gaps`, `ClassroomFillness`)" +
                        "VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)")) {
            statement.setObject(1, constraints.firstClassStarts);
            statement.setObject(2, constraints.classDuration);
            statement.setObject(3, constraints.shortBrakeDuration);
            statement.setObject(4, constraints.largeBrakeDuration);
            statement.setObject(5, constraints.studyDaysInWeek);
            statement.setObject(6, constraints.studyDaysInWeekForStudents);
            statement.setObject(7, constraints.studyDaysInWeekForTeachers);
            statement.setObject(8, constraints.classesPerDay);
            statement.setObject(9, constraints.classesPerDayStudents);
            statement.setObject(10, constraints.classesPerDayTeachers);
            statement.setObject(11, constraints.lunchBrake);
            statement.setObject(12, constraints.gaps);
            statement.setObject(13, constraints.classroomFillness);
            statement.execute();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public Constraints getConstraints() {
        try (PreparedStatement statement = this.connection.prepareStatement(
                "SELECT FirstClassStarts, ClassDuration, ShortBrakeDuration, LargeBrakeDuration, StudyDaysInWeek, StudyDaysInWeekForStudents, StudyDaysInWeekForTeachers, ClassesPerDay, ClassesPerDayStudents, ClassesPerDayTeachers, LunchBrake, Gaps, ClassroomFillness FROM Constraints")) {
            Constraints constraints = new Constraints("", "", "",
                    "", "", "", "", "",
                    "", "", "", "", "");
            ResultSet resultSet = statement.executeQuery();
            while (resultSet.next()) {
                constraints = new Constraints(resultSet.getString("FirstClassStarts"),
                        resultSet.getString("ClassDuration"),
                        resultSet.getString("ShortBrakeDuration"),
                        resultSet.getString("LargeBrakeDuration"),
                        resultSet.getString("StudyDaysInWeek"),
                        resultSet.getString("StudyDaysInWeekForStudents"),
                        resultSet.getString("StudyDaysInWeekForTeachers"),
                        resultSet.getString("ClassesPerDay"),
                        resultSet.getString("ClassesPerDayStudents"),
                        resultSet.getString("ClassesPerDayTeachers"),
                        resultSet.getString("LunchBrake"),
                        resultSet.getString("Gaps"),
                        resultSet.getString("ClassroomFillness"));
            }
            if (constraints.classroomFillness == null) {
                constraints = new Constraints("", "", "",
                        "", "", "", "", "",
                        "", "", "", "", "");
            }
            return constraints;
        } catch (SQLException e) {
            e.printStackTrace();
            return null;
        }
    }

    public void deleteAuditory(Auditory auditory) {
        try (PreparedStatement statement = this.connection.prepareStatement(
                "DELETE FROM Auditories WHERE TypeOfClass = ? AND Capacity = ? AND Number = ?")) {
            statement.setObject(1, auditory.typesOfClass);
            statement.setObject(2, auditory.capacity);
            statement.setObject(3, auditory.number);
            statement.execute();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void deleteTeacher(Teacher teacher) {
        try (PreparedStatement statement = this.connection.prepareStatement(
                "DELETE FROM Teachers WHERE Name = ? AND DaysCanWork = ? AND DaysWantWork = ? AND Weight = ?")) {
            statement.setObject(1, teacher.name);
            statement.setObject(2, teacher.daysTeacherCanWork);
            statement.setObject(3, teacher.daysTeacherWantWork);
            statement.setObject(4, teacher.weight);
            statement.execute();

            PreparedStatement selectStatement = this.connection.prepareStatement(
                    "SELECT * FROM Subjects WHERE Teacher = ?");
            selectStatement.setObject(1, teacher.name);
            ResultSet resultSet = selectStatement.executeQuery();
            PreparedStatement deleteStatement = this.connection.prepareStatement(
                    "DELETE FROM Subjects WHERE Teacher = ?");
            deleteStatement.setObject(1, teacher.name);
            deleteStatement.execute();
            while (resultSet.next()) {
                addSubject(new Subject(resultSet.getString("EducationalProgram"),
                        resultSet.getString("Name"), resultSet.getString("Semesters"),
                        resultSet.getString("TypeOfClass"), resultSet.getString("Frequency"),
                        "Undefined", resultSet.getString("AmountOfGroups")));
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void deleteSubject(Subject subject) {
        try (PreparedStatement statement = this.connection.prepareStatement(
                "DELETE FROM Subjects WHERE EducationalProgram = ? AND Name = ? AND Semesters = ? AND TypeOfClass = ? AND Frequency = ? AND Teacher = ? AND AmountOfGroups = ?")) {
            statement.setObject(1, subject.educationalProgram);
            statement.setObject(2, subject.subjectName);
            statement.setObject(3, subject.semesters);
            statement.setObject(4, subject.typeOfClass);
            statement.setObject(5, subject.frequency);
            statement.setObject(6, subject.teacher);
            statement.setObject(7, subject.amountOfGroups);
            statement.execute();

            /*PreparedStatement statement1 = this.connection.prepareStatement(
                    "DELETE FROM Teachers WHERE Subject = ?");
            statement1.setObject(1, subject.subjectName);*/
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void deleteGroup(Group group) {
        try (PreparedStatement statement = this.connection.prepareStatement(
                "DELETE FROM Groups WHERE EducationalProgram = ? AND Number = ? AND AmountOfStudents = ? AND YearOfStudy = ?")) {
            statement.setObject(1, group.specialization);
            statement.setObject(2, group.numberOfGroup);
            statement.setObject(3, group.amountOfStudents);
            statement.setObject(4, group.yearOfStudy);
            statement.execute();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void deleteEducationalProgram(EducationalProgram educationalProgram) {
        try (PreparedStatement statement = this.connection.prepareStatement(
                "DELETE FROM EducationalPrograms WHERE Faculty = ? AND EducationalProgram = ? AND Specialization = ?")) {
            statement.setObject(1, educationalProgram.faculty);
            statement.setObject(2, educationalProgram.name);
            statement.setObject(3, educationalProgram.specialization);
            statement.execute();

            PreparedStatement statement1 = this.connection.prepareStatement(
                    "DELETE FROM Faculties WHERE EducationalProgram = ?");
            statement1.setObject(1, educationalProgram.name);

            PreparedStatement statement2 = this.connection.prepareStatement(
                    "DELETE FROM Groups WHERE EducationalProgram = ?");
            statement2.setObject(1, educationalProgram.name);

            PreparedStatement statement3 = this.connection.prepareStatement(
                    "DELETE FROM Subjects WHERE EducationalProgram = ?");
            statement3.setObject(1, educationalProgram.name);

            //TODO удалить всех учителей из удаленных предметов

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void clearAll() {
        try {
            this.connection.prepareStatement(
                    "DELETE FROM Auditories").execute();
            this.connection.prepareStatement(
                    "DELETE FROM Constraints").execute();
            this.connection.prepareStatement(
                    "DELETE FROM EducationalPrograms").execute();
            this.connection.prepareStatement(
                    "DELETE FROM Faculties").execute();
            this.connection.prepareStatement(
                    "DELETE FROM Groups").execute();
            this.connection.prepareStatement(
                    "DELETE FROM Subjects").execute();
            this.connection.prepareStatement(
                    "DELETE FROM Teachers").execute();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public void addTimetable(List<GeneratedEntity> entities) {
        try {
            for (GeneratedEntity entity : entities) {
                PreparedStatement statement = this.connection.prepareStatement("" +
                        "INSERT INTO GeneratedEntities(`Specialization`, `Day`, `Subject`, `Teacher`, `Auditory`, `Groups`, `NumberOfClass`, `TypeOfClass`) " +
                        "VALUES(?, ?, ?, ?, ?, ?, ?, ?)");
                statement.setObject(1, entity.specialization);
                statement.setObject(2, entity.day);
                statement.setObject(3, entity.subjectName);
                statement.setObject(4, entity.teacherName);
                statement.setObject(5, entity.auditory);
                statement.setObject(6, entity.groups);
                statement.setObject(7, entity.numberOfClass);
                statement.setObject(8, entity.typeOfClass);
                statement.execute();
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public List<String> getTimetableSpecializations() {
        try {

            PreparedStatement statement = this.connection.prepareStatement(
                    "SELECT DISTINCT Specialization FROM GeneratedEntities");
            ResultSet resultSet = statement.executeQuery();
            List<String> specializations = new ArrayList<>();
            while (resultSet.next()) {
                specializations.add(resultSet.getString("Specialization"));
            }
            return specializations;
        } catch (SQLException e) {
            e.printStackTrace();
            return null;
        }
    }

    public List<String> getEvents(String specialization) {
        try {
            PreparedStatement statement = this.connection.prepareStatement(
                    "SELECT Day, Subject, Teacher, Auditory, Groups , NumberOfClass, TypeOfClass FROM GeneratedEntities WHERE Specialization = ?");
            statement.setObject(1, specialization);
            ResultSet resultSet = statement.executeQuery();
            List<String> events = new ArrayList<>();
            while (resultSet.next()) {
                String day = resultSet.getString("Day");
                String subject = resultSet.getString("Subject");
                String teacher = resultSet.getString("Teacher");
                String auditory = resultSet.getString("Auditory");
                String groups = resultSet.getString("Groups");
                String numberOfClass = resultSet.getString("NumberOfClass");
                String typeOfClass = resultSet.getString("TypeOfClass");
                String[] splitted = groups.split("\\(");
                groups = "";
                for (String gr: splitted) {
                    groups = groups.concat(gr);
                }
                events.add(day.concat("   ").concat(subject).concat("   ")
                        .concat(teacher).concat("   ").concat(auditory)
                        .concat("   ").concat(groups).concat("   ").concat(numberOfClass).concat("   ")
                        .concat(typeOfClass));
            }
            return events;
        } catch (SQLException e) {
            e.printStackTrace();
            return null;
        }
    }
}