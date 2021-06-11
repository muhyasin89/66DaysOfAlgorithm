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
// A recursive implementation of LCS problem
// of three strings
#include <bits/stdc++.h>
int max(int a, int b);

// Returns length of LCS for X[0..m-1], Y[0..n-1]
int lcs(char* X, char* Y, char* Z, int m, int n, int o)
{
	// base case
	if (m == 0 || n == 0 || o == 0)
		return 0;

	// if equal, then check for next combination
	if (X[m - 1] == Y[n - 1] and Y[n - 1] == Z[o - 1]) {

		// recursive call
		return 1 + lcs(X, Y, Z, m - 1, n - 1, o - 1);
	}
	else {

		// return the maximum of the three other
		// possible states in recursion
		return max(lcs(X, Y, Z, m, n - 1, o),
				max(lcs(X, Y, Z, m - 1, n, o),
					lcs(X, Y, Z, m, n, o - 1)));
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

	char X[] = "geeks";
	char Y[] = "geeksfor";
	char Z[] = "geeksforge";
	int m = strlen(X);
	int n = strlen(Y);
	int o = strlen(Z);
	printf("Length of LCS is %d", lcs(X, Y, Z, m, n, o));

	return 0;
}
