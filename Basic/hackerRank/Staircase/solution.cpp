int memo[38] = {0};
int stepPerms(int n) {
    if(n==1){
        return 1;
    }else if(n==2){
        return 2;
    }else if(n==3){
        return 4;
    }else if(memo[n]){
        return memo[n];
    }else{
        return memo[n] = stepPerms(n-1)+ stepPerms(n-2)+ stepPerms(n-3);
    }
}