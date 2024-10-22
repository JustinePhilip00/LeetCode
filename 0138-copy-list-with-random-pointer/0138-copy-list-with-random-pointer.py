"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mymap={None:None};
        ptr1 = head;
        while ptr1:
            copyNode = Node(ptr1.val);
            mymap[ptr1] = copyNode;
            ptr1=ptr1.next;
        ptr1= head;
        while ptr1:
            copyNode = mymap[ptr1];
            copyNode.next = mymap[ptr1.next];
            copyNode.random = mymap[ptr1.random];
            ptr1=ptr1.next;
        
        return mymap[head];
        
        
        
        