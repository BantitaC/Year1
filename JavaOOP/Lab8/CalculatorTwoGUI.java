
package Lab8;
import java.awt.*;
import javax.swing.*;
    public class CalculatorTwoGUI {
    private JFrame fr;
    private JPanel p1, p2;
    private JTextField txt;
    public CalculatorTwoGUI(){
        fr = new JFrame("My Calculator");
        p1 = new JPanel();
        p2 = new JPanel();
        txt = new JTextField();
        
        p1.setLayout(new GridLayout(4, 4));
        p1.add(new JButton("7"));
        p1.add(new JButton("8"));
        p1.add(new JButton("9"));
        p1.add(new JButton("+"));
        p1.add(new JButton("4"));
        p1.add(new JButton("5"));
        p1.add(new JButton("6"));
        p1.add(new JButton("-"));
        p1.add(new JButton("1"));
        p1.add(new JButton("2"));
        p1.add(new JButton("3"));
        p1.add(new JButton("x"));
        p1.add(new JButton("0"));
        p1.add(new JButton("c"));
        p1.add(new JButton("="));
        p1.add(new JButton("/"));
        
        fr.setLayout(new BorderLayout());
        fr.add(txt, BorderLayout.NORTH);
        fr.add(p1);
        
        fr.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        fr.pack();
        fr.setVisible(true);
    }
}
