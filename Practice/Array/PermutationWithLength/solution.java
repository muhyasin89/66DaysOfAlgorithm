package Practice.Array.PermutationWithLength;

import java.util.*;;

// Java implementation for above approach

class solution {

    // Convert the number to Lth
    // base and print the sequence
    ArrayList<Integer> convertToLenTHBase(solution obj, int n, int arr[], int len, int L) {
        ArrayList<Integer> result = new ArrayList<Integer>();
        // Sequence is of length L
        for (int i = 0; i < L; i++) {
            // Print the ith element
            // of sequence
            result.add(arr[n % len]);
            n /= len;
        }
        return result;
    }

    // Print all the permuataions
    List<ArrayList<Integer>> getAllPermutations(solution obj, List<ArrayList<Integer>> result, int arr[], int len,
            int L) {
        // There can be (len)^l
        // permutations
        for (int i = 0; i < (int) Math.pow(len, L); i++) {
            // Convert i to len th base
            result.add(convertToLenTHBase(obj, i, arr, len, L));
        }

        return result;
    }

    // Driver code
    public static void main(String[] args) {
        int arr[] = { 1, 2, 3 };
        int len = arr.length;
        int L = 2;
        List<ArrayList<Integer>> result = new ArrayList<>();
        solution obj = new solution();

        // function call
        result = obj.getAllPermutations(obj, result, arr, len, L);

        System.out.println(result);
    }
}

// This code is contributed by ajit.
