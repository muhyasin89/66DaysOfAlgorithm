def partition(low, high, arr):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def quickSort(low, high, arr):
    if low < high:
        p = partition(low, high, arr)

        quickSort(low, p - 1, arr)
        quickSort(p + 1, high, arr)

    return arr


arr = [3, 1, 5, 2, 6, 4, 9, 7, 8]

print(quickSort(0, len(arr) - 1, arr))
