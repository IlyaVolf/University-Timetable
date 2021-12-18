package gui;

import entities.Group;
import entities.Teacher;
import managers.DatabaseManager;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.SQLException;
import java.util.List;

public class AddTeacherWindow {
    JFrame frame;
    JLabel label;
    JList<String> teachers;
    String subject;
    JTextField enterNewTeacherName;
    JTextField enterDaysTeacherCanWork;
    JTextField enterDaysTeacherWantWork;
    JTextField enterWeight;
    JButton addButton;

    public AddTeacherWindow(String subject) {
        this.subject = subject;

        this.frame = new JFrame("Add Teacher");
        frame.setExtendedState(JFrame.MAXIMIZED_BOTH);
        frame.setVisible(true);

        this.label = new JLabel("List of teachers");
        frame.add(this.label, BorderLayout.NORTH);

        DefaultListModel<String> listModel = new DefaultListModel<>();
        try {
            DatabaseManager manager = DatabaseManager.getInstance();
            List<Teacher> teacherList = manager.getTeachers(subject);
            for (Teacher teacher: teacherList) {
                listModel.addElement("Teacher: " + teacher.name + " Can work: " + teacher.daysTeacherCanWork +
                        " Want work: " + teacher.daysTeacherWantWork + " Weight: " + teacher.weight);
            }
        } catch (SQLException ex) {
            ex.printStackTrace();
        }
        this.teachers = new JList<>(listModel);
        JScrollPane scrollableList = new JScrollPane(teachers);
        frame.add(scrollableList, BorderLayout.CENTER);

        JPanel addNewSubjectPanel = new JPanel();
        this.enterNewTeacherName = new JTextField("Enter new Subject...");
        this.enterDaysTeacherCanWork = new JTextField("Enter days when teacher can work [1-7]...");
        this.enterDaysTeacherWantWork = new JTextField("Enter days when teacher want work [1-7]...");
        this.enterWeight = new JTextField("Enter weight...");
        this.addButton = new JButton("add");
        addButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String teacher = enterNewTeacherName.getText();
                String canWork = enterDaysTeacherCanWork.getText();
                String wantWork = enterDaysTeacherWantWork.getText();
                String weight = enterWeight.getText();
                try {
                    DatabaseManager manager = DatabaseManager.getInstance();
                    manager.addTeacher(new Teacher(subject, teacher, canWork, wantWork, weight));
                } catch (SQLException ex) {
                    ex.printStackTrace();
                }
                listModel.addElement("Teacher: " + teacher + " Can work: " + canWork + " Want work: " +
                        wantWork + " Weight: " + weight);
            }
        });
        addNewSubjectPanel.add(enterNewTeacherName);
        addNewSubjectPanel.add(addButton);
        frame.add(addNewSubjectPanel, BorderLayout.SOUTH);
    }
}
