Memoization Method – Top Down Dynamic Programming

// Memoized version to find factorial x.
// To speed up we store the values
// of calculated states

// initialized to -1
int dp[MAXN]

// return fact x!
int solve(int x)
{
if (x==0)
return 1;
if (dp[x]!=-1)
return dp[x];
return (dp[x] = x \* solve(x-1));
}
