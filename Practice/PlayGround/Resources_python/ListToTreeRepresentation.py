import random


def printMsg(msg):
    print("============{}============".format(msg))


def printAll(Left, Right, k, arr, i, j):
    print(
        "Left {}> Right {} in k:{} arr:{} i:{}, j:{}".format(
            Left[i], Right[j], k, arr, i, j
        )
    )
    print("\n")


def printRight(Right, k, arr, j):
    print("Right {} in k:{} arr:{} , j:{}".format(Right[j], k, arr, j))


def printLeft(Left, k, arr, i):
    print("Left {}> in k:{} arr:{} i:{}".format(Left[i], k, arr, i))


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        Left = arr[:mid]
        Right = arr[mid:]
        # print("Left", Left)
        # print("Right", Right)

        mergeSort(Left)
        mergeSort(Right)
        i = j = k = 0

        while i < len(Left) and j < len(Right):
            print("check All")
            if Left[i] < Right[j]:
                arr[k] = Left[i]
                printAll(Left, Right, k, arr, i, j)
                i += 1

            else:
                arr[k] = Right[j]
                printAll(Left, Right, k, arr, i, j)
                j += 1

            k += 1

        while i < len(Left):
            print("In Left")
            arr[k] = Left[i]
            printLeft(Left, k, arr, i)
            i += 1
            k += 1

        while j < len(Right):
            print("In Right")
            arr[k] = Right[j]
            printRight(Right, k, arr, j)
            j += 1
            k += 1

        return arr
    return arr


def partition(start, end, arr):
    pivot_index = start
    pivot = arr[pivot_index]
    # print("pivot", pivot_index)
    # print("arr", arr[pivot_index])

    while start < end:
        while start < len(arr) and arr[start] <= pivot:
            start += 1
        while arr[end] > pivot:
            end -= 1
        if start < end:
            arr[start], arr[end] = arr[end], arr[start]
    arr[end], arr[pivot_index] = arr[pivot_index], arr[end]

    return end


# O(n log n)
def quick_sort(start, end, arr):
    if start < end:
        p = partition(start, end, arr)

        quick_sort(start, p - 1, arr)
        quick_sort(p + 1, end, arr)
    return arr


def normalize(tree, row=0, col=0):
    try:
        node = tree[row][col]
        left = normalize(tree, row + 1, col * 2)
        right = normalize(tree, row + 1, col * 2 + 1)
        return [node, left, right] if left or right else [node]
    except:
        return None  # child index does not exist


def random_list(n):
    arr = []

    for i in range(n):
        a = random.randint(1, 20)
        arr.append(a)

    return arr


a = random_list(10)
print(a)

# a = mergeSort(a)
a = quick_sort(0, len(a) - 1, a)
print(a)


# tree_based = normalize(remove_duplicate)

# print(tree_based)
printMsg("Tree")
remove_duplicate = list(dict.fromkeys(a))
print(remove_duplicate)


class Node:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def sortedArrayToBTS(arr):
    if not arr:
        return None

    mid = len(arr) // 2

    root = Node(arr[mid])
    print("root is", arr[mid])

    root.left = sortedArrayToBTS(arr[:mid])

    root.right = sortedArrayToBTS(arr[(mid + 1) :])

    return root


def preOrder(node):
    if node == None:
        return []

    print("->", node.data, end="")

    left_list = preOrder(node.left)
    right_list = preOrder(node.right)

    return [node.data] + left_list + right_list


def inOrder(node):
    if node == None:
        return []

    left_list = inOrder(node.left)
    print("->", node.data, end="")
    right_list = inOrder(node.right)

    return left_list + [node.data] + right_list


def postOrder(node):
    if node == None:
        return []
    left_list = postOrder(node.left)
    right_list = postOrder(node.right)
    print("->", node.data, end="")

    return left_list + right_list + [node.data]


root = sortedArrayToBTS(remove_duplicate)

printMsg("PreOrder")
pre_arr = preOrder(root)
print("\n")
printMsg("In Order")
in_arr = inOrder(root)

print("\n")
printMsg("PostOrder")
post_arr = postOrder(root)
print("\n")
print(
    "pre order: {}, in order: {}, post order: {}".format(
        pre_arr, in_arr, post_arr
    )
)

printMsg("Sorted Tree")


printMsg("Full Node in Tree")
