# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque();
        output =[];
        if root:
            q.append(root);
        while q:
            mylist=[];
            for i in range(len(q)):
                node=q.popleft();
                mylist.append(node.val);
                if node.left:
                    q.append(node.left);
                if node.right:
                    q.append(node.right);
            output.append(mylist);
        return output;
            
            

        
        