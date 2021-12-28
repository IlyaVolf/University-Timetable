package gui;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Gui {
    public static void main(String[] args) {
        StartWindow startWindow = new StartWindow();
        startWindow.generateButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                new AddFacultyWindow();

            }
        });
        startWindow.viewButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                new SelectSpecializationWindow();
            }
        });
    }
}
