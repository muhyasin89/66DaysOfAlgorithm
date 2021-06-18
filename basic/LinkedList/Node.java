public class Node {
    Node next;
    int data;
    public Node(int data){
        this.data = data;
    }

    
}

public class LinkedList{
    Node head; 
    
    public void append(int data) {
        if (head == null){
            head = new Node(data);
            return;
        }
        Node current = head;
        while (current.next != null) {
            current = current.next;
        }

        current.next = new Node(data);
    }

    public void prepend(int data){
        Node newHead = new Node(data);
        newHead.next = head;
        head = newHead;
    }

    public void deleteWithValue(int data){
        if(head == null) return;

        // if the data that want to delete is the head
        if(head.data == data){
            head = head.next; //cut from linked list
            return;
        }

        Node current = head;

        while(current.next != null){
            // if next data is the one you wanna delete
            if(current.next.data = data){
                //cut out the link to the list by skip it
                current.next = current.next.next;
                return;
            }

            current = current.next;
        }
    }
}