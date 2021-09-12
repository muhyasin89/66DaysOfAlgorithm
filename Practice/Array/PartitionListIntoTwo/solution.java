package Practice.Array.PartitionListIntoTwo;

import java.util.*;
import java.util.stream.Collectors;

// Java implementation for above approach

class solution {

    List<ArrayList<Integer>> chopped(List<Integer> list, int L) {
        List<ArrayList<Integer>> parts = new ArrayList<ArrayList<Integer>>();
        final int N = list.size();
        for (int i = 0; i < N; i += L) {
            parts.add(new ArrayList<Integer>(list.subList(i, Math.min(N, i + L))));
        }
        return parts;
    }

    public static void main(String[] args) {
        int arr[] = { 1, 2, 1, 3, 1, 4, 1, 5, 2, 3, 2, 4, 2, 5, 3, 4, 3, 5, 4, 5 };
        int r = 2;

        List<Integer> list_arr = Arrays.stream(arr).boxed().collect(Collectors.toList());

        solution obj = new solution();

        List<ArrayList<Integer>> parts = obj.chopped(list_arr, r);
        System.out.println(parts);
    }
}
