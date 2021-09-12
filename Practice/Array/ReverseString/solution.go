package main

import (
	"fmt"
)

func Reverse(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}

	return string(runes)
}

func main() {
	str1 := "Hello" // olleH
	str2 := "Test"  // tseT
	str3 := "Howdy" // ydwoH

	fmt.Println(Reverse(str1))
	fmt.Println(Reverse(str2))
	fmt.Println(Reverse(str3))
}
