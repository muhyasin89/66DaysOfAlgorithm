int memo[2] = {0};
int fib(int n) {
	if(n <= 1)
		return n;
	if(memo[n & 1])
		return memo[n & 1];
	return memo[n & 1] = fib(n - 1) + fib(n - 2);
	// or 1-liner:
	// return memo[n % 2] = memo[n % 2] ? memo[n % 2] : n <= 1 ? n : fib(n - 1) + fib(n - 2);
}