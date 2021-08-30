import java.util.*;

public class List {

    public static void main(String args[]) {
        List curr_class = new List();

        String a = "Hello World";
        System.out.println(a);

        ArrayList<Character> list_a = new ArrayList<Character>();

        String b = a.replaceAll("\\s+", "");

        for (int i = 0; i < b.length(); i++) {
            list_a.add(b.charAt(i));
        }

        System.out.println(list_a);

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
