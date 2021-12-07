package gui;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class AddGroupWindow {
    JFrame frame;
    JLabel label;
    JList<String> groups;
    String educationalProgram;
    JTextField enterNewGroup;
    JButton addButton;

    public AddGroupWindow(String educationalProgram) {
        this.educationalProgram = educationalProgram;

        this.frame = new JFrame("Add Group");
        frame.setExtendedState(JFrame.MAXIMIZED_BOTH);
        frame.setVisible(true);

        this.label = new JLabel("List of groups");
        frame.add(this.label, BorderLayout.NORTH);

        DefaultListModel<String> listModel = new DefaultListModel<>();
        listModel.addElement("empty group");
        this.groups = new JList<>(listModel);
        JScrollPane scrollableList = new JScrollPane(groups);
        frame.add(scrollableList, BorderLayout.CENTER);

        JPanel addNewGroupPanel = new JPanel();
        this.enterNewGroup = new JTextField("Enter new Group...");
        this.addButton = new JButton("add");
        addButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String text = enterNewGroup.getText();
                listModel.addElement(text);
            }
        });
        addNewGroupPanel.add(enterNewGroup);
        addNewGroupPanel.add(addButton);
        frame.add(addNewGroupPanel, BorderLayout.SOUTH);
    }
}
