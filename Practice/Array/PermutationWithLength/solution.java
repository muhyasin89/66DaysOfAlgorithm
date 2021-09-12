package Practice.Array.PermutationWithLength;

import java.io.*;

// Java implementation for above approach

class solution {

    // Convert the number to Lth
    // base and print the sequence
    static void convertToLenTHBase(int n, int arr[], int len, int L) {
        // Sequence is of length L
        for (int i = 0; i < L; i++) {
            // Print the ith element
            // of sequence
            System.out.print(arr[n % len]);
            n /= len;
        }
        System.out.println();
    }

    // Print all the permuataions
    static void print(int arr[], int len, int L) {
        // There can be (len)^l
        // permutations
        for (int i = 0; i < (int) Math.pow(len, L); i++) {
            // Convert i to len th base
            convertToLenTHBase(i, arr, len, L);
        }
    }

    // Driver code
    public static void main(String[] args) {
        int arr[] = { 1, 2, 3 };
        int len = arr.length;
        int L = 2;

        // function call
        print(arr, len, L);
    }
}

// This code is contributed by ajit.
