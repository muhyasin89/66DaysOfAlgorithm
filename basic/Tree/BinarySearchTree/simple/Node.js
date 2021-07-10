// A utility function to search
// a given key in BST
function search(root, key)
{
    // Base Cases: root is null
    // or key is present at root
    if (root == null ||
        root.key == key)
        return root;
 
   // Key is greater than root's key
    if (root.key < key)
       return search(root.right, key);
 
    // Key is smaller than root's key
    return search(root.left, key);
}
 
// This code is contributed by rrrtnx.