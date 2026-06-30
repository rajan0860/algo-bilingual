package main

import "fmt"

// solve runs the solution logic
func twoSum(nums []int, target int) (int, int) {

	m := make(map[int]int)
	for i, num := range nums {
		sub := target - num
		if j, ok := m[sub]; ok {
			return j, i
		}
		m[num] = i
	}
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
		i, j := twoSum(tc.nums, tc.target)
		fmt.Printf("twoSum(%v, %d) = (%d, %d)\n", tc.nums, tc.target, i, j)
	}
}
