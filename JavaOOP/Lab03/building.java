
package Lab03;
import java.util.*;
public class building {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Input height of building: ");
        int height = input.nextInt();
        
        for (int i = 1; i<=height; i+=1){
            System.out.println("#-#-#-#-#");
        }
    }
}
