package gui;

import managers.DatabaseManager;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.SQLException;
import java.util.List;

public class SelectSpecializationWindow {
    JFrame frame;
    JLabel label;
    JList<String> specializations;
    JButton viewTimetableButton;

    public SelectSpecializationWindow() {

        this.frame = new JFrame("Select specialization");
        frame.setExtendedState(JFrame.MAXIMIZED_BOTH);
        frame.setVisible(true);

        this.label = new JLabel("List of specializations");
        frame.add(this.label, BorderLayout.NORTH);

        DefaultListModel<String> listModel = new DefaultListModel<>();
        try {
            DatabaseManager manager = DatabaseManager.getInstance();
            List<String> specs = manager.getTimetableSpecializations();
            for (String spec : specs) {
                listModel.addElement(spec);
            }
        } catch (SQLException ex) {
            ex.printStackTrace();
        }
        this.specializations = new JList<>(listModel);
        JScrollPane scrollableList = new JScrollPane(specializations);
        frame.add(scrollableList, BorderLayout.WEST);


        viewTimetableButton = new JButton("View timetable");
        viewTimetableButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String selected = specializations.getSelectedValue();
                new ViewTimetableWindow(selected);
            }
        });
        frame.add(viewTimetableButton, BorderLayout.EAST);
    }
}

