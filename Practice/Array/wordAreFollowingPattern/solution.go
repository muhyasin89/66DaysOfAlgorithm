package main

import (
	"fmt"
	"strings"
)

func ContainsKey(m map[string]string, s string) bool {
	if _, ok := m[s]; ok {
		if ok {
			return true
		}
	}

	return false
}

func checkPattern(s string, str string) bool {
	m := map[string]string{}
	list_str := strings.Split(str, " ")
	a := []rune(s)
	if len(list_str) != len(a) {
		return false
	}

	for i, val := range a {
		c := string(val)
		if ContainsKey(m, c) {
			if m[c] != list_str[i] {
				return false
			}
		} else {
			m[c] = list_str[i]
		}
	}
	return true
}

func main() {
	str1 := "abba"
	string1 := "dog cat cat dog"
	// result True

	str2 := "abba"
	string2 := "dog cat cat fish"
	// return False

	fmt.Println(checkPattern(str1, string1))
	fmt.Println(checkPattern(str2, string2))

}
