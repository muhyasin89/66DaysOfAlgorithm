import random


def reversedBubbleSorted(arr):
    length_arr = len(arr)

    for i in range(0, length_arr - 1):
        for j in range(0, length_arr - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]

    return arr


def BubbleSorted(arr):
    len_arr = len(arr)

    for i in range(0, len_arr - 1):
        for j in range(0, len_arr - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def partition(start, end, arr):
    pivot = arr[end]
    i = start - 1

    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1

            arr[j], arr[i] = arr[i], arr[j]

    arr[i + 1], arr[end] = arr[end], arr[i + 1]

    return i + 1


def partitionReverse(start, end, arr):
    pivot = arr[end]
    i = start - 1

    for j in range(start, end):
        if arr[j] >= pivot:
            i += 1

            arr[j], arr[i] = arr[i], arr[j]

    arr[i + 1], arr[end] = arr[end], arr[i + 1]

    return i + 1


def quickSort(start, end, arr=[], reverse=False):
    if reverse:
        if start > end:
            p = partitionReverse(start, end, arr)
            quickSort(p + 1, end, arr)
            quickSort(start, p - 1, arr)

    else:
        if start < end:
            p = partition(start, end, arr)
            quickSort(start, p - 1, arr)
            quickSort(p + 1, end, arr)

    return arr


def get_random_list(n):
    arr = []

    for i in range(n):
        rand_num = random.randint(1, 11)
        arr.append(rand_num)

    return arr


def insert_list_beginning(arr, insert):
    reverse_insert = insert[::-1]
    for item in reverse_insert:
        arr.insert(0, item)

    return arr


def testing_with_list(arr):
    print("first random arr", arr)

    sorted_arr = quickSort(0, len(arr) - 1, arr)
    print("Sort", sorted_arr)

    print("Reverse Sort", sorted_arr[::-1])

    remove_duplicate = list(dict.fromkeys(arr))
    print(remove_duplicate)

    return remove_duplicate


n = 10

arr = get_random_list(n)

arr = testing_with_list(arr)


class LinkedList:
    none = None

    def __init__(self, val=0, next=none):
        assert next is LinkedList.none or isinstance(next, LinkedList)
        self.val = val
        self.next = next


def changeListIntoLinkedList(arr):
    if len(arr) == 1:
        return LinkedList(arr[0])

    return LinkedList(arr[0], changeListIntoLinkedList(arr[1:]))


def reverseLinkedList(head):
    prev = None
    curr = head
    while curr != None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    head = prev

    return head


def printLinkedList(linked_list):
    curr = linked_list
    while curr:
        print("->", curr.val, end="")
        curr = curr.next

    print("\n")


linked_list = changeListIntoLinkedList(arr)

# unsort linked list
print(printLinkedList(linked_list))


# insert_linked = changeListIntoLinkedList(insert)
# print(printLinkedList(insert_linked))

"""
===============================================
||||||||||||||    Tree Section      |||||||||||
===============================================
"""


class Tree:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def sortedArrIntoBST(arr):
    if not arr:
        return None

    mid = len(arr) // 2
    root = Tree(arr[mid])
    root.left = sortedArrIntoBST(arr[:mid])
    root.right = sortedArrIntoBST(arr[(mid + 1) :])
    return root


def preOrder(head):
    if head == None:
        return []

    left = preOrder(head.left)
    right = preOrder(head.right)

    return [head.data] + left + right


def inOrder(head):
    if head == None:
        return []

    left = inOrder(head.left)
    right = inOrder(head.right)

    return left + [head.data] + right


def postOrder(head):
    if head == None:
        return []

    left = postOrder(head.left)
    right = postOrder(head.right)

    return left + right + [head.data]
