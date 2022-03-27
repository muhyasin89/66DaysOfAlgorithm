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
