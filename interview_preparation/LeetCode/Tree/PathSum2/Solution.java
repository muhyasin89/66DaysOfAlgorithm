
/**
 * Definition for a binary tree node.
 */

import java.util.ArrayList;
import java.util.List;

@SuppressWarnings("unchecked")
public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {
    }

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    public void pathSum(TreeNode root, int sum, List<Integer> cur, List<List<Integer>> ret) {
        if (root == null) {
            return;
        }

        cur.add(root.val);
        if (root.left == null && root.right == null && root.val == sum) {
            ret.add(new ArrayList(cur));
        }

        pathSum(root.left, sum - root.val, cur, ret);
        pathSum(root.right, sum - root.val, cur, ret);
        cur.remove(cur.size() - 1);
    }

    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        int sum = targetSum;
        List<List<Integer>> ret = new ArrayList<List<Integer>>();
        List<Integer> cur = new ArrayList<Integer>();
        pathSum(root, sum, cur, ret);

        return ret;
    }

}