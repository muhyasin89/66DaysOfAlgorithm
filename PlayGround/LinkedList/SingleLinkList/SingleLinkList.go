package main

import "fmt"

type Node struct {
	next *Node
	key  interface{}
}

type SingleLinkedList struct {
	head *Node
}

func (S *SingleLinkedList) Insert(key interface{}) {
	singleLinkList := &Node{
		next: S.head,
		key:  key,
	}

	S.head = singleLinkList

	l := S.head
	for l.next != nil {
		l = l.next
	}
}

func (S *SingleLinkedList) PrintLinkedList() {
	list := S.head
	for list != nil {
		fmt.Printf("%+v ->", list.key)
		list = list.next
	}
	fmt.Println()
}

func PrintLinkedList(list *Node) {
	for list != nil {
		fmt.Printf("%v ->", list.key)
		list = list.next
	}
	fmt.Println()
}

func (S *SingleLinkedList) Reverse() {
	curr := S.head
	var prev *Node

	for curr != nil {
		next := curr.next
		curr.next = prev
		prev = curr
		curr = next
	}
	S.head = prev

	PrintLinkedList(S.head)
}

func (S *SingleLinkedList) changeListToLinked(arr []int) {
	for i := len(arr) - 1; i >= 0; i-- {
		S.Insert(arr[i])
	}
}

func (S *SingleLinkedList) changeLinkedListToArray() []int {
	arr := []int{}
	list := S.head

	for list != nil {
		arr = append(arr, list.key.(int))
		list = list.next
	}

	return arr
}

func main() {
	arr := []int{1, 4, 5, 6, 7}
	link := SingleLinkedList{}

	fmt.Println(arr)
	link.changeListToLinked(arr)

	fmt.Println("\n==============================\n")
	fmt.Printf("Head: %v\n", link.head.key)

	link.PrintLinkedList()
	fmt.Println("\n==============================\n")
	fmt.Printf("head: %v\n", link.head.key)
	link.Reverse()
	fmt.Println("\n==============================\n")
	result := link.changeLinkedListToArray()
	fmt.Println(result)
}
