package main

import "fmt"

func checkKeys(ind int, hash_map map[int]int) bool {
	if _, key := hash_map[ind]; key {
		if key {
			return true
		}
	}
	return false
}

func SumList(hash_map map[int]int, arr []int) map[int]int {
	for _, s := range arr {
		if checkKeys(s, hash_map) {
			hash_map[s] += 1
		} else {
			hash_map[s] = 1
		}
	}
	return hash_map
}

func printHashMap(hash_map map[int]int) {
	for key, val := range hash_map {
		fmt.Println("number ", key, "=", val, " times")
	}

}

func main() {
	arr := []int{1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5}
	hash_map := map[int]int{}

	// number 1 = 3 times

	hash_map = SumList(hash_map, arr)
	printHashMap(hash_map)

}
