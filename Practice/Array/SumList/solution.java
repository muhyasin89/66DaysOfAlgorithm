package Practice.Array.SumList;

import java.util.*;

public class solution {
    HashMap<Integer, Integer> SumList(HashMap<Integer, Integer> hash_map, int[] arr) {
        for (var i = 0; i < arr.length; i++) {
            if (hash_map.containsKey(arr[i])) {
                hash_map.put(arr[i], hash_map.get(arr[i]) + 1);
            } else {
                hash_map.put(arr[i], 1);
            }
        }

        return hash_map;
    }

    void printHashMap(HashMap<Integer, Integer> hash_map) {
        for (Map.Entry<Integer, Integer> set : hash_map.entrySet()) {
            System.out.println("number " + set.getKey() + " = " + set.getValue() + " times");
        }
    }

    public static void main(String[] args) {
        int[] arr = { 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5 };
        // expected answer
        // number 1 = 3 times

        HashMap<Integer, Integer> hash_map = new HashMap<>();
        solution obj = new solution();

        hash_map = obj.SumList(hash_map, arr);
        obj.printHashMap(hash_map);
    }
}