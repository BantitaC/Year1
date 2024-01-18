
package Lab7;
public class CheckingAccountRun {
    public static void main(String[] args) {
        CheckingAccount a1 = new CheckingAccount(50000,"61070033",5000);
        a1.showAccount();
        a1.deposit(500);
        System.out.println(a1);
        a1.withdraw("40000.00");
        System.out.println(a1.toString());
    }
}

//public class CheckingAccountRun {
//    public static void main(String[] args) {
//        CheckingAccount a1 = new CheckingAccount();
//        a1.deposit(500);
//        System.out.println(a1);
//        a1.withdraw(40000.0);
//        System.out.println(a1.toString());
//    }
//}

//public class CheckingAccountRun {
//    public static void main(String[] args) {
//        Account a1 = new CheckingAccount();
//        a1.setCredit(1000);
//        System.out.println(a1);
//    }
//}

//public class CheckingAccountRun {
//    public static void main(String[] args) {
//        Account a1 = new CheckingAccount();
//        a1.setName("Nook");
//        System.out.println(a1);
//        ((CheckingAccount)a1).setCredit(1000);
//        System.out.println(a1); }
//}
