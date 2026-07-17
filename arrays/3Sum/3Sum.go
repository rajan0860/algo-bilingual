package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	fmt.Println(thrSumWithBruteForce([]int{-4, -1, -1, 0, 1, 2}))

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
