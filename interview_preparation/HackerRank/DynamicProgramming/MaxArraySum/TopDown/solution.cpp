unordered_map<int, int> dp;
int ans;

int sub(vector<int> &a, int i)
{
    if (i < 0)
        return 0;

    // compare i with the end of list
    if (dp.find(i) != dp.end())
        return dp[i];

    dp[i] = max(sub(a, i - 1), sub(a, i - 2) + a[i]);

    //compare max with ans, and dp[i] the biggest will be new ans
    ans = max(ans, dp[i]);

    return dp[i];
}

int maxSubsetSum(vector<int> a)
{
    ans = a[0];
    sub(a, a.size() - 1);
    return ans;
}
