package Practice.Array.ValidBracket;

import java.util.*;

public class solution {

    Boolean ValidateBracket(String str, Map dict_map) {
        ArrayList<String> list_bracket = new ArrayList<>();
        String temp = new String();

        for (int i = 0; i < str.length(); i++) {
            temp = Character.toString(str.charAt(i));

            if (dict_map.containsValue(temp) && i < 1) {
                return false;
            } else if (dict_map.containsKey(temp)) {
                list_bracket.add(temp);
            } else if (dict_map.containsValue(temp)) {
                if (!dict_map.get(list_bracket.get(list_bracket.size() - 1)).equals(temp)) {
                    return false;
                } else {
                    list_bracket.remove(list_bracket.size() - 1);
                }
            }
        }

        if (list_bracket.size() > 0) {
            return false;
        }

        return true;
    }

    HashMap<String, String> setHashMap() {
        HashMap<String, String> result = new HashMap<>();
        result.put("{", "}");
        result.put("(", ")");
        result.put("[", "]");
        result.put("<", ">");

        return result;
    }

    public static void main(String[] args) {
        String inp_str = "[]"; // expected True
        String inp_str1 = "{([{}()[]])}"; // expected True
        String inp_str2 = "{(][)}";// expected False
        String inp_str3 = "][";// expected False
        String inp_str4 = "{<[adadas]@1234>#$%^}";// expected True
        String inp_str5 = "{{{{{";// expected False

        solution obj = new solution();
        Map<String, String> dict_map = new HashMap<>();
        dict_map = obj.setHashMap();

        System.out.println(obj.ValidateBracket(inp_str, dict_map));
        System.out.println(obj.ValidateBracket(inp_str1, dict_map));
        System.out.println(obj.ValidateBracket(inp_str2, dict_map));
        System.out.println(obj.ValidateBracket(inp_str3, dict_map));
        System.out.println(obj.ValidateBracket(inp_str4, dict_map));
        System.out.println(obj.ValidateBracket(inp_str5, dict_map));

    }
}
