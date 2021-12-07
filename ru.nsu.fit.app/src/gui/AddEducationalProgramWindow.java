package gui;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class AddEducationalProgramWindow {
    JFrame frame;
    JLabel label;
    JList<String> educationalPrograms;
    String faculty;
    JTextField enterNewEducationalProgram;
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
        listModel.addElement("empty educational program");
        this.educationalPrograms = new JList<>(listModel);
        JScrollPane scrollableList = new JScrollPane(educationalPrograms);
        frame.add(scrollableList, BorderLayout.CENTER);

        JPanel addNewEdProgPanel = new JPanel();
        this.enterNewEducationalProgram = new JTextField("Enter new Educational Program...");
        this.addButton = new JButton("add");
        addButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String text = enterNewEducationalProgram.getText();
                listModel.addElement(text);
            }
        });
        addNewEdProgPanel.add(enterNewEducationalProgram);
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
