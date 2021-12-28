package gui;

import managers.DatabaseManager;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.SQLException;
import java.util.List;

public class ViewTimetableWindow {
    JFrame frame;
    JLabel label;
    JList<String> eventList;

    String specialization;

    public ViewTimetableWindow(String specialization) {

        this.specialization = specialization;

        this.frame = new JFrame("View Timetable");
        frame.setExtendedState(JFrame.MAXIMIZED_BOTH);
        frame.setVisible(true);

        this.label = new JLabel("List of groups");
        //frame.add(this.label, BorderLayout.NORTH);

        DefaultListModel<String> listModel = new DefaultListModel<>();
        try {
            DatabaseManager manager = DatabaseManager.getInstance();
            List<String> events = manager.getEvents(specialization);
            for (String event: events) {
                listModel.addElement(event);
            }
        } catch (SQLException ex) {
            ex.printStackTrace();
        }
        this.eventList = new JList<>(listModel);
        JScrollPane scrollableList = new JScrollPane(eventList);
        frame.add(scrollableList, BorderLayout.WEST);
    }
}