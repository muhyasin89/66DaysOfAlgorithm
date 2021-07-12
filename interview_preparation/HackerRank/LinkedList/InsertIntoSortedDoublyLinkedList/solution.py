def sortedInsert(llist, data):
    # Write your code here
    new = DoublyLinkedListNode(data)
    # set a pointer to head in case our initial position is not 0
    pointer = llist
    # set our counter so we can traverse through SLL
    counter = 1

    if pointer == None:
        return new
    elif data < pointer.data:
        new.next = pointer
        pointer.prev = new
        return new

    else:
        rest = sortedInsert(pointer.next, data)
        pointer.next = rest
        rest.prev = pointer
        return pointer
