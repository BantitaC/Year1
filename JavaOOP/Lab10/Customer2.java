
package Lab10;
import java.util.*;
public class Customer2 {
    private String firstName;
    private String lastName;
    private ArrayList acct;
    private int numOfAccount;
    public Customer2(){
        this("", "");
        acct = new ArrayList();
    }
    public Customer2(String firstName, String lastName){
        this.firstName = firstName;
        this.lastName = lastName;
        acct = new ArrayList();
    }
    public void setFirstName(String firstName){
        this.firstName = firstName;
    }
    public String getFirstName(){
        return firstName;
    }
    public void setLastName(String lastName){
        this.lastName = lastName;
    }
    public String getLastName(){
        return lastName;
    }
    public Account getAccount(int index){
        return ((Account) acct.get(index));
    }
    public void addAccount(Account acct){
        this.acct.add(acct);
    }
    public int getNumOfAccount(){
        return acct.size();
    }
    @Override
    public String toString(){
        if(acct == null){
            return firstName + " " + lastName + " doesn’t have account.";
        }
        else{
            return this.firstName + " " + this.lastName + " has " + numOfAccount
                    + " Account.";
        }
    }
    public boolean equals(Customer2 c){
        return (this.firstName.equals(c.firstName)) & 
                (this.lastName.equals(c.lastName));
    }
}