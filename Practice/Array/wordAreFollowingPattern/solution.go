package main

import (
	"fmt"
	"strings"
)

func ContainsKey(str1 string, hash_map map[string]string) bool {
	if _, ok := hash_map[str1]; ok {
		if ok {
			return true
		}
	}

	return false
}

func checkFollowingPattern(str1 string, string1 string) bool {
	list_string := strings.Split(string1, " ")
	chars := []rune(str1)
	hash_map := map[string]string{}

	if len(list_string) != len(chars) {
		return false
	}

	for i, val := range chars {
		temp := string(val)
		if ContainsKey(temp, hash_map) {
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

	fmt.Println(checkFollowingPattern(str1, string1))
	fmt.Println(checkFollowingPattern(str2, string2))

}
