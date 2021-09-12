package Practice.Array.CombinationWithLength;

import java.util.*;

// Java program to print all combination of size r in an array of size n

class solution {
    List<ArrayList<Integer>> chopped(List<Integer> list, int L) {
        List<ArrayList<Integer>> parts = new ArrayList<ArrayList<Integer>>();
        final int N = list.size();
        for (int i = 0; i < N; i += L) {
            parts.add(new ArrayList<Integer>(list.subList(i, Math.min(N, i + L))));
        }
        return parts;
    }

    /*
     * arr[] ---> Input Array data[] ---> Temporary array to store current
     * combination start & end ---> Staring and Ending indexes in arr[] index --->
     * Current index in data[] r ---> Size of a combination to be printed
     */
    ArrayList<Integer> combinationUtil(solution obj, int arr[], int data[], int start, int end, int index, int r) {
        ArrayList<Integer> result = new ArrayList<Integer>();
        // Current combination is ready to be printed, print it
        if (index == r) {
            for (int j = 0; j < r; j++) {
                result.add(data[j]);
            }
            // System.out.println(result);
            return result;
        }

        // replace index with all possible elements. The condition
        // "end-i+1 >= r-index" makes sure that including one element
        // at index will make a combination with remaining elements
        // at remaining positions
        for (int i = start; i <= end && end - i + 1 >= r - index; i++) {
            data[index] = arr[i];
            result.addAll(obj.combinationUtil(obj, arr, data, i + 1, end, index + 1, r));
        }

        return result;
    }

    // The main function that prints all combinations of size r
    // in arr[] of size n. This function mainly uses combinationUtil()
    List<ArrayList<Integer>> getCombination(solution obj, List<ArrayList<Integer>> result, int arr[], int n, int r) {
        // A temporary array to store all combination one by one
        int data[] = new int[r];

        // Print all combination using temporary array 'data[]'
        result = obj.chopped(combinationUtil(obj, arr, data, 0, n - 1, 0, r), r);

        return result;
    }

    /* Driver function to check for above function */
    public static void main(String[] args) {
        int arr[] = { 1, 2, 3, 4, 5 };
        int r = 2;
        int n = arr.length;

        List<ArrayList<Integer>> result = new ArrayList<>();
        solution obj = new solution();

        result = obj.getCombination(obj, result, arr, n, r);
        System.out.println(result);
    }
}

/* This code is contributed by Devesh Agrawal */
