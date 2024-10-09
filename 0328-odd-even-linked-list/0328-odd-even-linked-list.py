# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head;
        oddptr = head;
        evenptr= head.next;
        evenhead = evenptr;
        
        while evenptr and evenptr.next:
            oddptr.next= evenptr.next;
            oddptr = oddptr.next;
            evenptr.next = oddptr.next;
            evenptr= evenptr.next;
        oddptr.next = evenhead;
        return head;
            

            
        