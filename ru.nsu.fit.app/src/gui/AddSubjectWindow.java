package gui;

import entities.Group;
import entities.Subject;
import managers.DatabaseManager;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.SQLException;
import java.util.List;

public class AddSubjectWindow {
    JFrame frame;
    JLabel label;
    JList<String> subjects;
    String educationalProgram;
    JTextField enterNewSubjectName;
    JTextField enterAmountOfSemesters;
    JTextField enterTypeOfClass;
    JTextField enterFrequency;
    JTextField enterTeacherName;
    JTextField enterAmountOfGroups;
    JButton addButton;
    JButton addTeacher;

    public AddSubjectWindow(String educationalProgram) {
        this.educationalProgram = educationalProgram;

        this.frame = new JFrame("Add Subject");
        frame.setExtendedState(JFrame.MAXIMIZED_BOTH);
        frame.setVisible(true);

        this.label = new JLabel("List of subjects");
        frame.add(this.label, BorderLayout.NORTH);

        DefaultListModel<String> listModel = new DefaultListModel<>();
        try {
            DatabaseManager manager = DatabaseManager.getInstance();
            List<Subject> subjectList = manager.getSubjects(educationalProgram);
            for (Subject subject: subjectList) {
                listModel.addElement("Subject: " + subject.subjectName + " Semesters: " +
                        subject.semesters + " Teacher: " + subject.teacher + " Frequency: " +
                        subject.frequency + " Type: " + subject.typeOfClass + " Groups: " +
                        subject.amountOfGroups);
            }
        } catch (SQLException ex) {
            ex.printStackTrace();
        }
        this.subjects = new JList<>(listModel);
        JScrollPane scrollableList = new JScrollPane(subjects);
        frame.add(scrollableList, BorderLayout.CENTER);

        JPanel addNewSubjectPanel = new JPanel();
        this.enterNewSubjectName = new JTextField("Enter new Subject...");
        this.enterAmountOfSemesters = new JTextField("Enter amount of semesters...");
        this.enterTeacherName = new JTextField("Enter teacher name...");
        this.enterFrequency = new JTextField("Enter frequency...");
        this.enterTypeOfClass = new JTextField("Enter type of class...");
        this.enterAmountOfGroups = new JTextField("Enter amount of groups...");
        this.addButton = new JButton("add");
        addButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String name = enterNewSubjectName.getText();
                String amountSemesters = enterAmountOfSemesters.getText();
                String teacher = enterTeacherName.getText();
                String freq = enterFrequency.getText();
                String type = enterTypeOfClass.getText();
                String groups = enterAmountOfGroups.getText();
                try {
                    DatabaseManager manager = DatabaseManager.getInstance();
                    manager.addSubject(new Subject(educationalProgram, name, amountSemesters,
                            type, freq, teacher, groups));
                } catch (SQLException ex) {
                    ex.printStackTrace();
                }
                listModel.addElement("Subject: " + name + " Semesters: " +
                        amountSemesters + " Teacher: " + teacher + " Frequency: " +
                        freq + " Type: " + type + " Groups: " + groups);
            }
        });
        addNewSubjectPanel.add(enterNewSubjectName);
        addNewSubjectPanel.add(enterAmountOfSemesters);
        addNewSubjectPanel.add(enterTeacherName);
        addNewSubjectPanel.add(enterFrequency);
        addNewSubjectPanel.add(enterTypeOfClass);
        addNewSubjectPanel.add(enterAmountOfGroups);
        addNewSubjectPanel.add(addButton);
        frame.add(addNewSubjectPanel, BorderLayout.SOUTH);

        this.addTeacher = new JButton("add Teacher");
        addTeacher.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String subject = String.valueOf(subjects.getSelectedValue());
                new AddTeacherWindow(subject);
            }
        });
        frame.add(addTeacher, BorderLayout.EAST);
    }
}
