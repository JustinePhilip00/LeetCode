# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        myset = set();
        def dfs(node):
            if not node: return;
            myset.add(node.val);
            # if node.left:
            dfs(node.left);
            # if node.right:
            dfs(node.right);

        dfs(root);
        if len(myset) < 2:
            return -1;
        return sorted(myset)[1];
