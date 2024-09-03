
import java.util.ArrayList;

public class CustomArray {

    private ArrayList<Integer> array;
    public CustomArray(){
        this.array=new ArrayList<>();
    }

    public void addLast(int element){
        array.add(element);
    }

    public void addFirst(int element){
        array.add(0,element);
    }

    public void addAtPosition(int index, int element){
        if(index>=0 && index<=array.size()){
            array.add(index,element);

        }
        else{
            System.out.println("invalid index");
        }

    }


    public void deleteFirst(){
        if(!array.isEmpty() ){
            array.remove(0);
        }
        else{
            System.out.println("invalid index");
        }
    }
    

    public void deleteLast(){
        if(!array.isEmpty() ){
            array.remove(array.size() -1);
        }
    }


    public void deleteAtPosition(int index){
        if( index>=0&& index<array.size()){
            array.remove(index);
        }
    }

    

public static void main(String[] args){
    CustomArray arr=new CustomArray();
    // // adding element in last 
    // arr.addLast(2);
    // arr.addLast(3);
    // arr.addLast(4);

    // // adding element in the first
    // arr.addFirst(1);

    // adding atposition in the array
    arr.addAtPosition(0,10);
    arr.addAtPosition(1,20);
    arr.addAtPosition(2,30);
    arr.addAtPosition(3,40);
    arr.addAtPosition(7,40);

    // deleting the first element
    // arr.deleteFirst();
    // arr.deleteLast();
    arr.deleteAtPosition(1);

    System.out.println(arr.array);

}
}




