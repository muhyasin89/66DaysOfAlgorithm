Reference:
https://www.youtube.com/watch?v=xFv_Hl4B83A

===========================
what the problem? |||
===========================
The N Queen is the problem of placing N chess queens on an N×N chessboard so that no two queens attack each other.
===========================
what the Goal? |||
===========================
{ 0, 1, 0, 0}
{ 0, 0, 0, 1}
{ 1, 0, 0, 0}
{ 0, 0, 1, 0}
===========================
|Example? |||
===========================

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

1. Start in the leftmost column
2. If all queens are placed
   return true
3. Try all rows in the current column.
   Do following for every tried row.
   a) If the queen can be placed safely in this row
   then mark this [row, column] as part of the
   solution and recursively check if placing
   queen here leads to a solution.
   b) If placing the queen in [row, column] leads to
   a solution then return true.
   c) If placing queen doesn't lead to a solution then
   unmark this [row, column] (Backtrack) and go to
   step (a) to try other rows.
4. If all rows have been tried and nothing worked,
   return false to trigger backtracking.

=====================================
how many ways to solve this problem?|
=====================================
so far just one

===========================
how long it takes? ||
===========================
space and time complexity is O(n)
