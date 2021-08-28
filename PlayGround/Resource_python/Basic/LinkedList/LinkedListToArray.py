class LinkedList:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def LinkedListToArray(linked_list):
    arr = []

    curr = linked_list
    while curr:
        arr.append(curr.val)
        curr = curr.next

    return arr


# [4, 2, 1, 3, 5]
head = LinkedList(4)
head.next = LinkedList(2)
head.next.next = LinkedList(1)
head.next.next.next = LinkedList(3)
head.next.next.next.next = LinkedList(5)


print(LinkedListToArray(head))
