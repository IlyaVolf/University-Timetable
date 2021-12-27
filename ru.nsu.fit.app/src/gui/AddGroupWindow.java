package gui;

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
    String specialization;
    JTextField enterNewGroupNumber;
    JTextField enterAmountOfStudents;
    JTextField enterYearOfStudy;
    JButton addButton;
    JButton deleteButton;

    public AddGroupWindow(String specialization) {
        this.specialization = specialization;

        this.frame = new JFrame("Add Group");
        frame.setExtendedState(JFrame.MAXIMIZED_BOTH);
        frame.setVisible(true);

        this.label = new JLabel("List of groups");
        frame.add(this.label, BorderLayout.NORTH);

        DefaultListModel<String> listModel = new DefaultListModel<>();
        try {
            DatabaseManager manager = DatabaseManager.getInstance();
            List<Group> groupList = manager.getGroups(specialization);
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
        addNewGroupPanel.setLayout(new GridLayout(8, 3, 20, 50));

        addNewGroupPanel.add(new JLabel(""));
        addNewGroupPanel.add(new JLabel(""));
        addNewGroupPanel.add(new JLabel(""));

        addNewGroupPanel.add(new JLabel("Enter new group: "));
        this.enterNewGroupNumber = new JTextField("", 20);
        addNewGroupPanel.add(enterNewGroupNumber);
        addNewGroupPanel.add(new JLabel("[e.g \"19213\"]"));

        addNewGroupPanel.add(new JLabel(""));
        addNewGroupPanel.add(new JLabel(""));
        addNewGroupPanel.add(new JLabel(""));

        addNewGroupPanel.add(new JLabel("Enter amount of students: "));
        this.enterAmountOfStudents = new JTextField("", 20);
        addNewGroupPanel.add(enterAmountOfStudents);
        addNewGroupPanel.add(new JLabel("[e.g \"14\"]"));

        addNewGroupPanel.add(new JLabel(""));
        addNewGroupPanel.add(new JLabel(""));
        addNewGroupPanel.add(new JLabel(""));

        addNewGroupPanel.add(new JLabel("Enter year of study: "));
        this.enterYearOfStudy = new JTextField("", 20);
        addNewGroupPanel.add(enterYearOfStudy);
        addNewGroupPanel.add(new JLabel("[e.g \"3\"]"));

        addNewGroupPanel.add(new JLabel(""));
        addNewGroupPanel.add(new JLabel(""));
        addNewGroupPanel.add(new JLabel(""));

        this.addButton = new JButton("add");
        addButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String number = enterNewGroupNumber.getText();
                String amountOfStudents = enterAmountOfStudents.getText();
                String yearOfStudy = enterYearOfStudy.getText();
                try {
                    DatabaseManager manager = DatabaseManager.getInstance();
                    manager.addGroup(new Group(specialization, number, amountOfStudents, yearOfStudy));
                } catch (SQLException ex) {
                    ex.printStackTrace();
                }
                listModel.addElement("Number: " + number + " Students: " + amountOfStudents +
                        " YearOfStudy: " + yearOfStudy);
            }
        });

        addNewGroupPanel.add(new JLabel(""));
        addNewGroupPanel.add(addButton);
        addNewGroupPanel.add(new JLabel(""));



        frame.add(addNewGroupPanel, BorderLayout.WEST);

        deleteButton = new JButton("Delete");
        deleteButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String selected = listModel.remove(groups.getSelectedIndex());
                String[] words = selected.split(" ");
                Group group = new Group(specialization, words[1], words[3], words[5]);
                try {
                    DatabaseManager manager = DatabaseManager.getInstance();
                    manager.deleteGroup(group);
                } catch (SQLException ex) {
                    ex.printStackTrace();
                }
            }
        });
    }
}
