===========================
what the problem? |||
===========================
Given a set of cities and distances between every pair of cities, the problem is to find the shortest possible route that visits every city exactly once and returns to the starting point
===========================
what the Goal? |||
===========================
find the shortest possible route that visits every city exactly once and returns to the starting point
===========================
|Example? |||
===========================

    ===================
    Information so far|
    ===================

    ==============
    unclear use?|
    ==============

========================================
step by step for solving this problem?|
========================================

1. Consider city 1 as the starting and ending point.
2. Generate all (n-1)! Permutations of cities.
3. Calculate cost of every permutation and keep track of minimum cost permutation.
4. Return the permutation with minimum cost.

========================================
Result Explanation?|
========================================
TSP tour in the graph is 1-2-4-3-1. The cost of the tour is 10+25+30+15 which is 80

=====================================
how many ways to solve this problem?|
=====================================

===========================
how long it takes? ||
===========================
Time Complexity: Θ(n!)
