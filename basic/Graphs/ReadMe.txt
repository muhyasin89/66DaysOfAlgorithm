===========================
what is  Graph?      |||
===========================
A graph is a data structure that consists of the following two components: 
1. A finite set of vertices also called as nodes. 
2. A finite set of ordered pair of the form (u, v) called as edge. 
The pair is ordered because (u, v) is not the same as (v, u) in case of a directed graph(di-graph). 
The pair of the form (u, v) indicates that there is an edge from vertex u to vertex v. The edges may contain weight/value/cost.

commonly used representations of a graph.
1. Adjacency Matrix 
2. Adjacency List 

------------------------------------------------
    ==============================
    what is Adjacency Matrix?  |||
    ==============================
    Adjacency Matrix is a 2D array of size V x V where V is the number of vertices in a graph.

    =======================
    can you colaborate? |||
    =======================
    Let the 2D array be adj[][], a slot adj[i][j] = 1 indicates that there is an edge from vertex i to vertex j. Adjacency matrix for undirected graph is always symmetric. Adjacency Matrix is also used to represent weighted graphs. If adj[i][j] = w, then there is an edge from vertex i to vertex j with weight w. 

    example
    ![alt text](https://cdncontribute.geeksforgeeks.org/wp-content/uploads/adjacencymatrix.png)

    ============================
    what is the advantage? |||
    ============================
    Representation is easier to implement and follow. Removing an edge takes O(1) time. Queries like whether there is an edge from vertex ‘u’ to vertex ‘v’ are efficient and can be done O(1).

    ============================
    what is the disadvantage? |||
    ============================
    Consumes more space O(V^2). Even if the graph is sparse(contains less number of edges), it consumes the same space. Adding a vertex is O(V^2) time. 

    practice:
    <https://leetcode.com/problems/find-the-town-judge/discuss/614768/straight-solution-adjacency-matrix >
------------------------------------------------
    ==============================
    what is Adjacency List?  |||
    ==============================
    An array of lists is used. The size of the array is equal to the number of vertices. 

    =======================
    can you colaborate? |||
    =======================
    Let the array be an array[]. An entry array[i] represents the list of vertices adjacent to the ith vertex. This representation can also be used to represent a weighted graph. The weights of edges can be represented as lists of pairs. 

    ============================
    what is the advantage? |||
    ============================
    Saves space O(|V|+|E|) . In the worst case, there can be C(V, 2) number of edges in a graph thus consuming O(V^2) space. Adding a vertex is easier.

    ============================
    what is the disadvantage? |||
    ============================
    Queries like whether there is an edge from vertex u to vertex v are not efficient and can be done O(V).

===========================
why we do need a Graph?|
===========================


===============================================
what Happen if we dont use it or understand it?|
===============================================


=========================================
can you give me simple example of Linked List?|
========================================

===========================================
what is related topic that you need to  |||
understand before Linked List,          |||
and explain why?                        |||
===========================================

===========================
example expected output |||
===========================
 Adjacency list of vertex 0
 head -> 1-> 4

 Adjacency list of vertex 1
 head -> 0-> 2-> 3-> 4

 Adjacency list of vertex 2
 head -> 1-> 3

 Adjacency list of vertex 3
 head -> 1-> 2-> 4

 Adjacency list of vertex 4
 head -> 0-> 1-> 3

 example:
 <https://leetcode.com/problems/course-schedule-ii/discuss/427037/adjacency-list-bfs>

 <https://leetcode.com/problems/find-the-town-judge/discuss/746120/adjacency-list-graph-solution-in-java>
===========================
Graph Representation |||
===========================

https://leetcode.com/problems/clone-graph/discuss/42317/graph-representation