package entities;

import java.util.List;

public class Faculty {
    public String name;
    List<EducationalProgram> educationalProgramList;

    public Faculty(String name) {
        this.name = name;
    }
}
