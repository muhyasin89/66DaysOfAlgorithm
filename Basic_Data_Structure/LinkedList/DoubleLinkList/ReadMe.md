==================================
what is Doubly Linked List?|||
==================================
Doubly Linked List (DLL) contains an extra pointer, typically called previous pointer, together with next pointer and data which are there in singly linked list.

========================================
why we do need a Doubly Linked List?|
========================================

1. A DLL can be traversed in both forward and backward direction.
2. The delete operation in DLL is more efficient if pointer to the node to be deleted is given.
3. We can quickly insert a new node before a given node.

==============================================
what id Disadvantages of Doubly Linked List?|
==============================================

1. Every node of DLL Require extra space for an previous pointer. It is possible to implement DLL with single pointer though (See this and this).
2. All operations require an extra pointer previous to be maintained. For example, in insertion, we need to modify previous pointers together with next pointers. For example in following functions for insertions at different positions, we need 1 or 2 extra steps to set previous pointer.

===============================================
what Happen if we dont use it or understand it?|
===============================================

================================================
can you give me simple example of Linked List?|
===============================================

===========================================
what is related topic that you need to |||
understand before Linked List, |||
and explain why? |||
===========================================

A node can be added in four ways

1. At the front of the DLL
2. After a given node.
3. At the end of the DLL
4. Before a given node.
