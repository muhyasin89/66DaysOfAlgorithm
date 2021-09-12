def minimumAbsoluteDifference(arr):
    # Write your code here
    if len(arr) != len(list(set(arr))):
        result = 0
    n, a = arr, sorted(map(int, arr))
    return min(abs(x - y) for x, y in zip(a, a[1:]))
