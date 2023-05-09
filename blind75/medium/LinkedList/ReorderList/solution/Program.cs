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
    
    public void ReorderList(ListNode head) {
        // set curr from 1 node after head
        var curr = head.next; 
      
        // create list for record visited from curr
        List<ListNode> listLinked = new List<ListNode>();
        // set curr to tail
        while(curr != null){
            listLinked.Add(curr);
            curr = curr.next;
        }
      
        // set head to temporary curr
        var last = head;
        // set 2 index 1 from first second at last
        var index0 = 0;
        var index1 = listLinked.Count - 1;
        var addFromLast = true;
        // check if last index is less than index head
        while(index0 <= index1){
            // if from end remove index 1 to back --
            // if not from end remove index 0 to front ++
            if(addFromLast){
                last.next = listLinked[index1];
                index1 --;
            }else{
                last.next = listLinked[index0];
                index0++;
            }
             
            addFromLast = !addFromLast;
            last = last.next;
        }
        last.next = null;
    }
}