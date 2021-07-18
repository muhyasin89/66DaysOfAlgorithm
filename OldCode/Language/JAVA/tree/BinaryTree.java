package tree;

public class BinaryTree {

    Node root;

    private class Node{
        int value;
        Node left;
        Node right;
    
        Node(int value){
            this.value = value;
            right = null;
            left = null;
        }
    }
    
    private Node addRecursive(Node current, int value){
        if(current == null){
            return new Node(value);
        }
    
        if(value < current.value){
            current.left = addRecursive(current.left, value);
        }else if(value < current.value){
            current.right = addRecursive(current.right, value);
        }else{
            return current;
        }
    
        return current;
    }
    
    public void add(int value){
        root = addRecursive(root, value);
    }
    
    private boolean containsNodeRecursive(Node current, int value){
        if(current == null){
            return false;
        }
    
        if(value == current.value){
            return true;
        }
    
        return value < current.value 
            ? containsNodeRecursive(current.left, value) 
            : containsNodeRecursive(current.right, value);
    }
    
    public boolean containsNode(int value){
        return containsNodeRecursive(root, value);
    }

    private Node deleteRecursive(Node current, int value){
        if(current == null){
            return null;
        }

        if(value == current.value){
            //code to delete node is here
        }

        if( value < current.value ){
            current.left =  deleteRecursive(current.left, value);
            return current;
        }

        current.right = deleteRecursive(current.right, value);

        return current;
    }

    private int findSmallestValue(Node root){
        return root.left == null ? root.value : findSmallestValue(root.left)
    }

    public static void main(String args[]){
        System.out.println("Hello Java");  
    }
}

