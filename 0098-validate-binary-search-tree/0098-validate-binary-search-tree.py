# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(curr, minVal, maxVal):
            if not curr:
                return True;
            if not (minVal<curr.val<maxVal):
                return False;
            
            return dfs(curr.left,minVal,curr.val) and dfs(curr.right,curr.val,maxVal);
        
        return dfs(root,float(-inf),float(inf));
        
            
        