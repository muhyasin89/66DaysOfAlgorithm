// JavaScript program to implement
// the above approach
 
// node
class Node
{
    constructor(data)
    {
        this.data=data;
        this.next=null;
    }
}
 
/* Function to insert a node
at the beginning of a Circular
linked list */
function push(head_ref, data)
{
    let ptr1 = new Node();
    let temp = head_ref;
    ptr1.data = data;
    ptr1.next = head_ref;
   
    /* If linked list is not null
    then set the next of last node */
    if (head_ref != null)
    {
        while (temp.next != head_ref)
            temp = temp.next;
        temp.next = ptr1;
    }
    else
        ptr1.next = ptr1;
   
    head_ref = ptr1;
       
    return head_ref;
}
 
/* Function to print nodes in a
given Circular linked list */
function printList(head)
{
    let temp = head;
    if (head != null)
    {
        do
        {
            document.write(temp.data + " ");
            temp = temp.next;
        }
        while (temp != head);
    }
}
 
// Driver Code
/* Initialize lists as empty */
let head = null;
 
/* Created linked list will
       be 11.2.56.12 */
head = push(head, 12);
head = push(head, 56);
head = push(head, 2);
head = push(head, 11);
 
document.write("Contents of Circular " +
                   "Linked List:<br>");
printList(head);
 
// This code is contributed by avanitrachhadiya2155