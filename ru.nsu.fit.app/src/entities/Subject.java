package entities;

import java.util.List;

public class Subject {
    public String educationalProgram;
    public String subjectName;
    public String semesters;
    public String typeOfClass;
    public String frequency;
    public String teacher;
    public String amountOfGroups;
    public List<Teacher> teachers;

    public Subject(String educationalProgram, String subjectName,
                   String semesters, String typeOfClass, String frequency,
                   String teacher, String amountOfGroups) {
        this.educationalProgram = educationalProgram;
        this.subjectName = subjectName;
        this.semesters = semesters;
        this.typeOfClass = typeOfClass;
        this.frequency = frequency;
        this.teacher = teacher;
        this.amountOfGroups = amountOfGroups;
    }
}
