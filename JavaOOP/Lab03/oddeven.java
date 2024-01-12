
package Lab03;
import java.util.*;
public class oddeven {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int num = input.nextInt();
        int odd = 0;
        int even = 0;
        while(num != -1){
            num = input.nextInt();
            if(num % 2 == 0){
                even += 1;
            }
            else{
                odd += 1;
            }
        }
        System.out.println("Odd number = " + odd + " and Even number = " + even);
    }
}
