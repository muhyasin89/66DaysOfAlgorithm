import java.util.*;

public class FistList {

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

    public static void main(String args[]) {

        List<Integer> i_list = new ArrayList<Integer>();
        List<String> s_list = new ArrayList<String>();
        String[] new_s_list = { "Volvo", "BMW", "Ford", "Mazda" };

        FistList curr_class = new FistList();
        i_list = curr_class.intValue(i_list);
        s_list = curr_class.stringValue(s_list);

        curr_class.printIntList(i_list);
        curr_class.printStrList(s_list);

        System.out.print(curr_class.changeToInt(i_list));
        System.out.println();

        System.out.print(curr_class.changeString(s_list));
        System.out.println();

        new_s_list = curr_class.changeString(s_list).split(" ");

        for (String i : new_s_list) {
            System.out.print(i);
        }

        System.out.println();

        HashMap<Integer, Integer> hash_int = new HashMap<Integer, Integer>();
        HashMap<String, String> hash_str = new HashMap<String, String>();
        hash_int.put(1, 7);
        hash_int.put(2, 5);
        hash_int.put(3, 4);
        System.out.print(hash_int);

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
