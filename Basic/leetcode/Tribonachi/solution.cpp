class Solution {
public:
   
    
    int memo[38] = {0};
    int tribonacci(int n) {
        if(n==0){
            return 0;
        }else if(n==1){
            return 1;
        }else if(n==2){
            return 1;
        }else if(memo[n]){
            return memo[n];    
        }
        return memo[n] = tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n-3);
        // or 1-liner:
        // return memo[n % 2] = memo[n % 2] ? memo[n % 2] : n <= 1 ? n : fib(n - 1) + fib(n - 2);
    }
};