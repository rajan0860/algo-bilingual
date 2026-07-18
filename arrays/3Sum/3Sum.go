package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	fmt.Println(thrSumOptimized([]int{-4, -1, -1, 0, 1, 2}))

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
	var b strings.Builder
	for _, num := range row {
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
	for i := 0; i <= len(num)-1; i++ {
		if i > 0 && num[i] == num[i-1] {
			continue
		}
		initPtr := i
		left := i + 1
		right := len(num) - 1
		for left < right {
			sum := num[i] + num[left] + num[right]
			if sum == 0 {
				outcome = append(outcome, []int{num[initPtr], num[left], num[right]})
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
