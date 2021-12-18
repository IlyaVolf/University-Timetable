package gui;

import entities.Auditory;
import entities.Group;
import managers.DatabaseManager;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.SQLException;
import java.util.List;

public class AddAuditoryWindow {
    JFrame frame;
    JLabel label;
    JList<String> auditories;
    JTextField enterTypesOfClass;
    JTextField enterCapacity;
    JTextField enterNumber;
    JButton addButton;

    public AddAuditoryWindow() {
        this.frame = new JFrame("Add Auditory");
        frame.setExtendedState(JFrame.MAXIMIZED_BOTH);
        frame.setVisible(true);

        this.label = new JLabel("List of auditories");
        frame.add(this.label, BorderLayout.NORTH);

        DefaultListModel<String> listModel = new DefaultListModel<>();
        try {
            DatabaseManager manager = DatabaseManager.getInstance();
            List<Auditory> auditoryList = manager.getAuditories();
            for (Auditory auditory: auditoryList) {
                listModel.addElement("Number: " + auditory.number +
                        " Capacity: " + auditory.capacity + " Types of classes: " +
                        auditory.typesOfClass);
            }
        } catch (SQLException ex) {
            ex.printStackTrace();
        }
        this.auditories = new JList<>(listModel);
        JScrollPane scrollableList = new JScrollPane(auditories);
        frame.add(scrollableList, BorderLayout.CENTER);

        JPanel addNewAuditoryPanel = new JPanel();
        this.enterNumber = new JTextField("Enter auditory number...");
        this.enterCapacity = new JTextField("Enter capacity...");
        this.enterTypesOfClass = new JTextField("Enter types of class...");
        this.addButton = new JButton("add");
        addButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String number = enterNumber.getText();
                String capacity = enterCapacity.getText();
                String types = enterTypesOfClass.getText();
                try {
                    DatabaseManager manager = DatabaseManager.getInstance();
                    manager.addAuditory(new Auditory(types, capacity, number));
                } catch (SQLException ex) {
                    ex.printStackTrace();
                }
                listModel.addElement("Number: " + number +
                        " Capacity: " + capacity + " Types of classes: " + types);
            }
        });
        addNewAuditoryPanel.add(enterNumber);
        addNewAuditoryPanel.add(enterCapacity);
        addNewAuditoryPanel.add(enterTypesOfClass);
        addNewAuditoryPanel.add(addButton);
        frame.add(addNewAuditoryPanel, BorderLayout.SOUTH);
    }
}
