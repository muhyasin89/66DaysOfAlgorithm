original
https://github.com/steelx/go-graph-traversing

BFS

```
Algorithm BFS(G, v)
    Q ← new empty FIFO queue
    Mark v as visited.
    Q.enqueue(v)
    while Q is not empty
        a ← Q.dequeue()
        // Perform some operation on a.
        for all unvisited neighbors x of a
            Mark x as visited.
            Q.enqueue(x)
```

Depth First Search

```
Algorithm DFS(G, v)
    if v is already visited
        return
    Mark v as visited.
    // Perform some operation on v.
    for all neighbors x of v
        DFS(G, x)
```
