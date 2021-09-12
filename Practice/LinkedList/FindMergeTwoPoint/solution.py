SinglyLinkedListNode:
    int data
    SinglyLinkedListNode next

def findMergeNode(head1, head2):
    currentA = head1
    currentB = head2

    # If you reached the end of one list start at the beginning of the other one
    # currentA
    if currentA.next == None:
        currentA = head2
    else:
        currentA = currentA.next

    # currentB
    if currentB.next == None:
        currentB = head1
    else:
        currentB = currentB.next

    return currentB.data
