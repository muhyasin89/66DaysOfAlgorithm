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

func PreOrder(root *Node) {
	if root == nil {
		return
	}

	if root.val != 0 {
		fmt.Printf("%d ", root.val)
	}
	PreOrder(root.left)
	PreOrder(root.right)
}

func InOrder(root *Node) {
	if root == nil {
		return
	}

	InOrder(root.left)
	if root.val != 0 {
		fmt.Printf("%d ", root.val)
	}
	InOrder(root.right)
}

func PostOrder(root *Node) {
	if root == nil {
		return
	}

	PostOrder(root.left)
	PostOrder(root.right)
	if root.val != 0 {
		fmt.Printf("%d ", root.val)
	}

}

func main() {
	arr := []int{1, 4, 5, 6, 7}

	first_tree := sortArrBST(arr)

	fmt.Println("PreOrder Transversal")
	PreOrder(first_tree)
	fmt.Println()

	fmt.Println("InOrder Transversal")
	InOrder(first_tree)
	fmt.Println()

	fmt.Println("PostOrder Transversal")
	PostOrder(first_tree)
	fmt.Println()
}
