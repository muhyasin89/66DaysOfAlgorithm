class Position:
    def __init__(self, val=0):
        self.val = val


def quickSort(start, end, arr):

    n = len(arr)

    start = (
        Position(start.val) if isinstance(start, Position) else Position(start)
    )
    left = (
        Position(start.val) if isinstance(start, Position) else Position(start)
    )
    right = (
        Position(start.val) if isinstance(start, Position) else Position(start)
    )
    mid = (
        Position(start.val) if isinstance(start, Position) else Position(start)
    )
    end = Position(end.val) if isinstance(end, Position) else Position(end)

    if start.val > end.val:
        return
    pivot = Position(arr[end.val])

    if start.val < 0 or start.val >= n or end.val < 0 or end.val >= n:
        raise AssertionError

    while right.val != end.val:
        if arr[right.val] < pivot.val:
            # left, right
            arr[left.val], arr[right.val] = arr[right.val], arr[left.val]
            # mid, right
            arr[mid.val], arr[right.val] = arr[right.val], arr[mid.val]
            left.val += 1
            right.val += 1
            mid.val += 1
        elif arr[right.val] == pivot.val:
            # mid, right
            arr[mid.val], arr[right.val] = arr[right.val], arr[mid.val]
            mid.val += 1
            right.val += 1
        elif arr[right.val] > pivot.val:
            right.val += 1

        # mid, right
        arr[mid.val], arr[right.val] = arr[right.val], arr[mid.val]
        start = start if isinstance(start, Position) else Position(start)
        left = left if isinstance(left, Position) else Position(left)
        mid = mid if isinstance(mid, Position) else Position(mid)
        end = end if isinstance(end, Position) else Position(end)

        quickSort(start.val, left.val - 1, arr)
        quickSort(mid.val + 1, end.val, arr)


# arr = [2, 3, 4, 1, 2, 4, 3, 5, 5, 2, 2, 2, 1, 1, 1, 6, 7]
arr = [
    400000,
    400000,
    400000,
    2000000,
    2000000,
    2000000,
    2000000,
    2000000,
    2000000,
    2000000,
    2000000,
    2000000,
    2000000,
    2500000,
    2500000,
    2500000,
    3000000,
    3000000,
    3000000,
    3000000,
    3000000,
    3000000,
    3000000,
    3000000,
    3000000,
    3000000,
    3000000,
]

quickSort(0, len(arr) - 1, arr)
print(arr)
