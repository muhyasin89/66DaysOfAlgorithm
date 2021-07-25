package Practice.LinkedList;

import java.util.List;
import java.util.Arrays;

public class LinkedList {

    void printListInteger(List<Integer> nums) {
        for (Integer s : nums) {
            int i = nums.indexOf(s);
            System.out.print("-> " + s);
            // System.out.println("Item " + i + " : " + s);
        }
        System.out.println();
    }

    public static void main(String[] args) {
        // ArrayList<Integer> firstList = new ArrayList<>();
        // [2, 4, 1, 5, 3, 7, 10, 8, 9];
        List<Integer> list_1 = Arrays.asList(2, 4, 1, 5, 3, 7, 10, 8, 9);

        LinkedList list_a = new LinkedList();
        list_a.printListInteger(list_1);

        // [4, 3, 1, 10, 5, 7, 6, 8, 9];
        List<Integer> list_2 = Arrays.asList(4, 3, 1, 10, 5, 7, 6, 8, 9);

        LinkedList list_b = new LinkedList();
        list_b.printListInteger(list_2);
    }
}