
public class Student {
    public String name;
    public double mScore;
    public double fScore;
    public void showGrade(){
        double s = (mScore * 0.4) + (fScore * 0.4) + 20;
        if (s < 50){
            System.out.println("Your grade is F.");
        }
        else if ((s >= 50) & (s < 60)){
            System.out.println("Your grade is D.");
        }
        else if ((s >= 60) & (s < 70)){
            System.out.println("Your grade is C.");
        }
        else if ((s >= 70) & (s < 80)){
            System.out.println("Your grade is D.");
        }
        else{
            System.out.println("Your grade is A.");
        }
    }
}