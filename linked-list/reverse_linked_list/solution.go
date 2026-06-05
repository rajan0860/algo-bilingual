package main

import "fmt"

type Node struct {
	data int
	next *Node
}

type LinkedList struct {
	head   *Node
	length int
}

// Append — add node at the end
func (ll *LinkedList) Append(data int) {
	newNode := &Node{data: data}
	if ll.head == nil {
		ll.head = newNode
		ll.length++
		return
	}
	current := ll.head
	for current.next != nil {
		current = current.next
	}
	current.next = newNode
	ll.length++
}

// Reverse — reverse list in-place → O(n)
func (ll *LinkedList) Reverse() {
	var prev *Node // starts as nil
	current := ll.head

	for current != nil {
		nextNode := current.next // 1. save next
		current.next = prev      // 2. reverse pointer
		prev = current           // 3. move prev forward
		current = nextNode       // 4. move current forward
	}

	ll.head = prev
}

// PrintList — display the linked list
func (ll *LinkedList) PrintList() {
	current := ll.head
	for current != nil {
		fmt.Printf("%d -> ", current.data)
		current = current.next
	}
	fmt.Println("nil")
}

func main() {
	ll := &LinkedList{}

	ll.Append(1)
	ll.Append(2)
	ll.Append(3)

	fmt.Print("Original: ")
	ll.PrintList() // 1 -> 2 -> 3 -> nil

	ll.Reverse()

	fmt.Print("Reversed: ")
	ll.PrintList() // 3 -> 2 -> 1 -> nil
}
