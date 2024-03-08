
package Lab12;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.io.*;
import java.time.*;
import java.time.format.*;

public class ChatDemo implements ActionListener, WindowListener {
    private JFrame fr;
    private JPanel p;
    private JTextArea txt;
    private JTextField txtf;
    private JButton btn1, btn2;
    private File file;
    
    public ChatDemo(){
        fr = new JFrame("ChatDemo");
        p = new JPanel();
        txt = new JTextArea(45, 20);
        txtf = new JTextField(45);
        btn1 = new JButton("Submit");
        btn2 = new JButton("Reset");
        
        fr.setLayout(new BorderLayout());
        txt.setEditable(false);
        fr.add(txt, BorderLayout.NORTH);
        fr.add(txtf, BorderLayout.CENTER);
        
        p.add(btn1);
        p.add(btn2);
        fr.add(p, BorderLayout.SOUTH);
        
        btn1.addActionListener(this);
        btn2.addActionListener(this);
        
        fr.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        fr.pack();
        fr.setVisible(true);
        
        file = new File("ChatDemo.dat");
        try {
            file.createNewFile();
        }
        catch(IOException e) {
            e.printStackTrace();
        }
        fr.addWindowListener(this);
    }
    
    @Override
    public void actionPerformed(ActionEvent ae){
        if (ae.getSource().equals(btn1)){
            DateTimeFormatter dt = DateTimeFormatter.ofPattern("yyyy/MM/dd HH:mm:ss : ");
            txt.setText(txt.getText() + "\n" + dt.format(LocalDateTime.now()) +
                    txtf.getText());
            txtf.setText("");
        }
        else if(ae.getSource().equals(btn2)) {
            txt.setText("");
        }
    }
    
    @Override
    public void windowOpened(WindowEvent we){
        String txtt = "";
        try(FileReader fr = new FileReader(file)){
            int tmp;
            while ((tmp = fr.read()) != -1){
                txtt += (char) tmp;
            }
        }
        catch (IOException e){
            e.printStackTrace();
        }
        txt.setText(txtt);
    }
    
    @Override
    public void windowClosing(WindowEvent we){
        try(FileWriter fw = new FileWriter(file)){
            fw.write(txt.getText());
        }
        catch(IOException e) {
            e.printStackTrace();
        }
    }
    
    @Override
    public void windowClosed(WindowEvent we){}
    
    public void windowActivated(WindowEvent we){}
    
    public void windowDeactivated(WindowEvent we){}
    
    public void windowDeiconified(WindowEvent we){}
    
    public void windowIconified(WindowEvent we){}
}
