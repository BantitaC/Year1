
package Lab10;
public class Customer {
    private String firstName;
    private String lastName;
    private Account acct[];
    private int numOfAccount;
    public Customer(){
        this("", "");
        acct = new Account[5];
    }
    public Customer(String firstName, String lastName){
        this.firstName = firstName;
        this.lastName = lastName;
        acct = new Account[5];
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
    public void setAcct(Account acct){
        this.acct[numOfAccount] = acct;
    }
    public Account getAcct(){
        return acct[numOfAccount];
    }
    public Account getAccount(int index){
        return this.acct[index];
    }
    public void addAccount(Account acct){
        this.acct[numOfAccount] = acct;
        numOfAccount++;
    }
    public int getNumOfAccount(){
        return numOfAccount;
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
    public boolean equals(Customer c){
        return (this.firstName.equals(c.firstName)) & 
                (this.lastName.equals(c.lastName));
    }
}