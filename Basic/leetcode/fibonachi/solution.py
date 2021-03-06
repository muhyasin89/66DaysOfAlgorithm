import collections

class Solution:
    def fib(self, n: int) -> int:
        memo = collections.defaultdict(int)
        memo[1], memo[2] = 1, 1
        
        for i in range(3, n+1):
            memo[i] = memo[i-1] + memo[i-2]
            
        return memo[n]