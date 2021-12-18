package entities;

import java.util.List;

public class Teacher {
    public String subject;
    public String name;
    public String daysTeacherCanWork; // List<Integer>
    public String daysTeacherWantWork; // List<Integer>
    public String weight; // int

    public Teacher(String subject, String name, String daysTeacherCanWork,
                   String daysTeacherWantWork, String weight) {
        this.subject = subject;
        this.name = name;
        this.daysTeacherCanWork = daysTeacherCanWork;
        this.daysTeacherWantWork = daysTeacherWantWork;
        this.weight = weight;
    }
}
