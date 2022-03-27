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