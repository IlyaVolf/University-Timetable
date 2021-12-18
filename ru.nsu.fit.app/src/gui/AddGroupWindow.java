package gui;

import entities.EducationalProgram;
import entities.Group;
import managers.DatabaseManager;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.SQLException;
import java.util.List;

public class AddGroupWindow {
    JFrame frame;
    JLabel label;
    JList<String> groups;
    String educationalProgram;
    JTextField enterNewGroupNumber;
    JTextField enterAmountOfStudents;
    JTextField enterYearOfStudy;
    JButton addButton;

    public AddGroupWindow(String educationalProgram) {
        this.educationalProgram = educationalProgram;

        this.frame = new JFrame("Add Group");
        frame.setExtendedState(JFrame.MAXIMIZED_BOTH);
        frame.setVisible(true);

        this.label = new JLabel("List of groups");
        frame.add(this.label, BorderLayout.NORTH);

        DefaultListModel<String> listModel = new DefaultListModel<>();
        try {
            DatabaseManager manager = DatabaseManager.getInstance();
            List<Group> groupList = manager.getGroups(educationalProgram);
            for (Group group: groupList) {
                listModel.addElement("Number: " + group.numberOfGroup + " Students: " +
                        group.amountOfStudents + " YearOfStudy: " + group.yearOfStudy);
            }
        } catch (SQLException ex) {
            ex.printStackTrace();
        }
        this.groups = new JList<>(listModel);
        JScrollPane scrollableList = new JScrollPane(groups);
        frame.add(scrollableList, BorderLayout.CENTER);

        JPanel addNewGroupPanel = new JPanel();
        this.enterNewGroupNumber = new JTextField("Enter new group...");
        this.enterAmountOfStudents = new JTextField("Enter amount of students...");
        this.enterYearOfStudy = new JTextField("Enter year of study...");
        this.addButton = new JButton("add");
        addButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String number = enterNewGroupNumber.getText();
                String amountOfStudents = enterAmountOfStudents.getText();
                String yearOfStudy = enterYearOfStudy.getText();
                try {
                    DatabaseManager manager = DatabaseManager.getInstance();
                    manager.addGroup(new Group(educationalProgram, number, amountOfStudents, yearOfStudy));
                } catch (SQLException ex) {
                    ex.printStackTrace();
                }
                listModel.addElement("Number: " + number + " Students: " + amountOfStudents +
                        " YearOfStudy: " + yearOfStudy);
            }
        });
        addNewGroupPanel.add(enterNewGroupNumber);
        addNewGroupPanel.add(enterAmountOfStudents);
        addNewGroupPanel.add(enterYearOfStudy);
        addNewGroupPanel.add(addButton);
        frame.add(addNewGroupPanel, BorderLayout.SOUTH);
    }
}
