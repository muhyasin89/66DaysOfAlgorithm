def climbingStaircase(n, k):
    if n < 0:
        return []
    if n == 0:
        return [[]]
    ans = []
    for i in range(1, k + 1):
        for seq in climbingStaircase(n - i, k):
            ans.append([i] + seq)
    return ans
