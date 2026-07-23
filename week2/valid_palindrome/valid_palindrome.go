package main

import (
	"fmt"
	"unicode"
)

func main() {
	testCases := []struct {
		input    string
		expected bool
	}{
		{"A man, a plan, a canal: Panama", true},
		{"race a car", false},
		{" ", true},
		{"0P", false},
		{".,", true},
	}
	for _, tc := range testCases {
		result := isPalindrome(tc.input)
		status := "Passed"
		if result != tc.expected {
			status = "Failed"
		}
		fmt.Printf("%s isPalindrome(%q) = %v\n", status, tc.input, result)
	}
}

// function to check if given string is palindrome or not
func isPalindrome(s string) bool {
	l := 0
	r := len(s) - 1
	runes := []rune(s)
	for l < r {
		if !unicode.IsDigit(runes[l]) && !unicode.IsLetter(runes[l]) {
			l++
			continue
		}
		if !unicode.IsDigit(runes[r]) && !unicode.IsLetter(runes[r]) {
			r--
			continue
		}
		if unicode.ToLower(runes[l]) != unicode.ToLower(runes[r]) {
			return false
		}
		l++
		r--
	}
	return true
}
