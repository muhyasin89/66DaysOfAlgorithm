package Basic.ConvertStringToList;

import java.util.*;
import java.util.stream.Collectors;

public class Solution {

    public static List<Character> convertStringToCharList(String str) {

        // Create an empty List of character
        List<Character> chars = str

                // Convert to String to IntStream
                .chars()

                // Convert IntStream to Stream<Character>
                .mapToObj(e -> (char) e)

                // Collect the elements as a List Of Characters
                .collect(Collectors.toList());

        // return the List
        return chars;
    }

    void printListInteger(ArrayList<Integer> nums) {
        for (Integer s : nums) {
            int i = nums.indexOf(s);
            // System.out.print(" "+s);
            System.out.println("Item " + i + " : " + s);
        }
        System.out.println();
    }

    void printListChar(List<Character> list_chars) {
        for (Character s : list_chars) {
            int i = list_chars.indexOf(s);
            // System.out.print(" "+s);
            System.out.println("Item " + i + " : " + s);
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

        Solution list_a = new Solution();
        list_a.printListInteger(firstList);

        String s = "Welcome";
        List<Character> string_a = list_a.convertStringToCharList(s);
        list_a.printListChar(string_a);

        // int[] list_2= [4, 3, 1, 10, 5, 7, 6, 8, 9];
        ArrayList<Integer> secondList = new ArrayList<>();
        // System.out.println(list_2);
    }

}