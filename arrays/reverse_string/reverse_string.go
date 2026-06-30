package main

import "fmt"

func reverseString(s string) string {
	l := 0
	r := len(s) - 1
	for l < r {
		s = s[:l] + string(s[r]) + s[l+1:r] + string(s[l]) + s[r+1:]
		l++
		r--
	}
	return s
}

func main() {
	str := "Hello"
	fmt.Println(reverseString(str))
}
