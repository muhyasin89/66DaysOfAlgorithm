import java.lang.ref.Cleaner;
import java.lang.reflect.Array;
import java.util.*;

import javax.lang.model.element.Element;

public class ListClass {

    ArrayList<Integer> RemoveDuplicate(ArrayList<Integer> list) {
        ArrayList<Integer> newList = new ArrayList<>();

        // Traverse through the first list
        for (Integer item : list) {

            // If this element is not present in newList
            // then add it
            if (!newList.contains(item)) {

                newList.add(item);
            }
        }

        // return the new list
        return newList;
    }

    public static void main(String args[]) {

        // make string "Hello World" and string "11223344"
        String str1 = "Hello World";
        String int1 = "11223344";
        // String[] str1 = { "Hello World" };
        // String[][] str2 = { { "Hello" }, { "Word" } };
        System.out.println("String:" + str1 + "Int:" + int1);
        // System.out.println(Arrays.toString(str1));
        // System.out.println(Arrays.deepToString(str2));

        // turn string into list
        ArrayList<Character> list_str = new ArrayList<Character>();
        ArrayList<Integer> list_int = new ArrayList<Integer>();

        for (int i = 0; i < str1.length(); i++) {
            list_str.add(str1.charAt(i));
        }
        System.out.println(list_str);

        // turn list str into list int
        for (int i = 0; i < int1.length(); i++) {
            list_int.add(Character.getNumericValue(int1.charAt(i)));
        }

        System.out.println(list_int);

        // turn list into string
        StringBuilder strbul = new StringBuilder();
        for (Character str : list_str) {
            strbul.append(str);
        }
        System.out.println(strbul.toString());

        // make another list
        ArrayList<Integer> list_int1 = new ArrayList<>();
        list_int1.add(6);
        list_int1.add(7);
        list_int1.add(8);
        list_int1.add(9);
        list_int1.add(10);

        // merge 2 list with same type
        list_int.addAll(list_int1);
        System.out.println(list_int);

        // remove duplicate
        ListClass obj = new ListClass();
        list_int = obj.RemoveDuplicate(list_int);
        System.out.println(list_int);

        // check if 'k' inside list
        System.out.println(list_str.contains(' '));

        // check index space
        int ind_arr = list_str.indexOf(' ');
        System.out.println(ind_arr);

        // remove space in list
        list_str.remove(ind_arr);
        System.out.println(list_str);
        // swap list
        Collections.swap(list_str, 4, 5);
        System.out.println(list_str);

        // cut list into 2 left and right
        Integer size_a = list_str.size();

        ArrayList<Character> left = new ArrayList<Character>(list_str.subList(0, (size_a + 1) / 2));
        ArrayList<Character> right = new ArrayList<Character>(list_str.subList((size_a + 1) / 2, size_a - 1));

        System.out.println(left);
        System.out.println(right);

        // make hash map
        HashMap<Integer, String> map = new HashMap<Integer, String>();
        map.put(1, "first");
        map.put(2, "second");
        map.put(3, "third");

        // check if n in keys
        System.out.println(map.containsKey(3));

        // print map get key
        System.out.println(map.get(2));

        // check if n in values
        System.out.println(map.containsValue("second"));

        // itterate hash map
        for (Map.Entry<Integer, String> set : map.entrySet()) {
            System.out.println(set.getKey() + " = " + set.getValue());
        }

    }
}