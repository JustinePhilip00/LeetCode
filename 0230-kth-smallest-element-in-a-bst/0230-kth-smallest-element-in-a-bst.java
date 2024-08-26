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

public class Solution {
    private int count = 0;
    private int result = -1;
    
    public int kthSmallest(TreeNode root, int k) {
        count = 0;
        result = -1;
        inOrderTraversal(root, k);
        return result;
    }
    
    private void inOrderTraversal(TreeNode node, int k) {
        if (node == null || count >= k) {
            return;
        }
        
        inOrderTraversal(node.left, k);
        count++;
        if (count == k) {
            result = node.val;
            return;
        }
        inOrderTraversal(node.right, k);
    }
}
    