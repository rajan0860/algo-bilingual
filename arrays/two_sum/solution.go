package main

import "fmt"

// solve runs the solution logic
func solve() {
	nums := []int{2, 7, 11, 15}
	target := 9
	fmt.Printf("Input: nums = %v, target = %d\n", nums, target)

	m := make(map[int]int)
	for i, num := range nums {
		sub := target - num
		if j, ok := m[sub]; ok {
			fmt.Printf("Output: [%d, %d]\n", j, i)
			return
		}
		m[num] = i
	}
	fmt.Println("No two sum solution found.")
}

func main() {
	solve()
	fmt.Println("Go solution ran successfully!")
}
