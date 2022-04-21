public class Solution {
    public int Tribonacci(int n) {
        if (n == 0) return 0;
	if (n == 1) return 1;
	if (n == 2) return 1;

	var a = new int[n + 1];
	a[0] = 0;
	a[1] = 1;
	a[2] = 1;

	for (var i = 3; i < n + 1; i++)
		a[i] = a[i - 3] + a[i - 2] + a[i - 1];

	return a[n];
    }
}
