package Practice.Array.wordFollowingPattern;

import java.util.*;

public class solution {
    Boolean checkPattern(String s, String str) {
        Map<Character, String> map_words = new HashMap<>();

        String[] spl = new String[] {};
        spl = str.split(" ");
        if (s.length() != spl.length) {
            return false;
        }
        byte[] strAsByteArray = s.getBytes();

        for (int i = 0; i < strAsByteArray.length; i++) {
            if (map_words.containsKey((char) strAsByteArray[i])) {
                if (!map_words.get((char) strAsByteArray[i]).equals(spl[i])) {
                    return false;
                }
            } else {
                map_words.put((char) strAsByteArray[i], spl[i]);
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