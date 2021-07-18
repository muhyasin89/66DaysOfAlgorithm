int main()
{
    int n;
    cin >> n;
    vector<int> a(n);
    for (auto &i : a)
        cin >> i;

    vector<int> dp(n + 3);

    for (int i = n - 1; i >= 0; i--)
        dp[i] = max(a[i] + dp[i + 2], dp[i + 1]);

    cout << dp[0];
}
