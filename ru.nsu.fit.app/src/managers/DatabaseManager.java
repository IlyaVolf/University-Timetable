package managers;

import entities.*;
import org.sqlite.JDBC;

import java.sql.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class DatabaseManager {
    private static final String DB = "jdbc:sqlite:timetable.sqlite";

    private static DatabaseManager instance = null;

    public static synchronized DatabaseManager getInstance() throws SQLException {
        if(instance == null) {
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
            statement.setObject(1, group.educationalProgram);
            statement.setObject(2, group.numberOfGroup);
            statement.setObject(3, group.amountOfStudents);
            statement.setObject(4, group.yearOfStudy);
            statement.execute();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
    public List<Group> getGroups(String educationalProgram) {
        try (PreparedStatement statement = this.connection.prepareStatement(
                "SELECT Number, AmountOfStudents, YearOfStudy FROM Groups WHERE EducationalProgram = ?")) {
            statement.setObject(1, educationalProgram);
            List<Group> groups = new ArrayList<>();
            ResultSet resultSet = statement.executeQuery();
            while (resultSet.next()) {
                groups.add(new Group(educationalProgram, resultSet.getString("Number"),
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
    public List<Subject> getSubjects(String educationalProgram) {
        try (PreparedStatement statement = this.connection.prepareStatement(
                "SELECT Name, Semesters, TypeOfClass, Frequency, Teacher, AmountOfGroups FROM Subjects WHERE EducationalProgram = ?")) {
            statement.setObject(1, educationalProgram);
            List<Subject> subjects = new ArrayList<>();
            ResultSet resultSet = statement.executeQuery();
            while (resultSet.next()) {
                subjects.add(new Subject(educationalProgram, resultSet.getString("Name"),
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
}