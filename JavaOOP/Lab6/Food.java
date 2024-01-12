package Lab6;
public class Food {
    private static final int energy = 10;
    private static double price = 50;
    public static void setPrice(double price){
        if(price > Food.price){
            Food.price = price;
        }
        else{
            System.out.println("Cannot update the food price.");
        }
    }
    public static double getPrice(){
        return price;
    }
    public static int getEnergy(){
        return energy;
    }
}