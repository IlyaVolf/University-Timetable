package gui;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class AddTeacherWindow {
    JFrame frame;
    JLabel label;
    JList<String> teachers;
    String subject;
    JTextField enterNewTeacher;
    JButton addButton;

    public AddTeacherWindow(String subject) {
        this.subject = subject;

        this.frame = new JFrame("Add Teacher");
        frame.setExtendedState(JFrame.MAXIMIZED_BOTH);
        frame.setVisible(true);

        this.label = new JLabel("List of teachers");
        frame.add(this.label, BorderLayout.NORTH);

        DefaultListModel<String> listModel = new DefaultListModel<>();
        listModel.addElement("empty teacher");
        this.teachers = new JList<>(listModel);
        JScrollPane scrollableList = new JScrollPane(teachers);
        frame.add(scrollableList, BorderLayout.CENTER);

        JPanel addNewSubjectPanel = new JPanel();
        this.enterNewTeacher = new JTextField("Enter new Subject...");
        this.addButton = new JButton("add");
        addButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String text = enterNewTeacher.getText();
                listModel.addElement(text);
            }
        });
        addNewSubjectPanel.add(enterNewTeacher);
        addNewSubjectPanel.add(addButton);
        frame.add(addNewSubjectPanel, BorderLayout.SOUTH);
    }
}
