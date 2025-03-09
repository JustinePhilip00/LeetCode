# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # if not root:
        #     return [];
        
        # q= deque([root]);
        # mylist=[];
        # while q:
        #     level_size = len(q)
        #     for i in range(level_size):
        #         node = q.popleft();
        #         if i==level_size-1:
        #             mylist.append(node.val);
        #         if node.left:
        #             q.append(node.left);
        #         if node.right:
        #             q.append(node.right);
                
        # return mylist;
        output = [];
        q = deque();
        q.append(root);

        while q:
            rightside = None;
            qlen = len(q);
            for i in range(qlen):
                node = q.popleft();
                if node:
                    rightside= node;
                    q.append(node.left);
                    q.append(node.right);
            if rightside:
                output.append(rightside.val);
        return output;
        