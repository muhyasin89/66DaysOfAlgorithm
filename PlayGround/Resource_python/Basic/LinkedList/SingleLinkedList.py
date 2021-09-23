class SingleLinkedList:
    none = None

    def __init__(self, val=0, next=none):
        assert next is SingleLinkedList.none or isinstance(
            next, SingleLinkedList
        )
        self.val = val
        self.next = next


arr = [1, 4, 5, 6, 7]

# change list to linked list
def changeListToLinked(arr):
    if len(arr) == 1:
        return SingleLinkedList(arr[0])
    else:
        return SingleLinkedList(arr[0], changeListToLinked(arr[1:]))


# print linked list
def printLinkedList(linkedlist):
    head = linkedlist

    while head:
        print("->", head.val, end="")
        head = head.next

    print("\n")


# linkedlist to Array
def LinkedListToArray(linked_list):
    arr = []

    curr = linked_list
    while curr:
        arr.append(curr.val)
        curr = curr.next

    return arr


printLinkedList(changeListToLinked(arr))
# [4, 2, 1, 3, 5]


# AddFront
# AddBack
# Traverse
# RemoveFront
# RemoveBack
# Size
