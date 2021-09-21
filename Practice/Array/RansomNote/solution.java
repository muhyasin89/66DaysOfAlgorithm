package Practice.Array.RansomNote;

import java.util.*;

class solution {
    Boolean canConstruct(String ransomNote, String magazine) {

        HashMap<Character, Integer> map = new HashMap<>();

        for (int i = 0; i < ransomNote.length(); i++) {

            char ch = ransomNote.charAt(i);
            map.put(ch, map.getOrDefault(ch, 0) + 1);
        }

        for (int i = 0; i < magazine.length(); i++) {

            char ch = magazine.charAt(i);
            if (map.containsKey(ch) && map.get(ch) > 0)
                map.put(ch, map.get(ch) - 1);
        }

        for (int count : map.values())
            if (count != 0)
                return false;

        return true;
    }
}
