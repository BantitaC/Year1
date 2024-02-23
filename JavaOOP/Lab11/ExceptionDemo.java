
public class ExceptionDemo {
    public static void main(String[] args) {
        try{
            double a = Double.parseDouble(args[0]);
            double b = Double.parseDouble(args[1]);
            double c = Double.parseDouble(args[2]);
            double x1 = (-b + Math.sqrt(Math.pow(b, 2) - (4 * a * c))) / (2 * a);
            double x2 = (-b - Math.sqrt(Math.pow(b, 2) - (4 * a * c))) / (2 * a);
            System.out.println("x1: " + x1);
            System.out.println("x2: " + x2);
        }
        catch(NumberFormatException e){
            System.out.println("Please input data in number format only.");
        }
        catch(Exception e){
            System.out.println("Please enter 3 numbers as a, b, and"
                    + " c respectively.”");
        }
    }
}
