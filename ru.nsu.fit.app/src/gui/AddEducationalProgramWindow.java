package gui;

import entities.EducationalProgram;
import entities.Faculty;
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
        this.enterNewEducationalProgramName = new JTextField("Enter new Educational Program name...");
        this.enterNewSpecialization = new JTextField("Enter specialization...");
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
        addNewEdProgPanel.add(enterNewEducationalProgramName);
        addNewEdProgPanel.add(enterNewSpecialization);
        addNewEdProgPanel.add(addButton);
        frame.add(addNewEdProgPanel, BorderLayout.SOUTH);

        JPanel addNewEntitiesPanel = new JPanel();
        this.addGroup = new JButton("add Group");
        this.addSubject = new JButton("add Subject");
        addGroup.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String educationalProgram = String.valueOf(educationalPrograms.getSelectedValue());
                //JOptionPane.showMessageDialog(frame, educationalProgram);
                new AddGroupWindow(educationalProgram);
            }
        });
        addSubject.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String educationalProgram = String.valueOf(educationalPrograms.getSelectedValue());
                //JOptionPane.showMessageDialog(frame, educationalProgram);
                new AddSubjectWindow(educationalProgram);
            }
        });
        addNewEntitiesPanel.add(addGroup);
        addNewEntitiesPanel.add(addSubject);
        frame.add(addNewEntitiesPanel, BorderLayout.EAST);
    }

}
