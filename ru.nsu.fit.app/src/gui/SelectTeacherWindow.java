package gui;

import entities.Teacher;
import managers.DatabaseManager;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.SQLException;
import java.util.List;

public class SelectTeacherWindow {
    JFrame frame;
    JList<String> teachers;
    JButton addTeacherToSubject;

    String subject;
    String specialization;
    String semesters;
    String types;
    String frequency;
    String amountOfGroups;

    public SelectTeacherWindow(String subject, String specialization, String semesters,
                               String types, String frequency, String amountOfGroups) {
        this.subject = subject;
        this.specialization = specialization;
        this.semesters = semesters;
        this.types = types;
        this.frequency = frequency;
        this.amountOfGroups = amountOfGroups;
        this.frame = new JFrame("Select Teacher");
        //frame.setSize(500, 500);
        frame.setExtendedState(Frame.MAXIMIZED_BOTH);
        //frame.setLayout(null);
        frame.setVisible(true);

        DefaultListModel<String> listModel = new DefaultListModel<>();
        try {
            DatabaseManager manager = DatabaseManager.getInstance();
            List<Teacher> teacherList = manager.getAllTeachers();
            for (Teacher teacher: teacherList) {
                listModel.addElement(teacher.name);
            }
        } catch (SQLException ex) {
            ex.printStackTrace();
        }
        this.teachers = new JList<>(listModel);
        JScrollPane scrollableList = new JScrollPane(teachers);
        frame.add(scrollableList, BorderLayout.CENTER);

        this.addTeacherToSubject = new JButton("Add Teacher");
        addTeacherToSubject.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String selected = teachers.getSelectedValue();
                try {
                    DatabaseManager manager = DatabaseManager.getInstance();
                    manager.updateSubject(specialization, subject, selected, semesters,
                            types, frequency, amountOfGroups);
                } catch (SQLException ex) {
                    ex.printStackTrace();
                }
            }
        });

        JPanel addButtonPanel = new JPanel();
        addButtonPanel.add(new JLabel(""));
        addButtonPanel.add(addTeacherToSubject);
        addButtonPanel.add(new JLabel(""));
        frame.add(addButtonPanel, BorderLayout.SOUTH);
    }
}
