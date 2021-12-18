package entities;

import java.util.List;

public class EducationalProgram {
    public String faculty;
    public String name;
    public String specialization;
    List<Subject> subjects;
    List<Group> groups;

    public EducationalProgram(String faculty, String name, String specialization) {
        this.faculty = faculty;
        this.name = name;
        this.specialization = specialization;
    }
}
