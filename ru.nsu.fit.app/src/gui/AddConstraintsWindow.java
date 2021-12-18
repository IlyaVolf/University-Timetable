package gui;

import entities.Constraints;
import managers.DatabaseManager;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.SQLException;

public class AddConstraintsWindow {
    JFrame frame;
    JLabel label;
    JButton save;

    JTextField enterFirstClassStarts;
    JTextField enterClassDuration;
    JTextField enterShortBrakeDuration;
    JTextField enterLargeBrakeDuration;
    JTextField enterStudyDaysInWeek;
    JTextField enterStudyDaysInWeekForStudents;
    JTextField enterStudyDaysInWeekForTeachers;
    JTextField enterClassesPerDay;
    JTextField enterClassesPerDayStudents;
    JTextField enterClassesPerDayTeachers;

    JTextField enterLunchBrake;
    JTextField enterGaps;
    JTextField enterClassroomFillness;

    public AddConstraintsWindow() {
        this.frame = new JFrame("Add Constraints");
        frame.setExtendedState(JFrame.MAXIMIZED_BOTH);
        frame.setVisible(true);

        this.label = new JLabel("List of constraints");
        frame.add(this.label, BorderLayout.NORTH);

        JPanel allConstraintsPanel = new JPanel();
        allConstraintsPanel.setLayout(new GridLayout(13, 1));

        Constraints constraints = new Constraints("", "", "",
                "", "", "", "", "",
                "", "", "", "", "");
        try {
            DatabaseManager manager = DatabaseManager.getInstance();
            constraints = manager.getConstraints();
        } catch (SQLException e) {
            e.printStackTrace();
        }
        JPanel firstClassStartsPanel = new JPanel();
        JLabel firstClassStartsLabel = new JLabel("First class starts: ");
        this.enterFirstClassStarts = new JTextField(constraints.firstClassStarts, 37);
        firstClassStartsPanel.add(firstClassStartsLabel);
        firstClassStartsPanel.add(enterFirstClassStarts);
        allConstraintsPanel.add(firstClassStartsPanel);

        JPanel classDurationPanel = new JPanel();
        JLabel classDurationLabel = new JLabel("Class duration: ");
        this.enterClassDuration = new JTextField(constraints.classDuration, 37);
        classDurationPanel.add(classDurationLabel);
        classDurationPanel.add(enterClassDuration);
        allConstraintsPanel.add(classDurationPanel);

        JPanel shortBrakeDurationPanel = new JPanel();
        JLabel shortBrakeDurationLabel = new JLabel("Short brake duration: ");
        this.enterShortBrakeDuration = new JTextField(constraints.shortBrakeDuration, 37);
        shortBrakeDurationPanel.add(shortBrakeDurationLabel);
        shortBrakeDurationPanel.add(enterShortBrakeDuration);
        allConstraintsPanel.add(shortBrakeDurationPanel);

        JPanel largeBrakeDurationPanel = new JPanel();
        JLabel largeBrakeDurationLabel = new JLabel("Large brake duration: ");
        this.enterLargeBrakeDuration = new JTextField(constraints.largeBrakeDuration, 37);
        largeBrakeDurationPanel.add(largeBrakeDurationLabel);
        largeBrakeDurationPanel.add(enterLargeBrakeDuration);
        allConstraintsPanel.add(largeBrakeDurationPanel);

        JPanel studyDaysInWeekPanel = new JPanel();
        JLabel studyDaysInWeekLabel = new JLabel("Study days in week: ");
        this.enterStudyDaysInWeek = new JTextField(constraints.studyDaysInWeek, 37);
        studyDaysInWeekPanel.add(studyDaysInWeekLabel);
        studyDaysInWeekPanel.add(enterStudyDaysInWeek);
        allConstraintsPanel.add(studyDaysInWeekPanel);

        JPanel studyDaysInWeekForStudentsPanel = new JPanel();
        JLabel studyDaysInWeekForStudentsLabel = new JLabel("Study days in week for students: ");
        this.enterStudyDaysInWeekForStudents = new JTextField(constraints.studyDaysInWeekForStudents, 37);
        studyDaysInWeekForStudentsPanel.add(studyDaysInWeekForStudentsLabel);
        studyDaysInWeekForStudentsPanel.add(enterStudyDaysInWeekForStudents);
        allConstraintsPanel.add(studyDaysInWeekForStudentsPanel);

        JPanel studyDaysInWeekForTeachersPanel = new JPanel();
        JLabel studyDaysInWeekForTeachersLabel = new JLabel("Study days in week for teachers: ");
        this.enterStudyDaysInWeekForTeachers = new JTextField(constraints.studyDaysInWeekForTeachers, 37);
        studyDaysInWeekForTeachersPanel.add(studyDaysInWeekForTeachersLabel);
        studyDaysInWeekForTeachersPanel.add(enterStudyDaysInWeekForTeachers);
        allConstraintsPanel.add(studyDaysInWeekForTeachersPanel);

        JPanel classesPerDayPanel = new JPanel();
        JLabel classesPerDayLabel = new JLabel("Classes per day: ");
        this.enterClassesPerDay = new JTextField(constraints.classesPerDay, 37);
        classesPerDayPanel.add(classesPerDayLabel);
        classesPerDayPanel.add(enterClassesPerDay);
        allConstraintsPanel.add(classesPerDayPanel);

        JPanel classesPerDayStudentsPanel = new JPanel();
        JLabel classesPerDayStudentsLabel = new JLabel("Classes per day for students: ");
        this.enterClassesPerDayStudents = new JTextField(constraints.classesPerDayStudents, 37);
        classesPerDayStudentsPanel.add(classesPerDayStudentsLabel);
        classesPerDayStudentsPanel.add(enterClassesPerDayStudents);
        allConstraintsPanel.add(classesPerDayStudentsPanel);

        JPanel classesPerDayTeachersPanel = new JPanel();
        JLabel classesPerDayTeachersLabel = new JLabel("Classes per day for teachers: ");
        this.enterClassesPerDayTeachers = new JTextField(constraints.classesPerDayTeachers, 37);
        classesPerDayTeachersPanel.add(classesPerDayTeachersLabel);
        classesPerDayTeachersPanel.add(enterClassesPerDayTeachers);
        allConstraintsPanel.add(classesPerDayTeachersPanel);

        JPanel lunchBrakePanel = new JPanel();
        JLabel lunchBrakeLabel = new JLabel("Lunch brake: ");
        this.enterLunchBrake = new JTextField(constraints.lunchBrake, 37);
        lunchBrakePanel.add(lunchBrakeLabel);
        lunchBrakePanel.add(enterLunchBrake);
        allConstraintsPanel.add(lunchBrakePanel);

        JPanel gapsPanel = new JPanel();
        JLabel gapsLabel = new JLabel("Gaps: ");
        this.enterGaps = new JTextField(constraints.gaps, 37);
        gapsPanel.add(gapsLabel);
        gapsPanel.add(enterGaps);
        allConstraintsPanel.add(gapsPanel);

        JPanel classroomFillnessPanel = new JPanel();
        JLabel classroomFillnessLabel = new JLabel("Classroom fillness: ");
        this.enterClassroomFillness = new JTextField(constraints.classroomFillness, 37);
        classroomFillnessPanel.add(classroomFillnessLabel);
        classroomFillnessPanel.add(enterClassroomFillness);
        allConstraintsPanel.add(classroomFillnessPanel);

        frame.add(allConstraintsPanel, BorderLayout.WEST);

        this.save = new JButton("save");
        save.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    DatabaseManager manager = DatabaseManager.getInstance();
                    manager.addConstraints(new Constraints(enterFirstClassStarts.getText(),
                            enterClassDuration.getText(),
                            enterShortBrakeDuration.getText(),
                            enterLargeBrakeDuration.getText(),
                            enterStudyDaysInWeek.getText(),
                            enterStudyDaysInWeekForStudents.getText(),
                            enterStudyDaysInWeekForTeachers.getText(),
                            enterClassesPerDay.getText(),
                            enterClassesPerDayStudents.getText(),
                            enterClassesPerDayTeachers.getText(),
                            enterLunchBrake.getText(),
                            enterGaps.getText(),
                            enterClassroomFillness.getText()));
                } catch (SQLException ex) {
                    ex.printStackTrace();
                }
            }
        });
        frame.add(save, BorderLayout.SOUTH);
    }
}
