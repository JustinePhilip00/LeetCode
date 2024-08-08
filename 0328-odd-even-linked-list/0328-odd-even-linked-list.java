/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode oddEvenList(ListNode head) {
       if(head==null)
       {
           return null;
       }
        ListNode oddptr= head;
        ListNode evenptr=head.next;
        ListNode evenhead= head.next;
        while( evenptr!=null && evenptr.next!=null)
        {
            oddptr.next=oddptr.next.next;
            evenptr.next=evenptr.next.next;
         
            oddptr= oddptr.next;
            evenptr=evenptr.next;
            
        }
        
       oddptr.next=evenhead;
       return head;
        
    }
}