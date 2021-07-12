SinglyLinkedListNode:
    int data
    SinglyLinkedListNode next

def insertNodeAtPosition(llist, data, position):
    # Write your code here
    # create a new node
    new = SinglyLinkedListNode(data)
    # set a pointer to head in case our initial position is not 0
    pointer = llist
    # set our counter so we can traverse through SLL
    counter = 1

    while pointer.next is not None:
        # and if our counter is equal to the position given
        if counter == position:
            # our new node will point to pointer.next
            new.next = pointer.next
            # and our pointer.next will be equal to our new node
            pointer.next = new
            break
        # we traverse the list one position at a time until
        # counter == position
        counter += 1
        pointer = pointer.next
    # we return the head as requested
    return llist
