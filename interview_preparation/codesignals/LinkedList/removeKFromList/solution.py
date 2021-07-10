def removeKFromList(l, k):
    # check if value none return it
    # if value is same as k(deleted value)
    # make head skip one
    if l == None:  # None
        return l
    elif l.value == k:
        l = l.next

    temp = l  # set temp for head
    # loop temp is not none and temp.next not None
    # if next node is k
    # skip next to another node
    # else just go to another node
    while temp and temp.next:
        if temp.next.value == k:
            temp.next = temp.next.next
        else:
            temp = temp.next

    # if temp not none and temp.value is k
    # move head forward
    if temp and temp.value == k:
        l = l.next

    return temp
