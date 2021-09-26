package main

import (
	"fmt"
	"strings"
)

func containsKey(hash_map map[string]string, str1 string) bool {
	if _, ok := hash_map[str1]; ok {
		if ok {
			return true
		}
	}
	return false
}

func areFollowingPattern(str1 string, string1 string) bool {
	hash_map := map[string]string{}
	list_string := strings.Split(string1, " ")
	runeAsStr := []rune(str1)

	if len(list_string) != len(runeAsStr) {
		return false
	}

	for i, val := range runeAsStr {
		temp := string(val)
		if containsKey(hash_map, temp) {
			if hash_map[temp] != list_string[i] {
				return false
			}
		} else {
			hash_map[temp] = list_string[i]
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

	fmt.Println(areFollowingPattern(str1, string1))
	fmt.Println(areFollowingPattern(str2, string2))

}
