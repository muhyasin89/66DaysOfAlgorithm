package Basic.List;

public class PermutationExample5 {
    // the function finds the total number of digits in a number
    static int noOfDigits(int N) {
        int count = 0;
        while (N > 0) {
            // increments the variable count by 1 if n>0
            count++;
            // divides the variable n by 10
            N = N / 10;
        }
        // returns the total number of digits
        return count;
    }

    // the function generates the cyclic permutations
    static void cyclicPermutation(int N) {
        int num = N;
        int n = noOfDigits(N);
        while (true) {
            System.out.println(num);
            // the next three statements generate the cyclic permutations
            int remainder = num % 10;
            int dev = num / 10;
            num = (int) ((Math.pow(10, n - 1)) * remainder + dev);
            // if the condition is true, it exits from the loop
            if (num == N)
                break;
        }
    }

    // main() method
    public static void main(String args[]) {
        // number to permutate
        int N = 9871;
        // calling the user-defined method
        cyclicPermutation(N);
    }
}
