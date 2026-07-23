package main

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
)

func main() {
	testCases := [][]int{
		{},                               // expected: [] (empty array)
		{0},                              // expected: [] (single element)
		{0, 0},                           // expected: [] (two elements, no triplet possible)
		{1, 2, -3},                       // expected: [[-3, 1, 2]]
		{1, 2, 3, 4, 5},                  // expected: [] (all positive, no valid triplet)
		{-1, -2, -3, -4},                 // expected: [] (all negative, no valid triplet)
		{0, 0, 0},                        // expected: [[0, 0, 0]]
		{0, 0, 0, 0},                     // expected: [[0, 0, 0]]
		{0, 0, 0, 0, 0},                  // expected: [[0, 0, 0]]
		{-2, -2, 0, 0, 2, 2},             // expected: [[-2, 0, 2]]
		{-1, -1, 2, 2, -1},               // expected: [[-1, -1, 2]]
		{1, 1, -2, -2, 1},                // expected: [[-2, 1, 1]]
		{-4, -1, -1, 0, 1, 2},            // expected: [[-1, -1, 2], [-1, 0, 1]]
		{3, 0, -2, -1, 1, 2},             // expected: [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]
		{0, 0, 2, -2, 1, 1, 2, -2, 4},    // expected: [[-2, 0, 2], [-2, 1, 1], [-2, -2, 4]]
		{1, -1, -3, 3, -3, -1, 1, 4, -2}, // expected: [[-2, 1, 1], [-3, -1, 4], [-2, -1, 3]]
	}

	for _, tc := range testCases {
		fmt.Println(tc, "->", thrSumWithBruteForce(tc))
		// and once your two-pointer version exists:
		// fmt.Println(tc, "->", thrSumOptimized(tc))
	}
}
func thrSumWithBruteForce(num []int) [][]int {
	outcome := [][]int{}
	seen := make(map[string]bool)
	for i := 0; i <= len(num)-1; i++ {
		for j := i + 1; j <= len(num)-1; j++ {
			for k := j + 1; k <= len(num)-1; k++ {
				if num[i]+num[j]+num[k] == 0 {
					outcome = addUnique(outcome, seen, []int{num[i], num[j], num[k]})
				}
			}
		}
	}

	return outcome
}

func makeKey(row []int) string {
	sorted := append([]int{}, row...) // copy so you don't mutate the original slice
	sort.Ints(sorted)
	var b strings.Builder
	for _, num := range sorted {
		b.WriteString(strconv.Itoa(num))
		b.WriteByte(',')
	}
	return b.String()
}

func addUnique(result [][]int, seen map[string]bool, row []int) [][]int {
	key := makeKey(row)

	if seen[key] {
		return result
	}

	seen[key] = true
	return append(result, row)
}

func thrSumOptimized(num []int) [][]int {
	outcome := [][]int{}
	sort.Ints(num)
	for i := 0; i <= len(num)-1; i++ {
		if i > 0 && num[i] == num[i-1] {
			continue
		}
		left := i + 1
		right := len(num) - 1
		for left < right {
			sum := num[i] + num[left] + num[right]
			if sum == 0 {
				outcome = append(outcome, []int{num[i], num[left], num[right]})
				left += 1
				right -= 1
				left = skipLeftDuplicates(num, left, right)
				right = skipRightDuplicates(num, left, right)
			} else if sum < 0 {
				left += 1
			} else if sum > 0 {
				right -= 1
			}
		}
	}
	return outcome
}

func skipLeftDuplicates(num []int, left, right int) int {
	for left < right && num[left] == num[left-1] {
		left += 1
	}
	return left
}

func skipRightDuplicates(num []int, left, right int) int {
	for left < right && num[right] == num[right+1] {
		right -= 1
	}
	return right
}
