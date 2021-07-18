==================================
Things that i dont understand? ||
==================================

How the solution set an Array, and what happen to n = int(input())

```
for i, num in enumerate(arr[2:], start=2)
```

i know that array is skipping 2 elemnt [0] and [1] which wil be using for standart for adding latter

```
for i, num in enumerate(arr[2:], start=2):
    dp[i] = max(dp[i-1], dp[i-2]+num, dp[i-2], num)
```

if first element is 2 the comparasion max is dp[1], dp[0]+ num, dp[0], num
since dp[0] and dp[1] already declare by arr[0] and arr[1]

### is it top down or bottom up
