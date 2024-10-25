# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(curr):
            if curr is None:
                return 0  
            
            left_child = dfs(curr.left)
            if left_child == -1:
                return -1  
            
            right_child = dfs(curr.right)
            if right_child == -1:
                return -1  
            
            if abs(left_child - right_child) > 1:
                return -1 
            
            return max(left_child, right_child) + 1  
     
        return dfs(root) != -1
