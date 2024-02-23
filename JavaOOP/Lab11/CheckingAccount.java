public class CheckingAccount extends Account {
    private double credit;
    public CheckingAccount(){
        super(0, "");
        this.credit = 0;
    }
    public CheckingAccount(double balance, String name, double credit){
        super(balance, name);
        this.credit = credit;
    }
    public void setCredit(double credit){
        if(credit > 0){
            this.credit = credit;
        }
        else{
            System.out.println("Input number must be a positive integer.");
        }
    }
    public double getCredit(){
        return credit;
    }
    @Override
    public void withdraw(double a) throws WithdrawException {
        if(a > 0){
            if(getBalance() - a > 0){
                setBalance(getBalance() - a);
                System.out.println(a + " baht is withdrawn from " + 
                        this.getName() + " and your credit balance is " 
                        + this.credit + ".");
            } else if (getBalance() - a + credit > 0) {
                this.credit = credit - Math.abs(getBalance() - a);
                System.out.println(a + " baht is withdrawn from " 
                        + this.getName() + " and your credit balance is " 
                        + this.credit + ".");
                this.setBalance(0);
            } else {
                throw new WithdrawException("Account " + getName() 
                        + " has not enough money.");
            }
        }
    }
    public void withdraw(String a) throws WithdrawException {
        this.withdraw(Double.parseDouble(a));
    }
    public String toString(){
        return "The " + getName() + " account has " + getBalance() + 
                " baht and " + credit + " credits.";
    }
}