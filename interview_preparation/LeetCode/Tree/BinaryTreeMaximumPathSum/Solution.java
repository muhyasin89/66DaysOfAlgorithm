package interview_preparation.LeetCode.Tree.BinaryTreeMaximumPathSum;

public class Solution {
    int max;

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode(int x) {
            val = x;
        }
    }

    private int search(TreeNode root) {
        if (root == null) {
            return 0;
        }
        int left = Math.max(0, search(root.left));
        int right = Math.max(0, search(root.right));
        max = Math.max(max, root.val + left + right);

        return Math.max(left, right) + root.val;
    }

    public int MaxPathSum(TreeNode root) {
        max = Integer.MIN_VALUE;
        search(root);
        return max;
    }
}
