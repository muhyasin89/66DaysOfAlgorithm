# from typing import List


def section_message(section):
    message = "=================" + section + "================="
    print(message)


"""
===============================================
||||||||||||||     Array Section   |||||||||||
===============================================
"""


def bubble_sort(array):

    n = len(array)

    for i in range(n):
        # print("i", i)
        for j in range(0, n - i - 1):
            # print("j", j)
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


def partition(start, end, arr):
    pivot_index = start
    pivot = arr[pivot_index]

    while start < end:
        while start < len(arr) and arr[start] <= pivot:
            start += 1

        while arr[end] > pivot:
            end -= 1

        if start < end:
            arr[start], arr[end] = arr[end], arr[start]
    arr[end], arr[pivot_index] = arr[pivot_index], arr[end]

    return end


def quickSort(start, end, arr):
    if start < end:
        p = partition(start, end, arr)

        quickSort(start, p - 1, arr)
        quickSort(p + 1, end, arr)

    return arr


section_message("List")
first_input = [4, 2, 1, 3, 5]
print(first_input)
quick_sort = quickSort(0, len(first_input) - 1, first_input)
print("quick_sort", quick_sort)
# sort_list = bubble_sort(first_input)

reverse_input = first_input[::-1]
print(reverse_input)

"""
===============================================
||||||||||||||  Linked List Section |||||||||||
===============================================
"""


class ListNode:
    empty = None

    def __init__(self, val=0, next=empty):
        assert next is ListNode.empty or isinstance(next, ListNode)
        self.val = val
        self.next = next


# push node at beginning
def push(new_data, linked_list):
    new_data = ListNode(new_data)
    new_data.next = linked_list
    linked_list = new_data

    return linked_list  # return new head


def push_node(new_node, linked_list):
    new_node.next = linked_list
    linked_list = new_node

    return linked_list


def append_node(new_node, linked_list):
    curr = linked_list
    while curr:
        curr = curr.next

    curr = new_node
    curr.next = None


def insert_after(prev_node, new_data, linked_list):
    pass


def changeLinkedListToArray(head):
    array = []
    curr = head
    while curr != None:
        array.append(curr.val)
        curr = curr.next
    return array


def reverseLinkedList(linked_list):
    prev = None
    current = linked_list
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    head = prev

    return head


def changeListIntoLinkedList(array):
    """Takes a Python list and returns a Link with the same elements."""
    if len(array) == 1:
        return ListNode(array[0])
    return ListNode(array[0], changeListIntoLinkedList(array[1:]))


def print_linked_list(head):
    curr = head
    while curr != None:
        print("->", curr.val, end=" ")
        curr = curr.next

    print("\n")


# head = example1()

section_message("Linked Link")
linked_list = changeListIntoLinkedList(first_input)
new_list = changeLinkedListToArray(linked_list)
print("linkedList to Array", new_list)

result_linkedList = changeListIntoLinkedList(quick_sort)
print_linked_list(result_linkedList)

reverse_linked = reverseLinkedList(result_linkedList)

print_linked_list(reverse_linked)

section_message("Tree")

"""
===============================================
||||||||||||||    Tree Section      |||||||||||
===============================================
"""
