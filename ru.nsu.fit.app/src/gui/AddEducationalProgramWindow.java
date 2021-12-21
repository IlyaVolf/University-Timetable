package gui;

import entities.EducationalProgram;
import entities.Faculty;
import entities.Subject;
import managers.DatabaseManager;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.SQLException;
import java.util.List;

public class AddEducationalProgramWindow {
    JFrame frame;
    JLabel label;
    JList<String> educationalPrograms;
    String faculty;
    JTextField enterNewEducationalProgramName;
    JTextField enterNewSpecialization;
    JButton addButton;
    JButton deleteButton;
    JButton addSubject;
    JButton addGroup;

    public AddEducationalProgramWindow(String faculty) {
        this.faculty = faculty;

        this.frame = new JFrame("Add Educational Program");
        frame.setExtendedState(JFrame.MAXIMIZED_BOTH);
        frame.setVisible(true);

        this.label = new JLabel("List of educational programs");
        frame.add(this.label, BorderLayout.NORTH);

        DefaultListModel<String> listModel = new DefaultListModel<>();
        try {
            DatabaseManager manager = DatabaseManager.getInstance();
            List<EducationalProgram> educationalProgramList = manager.getEducationalPrograms(faculty);
            for (EducationalProgram educationalProgram: educationalProgramList) {
                listModel.addElement("Educational program: " + educationalProgram.name + " Specialization: " + educationalProgram.specialization);
            }
        } catch (SQLException ex) {
            ex.printStackTrace();
        }
        this.educationalPrograms = new JList<>(listModel);
        JScrollPane scrollableList = new JScrollPane(educationalPrograms);
        frame.add(scrollableList, BorderLayout.CENTER);

        JPanel addNewEdProgPanel = new JPanel();
        addNewEdProgPanel.setLayout(new GridLayout(8, 3, 20, 50));

        addNewEdProgPanel.add(new JLabel(""));
        addNewEdProgPanel.add(new JLabel(""));
        addNewEdProgPanel.add(new JLabel(""));

        addNewEdProgPanel.add(new JLabel("Enter new Educational Program name: "));
        this.enterNewEducationalProgramName = new JTextField("", 20);
        addNewEdProgPanel.add(enterNewEducationalProgramName);
        addNewEdProgPanel.add(new JLabel("[e.g \"Bach\"]"));

        addNewEdProgPanel.add(new JLabel(""));
        addNewEdProgPanel.add(new JLabel(""));
        addNewEdProgPanel.add(new JLabel(""));

        addNewEdProgPanel.add(new JLabel("Enter specialization: "));
        this.enterNewSpecialization = new JTextField("", 20);
        addNewEdProgPanel.add(enterNewSpecialization);
        addNewEdProgPanel.add(new JLabel("[e.g \"ComputerScience\"]"));

        addNewEdProgPanel.add(new JLabel(""));
        addNewEdProgPanel.add(new JLabel(""));
        addNewEdProgPanel.add(new JLabel(""));

        this.addButton = new JButton("add");
        addButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String edPr = enterNewEducationalProgramName.getText();
                String sp = enterNewSpecialization.getText();
                try {
                    DatabaseManager manager = DatabaseManager.getInstance();
                    manager.addEducationalProgram(new EducationalProgram(faculty, edPr, sp));
                } catch (SQLException ex) {
                    ex.printStackTrace();
                }
                listModel.addElement("Educational program: " + edPr + " Specialization: " + sp);
            }
        });
        addNewEdProgPanel.add(new JLabel(""));
        addNewEdProgPanel.add(addButton);
        addNewEdProgPanel.add(new JLabel(""));

        addNewEdProgPanel.add(new JLabel(""));
        addNewEdProgPanel.add(new JLabel(""));
        addNewEdProgPanel.add(new JLabel(""));
        addNewEdProgPanel.add(new JLabel(""));
        addNewEdProgPanel.add(new JLabel(""));
        addNewEdProgPanel.add(new JLabel(""));
        frame.add(addNewEdProgPanel, BorderLayout.WEST);

        JPanel addNewEntitiesPanel = new JPanel();
        addNewEntitiesPanel.setLayout(new GridLayout(5, 1, 20, 50));
        this.addGroup = new JButton("add Group");
        this.addSubject = new JButton("add Subject");
        addGroup.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String educationalProgram = String.valueOf(educationalPrograms.getSelectedValue());
                String[] words = educationalProgram.split(" ");
                new AddGroupWindow(words[2]);
            }
        });
        addSubject.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String educationalProgram = String.valueOf(educationalPrograms.getSelectedValue());
                String[] words = educationalProgram.split(" ");
                new AddSubjectWindow(words[2]);
            }
        });

        deleteButton = new JButton("Delete");
        deleteButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String selected = listModel.remove(educationalPrograms.getSelectedIndex());
                String[] words = selected.split(" ");
                EducationalProgram ep = new EducationalProgram(faculty, words[2], words[4]);
                try {
                    DatabaseManager manager = DatabaseManager.getInstance();
                    manager.deleteEducationalProgram(ep);
                } catch (SQLException ex) {
                    ex.printStackTrace();
                }
            }
        });
        addNewEntitiesPanel.add(new JLabel(""));
        addNewEntitiesPanel.add(addGroup);
        addNewEntitiesPanel.add(addSubject);
        addNewEntitiesPanel.add(deleteButton);
        addNewEntitiesPanel.add(new JLabel(""));
        frame.add(addNewEntitiesPanel, BorderLayout.EAST);
    }

}
