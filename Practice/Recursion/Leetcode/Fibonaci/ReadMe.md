Solution - I (Recursion)

Time Complexity : O(2^N) It can be calculated from the recurrence relation T(N) = T(N-1) + T(N-2). This is the most naive approach to calculate fibonacci number and recursion tree grows exponentially. There's a lot of repeated work that happens here.
Space Complexity : O(N), required for recursive call stack.

Solution - II (Top-Down Recursive Approach - Dynamic Programming)

Time Complexity : O(N), each fibonacci number is only calculated once.
Space Complexity : O(N), required for memoization.

Solution - III (Space-Optimized Top-Down Recursive Approach - Dynamic Programming)

Solution - IV (Bottom-Up Iterative Approach - Dynamic Programming)

Time Complexity : O(N), each fibonacci number is only calculated once.
Space Complexity : O(N), required for dp array.

Solution - V (Space Optimized Bottom-Up Iterative Approach - Dynamic Programming)

Time Complexity : O(N), each fibonacci number is only calculated once.
Space Complexity : O(1), only constant space is being used.


Solution - VI (Matrix Exponentiation)

Time Complexity : O(N), we are doing N matrix multiplications.
Space Complexity : O(1), only constant amount of space is used.

Solution - VII (Optimized Matrix Exponentiation)

Time Complexity : O(logN)
Space Complexity : O(logN), considering recursive stack space.


Reference:
https://leetcode.com/problems/fibonacci-number/discuss/1159786/Fibonacci-Number-or-Easy-Solution-w-Multiple-Approaches-Explained-!