import java.util.*;

public class Example2 {

    public static void main(String args[]) {
        Example2 curr_class = new Example2();

        String a = "Hello World";
        int a_int = 112233;
        System.out.println(a);
        String a_str = String.valueOf(a_int);

        ArrayList<Character> list_a = new ArrayList<Character>();
        ArrayList<Character> list_b = new ArrayList<Character>();
        ArrayList<Integer> list_c = new ArrayList<Integer>();

        String b = a.replaceAll("\\s+", "");

        for (int i = 0; i < b.length(); i++) {
            list_a.add(b.charAt(i));
        }

        for (int i = 0; i < a_str.length(); i++) {
            list_b.add(a_str.charAt(i));
            list_c.add(Character.getNumericValue(a_str.charAt(i)));
        }

        System.out.println(list_a);
        System.out.println(list_b);
        System.out.println(list_c);

        list_a.remove(2);
        System.out.println(list_a);
        Collections.swap(list_a, 3, 4);

        System.out.println(list_a);

        // StringBuilder sb = new StringBuilder();
        // for (Character ch : list_a) {
        // sb.append(ch);
        // }

        // String result_string = sb.toString();
        // System.out.println(result_string);

        int size = list_a.size();

        ArrayList<Character> left = new ArrayList<Character>(list_a.subList(0, (size + 1) / 2));
        ArrayList<Character> right = new ArrayList<Character>(list_a.subList((size + 1) / 2, size));

        System.out.println(left);
        System.out.println(right);
    }
}
