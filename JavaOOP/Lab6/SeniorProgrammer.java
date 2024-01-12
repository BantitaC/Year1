package Lab6;
public class SeniorProgrammer extends Programmer {
    public void coding(String str){
        if(getEnergy() >= 10){
            System.out.println("I'm coding about " + str);
            setEnergy(getEnergy() - 5);
            setHappiness(getHappiness() - 5);
        }
        else{
            System.out.println("ZzZzZz");
            setEnergy(getEnergy() - 5);
            setHappiness(getHappiness() - 5);
        }
    }
    public void coding(String str, int num){
        for(int i = 0; i < num; i++){
            this.coding(str);
        }
    }
    public void compliment(Programmer p){
        p.setHappiness(p.getHappiness() + 20);
        System.out.println(p.getName() + " in a good mood");
    }
    public void blame(Programmer p){
        p.setHappiness(p.getHappiness() - 20);
        System.out.println(p.getName() + " in a bad mood");
    }
}