package entities;

public class Group {
    public String specialization;
    public String numberOfGroup;
    public String amountOfStudents;
    public String yearOfStudy;

    public Group(String specialization, String numberOfGroup,
                 String amountOfStudents, String yearOfStudy) {
        this.specialization = specialization;
        this.numberOfGroup = numberOfGroup;
        this.amountOfStudents = amountOfStudents;
        this.yearOfStudy = yearOfStudy;
    }
}
