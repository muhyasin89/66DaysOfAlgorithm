def partition(start, end, array):
    pivot = array[start]

    while start < end:
        while start < len(array) and array[start] <= pivot:
            start += 1

        # Decrement the end pointer till it finds an
        # element less than pivot
        while array[end] > pivot:
            end -= 1

        # If start and end have not crossed each other,
        # swap the numbers on start and end
        if start < end:
            array[start], array[end] = array[end], array[start]

    # Swap pivot element with element on end pointer.
    # This puts pivot on its correct sorted place.
    array[end], array[start] = array[start], array[end]

    # Returning end pointer to divide the array into 2
    return end


# The main function that implements QuickSort
def quick_sort(start, end, array):

    if start < end:

        # p is partitioning index, array[p]
        # is at right place
        p = partition(start, end, array)

        # Sort elements before partition
        # and after partition
        quick_sort(start, p - 1, array)
        quick_sort(p + 1, end, array)


array = [
    2000000.0,
    2500000,
    2000000.0,
    2000000.0,
    2000000.0,
    2000000.0,
    2000000.0,
    2000000.0,
    2000000.0,
    400000.0,
    400000.0,
    400000.0,
    2000000.0,
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
    2000000.0,
]
# array = [10, 7, 8, 9, 1, 5]
# array1 = [1, 3, 7, 10, 6, 5, 2]
quick_sort(0, len(array) - 1, array)

print(f"Sorted array: {array}")
