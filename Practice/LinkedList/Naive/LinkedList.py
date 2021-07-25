# Declare Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


def printList(linkedList, stack_temp):
    # Print the linked list item
    while linkedList.head != None:
        print(linkedList.head.data, end=" ")
        linkedList.head = linkedList.head.next


def setList(linkedList, list_a):
    # remove 2 element that dont count
    stack_temp = [None] * len(list_a)

    linkedList.head = Node(list_a[0])
    linkedList.head.next = Node(list_a[1])
    del list_a[1]
    del list_a[0]
    curr_Node = linkedList.head.next
    for i in range(len(list_a)):
        stack_temp[i] = Node(list_a[i])
        # check previous
        curr_Node.next = stack_temp[i]
        curr_Node = curr_Node.next

    return stack_temp


if __name__ == "__main__":
    first_linkedList = LinkedList()
    stack_temp = setList(first_linkedList, [2, 4, 1, 5, 3, 7, 10, 8, 9])
    printList(first_linkedList, stack_temp)

    print("\n")
    second_linkedList = LinkedList()
    stack_temp_2 = setList(second_linkedList, [4, 3, 1, 10, 5, 7, 6, 8, 9])
    printList(second_linkedList, stack_temp_2)
