package Lab6;
//public class Lab6Run {
//    public static void main(String[] args) {
//        Wallet w1 = new Wallet();
//        Wallet w2 = new Wallet();
//        w1.setBalance(200);
//        w2.setBalance(100);
//
//        Seller s1 = new Seller();
//        s1.setName("Peter");
//        s1.setEnergy(100);
//        s1.setWallet(w1);
//
//        Employee e1 = new Employee();
//        e1.setName("Adam");
//        e1.setEnergy(100);
//        e1.setWallet(w2);
//
//        System.out.println(s1);
//        System.out.println(e1);
//        e1.buyFood(s1);
//        System.out.println(s1);
//        System.out.println(e1);
//    }
//}

//public class Lab6Run {
//    public static void main(String[] args) {
//        Wallet w1 = new Wallet();
//        Wallet w2 = new Wallet();
//        w1.setBalance(200);
//        w2.setBalance(100);
//
//        Programmer p1 = new Programmer();
//        p1.setName("Sara");
//        p1.setEnergy(100);
//        p1.setWallet(w1);
//        p1.setHappiness(100);
//
//        SeniorProgrammer sp1 = new SeniorProgrammer();
//        sp1.setName("Kim");
//        sp1.setEnergy(100);
//        sp1.setWallet(w2);
//        sp1.setHappiness(100);
//
//        System.out.println(p1 + "\nHappiness : " +p1.getHappiness());
//        System.out.println(sp1 + "\nHappiness : " +sp1.getHappiness());
//        sp1.compliment(p1);
//        sp1.compliment(p1);
//        System.out.println(p1 + "\nHappiness : " +p1.getHappiness());
//        System.out.println(sp1 + "\nHappiness : " +sp1.getHappiness());
//        sp1.blame(p1);
//        System.out.println(p1 + "\nHappiness : " +p1.getHappiness());
//        System.out.println(sp1 + "\nHappiness : " +sp1.getHappiness());
//    }
//}

public class Lab6Run {
    public static void main(String[] args) {
        Wallet w1 = new Wallet();
        Wallet w2 = new Wallet();
        w1.setBalance(200);
        w2.setBalance(100);

        Programmer p1 = new Programmer();
        p1.setName("Boy");
        p1.setEnergy(100);
        p1.setWallet(w1);
        p1.setHappiness(100);

        SeniorProgrammer sp1 = new SeniorProgrammer();
        sp1.setName("Ploy");
        sp1.setEnergy(100);
        sp1.setWallet(w2);
        sp1.setHappiness(100);

        System.out.println(sp1 + "\nHappiness : " +sp1.getHappiness());
        sp1.coding('A');
        sp1.coding("Bugggggg");
        sp1.coding("Bugggggg",2);
        System.out.println(sp1 + "\nHappiness : " +sp1.getHappiness());
        System.out.println("---------------------------------");
        System.out.println(p1 + "\nHappiness : " +p1.getHappiness());
        p1.coding('B');
        p1.coding("Deathhhhhhhh");
        System.out.println(p1 + "\nHappiness : " +p1.getHappiness());
    }
}