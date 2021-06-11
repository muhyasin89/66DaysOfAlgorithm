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

//C++ program to find the Nth term
// of Fibonacci series

#include <iostream>
using namespace std; 

//Fibonacci series using recursion
int fib(int n){
    //Base Case
    if (n <= 1){
        return n;
    }

    //Recursive Call
    return fib(n - 1) + fib(n-2);
}

//Driver Code
int main(){
    int n = 6;
    printf("%d", fib(n));

    return 0;
}