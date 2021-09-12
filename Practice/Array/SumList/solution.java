package Practice.Array.SumList;

import java.util.HashMap;
import java.util.Map;

public class solution {

    HashMap<Integer, Integer> sumList(HashMap<Integer, Integer> map, int[] arr) {

        for (var i = 0; i < arr.length; i++) {
            if (map.containsKey(arr[i])) {
                map.put(arr[i], map.get(arr[i]) + 1);
            } else {
                map.put(arr[i], 1);
            }
        }

        return map;
    }

    void printHashMap(HashMap<Integer, Integer> map) {
        for (Map.Entry<Integer, Integer> set : map.entrySet()) {
            System.out.println("number: " + set.getKey() + " = " + set.getValue() + " times");
        }
    }

    public static void main(String args[]) {
        int[] arr = { 1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5 };

        HashMap<Integer, Integer> map = new HashMap<>();
        solution obj = new solution();

        map = obj.sumList(map, arr);
        obj.printHashMap(map);

    }
}
