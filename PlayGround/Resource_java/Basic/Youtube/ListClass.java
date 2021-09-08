import java.lang.ref.Cleaner;
import java.lang.reflect.Array;
import java.util.*;

import javax.lang.model.element.Element;

public class ListClass {

    public static void main(String args[]) {

        // make string "Hello World" and string "11223344"

        String str_a = "Hello World";
        // String[] str_a1 = { "Hello World" };
        // String[][] str_a11 = { { "Hello" }, { "Word" } };
        Integer int_a = 1122345;
        String str_int_a = String.valueOf(int_a);

        System.out.println(str_a);
        System.out.println(int_a);
        // System.out.println(Arrays.toString(str_a1));
        // System.out.println(Arrays.deepToString(str_a11));

        // turn string into list

        ArrayList<Character> list_str_a = new ArrayList<Character>();
        ArrayList<Integer> list_int_a = new ArrayList<Integer>();

        for (int i = 0; i < str_a.length(); i++) {
            list_str_a.add(str_a.charAt(i));
        }
        list_str_a.remove(5);
        System.out.println(list_str_a);

        // turn list int into list
        for (int i = 0; i < str_int_a.length(); i++) {
            list_int_a.add(Character.getNumericValue(str_int_a.charAt(i)));
        }

        System.out.println(list_int_a);

        // turn list into string

        // swap list
        Collections.swap(list_str_a, 4, 5);
        System.out.println(list_str_a);

        // make another list

        // merge 2 list with same type

        // check if 'k' inside list
        System.out.println(right.contains('l'));

        // check index space

        // remove space in list

        // remove duplicate

        ArrayList<Integer> listWithoutDuplicates = new ArrayList<Integer>();

        for (Integer a : list_int_a) {
            if (!listWithoutDuplicates.contains(a)) {
                listWithoutDuplicates.add(a);
            }
        }

        System.out.println(listWithoutDuplicates);

        // cut list into 2 left and right
        Integer size_a = list_str_a.size();

        ArrayList<Character> left = new ArrayList<Character>(list_str_a.subList(0, (size_a + 1) / 2));
        ArrayList<Character> right = new ArrayList<Character>(list_str_a.subList((size_a + 1) / 2, size_a - 1));

        System.out.println(left);
        System.out.println(right);

        // make hash map
        HashMap<Integer, String> map = new HashMap<Integer, String>();
        map.put(1, "Hello");
        map.put(2, "word");
        map.put(3, "everyone");

        // check if n in keys
        System.out.println(map.containsKey(3));
        // check if n in values
        System.out.println(map.containsValue("word"));

    }
}