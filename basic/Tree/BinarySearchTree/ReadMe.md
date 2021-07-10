===========================
what is Binary Search Tree? |||
===========================

Binary Search Tree is a node-based binary tree data structure which has the following properties:

- The left subtree of a node contains only nodes with keys lesser than the node’s key.
- The right subtree of a node contains only nodes with keys greater than the node’s key.
- The left and right subtree each must also be a binary search tree.
- There must be no duplicate nodes.

===========================
why we do need a Tree?|
===========================

===========================================
what is related topic that you need to |||
understand before Tree, |||
and explain why? |||
===========================================

Inorder traversal

```
        1
       / \
      2   3
     / \
    4  5
```

Depth First Traversals:
(a) Inorder (Left, Root, Right) : 4 2 5 1 3
(b) Preorder (Root, Left, Right) : 1 2 4 5 3
(c) Postorder (Left, Right, Root) : 4 5 2 3 1

Practice:
Inorder : <https://leetcode.com/problems/binary-tree-inorder-traversal/>
Preorder : <https://leetcode.com/problems/binary-tree-preorder-traversal/>
PostOrder: <https://leetcode.com/problems/binary-tree-postorder-traversal/>

======================================
Advantages of BST over Hash Table |||
======================================
Hash Table supports following operations in Θ(1) time.

1. Search
2. Insert
3. Delete

The time complexity of above operations in a self-balancing Binary Search Tree (BST) (like Red-Black Tree, AVL Tree, Splay Tree, etc) is O(Logn).

So Hash Table seems to beating BST in all common operations

but BST has advantage over hash:

1. We can get all keys in sorted order by just doing Inorder Traversal of BST.
   - This is not a natural operation in Hash Tables and requires extra efforts.
2. Doing order statistics, finding closest lower and greater elements, doing range queries are easy to do with BSTs.
   - Like sorting, these operations are not a natural operation with Hash Tables.
3. BSTs are easy to implement compared to hashing, we can easily implement our own customized BST.
   - To implement Hashing, we generally rely on libraries provided by programming languages.
4. With Self-Balancing BSTs, all operations are guaranteed to work in O(Logn) time.
   - But with Hashing, Θ(1) is average time and some particular operations may be costly, especially when table resizing happens

===================
Time Complexity |||
===================
The worst-case time complexity of search and insert operations is O(h) where h is the height of the Binary Search Tree. In the worst case, we may have to travel from root to the deepest leaf node. The height of a skewed tree may become n and the time complexity of search and insert operation may become O(n).
