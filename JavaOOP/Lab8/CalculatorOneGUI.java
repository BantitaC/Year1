
package Lab8;
import java.awt.*;
import javax.swing.*;
public class CalculatorOneGUI {
    private JFrame fr;
    private JPanel p;
    private JLabel lbl;
    private JTextField txt, txt1, txt2;
    private JButton btn1, btn2, btn3, btn4;
    public CalculatorOneGUI(){
        fr = new JFrame("Calculator");
        p = new JPanel();
        txt = new JTextField();
        txt1 = new JTextField();
        txt2 = new JTextField();
        lbl = new JLabel();
        btn1 = new JButton("Add");
        btn2 = new JButton("Substract");
        btn3 = new JButton("Multiply");
        btn4 = new JButton("Divide");
        
        txt1.setEditable(false);
        
        fr.setLayout(new GridLayout(4, 1));
        p.setLayout(new FlowLayout());
        p.add(btn1);
        p.add(btn2);
        p.add(btn3);
        p.add(btn4);
        fr.add(txt);
        fr.add(txt2);
        fr.add(p);
        fr.add(txt1);
        
        fr.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        fr.pack();
        fr.setVisible(true);
    }
}
