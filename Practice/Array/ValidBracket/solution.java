package Practice.Array.ValidBracket;

import java.util.*;

public class solution {
    Boolean ValidBracket(String str, Map hash_map) {
        ArrayList<String> list_bracket = new ArrayList<>();
        String temp = new String();

        if (str.length() == 1) {
            return false;
        }

        for (int i = 0; i < str.length(); i++) {
            temp = Character.toString(str.charAt(i));
            // System.out.println(temp);

            if (hash_map.containsValue(temp) && i < 1) {
                return false;
            } else if (hash_map.containsKey(temp)) {
                list_bracket.add(temp);
            } else if (hash_map.containsValue(temp)) {
                if (!hash_map.get(list_bracket.get(list_bracket.size() - 1)).equals(temp)) {
                    // System.out.println(hash_map.get(list_bracket.get(list_bracket.size() - 1)) +
                    // "=" + temp);
                    return false;
                } else {
                    list_bracket.remove(list_bracket.size() - 1);
                }
            } else {

            }
        }

        return true;
    }

    HashMap setHashMap() {
        HashMap<String, String> result = new HashMap<>();
        result.put("{", "}");
        result.put("[", "]");
        result.put("(", ")");
        result.put("<", ">");
        return result;
    }

    public static void main(String[] args) {
        String inp_str = "[]"; // expected True
        String inp_str1 = "{([{}()[]])}"; // expected True
        String inp_str2 = "{(][)}";// expected False
        String inp_str3 = "][";// expected False
        String inp_str4 = "{<[adadas]@1234>#$%^}";// expected True

        solution obj = new solution();
        Map<String, String> result = new HashMap<>();
        result = obj.setHashMap();

        System.out.println(obj.ValidBracket(inp_str, result));
        System.out.println(obj.ValidBracket(inp_str1, result));
        System.out.println(obj.ValidBracket(inp_str2, result));
        System.out.println(obj.ValidBracket(inp_str3, result));
        System.out.println(obj.ValidBracket(inp_str4, result));
    }
}
