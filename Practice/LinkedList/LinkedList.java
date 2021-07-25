package Practice.LinkedList;

import java.util.ArrayList;

public class LinkedList {

    void printListInteger(ArrayList<Integer> nums) {
        for (Integer s : nums) {
            int i = nums.indexOf(s);
            System.out.print("-> " + s);
            // System.out.println("Item " + i + " : " + s);
        }
        System.out.println();
    }

    public static void main(String[] args) {
        ArrayList<Integer> firstList = new ArrayList<>();
        // [2, 4, 1, 5, 3, 7, 10, 8, 9];
        firstList.add(2);
        firstList.add(4);
        firstList.add(1);
        firstList.add(5);
        firstList.add(3);
        firstList.add(7);
        firstList.add(10);
        firstList.add(8);
        firstList.add(9);

        LinkedList list_a = new LinkedList();
        list_a.printListInteger(firstList);

        ArrayList<Integer> secondList = new ArrayList<>();
        // int[] list_2= [4, 3, 1, 10, 5, 7, 6, 8, 9];
        secondList.add(4);
        secondList.add(3);
        secondList.add(1);
        secondList.add(10);
        secondList.add(5);
        secondList.add(7);
        secondList.add(6);
        secondList.add(8);
        secondList.add(9);

        LinkedList list_b = new LinkedList();
        list_b.printListInteger(secondList);
    }
}