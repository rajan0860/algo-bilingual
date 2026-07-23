package main

import "fmt"

func longestSubString(s string) int {
	l, maxLen := 0, 0
	seen := make(map[rune]int)
	for r, ch := range s {
		if idx, ok := seen[ch]; ok && idx >= l {
			l = idx + 1
		}
		seen[ch] = r
		maxLen = max(maxLen, r-l+1)
	}
	return maxLen
}

func main() {
	testCases := []struct {
		input    string
		expected int
	}{
		{"", 0},
		{"a", 1},
		{"bbbbb", 1},
		{"abcabcbb", 3},
		{"pwwkew", 3},
		{"abcdef", 6},
		{" ", 1},
	}

	for _, tc := range testCases {
		result := longestSubString(tc.input)
		status := "Passed"
		if result != tc.expected {
			status = "Failed"
		}
		fmt.Printf("%s longestSubString(%q) = %v\n", status, tc.input, result)
	}
}
