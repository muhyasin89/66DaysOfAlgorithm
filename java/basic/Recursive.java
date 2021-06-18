package hackerRankGroup;

import java.util.*;

/**
 ** 
 * https://www.hackerrank.com/challenges/ctci-fibonacci-numbers/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=recursion-backtracking
 * 
 */
public class Recursive {

    public static int fibonacci(int n) {
        // Complete the function.
        int[] fib = new int[2];
        fib[0] = 0;
        fib[1] = 1;
        for (int i = 2; i <= n; ++i) {
            fib[i % 2] = fib[0] + fib[1];
        }
        return fib[n % 2];
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        scanner.close();
        System.out.println(fibonacci(n));
    }
}
