package main

import (
	"fmt"
	"math"
)

type Node struct {
	val   int
	left  *Node
	right *Node
}

func postOrderRecursive(root *Node) {
	if root == nil {
		return
	}

	postOrderRecursive(root.left)
	postOrderRecursive(root.right)
	if root.val != 0 {
		fmt.Printf("%d ", root.val)
	}
}

func preOrderRecursive(root *Node) {
	if root == nil {
		return
	}

	if root.val != 0 {
		fmt.Printf("%d ", root.val)
	}
	preOrderRecursive(root.left)
	preOrderRecursive(root.right)
}

func InOrderRecursive(root *Node) {
	if root == nil {
		return
	}

	InOrderRecursive(root.left)
	if root.val != 0 {
		fmt.Printf("%d ", root.val)
	}

	InOrderRecursive(root.right)

}

func sortArrBST(arr []int) *Node {
	if len(arr) == 0 {
		return &Node{}

	}

	mid := int(math.Floor(float64(len(arr) / 2)))
	root := &Node{arr[mid], nil, nil}
	root.left = sortArrBST(arr[:mid])
	root.right = sortArrBST(arr[(mid + 1):])

	return root
}

func main() {
	arr := []int{1, 4, 5, 6, 7}

	// mid := math.Floor(float64(len(arr) / 2))

	// fmt.Println(mid)
	// fmt.Println(arr[int(mid)])
	first_tree := sortArrBST(arr)
	fmt.Println("PreOrder Traversal - recursive solution : ")
	preOrderRecursive(first_tree)

	fmt.Println("\nInorder Traversal - recursive solution : ")
	InOrderRecursive(first_tree)

	fmt.Println("\nPost Order Traversal - recursive solution : ")
	postOrderRecursive(first_tree)

	fmt.Println("\n")

}
