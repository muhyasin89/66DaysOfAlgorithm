package Practice.Array.wordAreFollowingPattern;

import java.util.HashMap;
import java.util.Map;

public class solution {

    Boolean checkPattern(String s, String str) {
        Map<Character, String> hash_map = new HashMap<>();

        String[] spl = new String[] {};
        spl = str.split(" ");

        if (s.length() != spl.length) {
            return false;
        }

        byte[] strAsByteArray = s.getBytes();

        for (int i = 0; i < strAsByteArray.length; i++) {

            char c = (char) strAsByteArray[i];
            if (hash_map.containsKey(c)) {
                if (!hash_map.get(c).equals(spl[i])) {
                    return false;
                }
            } else {
                hash_map.put(c, spl[i]);
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

        System.out.println(obj.checkPattern(str1, string1));
        System.out.println(obj.checkPattern(str2, string2));

    }
}