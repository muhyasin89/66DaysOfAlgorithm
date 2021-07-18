# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def removeKFromList(l, k):
    # head if not none return head
    if not l:
        return l

    # if head not None and value same as k
    # go to next node
    while l and l.value == k:
        l = l.next

    n = l

    # when head and head have next node
    # if next node value is same as k
    # skip one node else go to next node
    while n and n.next:
        if n.next.value == k:
            n.next = n.next.next
        else:
            n = n.next

    return l
