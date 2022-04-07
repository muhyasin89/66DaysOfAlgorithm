void matrixMul(int F[2][2], int M[2][2]){
	int m00 = F[0][0] * M[0][0] + F[0][1] * M[1][0];
	int m01 = F[0][0] * M[0][1] + F[0][1] * M[1][1];
	int m10 = F[1][0] * M[0][0] + F[1][1] * M[1][0];
	int m11 = F[1][0] * M[0][1] + F[1][1] * M[1][1];
	F[0][0] = m00, F[0][1] = m01, F[1][0] = m10, F[1][1] = m11;
}

int fib(int n) {
	if(n <= 1) return n;
	int M[2][2] = {{1, 1}, {1, 0}},
		F[2][2] = {{1, 1}, {1, 0}};
	for(int i = 2; i < n; i++)
		matrixMul(F, M);
	return F[0][0];
}
