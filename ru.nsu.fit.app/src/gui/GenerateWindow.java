package gui;

import javax.swing.*;
import javax.swing.tree.DefaultMutableTreeNode;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class GenerateWindow {
    JFrame frame;
    JTree tree;
    JMenuBar menuBar;
    JPanel panel;

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
        listModel.addElement("empty faculty");
        JList<String> faculties = new JList<>(listModel);
        JScrollPane scrollableList = new JScrollPane(faculties);
        JLabel label = new JLabel("List of faculties");
        JButton addButton = new JButton("add");
        JTextField enterNewFaculty = new JTextField("Enter name of new faculty...");
        JPanel addNewFacultyPanel = new JPanel();
        addButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String text = enterNewFaculty.getText();
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

        JMenuItem generate = new JMenuItem("Generate!");
        JMenuItem view = new JMenuItem("View");
        JMenuItem removeAll = new JMenuItem("Remove all");
        menu.add(generate);
        menu.add(view);
        menu.add(removeAll);

        mb.add(menu);
        mb.add(faculties);
        mb.add(educationalPrograms);
        mb.add(subjects);
        mb.add(groups);
        mb.add(teachers);
        mb.add(auditories);

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

    public GenerateWindow() {
        frame = new JFrame("Generate Timetable");
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

    }
}
