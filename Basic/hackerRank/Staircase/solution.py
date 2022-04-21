import collections
def stepPerms(n):
    memo = collections.defaultdict(int)
    memo[1], memo[2], memo[3] = 1, 2, 4
    
    for i in range(4, n+1):
        memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
    return memo[n]