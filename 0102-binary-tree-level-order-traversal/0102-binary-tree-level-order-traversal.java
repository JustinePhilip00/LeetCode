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
    public List<List<Integer>> levelOrder(TreeNode root) {
      List<List<Integer>> output = new ArrayList<>();
      Queue <TreeNode> q= new ArrayDeque<>();
      if(root!=null)
      {
          q.add(root);
      }
        while(!q.isEmpty())
        {   List<Integer> currentval = new ArrayList<>(); 
            for(int i=0,size=q.size();i<size;i++)
            {    TreeNode node = q.poll();
                currentval.add(node.val);
                if(node.left!=null)
                {
                    q.add(node.left);
                }
                if(node.right!=null)
                {
                    q.add(node.right);
                }
            }
                output.add(currentval);
        }
       return output;
    }
}