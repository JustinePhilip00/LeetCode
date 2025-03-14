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
    public int findSecondMinimumValue(TreeNode root) {
        Set<Integer> myset = new HashSet<Integer>();
        dfs(root, myset);
        if (myset.size() < 2){
            return -1;

        }

        List<Integer> sortedList = new ArrayList<>(myset);
        Collections.sort(sortedList);
        return sortedList.get(1);

    }

    private void dfs(TreeNode node, Set<Integer> myset) {
        if (node == null) {
            return;
        }
        myset.add(node.val);
        dfs(node.left, myset);
        dfs(node.right, myset);
    }
    

}
