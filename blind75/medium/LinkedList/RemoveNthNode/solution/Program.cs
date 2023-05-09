/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode RemoveNthFromEnd(ListNode head, int n) {
       //create list node and itterate all

       List<int> listNode = new List<int>();

        var curr = head;
        while(curr != null){
            listNode.Add(curr.val);
            curr = curr.next;
        } 

        //remove index in list
        var removeIndex = listNode.Count - n;
        listNode.RemoveAt(removeIndex);

        // ittreate all into linkList again
        ListNode result = new ListNode();
        var dummy = result;
        foreach(int i in listNode){
            dummy.next = new ListNode(i);
            dummy = dummy.next;
        }
        // return head

        return result.next;
        
    }
}