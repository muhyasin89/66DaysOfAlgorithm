package hackerRankGroup;

import java.util.Scanner;

public class EndOfFile {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        int loopInt = 0;
        
        while(scan.hasNext()){
            ++loopInt;
            System.out.println(loopInt+"."+scan.next());
            
        }

        scan.close();


        //alternative 2
        // Scanner scan = new Scanner(System.in);
        // for (int i = 1; scan.hasNext(); i++) {
        //     System.out.println(i++ + " " + scan.nextLine());
        // }
    }
}