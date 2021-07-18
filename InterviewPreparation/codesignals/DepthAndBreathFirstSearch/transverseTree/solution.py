def traverseTree(t):
    if t is None:
        return []
    res = []
    q = [t]
    while q:
        v = q.pop(0)
        res += [v.value]
        if v.left:
            q += [v.left]
        if v.right:
            q += [v.right]
    return res
