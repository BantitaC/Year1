
public class Fraction {
    public int topN;
    public int btmN;
    public String toFraction(){
        return Integer.toString(topN) + "/" + Integer.toString(btmN);
    }
    public String toFloat(){
        double ftop = topN;
        double fbtm = btmN;
        String result = Double.toString(ftop / fbtm);
        return result;
    }
    public void addFraction(Fraction f){
        if(btmN == f.btmN){
            topN += f.topN;
        }
        else{
            topN = topN * f.btmN + f.topN * btmN;
            btmN = btmN * f.btmN;
        }
    }
}