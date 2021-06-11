"""
===========================
what the problem?       |||
===========================
We need to check the Horizontal Distances from the root for all nodes. 
If two nodes have the same Horizontal Distance (HD), then they are on the same vertical line. 
The idea of HD is simple. HD for root is 0, a right edge (edge connecting to right subtree) is 
considered as +1 horizontal distance and a left edge is considered as -1 horizontal distance. 

For example, in the above tree, HD for Node 4 is at -2, HD for Node 2 is -1, HD for 5 and 6 is 0 
and HD for node 7 is +2.

We can do preorder traversal of the given Binary Tree. 
While traversing the tree, we can recursively calculate HDs. 
We initially pass the horizontal distance as 0 for root. 
For left subtree, we pass the Horizontal Distance as Horizontal distance of root minus 1. 
For right subtree, we pass the Horizontal Distance as Horizontal Distance of root plus 1. 
For every HD value, we maintain a list of nodes in a hash map. Whenever we see a node in traversal, 
we go to the hash map entry and add the node to the hash map using HD as a key in a map.

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

We have discussed a O(n2) solution in the previous post. In this post, an efficient solution based on the hash map is discussed.  

Following is the C++ implementation of the above method. Thanks to Chirag for providing the below C++ implementation



""""