
package Lab9;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
public class CalculatorSample implements ActionListener {
    private JFrame fr;
    private JPanel p1, p2;
    private JTextField txt;
    private JButton btn0, btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9,
            addBtn, minusBtn, multiplyBtn, divideBtn, reBtn, resultBtn ;
    
    int num1 = 0, num2 = 0, result = 0;
    char opr;
    
    public CalculatorSample(){
        fr = new JFrame("My Calculator");
        p1 = new JPanel();
        p2 = new JPanel();
        txt = new JTextField();
        btn0 = new JButton("0");
        btn1 = new JButton("1");
        btn2 = new JButton("2");
        btn3 = new JButton("3");
        btn4 = new JButton("4");
        btn5 = new JButton("5");
        btn6 = new JButton("6");
        btn7 = new JButton("7");
        btn8 = new JButton("8");
        btn9 = new JButton("9");
        addBtn = new JButton("+");
        minusBtn = new JButton("-");
        multiplyBtn = new JButton("x");
        divideBtn = new JButton("/");
        reBtn = new JButton("c");
        resultBtn = new JButton("=");
        
        btn0.addActionListener(this);
        btn1.addActionListener(this);
        btn2.addActionListener(this);
        btn3.addActionListener(this);
        btn4.addActionListener(this);
        btn5.addActionListener(this);
        btn6.addActionListener(this);
        btn7.addActionListener(this);
        btn8.addActionListener(this);
        btn9.addActionListener(this);
        addBtn.addActionListener(this);
        minusBtn.addActionListener(this);
        multiplyBtn.addActionListener(this);
        divideBtn.addActionListener(this);
        reBtn.addActionListener(this);
        resultBtn.addActionListener(this);
        
        p1.setLayout(new GridLayout(4, 4));
        p1.add(btn7);
        p1.add(btn8);
        p1.add(btn9);
        p1.add(addBtn);
        p1.add(btn4);
        p1.add(btn5);
        p1.add(btn6);
        p1.add(minusBtn);
        p1.add(btn1);
        p1.add(btn2);
        p1.add(btn3);
        p1.add(multiplyBtn);
        p1.add(btn0);
        p1.add(reBtn);
        p1.add(resultBtn);
        p1.add(divideBtn);
        
        fr.setLayout(new BorderLayout());
        fr.add(txt, BorderLayout.NORTH);
        fr.add(p1);
        
        fr.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        fr.setSize(500, 400);
        fr.setVisible(true);
    }
    
    @Override
    public void actionPerformed(ActionEvent ae){
        if(ae.getSource().equals(btn0)){
            txt.setText(txt.getText().concat("0"));
        }
        if(ae.getSource().equals(btn1)){
            txt.setText(txt.getText().concat("1"));
        }
        if(ae.getSource().equals(btn2)){
            txt.setText(txt.getText().concat("2"));
        }
        if(ae.getSource().equals(btn3)){
            txt.setText(txt.getText().concat("3"));
        }
        if(ae.getSource().equals(btn4)){
            txt.setText(txt.getText().concat("4"));
        }
        if(ae.getSource().equals(btn5)){
            txt.setText(txt.getText().concat("5"));
        }
        if(ae.getSource().equals(btn6)){
            txt.setText(txt.getText().concat("6"));
        }
        if(ae.getSource().equals(btn7)){
            txt.setText(txt.getText().concat("7"));
        }
        if(ae.getSource().equals(btn8)){
            txt.setText(txt.getText().concat("8"));
        }
        if(ae.getSource().equals(btn9)){
            txt.setText(txt.getText().concat("9"));
        }
        if(ae.getSource().equals(addBtn)){
            num1 = Integer.parseInt(txt.getText());
            opr = '+';
            txt.setText("");
        }
        if(ae.getSource().equals(minusBtn)){
            num1 = Integer.parseInt(txt.getText());
            opr = '-';
            txt.setText("");
        }
        if(ae.getSource().equals(multiplyBtn)){
            num1 = Integer.parseInt(txt.getText());
            opr = 'x';
            txt.setText("");
        }
        if(ae.getSource().equals(divideBtn)){
            num1 = Integer.parseInt(txt.getText());
            opr = '/';
            txt.setText("");
        }
        if(ae.getSource().equals(reBtn)){
            txt.setText("");
        }
        if(ae.getSource().equals(resultBtn)){
            num2 = Integer.parseInt(txt.getText());
            
            switch(opr){
                case '+':
                    result = num1 + num2;
                    break;
                case '-':
                    result = num1 - num2;
                    break;
                case 'x':
                    result = num1 * num2;
                    break;
                case '/':
                    result = num1 / num2;
                    break;
            }
            txt.setText(String.valueOf(result));
            num1 = result;
        }
    }
}
