===========================
what is Binary Tree? |||
===========================
A tree whose elements have at most 2 children is called a binary tree. Since each element in a binary tree can have only 2 children, we typically name them the left and right child.

Binary Tree Representation in C: A tree is represented by a pointer to the topmost node in tree.

    ===========================
    Tree Node contains? |||
    ===========================
    1. Data
    2. Pointer to left child
    3. Pointer to right child


    ===========================
    Type of Binary Tree? |||
    ===========================
    1. Full Binary Tree
    2. Complete Binary Tree
    3. Perfect Binary Tree A
    4. Balanced Binary Tree

    ===========================
    what is Full Binary Tree? |||
    ===========================
    A Binary Tree is a full binary tree if every node has 0 or 2 children

    <https://leetcode.com/problems/all-possible-full-binary-trees/>

    ===========================
    what is Complete Binary Tree ? |||
    ===========================
    A Binary Tree is a Complete Binary Tree if all the levels are completely filled except possibly the last level and the last level has all keys as left as possible

```
             18
           /    \
         15      30
        /  \     /  \
      40    50 100   40


               18
           /       \
         15         30
        /  \        /  \
      40    50    100   40
     /  \   /
    8   7  9
```

    Practice:
    <https://leetcode.com/problems/check-completeness-of-a-binary-tree/>


    =================================
    what is Perfect Binary Tree? |||
    =================================
    A Binary tree is a Perfect Binary Tree in which all the internal nodes have two children and all leaf nodes are at the same level.

```
             18
           /    \
         15       30
        /  \     /  \
      40    50 100   40


            18
           /  \
         15    30
```

    Practice:
    <https://leetcode.com/problems/balanced-binary-tree/>

    =================================
    what is Balanced Binary Tree? |||
    =================================
    A binary tree is balanced if the height of the tree is O(Log n) where n is the number of nodes.

    Practice
    <https://leetcode.com/problems/balanced-binary-tree/>

==============================
why we do need a Binary Tree?|
==============================

1. One reason to use trees might be because you want to store information that naturally forms a hierarchy.
2. Trees (with some ordering e.g., BST) provide moderate access/search (quicker than Linked List and slower than arrays).
3. Trees provide moderate insertion/deletion (quicker than Arrays and slower than Unordered Linked Lists).
4. Like Linked Lists and unlike Arrays, Trees don’t have an upper limit on number of nodes as nodes are linked using pointers.

==============================
what is Binary Tree used for?|
==============================

1. Manipulate hierarchical data.
2. Make information easy to search (see tree traversal).
3. Manipulate sorted lists of data.
4. As a workflow for compositing digital images for visual effects.
5. Router algorithms
6. Form of a multi-stage decision-making (see business chess).

=========================================
can you give me simple example of Tree?|
========================================

===========================================
what is related topic that you need to |||
understand before Tree, |||
and explain why? |||
===========================================

1. The maximum number of nodes at level ‘l’ of a binary tree is 2l.
   Here level is the number of nodes on the path from the root to the node (including root and node). Level of the root is 0.
   This can be proved by induction.
   For root, l = 0, number of nodes = 20 = 1
   Assume that the maximum number of nodes on level ‘l’ is 2l
   Since in Binary tree every node has at most 2 children, next level would have twice nodes, i.e. 2 \* 2l

2. The Maximum number of nodes in a binary tree of height ‘h’ is 2h – 1.
   A tree has maximum nodes if all levels have maximum nodes. So maximum number of nodes in a binary tree of height h is 1 + 2 + 4 + .. + 2h. This is a simple geometric series with h terms and sum of this series is 2h– 1.
   In some books, the height of the root is considered as 0. so above formula becomes 2h+1 – 1

3. In a Binary Tree with N nodes, minimum possible height or the minimum number of levels is? Log2(N+1) ?  
   This can be directly derived from point 2 above. If we consider the convention where the height of a root node is considered as 0, then above formula for minimum possible height becomes | Log2(N+1) | – 1

4. A Binary Tree with L leaves has at least | Log2L? |+ 1 levels
   A Binary tree has the maximum number of leaves (and a minimum number of levels) when all levels are fully filled.
