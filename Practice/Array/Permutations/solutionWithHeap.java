package Practice.Array.Permutations;

import java.util.*;

// Java program to print all permutations using
// Heap's algorithm
public class solutionWithHeap {
    // Prints the array
    ArrayList<Integer> printArr(solutionWithHeap obj, int a[], int n) {
        ArrayList<Integer> result = new ArrayList<Integer>();
        for (int i = 0; i < n; i++) {
            result.add(a[i]);
        }
        return result;
    }

    // Generating permutation using Heap Algorithm
    List<ArrayList<Integer>> heapPermutation(solutionWithHeap obj, List<ArrayList<Integer>> result, int a[], int size,
            int n) {
        // if size becomes 1 then prints the obtained
        // permutation
        if (size == 1) {
            result.add(printArr(obj, a, n));
        }

        for (int i = 0; i < size; i++) {
            heapPermutation(obj, result, a, size - 1, n);

            // if size is odd, swap 0th i.e (first) and
            // (size-1)th i.e (last) element
            if (size % 2 == 1) {
                int temp = a[0];
                a[0] = a[size - 1];
                a[size - 1] = temp;
            }

            // If size is even, swap ith
            // and (size-1)th i.e last element
            else {
                int temp = a[i];
                a[i] = a[size - 1];
                a[size - 1] = temp;
            }
        }

        return result;
    }

    public static void main(String args[]) {
        List<ArrayList<Integer>> result = new ArrayList<>();
        solutionWithHeap obj = new solutionWithHeap();
        int a[] = { 1, 2, 3 };
        result = obj.heapPermutation(obj, result, a, a.length, a.length);

        System.out.println(result);
    }
}
