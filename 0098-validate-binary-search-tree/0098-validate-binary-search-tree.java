/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isValidBST(TreeNode root) {
//         if(root == null)
//         {
//             return true;
//         }
//         if(root.left==null || root.right==null)
//         {
//             return true;
//         }
//         if(root.left.val< root.val && root.right.val>root.val)
//         {
//             return true;
//         }
//         else
//         {
//             return false;
//         }
        
        
//         return isValidBST(root.left) && isValidBST(root.right);
        return validate(root,Double.NEGATIVE_INFINITY,Double.POSITIVE_INFINITY);
    }
    private boolean validate(TreeNode root, double left, double right )
    {
        if(root==null)
        {
            return true;
        }
        if(!(left<root.val && right>root.val))
        {
            return false;
        }
        return validate(root.left,left,root.val) && validate(root.right, root.val, right);
    }
}