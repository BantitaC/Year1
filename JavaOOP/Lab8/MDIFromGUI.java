
package Lab8;
import java.awt.*;
import javax.swing.*;
public class MDIFromGUI extends JFrame {
    private JFrame fr;
    private JMenu m1, m2, m3, m4;
    private JMenuBar mb;
    private JMenuItem mi1, mi2, mi3, mi4, mi5;
    private JDesktopPane desktopPane;
    private JInternalFrame mainframe, frame1, frame2, frame3;
    
    public MDIFromGUI(){
        desktopPane = new JDesktopPane();
        mainframe = new JInternalFrame("SubMenuItem Demo", true, 
        true, true, true);
        frame1 = new JInternalFrame("Application 01", true, 
        true, true, true);
        frame2 = new JInternalFrame("Application 02", true, 
        true, true, true);
        frame3 = new JInternalFrame("Application 03", true, 
        true, true, true);
        
        frame1.pack();
        frame1.setVisible(true);
        
        frame2.pack();
        frame2.setVisible(true);
       
        frame3.pack();
        frame3.setVisible(true);
        
        int x2 = frame1.getX() + frame1.getWidth() + 10;
        int y2 = frame1.getY();
        frame2.setLocation(x2, y2);
        
        int x3 = frame2.getX() + frame2.getWidth() + 10;
        int y3 = frame2.getY();
        frame3.setLocation(x3, y3);
        
        desktopPane.add(mainframe);
        desktopPane.add(frame1);
        desktopPane.add(frame2);
        desktopPane.add(frame3);
        
        fr = new JFrame("SubMenuItem Demo");
        fr.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        mb = new JMenuBar();
        m1 = new JMenu("File");
        m2 = new JMenu("Edit");
        m3 = new JMenu("VIew");
        m4 = new JMenu("New");
        
        mainframe.setJMenuBar(mb);
        mb.add(m1);
        mb.add(m2);
        mb.add(m3);
        
        mi1 = new JMenuItem("Window");
        mi2 = new JMenuItem("Message");
        mi3 = new JMenuItem("Open");
        mi4 = new JMenuItem("Save");
        mi5 = new JMenuItem("Exit");
        
        m1.add(m4);
        m4.add(mi1);
        m4.addSeparator();
        m4.add(mi2);
        m1.add(mi3);
        m1.addSeparator();
        m1.add(mi4);
        m1.addSeparator();
        m1.add(mi5);
        
        fr.getContentPane().add(desktopPane);
        fr.getContentPane().add(mainframe);
        
        this.add(desktopPane, BorderLayout.CENTER);
        this.setMinimumSize(new Dimension(300, 300));
        this.pack();
        this.setVisible(true);
       
        fr.pack();
        fr.setVisible(true);
    }
}
