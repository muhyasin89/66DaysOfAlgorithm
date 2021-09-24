arr = [1, 4, 5, 6, 7]


print(arr)


class LinkedList:
    none = None

    def __init__(self, val=0, next=none):
        assert next is LinkedList.none or isinstance(next, LinkedList)
        self.val = val
        self.next = next


def changeListToLinked(arr):
    if len(arr) == 1:
        return LinkedList(arr[0])
    else:
        return LinkedList(arr[0], changeListToLinked(arr[1:]))


def printLinkedList(linkedlist):
    head = linkedlist

    while head:
        print("->", head.val, end="")
        head = head.next

    print("\n")


linkL = changeListToLinked(arr)
printLinkedList(linkL)


def reverseLinkedList(linkedlist):
    head = linkedlist
    curr = head
    prev = None

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    head = prev

    return head


linkL = reverseLinkedList(linkL)
printLinkedList(linkL)


def changeLinkedListToArr(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next

    return arr


print(changeLinkedListToArr(linkL))
