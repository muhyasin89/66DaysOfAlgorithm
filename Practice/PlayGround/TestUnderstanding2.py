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


def testing_with_list(arr, insert):
    print("first random arr", arr)

    print("insert arr", insert)

    reversed_sort = reversedBubbleSorted(arr)
    print(reversed_sort)

    sorted_arr = BubbleSorted(arr)
    print(sorted_arr)

    print(insert_list_beginning(arr, insert))

    sorted_arr = BubbleSorted(arr)
    print(sorted_arr)

    remove_duplicate = list(dict.fromkeys(arr))
    # print(remove_duplicate)

    return remove_duplicate


n = 10

arr = get_random_list(n)
insert = get_random_list(n)

# arr = testing_with_list(arr, insert)

# insert_list_beginning(arr, insert)
print(arr)


print("============|LinkedList Section|================")
# LinkedList section


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


def printLinkedList(linked_list):
    curr = linked_list
    while curr:
        print("->", curr.val, end="")
        curr = curr.next

    print("\n")


linked_list = changeListIntoLinkedList(arr)

# unsort linked list
print(printLinkedList(linked_list))


insert_linked = changeListIntoLinkedList(insert)
print(printLinkedList(insert_linked))

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
