
import java.util.ArrayList;

public class CustomArray {

    private ArrayList<Integer> array;
    public CustomArray(){
        this.array=new ArrayList<>();
    }

    public void addLast(int element){
        array.add(element);
    }

public static void main(String[] args){
    CustomArray arr=new CustomArray();
    arr.addLast(1);
    arr.addLast(2);
    arr.addLast(4);

    System.out.println(arr.array);
}
}