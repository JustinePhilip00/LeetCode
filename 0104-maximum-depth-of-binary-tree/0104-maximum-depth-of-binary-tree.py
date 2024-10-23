# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
#     recursive method
#         if root==None:
#             return 0;
        
#         left_subtree = self.maxDepth(root.left);
#         right_subtree = self.maxDepth(root.right);
#         return 1+ max(left_subtree,right_subtree);

    #     Breadth first search method
            if not root:
                return 0;
            level=0;
            q = deque([root]);
            while q:
                for i in range (len(q)):
                    node=q.popleft();
                    if node.left:
                        q.append(node.left);
                    if node.right:
                        q.append(node.right);
                level = level+1;
            return level;
            
        