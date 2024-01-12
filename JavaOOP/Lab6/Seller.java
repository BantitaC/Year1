package Lab6;
public class Seller extends Employee {
    public Food sell(Employee e){
        Food f = new Food();
        double price = f.getPrice();
        if(e.getWallet().getBalance() >= f.getPrice()){
            this.getWallet().setBalance(this.getWallet().getBalance() + price);
            e.getWallet().setBalance(e.getWallet().getBalance() - price);
            return f;
        }
        else{
            System.out.println("Your money is not enough.");
            return null;
        }
    }
}