package gui;


import javax.swing.*;

public class StartWindow {
    JFrame frame;
    JButton generateButton;
    JButton viewButton;

    public StartWindow() {
        frame = new JFrame("University Timetable");
        generateButton = new JButton("Generate");
        viewButton = new JButton("View");
        generateButton.setBounds(140, 100, 95, 30);
        viewButton.setBounds(140, 175, 95, 30);
        frame.add(generateButton);
        frame.add(viewButton);
        frame.setSize(400, 400);
        frame.setLayout(null);
        //frame.setExtendedState(JFrame.MAXIMIZED_BOTH);
        //frame.setUndecorated(true);
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}
