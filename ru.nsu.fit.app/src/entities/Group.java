package entities;

public class Group {
    public String educationalProgram;
    public String numberOfGroup;
    public String amountOfStudents;
    public String yearOfStudy;

    public Group(String educationalProgram, String numberOfGroup,
                 String amountOfStudents, String yearOfStudy) {
        this.educationalProgram = educationalProgram;
        this.numberOfGroup = numberOfGroup;
        this.amountOfStudents = amountOfStudents;
        this.yearOfStudy = yearOfStudy;
    }
}
