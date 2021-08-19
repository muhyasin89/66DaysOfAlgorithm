class Position:
    def __init__(self, val=0):
        self.val = val


def change_to_position(pos, initial=True):
    if initial:
        return Position(pos.val) if isinstance(pos, Position) else Position(pos)
    else:
        return pos if isinstance(pos, Position) else Position(pos)


def quickSort(start, end, arr):

    n = len(arr)

    start = change_to_position(start)
    left = change_to_position(start)
    right = change_to_position(start)
    mid = change_to_position(start)
    end = change_to_position(end)

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
        start = change_to_position(start, False)
        left = change_to_position(left, False)
        mid = change_to_position(mid, False)
        end = change_to_position(end, False)

        quickSort(start.val, left.val - 1, arr)
        quickSort(mid.val + 1, end.val, arr)

    return arr


arr = [2, 3, 4, 1, 2, 4, 3, 5, 5, 2, 2, 2, 1, 1, 1, 6, 7]


arr = quickSort(0, len(arr) - 1, arr)
print(arr)
