package main

import (
	"fmt"
)

func checkKeys(ind int, hash_map map[int]int) bool {
	if _, ok := hash_map[ind]; ok {
		if ok {
			return true
		} else {
			return false
		}
	}

	return false
}

func sumList(arr []int, hash_map map[int]int) map[int]int {
	for _, s := range arr {
		if checkKeys(s, hash_map) {
			hash_map[s] += 1
		} else {
			hash_map[s] = 1
		}
	}

	return hash_map
}

func main() {
	arr := []int{1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5}
	hash_map := map[int]int{}

	hash_map = sumList(arr, hash_map)
	for key, val := range hash_map {
		fmt.Println("number:", key, "=", val, " times")
	}

}
