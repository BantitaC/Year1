
package Lab9;
import java.awt.event.*;
import java.awt.*;
import javax.swing.*;
public class TellerGUI implements ActionListener {
    private JFrame fr;
    private JPanel p, p1;
    private JTextField txt, txt1;
    private JLabel lbl, lbl1, lbl2;
    private JButton btn1, btn2, btn3;
    private double balance;
    
    public TellerGUI(){
        fr = new JFrame("Teller GUI");
        p = new JPanel();
        p1 = new JPanel();
        txt = new JTextField();
        txt1 = new JTextField(String.valueOf(balance));
        lbl = new JLabel();
        lbl1 = new JLabel("Balance");
        lbl2 = new JLabel("Amount");
        btn1 = new JButton("Deposit");
        btn2 = new JButton("Withdraw");
        btn3 = new JButton("Exit");
        
        btn1.addActionListener(this);
        btn2.addActionListener(this);
        btn3.addActionListener(this);
        
        txt1.setEditable(false);

        fr.setLayout(new GridLayout(3,1));
        p.setLayout(new GridLayout(2,2));
        p.add(lbl1);
        p.add(txt1);
        p.add(lbl2);
        p.add(txt);
        p1.setLayout(new FlowLayout());
        p1.add(btn1);
        p1.add(btn2);
        p1.add(btn3);
        fr.add(p);
        fr.add(p1);
        
        fr.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        fr.pack();
        fr.setVisible(true);
    }
    
    @Override
    public void actionPerformed(ActionEvent ae){
        if(ae.getSource().equals(btn1)){
            balance += Double.parseDouble(txt.getText());
            txt1.setText(String.valueOf(balance));
        }
        if(ae.getSource().equals(btn2)){
            if(balance >= Double.parseDouble(txt.getText())){
                balance -= Double.parseDouble(txt.getText());
                txt1.setText(String.valueOf(balance));
            }
        }
        if(ae.getSource().equals(btn3)){
            System.exit(0);
        }
    }
    
}
