class Solution {
public:
    int memo[38] = {0};
    int climbStairs(int n) {
        if(n <= 1){
            return 1;
        }else if(n == 2){
            return 2;
        }else if(memo[n]){
            return memo[n];
        }else{
            return memo[n] = climbStairs(n-1) + climbStairs(n-2);
        }
    }
};

