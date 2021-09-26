package Practice.Array.wordAreFollowingPattern;

import java.util.HashMap;
import java.util.Map;

public class solution {
    Boolean areFollowingPattern(String str1, String string1) {
        Map<Character, String> hash_map = new HashMap<>();

        String[] list_string = new String[] {};
        list_string = string1.split(" ");

        if (str1.length() != list_string.length) {
            return false;
        }

        byte[] strAsByteArray = str1.getBytes();

        for (int i = 0; i < strAsByteArray.length; i++) {
            char temp = (char) strAsByteArray[i];
            if (hash_map.containsKey(temp)) {
                if (!hash_map.get(temp).equals(list_string[i])) {
                    return false;
                }
            } else {
                hash_map.put(temp, list_string[i]);
            }
        }

        return true;
    }

    public static void main(String[] args) {
        String str1 = "abba";
        String string1 = "dog cat cat dog";
        // result True

        String str2 = "abba";
        String string2 = "dog cat cat fish";
        // return False

        solution obj = new solution();

        System.out.println(obj.areFollowingPattern(str1, string1));
        System.out.println(obj.areFollowingPattern(str2, string2));

    }
}