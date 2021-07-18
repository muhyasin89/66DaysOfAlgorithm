package interview_preparation.LeetCode.Tree.BinaryTreeLongestConsecutiveSequence;

public class Solution {
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode(int x) {
            val = x;
        }
    }

    private int result = 0;

    private int lc(TreeNode node) {
        if (node == null) {
            return 0;
        }

        int left = lc(node.left);
        int right = lc(node.right);
        int max = 1;
        if (node.left == null || node.left.val == node.val + 1) {
            max = Math.max(left + 1, max);
        }

        if (node.right == null || node.right.val == node.val + 1) {
            max = Math.max(right + 1, max);
        }

        result = Math.max(result, max);
        return max;

    }

    public int longestConsecutive(TreeNode root) {
        if (root == null) {
            return 0;
        }
        result = 0;
        lc(root);
        return result;
    }

    public int main(String[] args) {
        TreeNode root = null;
        result = longestConsecutive(root);

        return result;
    }
}