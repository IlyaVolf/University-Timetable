package gui;

import entities.Auditory;
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
    JButton deleteButton;

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

        JPanel addNewTeacherPanel = new JPanel();
        addNewTeacherPanel.setLayout(new GridLayout(8,3,20,50));

        addNewTeacherPanel.add(new JLabel(""));
        addNewTeacherPanel.add(new JLabel(""));
        addNewTeacherPanel.add(new JLabel(""));

        addNewTeacherPanel.add(new JLabel("Enter new Teacher: "));
        this.enterNewTeacherName = new JTextField("", 20);
        addNewTeacherPanel.add(enterNewTeacherName);
        addNewTeacherPanel.add(new JLabel("[e.g \"Vladimir Vaskevich\"]"));

        addNewTeacherPanel.add(new JLabel("Enter days when teacher can work: "));
        this.enterDaysTeacherCanWork = new JTextField("", 20);
        addNewTeacherPanel.add(enterDaysTeacherCanWork);
        addNewTeacherPanel.add(new JLabel("[e.g \"[1,2,3,4,5]\"]"));

        addNewTeacherPanel.add(new JLabel("Enter days when teacher want work: "));
        this.enterDaysTeacherWantWork = new JTextField("", 20);
        addNewTeacherPanel.add(enterDaysTeacherWantWork);
        addNewTeacherPanel.add(new JLabel("[e.g \"[1,3,5]\"]"));

        addNewTeacherPanel.add(new JLabel("Enter weight: "));
        this.enterWeight = new JTextField("", 20);
        addNewTeacherPanel.add(enterWeight);
        addNewTeacherPanel.add(new JLabel("[e.g \"10\"]"));

        addNewTeacherPanel.add(new JLabel(""));
        addNewTeacherPanel.add(new JLabel(""));
        addNewTeacherPanel.add(new JLabel(""));

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
        //addNewSubjectPanel.add(enterNewTeacherName);
        addNewTeacherPanel.add(new JLabel(""));
        addNewTeacherPanel.add(addButton);
        addNewTeacherPanel.add(new JLabel(""));
        frame.add(addNewTeacherPanel, BorderLayout.WEST);

        deleteButton = new JButton("Delete");
        deleteButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String selected = listModel.remove(teachers.getSelectedIndex());
                String[] words = selected.split(" ");
                Teacher teacher = new Teacher(subject, words[1],words[4],words[7], words[9]);
                try {
                    DatabaseManager manager = DatabaseManager.getInstance();
                    manager.deleteTeacher(teacher);
                } catch (SQLException ex) {
                    ex.printStackTrace();
                }
            }
        });
        frame.add(deleteButton, BorderLayout.EAST);
    }
}
