import java.util.*;

public class Example {

    List<Integer> intValue(List<Integer> intList) {
        intList.add(1);
        intList.add(2);
        intList.add(3);

        return intList;
    }

    List<String> stringValue(List<String> stringList) {
        stringList.add("Mango");
        stringList.add("Apple");
        stringList.add("Banana");

        return stringList;
    }

    void printIntList(List<Integer> list) {
        // Iterating the List element using for-each loop
        for (Integer i : list) {
            System.out.println(i);

        }
    }

    void printStrList(List<String> list) {
        // Iterating the List element using for-each loop
        for (String i : list) {
            System.out.println(i);

        }
    }

    Integer changeToInt(List<Integer> list) {
        int a = 0;

        for (Integer i : list) {
            a = a + i;
        }

        return a;
    }

    String changeString(List<String> list) {
        String a = "";

        for (String i : list) {
            if (a != "") {
                a = a + " " + i;
            } else {
                a = a + i;
            }

        }

        return a;
    }

    int[] removeElement(int[] arr, int index) {
        if (arr == null || index < 0 || index > arr.length) {
            return arr;
        }

        int[] copyArray = new int[arr.length - 1];
        for (int i = 0, k = 0; i < arr.length; i++) {
            if (i == index) {
                continue;
            }

            copyArray[k++] = arr[i];
        }

        return copyArray;
    }

    public static void main(String args[]) {

        List<Integer> i_list = new ArrayList<Integer>();
        List<String> s_list = new ArrayList<String>();
        String[] new_s_list = { "Volvo", "BMW", "Ford", "Mazda" };
        String[][] new_s_list_1 = new String[][] { { "John", "Mary" }, { "Alice", "Bob" } };
        int[] new_i_list = { 1, 2, 3, 4, 5, 6 };
        int[][] new_i_list_1 = new int[][] { { 1, 2 }, { 3, 4 } };

        Example curr_class = new Example();
        i_list = curr_class.intValue(i_list);
        s_list = curr_class.stringValue(s_list);
        s_list.add("end");
        i_list.add(4);

        // new_i_list = curr_class.removeElement(new_i_list, 2);

        int getIntIndex = Arrays.asList(i_list).indexOf(3);
        int getStrIndex = Arrays.asList(s_list).indexOf("Banana");
        int getStr1Index = Arrays.asList(new_s_list).indexOf("Ford");

        System.out.println(
                "i_list:3 ->" + getIntIndex + " s_list:banana->" + getStrIndex + " new_s_list:Ford-> " + getStr1Index);

        // curr_class.printIntList(i_list);
        // curr_class.printStrList(s_list);
        System.out.print(Arrays.toString(new_s_list));
        // System.out.print(new_i_list);
        System.out.println(Arrays.toString(new_i_list));
        System.out.println(Arrays.deepToString(new_s_list_1));
        System.out.println(Arrays.deepToString(new_i_list_1));

        System.out.print(curr_class.changeToInt(i_list));
        System.out.println();

        System.out.print(curr_class.changeString(s_list));
        System.out.println();

        new_s_list = curr_class.changeString(s_list).split(" ");

        // for (String i : new_s_list) {
        // System.out.print(i);
        // }

        System.out.println();

        HashMap<Integer, Integer> hash_int = new HashMap<Integer, Integer>();
        HashMap<String, String> hash_str = new HashMap<String, String>();
        hash_int.put(1, 7);
        hash_int.put(2, 5);
        hash_int.put(3, 4);
        System.out.print(hash_int);
        hash_str.put("a", "b");
        System.out.print(hash_str);

        Map<Integer, String> map_words = new HashMap<>();
        map_words.put(1, "a");
        map_words.put(2, "b");
        map_words.put(3, "c");
        System.out.println(map_words);

        boolean check_key = map_words.containsKey("c");
        boolean check_val = map_words.containsValue("c");

        System.out.println(check_key);
        System.out.println(check_val);

    }
}
