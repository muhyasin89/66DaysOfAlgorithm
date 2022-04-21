var tribonacci = function(n) {
    
    let memo = [1, 1];

    for(let i=3; i<=n; i++){
        let cur = memo[i-1] + memo[i-2];
        memo.push(cur);
    }
    return memo[n]
    
};