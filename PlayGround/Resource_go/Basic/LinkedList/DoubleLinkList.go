package main

import "fmt"

type Node struct {
	prev *Node
	next *Node
	key  interface{}
}

type DoubleLinkList struct {
	head *Node
	tail *Node
}

func (L *DoubleLinkList) Insert(key interface{}) {
	list := &Node{
		next: L.head,
		key:  key,
	}
	if L.head != nil {
		L.head.prev = list
	}
	L.head = list

	l := L.head
	for l.next != nil {
		l = l.next
	}
	L.tail = l
}

func (l *DoubleLinkList) PrintLinkedList() {
	list := l.head
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

func ShowBackwards(list *Node) {
	for list != nil {
		fmt.Printf("%v <-", list.key)
		list = list.prev
	}
	fmt.Println()
}

func (l *DoubleLinkList) Reverse() {
	curr := l.head
	var prev *Node
	l.tail = l.head

	for curr != nil {
		next := curr.next
		curr.next = prev
		prev = curr
		curr = next
	}
	l.head = prev
	PrintLinkedList(l.head)
}

func (S *DoubleLinkList) changeListToLinked(arr []int) {
	for i := len(arr) - 1; i >= 0; i-- {
		S.Insert(arr[i])
	}
}

func main() {
	arr := []int{1, 4, 5, 6, 7}
	link := DoubleLinkList{}

	link.changeListToLinked(arr)

	fmt.Println("\n==============================\n")
	fmt.Printf("Head: %v\n", link.head.key)
	fmt.Printf("Tail: %v\n", link.tail.key)
	link.PrintLinkedList()
	fmt.Println("\n==============================\n")
	fmt.Printf("Head: %v\n", link.head.key)
	fmt.Printf("Tail: %v\n", link.tail.key)
	link.Reverse()
	fmt.Println("\n==============================\n")
}
