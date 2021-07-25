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
        linkedList.head = linkedList.head.next  # only work for 3 linkedList
    # print(linkedList.head.data, end=" ")
    # print(linkedList.head.next.data, end=" ")
    # for i in range(len(stack_temp)):
    #     print(stack_temp[i].data, end=" ")


def set_list(linkedList, list_a):
    # remove 2 element that dont count
    stack_temp = [None] * ((len(list_a) - 1) - 2)
    curr_Node = None
    for i in range(len(list_a)):
        if i == 0:
            linkedList.head = Node(list_a[0])
        elif i == 1:
            linkedList.head.next = Node(list_a[1])
            stack_temp.append(linkedList)
            curr_Node = linkedList.head.next
        else:
            curr = i - 2
            stack_temp[curr] = Node(list_a[i])
            # check previous
            if curr > 0:
                curr_Node.next = stack_temp[curr]
                curr_Node = curr_Node.next
            else:
                curr_Node.next = Node(list_a[i])
                curr_Node = curr_Node.next
    return stack_temp


if __name__ == "__main__":
    # 2 -> 4 -> 1
    first_linkedList = LinkedList()
    # first_linkedList.head = Node(2)
    # first_linkedList_2 = Node(4)
    # first_linkedList_3 = Node(1)
    # first_linkedList.head.next = first_linkedList_2
    # first_linkedList_2.next = first_linkedList_3
    stack_temp = set_list(first_linkedList, [2, 4, 1, 5, 3, 7, 10, 8, 9])

    printList(first_linkedList, stack_temp)

    # 1 -> 4 -> 3
    second_linkedList = LinkedList()
    # second_linkedList.head = Node(1)
    # second_linkedList_2 = Node(4)
    # second_linkedList_3 = Node(3)
    # second_linkedList.next = second_linkedList_2
    # second_linkedList.next.next = second_linkedList_3

    stack_temp_2 = set_list(second_linkedList, [4, 3, 1, 10, 5, 7, 6, 8, 9])
    print("\n")
    printList(second_linkedList, stack_temp_2)
