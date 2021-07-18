"""
===========================
what the problem?       |||
===========================

===========================
what the expected result? |
===========================


========================================
how many step for solving this problem?|
========================================


=====================================
how many ways to solve this problem?|
=====================================

===========================
how long it takes?       ||
===========================
"""

// A memoize recursive implementation of LCS problem
#include <bits/stdc++.h>
int arr[100][100][100];
int max(int a, int b);

// Returns length of LCS for X[0..m-1], Y[0..n-1] */
// memoization applied in recursive solution
int lcs(char* X, char* Y, char* Z, int m, int n, int o)
{
	// base case
	if (m == 0 || n == 0 || o == 0)
		return 0;

	// if the same state has already been
	// computed
	if (arr[m - 1][n - 1][o - 1] != -1)
		return arr[m - 1][n - 1][o - 1];

	// if equal, then we store the value of the
	// function call
	if (X[m - 1] == Y[n - 1] and Y[n - 1] == Z[o - 1]) {

		// store it in arr to avoid further repetitive work
		// in future function calls
		arr[m - 1][n - 1][o - 1] = 1 + lcs(X, Y, Z, m - 1,
											n - 1, o - 1);
		return arr[m - 1][n - 1][o - 1];
	}
	else {

		// store it in arr to avoid further repetitive work
		// in future function calls
		arr[m - 1][n - 1][o - 1] =
							max(lcs(X, Y, Z, m, n - 1, o),
								max(lcs(X, Y, Z, m - 1, n, o),
									lcs(X, Y, Z, m, n, o - 1)));
		return arr[m - 1][n - 1][o - 1];
	}
}

// Utility function to get max of 2 integers
int max(int a, int b)
{
	return (a > b) ? a : b;
}

// Driver Code
int main()
{
	memset(arr, -1, sizeof(arr));
	char X[] = "geeks";
	char Y[] = "geeksfor";
	char Z[] = "geeksforgeeks";
	int m = strlen(X);
	int n = strlen(Y);
	int o = strlen(Z);
	printf("Length of LCS is %d", lcs(X, Y, Z, m, n, o));

	return 0;
}
