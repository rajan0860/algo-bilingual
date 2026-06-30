package main

import "fmt"

func reverseString(s string) string {
	l, r := 0, len(s)-1
	bytes := []byte(s)
	for l < r {
		bytes[l], bytes[r] = bytes[r], bytes[l]
		l++
		r--
	}
	return string(bytes)
}

func main() {
	tests := []string{"Hello", "Hannah", "a", "", "ab"}
	for _, str := range tests {
		fmt.Printf("reverseString(%q) = %q\n", str, reverseString(str))
	}
}
