package gui;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class AddSubjectWindow {
    JFrame frame;
    JLabel label;
    JList<String> subjects;
    String educationalProgram;
    JTextField enterNewSubject;
    JButton addButton;
    JButton addTeacher;

    public AddSubjectWindow(String educationalProgram) {
        this.educationalProgram = educationalProgram;

        this.frame = new JFrame("Add Subject");
        frame.setExtendedState(JFrame.MAXIMIZED_BOTH);
        frame.setVisible(true);

        this.label = new JLabel("List of subjects");
        frame.add(this.label, BorderLayout.NORTH);

        DefaultListModel<String> listModel = new DefaultListModel<>();
        listModel.addElement("empty subject");
        this.subjects = new JList<>(listModel);
        JScrollPane scrollableList = new JScrollPane(subjects);
        frame.add(scrollableList, BorderLayout.CENTER);

        JPanel addNewSubjectPanel = new JPanel();
        this.enterNewSubject = new JTextField("Enter new Subject...");
        this.addButton = new JButton("add");
        addButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String text = enterNewSubject.getText();
                listModel.addElement(text);
            }
        });
        addNewSubjectPanel.add(enterNewSubject);
        addNewSubjectPanel.add(addButton);
        frame.add(addNewSubjectPanel, BorderLayout.SOUTH);

        this.addTeacher = new JButton("add Teacher");
        addTeacher.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String subject = String.valueOf(subjects.getSelectedValue());
                new AddTeacherWindow(subject);
            }
        });
        frame.add(addTeacher, BorderLayout.EAST);
    }
}
