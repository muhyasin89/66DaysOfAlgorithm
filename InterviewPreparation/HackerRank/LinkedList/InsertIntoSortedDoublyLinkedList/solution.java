class DoublyLinkedListNode {
    int data;
    DoublyLinkedListNode next;
    DoublyLinkedListNode prev;
}

public class DoublyLinkedListNode
SortedInsert(DoublyLinkedListNode head,int data) {
    DoublyLinkedListNode n = new DoublyLinkedListNode();
    n.data = data;
    if (head == null) {
        return n;
    }
    else if (data < head.data) {
        n.next = head;
        head.prev = n;
        return n;
    }
    else {
        Node rest = SortedInsert(head.next, data);
        head.next = rest;
        rest.prev = head;
        return head;
    }
}