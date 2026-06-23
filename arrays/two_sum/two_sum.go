package main

import "fmt"

// solve runs the solution logic
func twoSum(nums []int, target int) (int, int) {
	fmt.Printf("Input: nums = %v, target = %d\n", nums, target)

	m := make(map[int]int)
	for i, num := range nums {
		sub := target - num
		if j, ok := m[sub]; ok {
			fmt.Printf("Output: [%d, %d]\n", j, i)
			return j, i
		}
		m[num] = i
	}
	fmt.Println("No two sum solution found.")
	return -1, -1
}

func main() {
	testCases := []struct {
		nums   []int
		target int
	}{
		{[]int{2, 7, 11, 15}, 9},
		{[]int{3, 2, 4}, 6},
		{[]int{3, 3}, 6},
	}

	for _, tc := range testCases {
		twoSum(tc.nums, tc.target)
	}
	fmt.Println("Go solution ran successfully!")
}
