
package Lab12;

import java.awt.*;
import java.awt.event.*;
import java.io.*;
import javax.swing.*;

public class StudentView implements ActionListener, WindowListener {
    private JFrame fr;
    private JPanel p1, p2;
    private JLabel lbl1, lbl2, lbl3;
    private JTextField txt1, txt2, txt3;
    private JButton btn1, btn2;
    private File file;
    private Student ppl;
    
    public StudentView(){
        fr = new JFrame();
        p1 = new JPanel();
        p2 = new JPanel();
        ppl = new Student();
        lbl1 = new JLabel(" ID: ");
        lbl2 = new JLabel(" Name: ");
        lbl3 = new JLabel(" Money: ");
        txt1 = new JTextField();
        txt2 = new JTextField();
        txt3 = new JTextField(String.valueOf(ppl.getMoney()));
        btn1 = new JButton("Deposit");
        btn2 = new JButton("Withdraw");
        
        btn1.addActionListener(this);
        btn2.addActionListener(this);
        
        txt3.setEditable(false);
        
        p1.setLayout(new GridLayout(3, 2));
        p1.add(lbl1);
        p1.add(txt1);
        p1.add(lbl2);
        p1.add(txt2);
        p1.add(lbl3);
        p1.add(txt3);
        
        fr.add(p1, BorderLayout.NORTH);
        
        p2.setLayout(new FlowLayout());
        p2.add(btn1);
        p2.add(btn2);
        
        fr.add(p2, BorderLayout.CENTER);
        
        fr.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        fr.pack();
        fr.setVisible(true);
        
        file = new File("Student.dat");
        try {
            file.createNewFile();
        }
        catch(IOException e){
            e.printStackTrace();
        }
        fr.addWindowListener(this);
    }
    
    @Override
    public void actionPerformed(ActionEvent ae){
        if(ae.getSource().equals(btn1)){
            ppl.setMoney(ppl.getMoney() + 100);
            txt3.setText(String.valueOf(ppl.getMoney()));
        }
        else if(ae.getSource().equals(btn2)){
            if(ppl.getMoney() <= 0){
                ppl.setMoney(0);
            }
            else if(ppl.getMoney() >= 100){
                ppl.setMoney(ppl.getMoney() - 100);
                txt3.setText(String.valueOf(ppl.getMoney()));
            }
        }
    }
    
    @Override
    public void windowOpened(WindowEvent we){
        try(FileInputStream fi = new FileInputStream(file); ObjectInputStream oi = new ObjectInputStream(fi);){
            ppl = (Student) oi.readObject();
            if(ppl == null){
                ppl = new Student();
                ppl.setID(-1);
            }
        }
        catch(IOException | ClassNotFoundException e){
            e.printStackTrace();
        }
        if(ppl.getID() == -1){
            txt1.setText("");
        }
        else{
            txt1.setText(String.valueOf(ppl.getID()));
        }
        txt2.setText(ppl.getName());
        txt3.setText(String.valueOf(ppl.getMoney()));
    }
    
    @Override
    public void windowClosing(WindowEvent e){
        if(txt1.getText().equals("")){
            ppl.setID(-1);
        }
        else{
            ppl.setID(Integer.parseInt(txt1.getText()));
        }
        ppl.setName(txt2.getText());
        ppl.setMoney(Integer.parseInt(txt3.getText()));
        try(FileOutputStream fo = new FileOutputStream(file); ObjectOutputStream ou = new ObjectOutputStream(fo);){
            ou.writeObject(ppl);
        }
        catch(IOException ex){
            ex.printStackTrace();
        }
    }
    
    @Override
    public void windowActivated(WindowEvent we){}
    
    @Override
    public void windowDeactivated(WindowEvent we){}
    
    @Override
    public void windowClosed(WindowEvent we){}
    
    @Override
    public void windowIconified(WindowEvent we){}
    
    @Override
    public void windowDeiconified(WindowEvent we){}
}
