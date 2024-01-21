
public class Player {
    private Houses houses;
    private int hp = 20;
    private int mana = 50;
    private final int attackDamage = 2;
    private final String name;
    public Player(){
        this("", 0);
        this.houses = null;
        this.mana = 50;
    }
    public Player(String name){
        this(name, 20);
    }
    public Player(String name, int hp){
        this.name = name;
        this.hp = hp;
        this.houses = null;
        this.mana = 50;
    }
    public int getAttackDamage(){
        return attackDamage;
    }
    public int getHP(){
        return hp;
    }
    public Houses getHouses(){
        return houses;
    }
    public int getMana(){
        return mana;
    }
    public String getName(){
        return name;
    }
    public void setHP(int hp){
        if(hp < 0){
            this.hp = 0;
        }
        else if(hp > 20){
            this.hp = 20;
        }
        else{
            this.hp = hp;
        }
    }
    public void setHouses(Houses houses){
        this.houses = houses;
    }
    public void setMana(int mana){
        if(mana < 0){
            this.mana = 0;
        }
        else if(mana > 50){
            this.mana = 50;
        }
        else{
            this.mana = mana;
        }
    }
    public void attack(Player target, Spell spell){
        if(houses instanceof Gryffindor){
            ((Gryffindor) houses).attackSpell(this, target, spell);
        }
        else if(houses instanceof Hufflepuff){
            ((Hufflepuff) houses).attackSpell(this, target, spell);
        }
        if(target.getHP() == 0){
            System.out.println("[DEAD]: " + target.getName() + 
                    " was killed by " + this.name);
        }
    }
    public boolean equals(Player player){
        return (player.name.equals(this.name)) 
                && (player.houses.equals(this.houses));
    }
    public void protectFromPlayer(Player target){
        if(houses instanceof Gryffindor){
            ((Gryffindor) houses).defense(this, target);
        }
        else if(houses instanceof Hufflepuff){
            ((Hufflepuff) houses).defense(this, target);
        }
    }
    @Override
    public String toString(){
        return "[Player] : " + this.name + " HP : " + this.hp + " Mana: "
                + this.mana + " || " + this.houses;
    }
        
}
