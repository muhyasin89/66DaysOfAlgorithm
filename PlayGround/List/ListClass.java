import java.util.*;

public class ListClass {
    ArrayList<Integer> RemoveDuplicate(ArrayList<Integer> list_int) {
        ArrayList<Integer> newList = new ArrayList<>();

        for (Integer item : list_int) {
            if (!newList.contains(item)) {
                newList.add(item);
            }
        }

        return newList;
    }

    public static void main(String args[]) {
        // make string "Hello World" and string "1122334455"
        String str1 = "Hello World";
        String int1 = "1122334455";
        // String[] str2 = { "Hello World" };
        // String[][] str3 = { { "Hello" }, { "World" } };

        System.out.println("Str:" + str1 + " Int:" + int1);
        // System.out.println(Arrays.toString(str2));
        // System.out.println(Arrays.deepToString(str3));

        // turn string into list
        ArrayList<Character> list_str = new ArrayList<>();
        ArrayList<Integer> list_int = new ArrayList<>();

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
        for (Character c : list_str) {
            strbul.append(c);
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

        // check if 'space' inside list
        System.out.println(list_str.contains(' '));
        // check index space
        int ind_arr = list_str.indexOf(' ');
        System.out.println(ind_arr);

        // remove space in list
        list_str.remove(ind_arr);
        System.out.println(list_str);

        // swap
        Collections.swap(list_str, 4, 5);
        System.out.println(list_str);

        // cut list into 2 left and right
        int mid = list_str.size() / 2;
        ArrayList<Character> left = new ArrayList<>(list_str.subList(0, mid));
        ArrayList<Character> right = new ArrayList<>(list_str.subList(mid, list_str.size() - 1));
        System.out.println(left);
        System.out.println(right);

        // make hash map
        HashMap<Integer, String> hash_map = new HashMap<>();
        hash_map.put(1, "first");
        hash_map.put(2, "second");
        hash_map.put(3, "third");

        // check if n in keys
        System.out.println(hash_map.containsKey(1));

        // print map get key
        System.out.println(hash_map.get(1));

        // check if n in values
        System.out.println(hash_map.containsValue("second"));

        // itterate hash map
        for (Map.Entry<Integer, String> set : hash_map.entrySet()) {
            System.out.println(set.getKey() + " = " + set.getValue());
        }

    }
}