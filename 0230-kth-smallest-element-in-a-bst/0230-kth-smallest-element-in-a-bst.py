# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
# # #         O(n) approach : recursive
# #         mystack=[];
# #         def dfs(curr):
            
# #             if not curr:
# #                 return ;
# #             dfs(curr.left);
# #             mystack.append(curr.val);
# #             dfs(curr.right);
# #             if mystack:
# #                 for i in range(len(mystack)):
# #                     if i== k-1:
# #                         return mystack[i];
# #         return dfs(root);

# # faster way as it is Iterative DFS method: O(n) space
#             mystack =[];
#             curr= root;
#             while mystack or curr :
#                 while curr:
#                     mystack.append(curr);
#                     curr = curr.left;
#                 curr= mystack.pop();
#                 k=k-1;
#                 if k==0:
#                     return curr.val;
#                 curr=curr.right;
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        mystack = [];
        def dfs(node):
            if not node: return ;
            dfs(node.left)
            mystack.append(node.val); 
            if len(mystack) == k:
                return;
            dfs(node.right)
        dfs(root);
        return mystack[k-1];                
                    
        