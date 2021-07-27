package InterviewPreparation.LeetCode.Tree.PathSum2;

import java.util.List;
import java.util.ArrayList;

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

    public void getLeafPathSum(TreeNode root, List<List<Integer>> Olist, List<Integer> list, int targetSum) {
        if (root == null)
            return;
        if (root.left == null && root.right == null) {
            if (targetSum - root.val == 0) {
                list.add(root.val);
                Olist.add(new ArrayList<Integer>(list));
                list.remove(list.size() - 1);
            }
            return;
        }
        list.add(root.val);

        getLeafPathSum(root.left, Olist, list, targetSum - root.val);
        getLeafPathSum(root.right, Olist, list, targetSum - root.val);

        System.out.println("Inside half complete list" + list + " Olist:" + Olist);
        list.remove(list.size() - 1);
    }

    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        List<List<Integer>> output = new ArrayList<List<Integer>>();
        getLeafPathSum(root, output, new ArrayList<Integer>(), targetSum);
        return output;
    }

    public static void main(String[] args) {

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
