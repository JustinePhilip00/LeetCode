# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter= 0;
        
        def dfs(root):
            if not root:
                return 0;
            
            
            left_child = dfs(root.left);
            right_child =dfs(root.right);
            
            self.diameter = max(self.diameter,left_child+right_child);
            # print("self.diameter:"+ str(self.diameter));
            # print("1+max(left_child,right_child)"+ str(1+max(left_child,right_child)) );
            return 1+max(left_child,right_child);
            
        dfs(root);
        return self.diameter;
        