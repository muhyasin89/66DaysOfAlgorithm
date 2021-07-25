package Practice.Tree;

class Node {
    int key;
    Node left, right;

    public Node(int data) {
        key = data;
        left = right = null;
    }

    public static void main(String[] args) {
        System.out.println();
    }
}

class Tree {
    Node root;

    Tree(int key) {
        root = new Node(key);
    }

    Tree() {
        root = null;
    }

    Tree setPerfectTree() {
        Tree tree = new Tree();
        tree.root = new Node(7);
        tree.root.left = new Node(5);
        tree.root.left.left = new Node(4);
        tree.root.left.right = new Node(3);

        tree.root.right = new Node(8);
        tree.root.right.left = new Node(9);
        tree.root.right.right = new Node(20);

        return tree;
    }

    Tree setCompleteTree() {
        Tree tree = new Tree();
        tree.root = new Node(7);
        tree.root.left = new Node(5);
        tree.root.left.left = new Node(4);
        tree.root.left.left.left = new Node(2);
        tree.root.left.left.right = new Node(1);

        tree.root.left.right = new Node(3);
        tree.root.left.right.left = new Node(7);
        tree.root.left.right.right = new Node(10);
        tree.root.left.right.left.left = new Node(8);
        tree.root.left.right.left.right = new Node(9);

        return tree;

    }

    Tree setFullTree() {
        Tree tree = new Tree();
        tree.root = new Node(5);
        tree.root.left = new Node(1);
        tree.root.left.left = new Node(2);
        tree.root.left.right = new Node(4);

        tree.root.right = new Node(3);
        tree.root.right.left = new Node(7);
        tree.root.right.left.left = new Node(8);
        tree.root.right.left.right = new Node(9);

        tree.root.right.right = new Node(10);

        return tree;
    }

    public static void main(String[] args) {
        System.out.println();
    }
}