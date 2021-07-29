
/**
 * Definition for a binary tree node.
 */

import java.util.ArrayList;
import java.util.List;

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

    public void pathSum(TreeNode root, int sum, List<Integer> cur, List<List<Integer>> ret) {
        if (root == null) {
            return;
        }

        cur.add(root.val);
        if (root.left == null && root.right == null && root.val == sum) {
            ret.add(new ArrayList<Integer>(cur));
        }

        pathSum(root.left, sum - root.val, cur, ret);
        pathSum(root.right, sum - root.val, cur, ret);
        System.out.println("Inside complete cur:" + cur + " ret" + ret);
        cur.remove(cur.size() - 1);
    }

    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        int sum = targetSum;
        List<List<Integer>> ret = new ArrayList<List<Integer>>();
        List<Integer> cur = new ArrayList<Integer>();

        pathSum(root, sum, cur, ret);
        System.out.println("Inside half complete cur:" + cur + " ret" + ret);

        return ret;
    }

    public static void main(String[] args) {
        System.out.println("welcome");

        int sum = 22;

        // [5,4,8,11,null,13,4,7,2,null,null,5,1]
        TreeNode root = new TreeNode(5);
        root.left = new TreeNode(4);
        root.left.left = new TreeNode(11);
        root.left.left.left = new TreeNode(7);
        root.left.left.right = new TreeNode(2);

        root.right = new TreeNode(8);
        root.right.left = new TreeNode(13);
        root.right.right = new TreeNode(4);
        root.right.right.left = new TreeNode(5);
        root.right.right.right = new TreeNode(1);

        TreeNode tree = new TreeNode();

        System.out.println(tree.pathSum(root, sum));
        // [[5,4,11,2],[5,8,4,5]]
    }
}