package JAVA.basic;

import java.util.*;


public class javaEndOfFile {
    /*public static void main(String[] args) {
        
        Scanner userInput = new Scanner(System.in);
        int count = 1;

        while (!(userInput.nextLine()).isEmpty()) {
            System.out.println(count + " " + userInput.nextLine());
            count++;
        }


        userInput.close();
    }*/

    //alternative 2
    public static void main(String[] args) {
       
        Scanner userInput = new Scanner(System.in);
        int count = 1;

        while (userInput.hasNext()) {
            System.out.println(count + " " + userInput.nextLine());
            count++;
        }
    }

    // alternative 3
    public static void main(String[] args) {
        Scanner userInput = new Scanner(System.in);
        int count = 1;

        for(int i = 0; userInput.hasNext() == true; i++ ){
            System.out.println(i +" "+userInput.nextLine());
 
        }
    }
}
