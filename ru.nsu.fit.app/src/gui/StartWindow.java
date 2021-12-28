package gui;


import javax.swing.*;

public class StartWindow {
    JFrame frame;
    JButton generateButton;
    JButton viewButton;

    public StartWindow() {
        frame = new JFrame("University Timetable");
        generateButton = new JButton("Edit restrictions");
        viewButton = new JButton("View");
        generateButton.setBounds(140, 100, 135, 30);
        viewButton.setBounds(140, 175, 135, 30);
        frame.add(generateButton);
        frame.add(viewButton);
        frame.setSize(400, 400);
        frame.setLayout(null);
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}
