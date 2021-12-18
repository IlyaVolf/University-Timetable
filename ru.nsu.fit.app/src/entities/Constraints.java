package entities;

public class Constraints {
    public String firstClassStarts;
    public String classDuration;
    public String shortBrakeDuration;
    public String largeBrakeDuration;
    public String studyDaysInWeek;
    public String studyDaysInWeekForStudents;
    public String studyDaysInWeekForTeachers;
    public String classesPerDay;
    public String classesPerDayStudents;
    public String classesPerDayTeachers;

    public String lunchBrake;
    public String gaps;
    public String classroomFillness;

    public Constraints(String firstClassStarts, String classDuration, String shortBrakeDuration,
                       String largeBrakeDuration, String studyDaysInWeek, String studyDaysInWeekForStudents,
                       String studyDaysInWeekForTeachers, String classesPerDay, String classesPerDayStudents,
                       String classesPerDayTeachers, String lunchBrake, String gaps, String classroomFillness) {
        this.firstClassStarts = firstClassStarts;
        this.classDuration = classDuration;
        this.shortBrakeDuration = shortBrakeDuration;
        this.largeBrakeDuration = largeBrakeDuration;
        this.studyDaysInWeek = studyDaysInWeek;
        this.studyDaysInWeekForStudents = studyDaysInWeekForStudents;
        this.studyDaysInWeekForTeachers = studyDaysInWeekForTeachers;
        this.classesPerDay = classesPerDay;
        this.classesPerDayStudents = classesPerDayStudents;
        this.classesPerDayTeachers = classesPerDayTeachers;
        this.lunchBrake = lunchBrake;
        this.gaps = gaps;
        this.classroomFillness = classroomFillness;
    }
}
