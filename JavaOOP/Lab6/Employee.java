package Lab6;
public class Employee {
    private static String nationality = "Thai";
    private String name;
    private Wallet wallet;
    private int energy;
    public boolean equals(Employee e){
        return e.name == this.name;
    }
    public String toString(){
        return "My name is " + name + ". \n" + "I have " + energy +
                " energy left.\n" + "I have a balance of " + 
                wallet.getBalance() + " baht.";
    }
    public boolean buyFood(Seller s){
       Food f = s.sell(this);
       if(f != null){
           this.eat(f);
           return true;
       }
       else{
           return false;
       }
    }
    public void eat(Food f){
        this.energy += f.getEnergy();
    }
    public String getName(){
        return name;
    }
    public void setName(String name){
        this.name = name;
    }
    public Wallet getWallet(){
        return wallet;
    }
    public void setWallet(Wallet wallet){
        this.wallet = wallet;
    }
    public int getEnergy(){
        return energy;
    }
    public void setEnergy(int energy){
        this.energy = energy;
    }
    public static String getNationality(){
        return nationality;
    }
    public static void setNationality(String nationality){
        Employee.setNationality(nationality);
    }
}