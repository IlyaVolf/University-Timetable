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
    JButton deleteButton;

    public AddAuditoryWindow() {
        this.frame = new JFrame("Edit Auditory");
        frame.setExtendedState(JFrame.MAXIMIZED_BOTH);
        frame.setVisible(true);

        this.label = new JLabel("List of auditories");
        frame.add(this.label, BorderLayout.NORTH);

        DefaultListModel<String> listModel = new DefaultListModel<>();
        try {
            DatabaseManager manager = DatabaseManager.getInstance();
            List<Auditory> auditoryList = manager.getAuditories();
            for (Auditory auditory: auditoryList) {
                listModel.addElement("Number: \t" + auditory.number +
                        "\t Capacity: \t" + auditory.capacity + "\t Types of classes: \t" +
                        auditory.typesOfClass);
            }
        } catch (SQLException ex) {
            ex.printStackTrace();
        }
        this.auditories = new JList<>(listModel);
        JScrollPane scrollableList = new JScrollPane(auditories);
        frame.add(scrollableList, BorderLayout.CENTER);

        JPanel addNewAuditoryPanel = new JPanel();
        addNewAuditoryPanel.setLayout(new GridLayout(8, 3, 20, 50));

        addNewAuditoryPanel.add(new JLabel(""));
        addNewAuditoryPanel.add(new JLabel(""));
        addNewAuditoryPanel.add(new JLabel(""));

        addNewAuditoryPanel.add(new JLabel("Enter auditory number: "));
        this.enterNumber = new JTextField("", 20);
        addNewAuditoryPanel.add(enterNumber);
        addNewAuditoryPanel.add(new JLabel("[e.g \"1156\"]"));

        addNewAuditoryPanel.add(new JLabel(""));
        addNewAuditoryPanel.add(new JLabel(""));
        addNewAuditoryPanel.add(new JLabel(""));

        addNewAuditoryPanel.add(new JLabel("Enter capacity: "));
        this.enterCapacity = new JTextField("", 20);
        addNewAuditoryPanel.add(enterCapacity);
        addNewAuditoryPanel.add(new JLabel("[e.g \"32\"]"));

        addNewAuditoryPanel.add(new JLabel(""));
        addNewAuditoryPanel.add(new JLabel(""));
        addNewAuditoryPanel.add(new JLabel(""));

        addNewAuditoryPanel.add(new JLabel("Enter types of class: "));
        this.enterTypesOfClass = new JTextField("", 20);
        addNewAuditoryPanel.add(enterTypesOfClass);
        addNewAuditoryPanel.add(new JLabel("[e.g \"lec\", \"lab\", \"pr\"]"));

        addNewAuditoryPanel.add(new JLabel(""));
        addNewAuditoryPanel.add(new JLabel(""));
        addNewAuditoryPanel.add(new JLabel(""));

        this.addButton = new JButton("edit");
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
                listModel.addElement("Number: \t" + number +
                        "\t Capacity: \t" + capacity + "\t Types of classes: \t" + types);
            }
        });
        addNewAuditoryPanel.add(new JLabel(""));
        addNewAuditoryPanel.add(addButton);
        addNewAuditoryPanel.add(new JLabel(""));
        frame.add(addNewAuditoryPanel, BorderLayout.WEST);

        deleteButton = new JButton("Delete");
        deleteButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String selected = listModel.remove(auditories.getSelectedIndex());
                String[] words = selected.split("\t");
                Auditory auditory = new Auditory(words[7], words[3], words[1]);
                try {
                    DatabaseManager manager = DatabaseManager.getInstance();
                    manager.deleteAuditory(auditory);
                } catch (SQLException ex) {
                    ex.printStackTrace();
                }
            }
        });
        frame.add(deleteButton, BorderLayout.EAST);
    }
}
