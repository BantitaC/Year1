
public class Account {
    public double balance;
    public String name;
    public void deposit(double b){
        if(b >= 0){
            balance += b;
        }
        else{
            System.out.println("The balance variable must be greather than"
                    + " or equal to zero.");
        }
    }
    public double withdraw(double b){
        if(balance < 0){
            System.out.println("The balance variable must be greather than "
                        + "or equal to zero.");
            return 0;
        }
        else if(b <= balance & b >= 0){
            balance -= b;
            return balance;
        }
        else{
            System.out.println("Your account balance is insufficient.");
            return 0;
        }
    }
    public void showInfo(){
        System.out.println("In " + name + " account, there is a balance equal "
                + "to " + balance + " baht. ");
    }
}