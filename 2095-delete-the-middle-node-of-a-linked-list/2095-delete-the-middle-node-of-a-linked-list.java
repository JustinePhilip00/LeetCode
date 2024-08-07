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
    public ListNode deleteMiddle(ListNode head) {
        int n=0;
        int mid=0;
        ListNode temp = head;
        if(head==null || head.next==null)
        {
            return null;
        }
        while(temp.next!=null)
        {
            temp= temp.next;
            n++;
        }
    
        if((n+1)%2!=0)
        {
            mid=n/2;
        }
        else
        {
            mid=(n/2)+1;
        }
        temp =head;
        System.out.println(mid);
        for(int i=0;i<mid-1;i++)
        {
            temp=temp.next;
        }
        temp.next=temp.next.next;
        
        
        
        return head;
    }
    
}