package gui;

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
    JTree tree;
    JMenuBar menuBar;
    JPanel panel;
    JList<String> faculties;

    private void expandAllNodes(JTree tree, int startingIndex, int rowCount) {
        for (int i = startingIndex; i < rowCount; ++i) {
            tree.expandRow(i);
        }

        if (tree.getRowCount() != rowCount) {
            expandAllNodes(tree, rowCount, tree.getRowCount());
        }
    }

    public JPanel createPanel() {
        JPanel panel = new JPanel();

        DefaultListModel<String> listModel = new DefaultListModel<>();
        try {
            DatabaseManager manager = DatabaseManager.getInstance();
            List<Faculty> facultyList = manager.getAllFaculties();
            for (Faculty faculty: facultyList) {
                listModel.addElement(faculty.name);
            }
        } catch (SQLException ex) {
            ex.printStackTrace();
        }
        faculties = new JList<>(listModel);
        JScrollPane scrollableList = new JScrollPane(faculties);
        JLabel label = new JLabel("List of faculties");
        JButton addButton = new JButton("add");
        JTextField enterNewFaculty = new JTextField("Enter name of new faculty...");
        JPanel addNewFacultyPanel = new JPanel();
        addButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String text = enterNewFaculty.getText();
                try {
                    DatabaseManager manager = DatabaseManager.getInstance();
                    manager.addFaculty(new Faculty(text));
                } catch (SQLException ex) {
                    ex.printStackTrace();
                }
                listModel.addElement(text);
            }
        });
        addNewFacultyPanel.add(enterNewFaculty);
        addNewFacultyPanel.add(addButton);


        panel.setLayout(new BorderLayout());
        panel.add(label, BorderLayout.NORTH);
        panel.add(scrollableList, BorderLayout.CENTER);
        panel.add(addNewFacultyPanel, BorderLayout.SOUTH);

        return panel;
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

    public JTree createTree() {
        DefaultMutableTreeNode structure = new DefaultMutableTreeNode("University");
        DefaultMutableTreeNode faculty = new DefaultMutableTreeNode("Faculties");
        DefaultMutableTreeNode educationalProgram = new DefaultMutableTreeNode("Educational Programs");
        DefaultMutableTreeNode group = new DefaultMutableTreeNode("Groups");
        DefaultMutableTreeNode subject = new DefaultMutableTreeNode("Subjects");
        DefaultMutableTreeNode teacher = new DefaultMutableTreeNode("Teachers");
        DefaultMutableTreeNode auditory = new DefaultMutableTreeNode("Auditories");

        subject.add(teacher);
        educationalProgram.add(subject);
        educationalProgram.add(group);
        faculty.add(educationalProgram);
        structure.add(faculty);
        structure.add(auditory);
        return new JTree(structure);
    }

    public AddFacultyWindow() {
        frame = new JFrame("Add Restrictions");
        //frame.setSize(600, 600);
        frame.setExtendedState(JFrame.MAXIMIZED_BOTH);
        frame.setVisible(true);

        tree = createTree();
        tree.setSize(200, 600);
        frame.add(tree, BorderLayout.WEST);
        expandAllNodes(tree, 0, tree.getRowCount());

        menuBar = createMenu();
        frame.add(menuBar, BorderLayout.NORTH);

        panel = createPanel();
        frame.add(panel, BorderLayout.CENTER);

        JButton addEP = new JButton("Add Educational Program");
        addEP.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String faculty = String.valueOf(faculties.getSelectedValue());
                // JOptionPane.showMessageDialog(frame, faculty);
                new AddEducationalProgramWindow(faculty);
            }
        });
        frame.add(addEP, BorderLayout.EAST);

    }
}
