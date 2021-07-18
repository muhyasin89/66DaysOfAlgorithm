===========================
what the problem? |||
===========================
the two list not same length
===========================
what the Goal? |||
===========================
Your task is to add up these huge integers and return the result in the same format
===========================
|Example? |||
===========================
For a = [9876, 5432, 1999] and b = [1, 8001], the output should be
addTwoHugeNumbers(a, b) = [9876, 5434, 0].

Explanation: 987654321999 + 18001 = 987654340000.

For a = [123, 4, 5] and b = [100, 100, 100], the output should be
addTwoHugeNumbers(a, b) = [223, 104, 105].

Explanation: 12300040005 + 10001000100 = 22301040105

===================
Information so far|
===================
the value of string must be
4 digit if not add 0 infront so it can be one

==============
unclear use?|
==============

========================================
step by step for solving this problem?|
========================================
if len of the list different populate the small one with zero

=====================================
how many ways to solve this problem?|
=====================================
so far just one

===========================
how long it takes? ||
===========================
space and time complexity is O(n)
