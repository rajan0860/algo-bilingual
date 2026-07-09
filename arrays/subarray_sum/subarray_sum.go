package main

import "fmt"

func main() {
	testCases := []struct {
		input    []int
		window   int
		expected int
	}{
		{[]int{2, 1, 5, 1, 3, 2}, 3, 9},
		{[]int{2, 3, 4, 1, 5}, 2, 7},
		{[]int{1, 2, 3}, 3, 6},
		{[]int{-1, -2, -3, -4}, 2, -3},
		{[]int{5}, 1, 5},
	}
	for _, tc := range testCases {
		result := bruteForceSubarraySum(tc.input, tc.window)
		status := "failed"
		if result == tc.expected {
			status = "passed"
		}
		fmt.Printf("bruteForceSubarraySum(%v, %d) = (%d) -> %s\n", tc.input, tc.window, result, status)
	}
}

func bruteForceSubarraySum(nums []int, k int) int {
	maxSum := 0
	for i := 0; i < len(nums)-k+1; i++ {
		currentSum := 0
		for j := i; j < i+k; j++ {
			currentSum = currentSum + nums[j]
		}
		maxSum = max(currentSum, maxSum)
	}
	return maxSum
}

// func optSubarraySum(nums []int, k int) int {

// }
