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
    List<List<Integer>> result = new ArrayList<>();
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
    if(root==null)
    {
        return result;
    }
    else{
        findPath( root, targetSum, new ArrayList<>());
    }
        return result;
    }
    private void findPath (TreeNode node, int targetSum, List<Integer> pathSum)
    {
        targetSum = targetSum - node.val;
        pathSum.add(node.val);
        if(node.left==null && node.right==null && targetSum==0)
        {
            result.add(new ArrayList<>(pathSum));
        }
        else
        {
            if(node.left!=null)
            {
                findPath(node.left,targetSum,pathSum);
            }
            if(node.right!=null)
            {
                findPath(node.right,targetSum,pathSum);
            }
        }
        pathSum.remove(pathSum.size()-1);
    }
        
        
        
        
    }
