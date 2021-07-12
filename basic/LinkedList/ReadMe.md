===========================
what is Linked List?|||
===========================

a linear data structure, in which the elements are not stored at contiguous memory locations.

In simple words, a linked list consists of nodes where each node contains a data field and a reference(link) to the next node in the list.

    ===========================
    Type of Linked List?|
    ===========================
    * Singly Linked List
    * Circular Linked List
    * Doubly Linked List

===============================
why we do need a Linked List?|
===============================
Advantages over arrays

1. Dynamic size
2. Ease of insertion/deletion

===================================
What is disadvantage Linked List?|
===================================

1. Random access is not allowed. We have to access elements sequentially starting from the first node. So we cannot do binary search with linked lists efficiently with its default implementation. Read about it here.
2. Extra memory space for a pointer is required with each element of the list.
3. # Not cache friendly. Since array elements are contiguous locations, there is locality of reference which is not there in case of linked lists.
   # can you give me simple example of Linked List?|

===========================================
what is related topic that you need to |||
understand before Linked List, |||
and explain why? |||
===========================================
Tranversal
Traversing a data structure means: "visiting" or "touching" the elements of the structure, and doing something with the data. (Traversing is also sometimes called iterating over the data structure)

To delete a node of a linked list recursively we need to do the following steps.

1.We pass node* (node pointer) as a reference to the function (as in node* &head)

2.Now since current node pointer is derived from previous node’s next (which is passed by reference) so now if the value of the current node pointer is changed, previous next node’s value also gets changed which is the required operation while deleting a node (i.e points previous node’s next to current node’s (containing key) next).

3.Find the node containing the given value.

4.Store this node to deallocate it later using free() function.

5.Change this node pointer so that it points to it’s next and by performing this previous node’s next also get properly linked.

===================================
Array vs Linked List?|
===================================
Arrays store elements in contiguous memory locations, resulting in easily calculable addresses for the elements stored and this allows a faster access to an element at a specific index

Linked lists are less rigid in their storage structure and elements are usually not stored in contiguous locations, hence they need to be stored with additional tags giving a reference to the next element.

    ===================================
    Major differences are listed below:
    ===================================
    size: dynamic size which can change at runtime.
    Memory allocation: dynamically allocated array also allocates memory at runtime.
    Memory efficiency: linked lists can increase their sizes step-by-step proportionately to the amount of data.
    Execution time: modifying a certain element are faster in array, inserting/deleting an element in the data are faster in linked list

===================================
favour of Linked Lists:
===================================

- The size of the arrays is fixed
- Inserting a new element in an array of elements is expensive
- Deletion is also expensive with arrays until unless some special techniques are used.

Advantage LinkedList over Array:

- Dynamic size
- Ease of insertion/deletion

Disadvantage of LinkedList:

- Random access is not allowed
- Extra memory space for a pointer
- Arrays have better cache locality that can make a pretty big difference in performance.
