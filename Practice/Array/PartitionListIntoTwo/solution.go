package main

import (
	"fmt"
)

func chopped(arr []int, L int) [][]int {
	list_arr := [][]int{}
	arr_len := len(arr)
	for i := 0; i < arr_len; i += L {
		list_arr = append(list_arr, arr[i:i+L])
	}

	return list_arr
}

func main() {
	arr := []int{1, 2, 1, 3, 1, 4, 1, 5, 2, 3, 2, 4, 2, 5, 3, 4, 3, 5, 4, 5}
	l := 2
	fmt.Println(chopped(arr, l))
}
