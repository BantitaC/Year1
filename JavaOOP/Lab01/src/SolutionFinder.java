
public class SolutionFinder {
    public static void main(String[] args) {
        double a = 4;
        double b = 8;
        double c = 3;
        double one = (-b + (Math.sqrt(Math.pow(b, 2) - (4 * a * c)))) / (2 * a);
        double two = (-b - (Math.sqrt(Math.pow(b, 2) - (4 * a * c)))) / (2 * a);
        System.out.println(one);
        System.out.println(two);
    }
}