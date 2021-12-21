package gui;

import entities.EducationalProgram;
import entities.Faculty;
import managers.DatabaseManager;

import javax.swing.*;
import javax.swing.tree.DefaultMutableTreeNode;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.SQLException;
import java.util.List;

public class AddFacultyWindow {
    JFrame frame;
    JList<String> faculties;
    JMenuBar menuBar;
    JTextField enterNewFaculty;
    JButton addButton;
    JButton deleteButton;
    JButton addEducationalProgram;

    public AddFacultyWindow() {
        this.frame = new JFrame("Add Restrictions");
        frame.setExtendedState(JFrame.MAXIMIZED_BOTH);
        frame.setVisible(true);

        this.menuBar = createMenu();
        frame.add(menuBar, BorderLayout.NORTH);

        DefaultListModel<String> listModel = new DefaultListModel<>();
        try {
            DatabaseManager manager = DatabaseManager.getInstance();
            List<Faculty> facultyList = manager.getAllFaculties();
            for (Faculty faculty: facultyList) {
                listModel.addElement("Faculty: " + faculty.name);
            }
        } catch (SQLException ex) {
            ex.printStackTrace();
        }
        this.faculties = new JList<>(listModel);
        JScrollPane scrollableList = new JScrollPane(faculties);
        frame.add(scrollableList, BorderLayout.CENTER);


        JPanel addNewFacultyPanel = new JPanel();
        addNewFacultyPanel.setLayout(new GridLayout(8, 3, 20, 50));

        addNewFacultyPanel.add(new JLabel(""));
        addNewFacultyPanel.add(new JLabel(""));
        addNewFacultyPanel.add(new JLabel(""));
        addNewFacultyPanel.add(new JLabel(""));
        addNewFacultyPanel.add(new JLabel(""));
        addNewFacultyPanel.add(new JLabel(""));

        addNewFacultyPanel.add(new JLabel("Enter new Faculty name: "));
        this.enterNewFaculty = new JTextField("", 20);
        addNewFacultyPanel.add(enterNewFaculty);
        addNewFacultyPanel.add(new JLabel("[e.g \"FIT\"]"));

        addNewFacultyPanel.add(new JLabel(""));
        addNewFacultyPanel.add(new JLabel(""));
        addNewFacultyPanel.add(new JLabel(""));

        this.addButton = new JButton("add");
        addButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String faculty = enterNewFaculty.getText();
                try {
                    DatabaseManager manager = DatabaseManager.getInstance();
                    manager.addFaculty(new Faculty(faculty));
                } catch (SQLException ex) {
                    ex.printStackTrace();
                }
                listModel.addElement("Faculty: " + faculty);
            }
        });

        addNewFacultyPanel.add(new JLabel(""));
        addNewFacultyPanel.add(new JLabel(""));
        addNewFacultyPanel.add(new JLabel(""));

        addNewFacultyPanel.add(new JLabel(""));
        addNewFacultyPanel.add(addButton);
        addNewFacultyPanel.add(new JLabel(""));

        addNewFacultyPanel.add(new JLabel(""));
        addNewFacultyPanel.add(new JLabel(""));
        addNewFacultyPanel.add(new JLabel(""));
        addNewFacultyPanel.add(new JLabel(""));
        addNewFacultyPanel.add(new JLabel(""));
        addNewFacultyPanel.add(new JLabel(""));

        frame.add(addNewFacultyPanel, BorderLayout.WEST);

        JPanel addNewEntitiesPanel = new JPanel();
        addNewEntitiesPanel.setLayout(new GridLayout(5, 1, 20, 50));
        this.addEducationalProgram = new JButton("add EducationalProgram");
        addEducationalProgram.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String educationalProgram = String.valueOf(faculties.getSelectedValue());
                String[] words = educationalProgram.split(" ");
                new AddEducationalProgramWindow(words[1]);
            }
        });

        deleteButton = new JButton("Delete");
        deleteButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String selected = listModel.remove(faculties.getSelectedIndex());
                String[] words = selected.split(" ");
                Faculty faculty = new Faculty(words[1]);
                try {
                    DatabaseManager manager = DatabaseManager.getInstance();
                    manager.deleteFaculty(faculty.name);
                } catch (SQLException ex) {
                    ex.printStackTrace();
                }
            }
        });
        addNewEntitiesPanel.add(new JLabel(""));
        addNewEntitiesPanel.add(addEducationalProgram);
        addNewEntitiesPanel.add(new JLabel(""));
        addNewEntitiesPanel.add(deleteButton);
        addNewEntitiesPanel.add(new JLabel(""));
        frame.add(addNewEntitiesPanel, BorderLayout.EAST);
    }

    public JMenuBar createMenu() {
        JMenuBar mb = new JMenuBar();
        JMenu menu = new JMenu("Menu");
        JMenu faculties = new JMenu("Faculties");
        JMenu educationalPrograms = new JMenu("Educational Programs");
        JMenu subjects = new JMenu("Subjects");
        JMenu groups = new JMenu("Groups");
        JMenu teachers = new JMenu("Teachers");
        JMenu auditories = new JMenu("Auditories");
        JMenu constraints = new JMenu("Constraints");

        JMenuItem generate = new JMenuItem("Generate!");
        JMenuItem addAuditory = new JMenuItem("Add");
        addAuditory.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                new AddAuditoryWindow();
            }
        });
        JMenuItem addConstraints = new JMenuItem("Add");
        addConstraints.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                new AddConstraintsWindow();
            }
        });
        JMenuItem view = new JMenuItem("View");
        JMenuItem removeAll = new JMenuItem("Remove all");
        menu.add(generate);
        menu.add(view);
        menu.add(removeAll);
        auditories.add(addAuditory);
        constraints.add(addConstraints);

        mb.add(menu);
        mb.add(faculties);
        mb.add(educationalPrograms);
        mb.add(subjects);
        mb.add(groups);
        mb.add(teachers);
        mb.add(auditories);
        mb.add(constraints);

        return mb;
    }


}
