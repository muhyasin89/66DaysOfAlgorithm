#Recursion: Fibonacci Numbers

#Question: https://www.hackerrank.com/challenges/ctci-fibonacci-numbers/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=recursion-backtracking

def fibonacci(n):
    n1, n2 = 0, 1
    count = 0
    # Write your code here.
    if n == 0:
        return n1
    while count < n:
        nth = n1+n2

        n1=n2
        n2=nth

    return nth

n = int(input())
print(fibonacci(n))