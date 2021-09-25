package main

import (
	"fmt"
	"math"
)

func convertArrayList(arr []int, n int, arr_len int, L int) []int {
	result := []int{}
	for i := 0; i < L; i++ {
		result = append(result, arr[n%arr_len])
		n /= arr_len
	}

	return result
}

func getAllPermutations(result_arr [][]int, arr []int, L int) [][]int {
	arr_len := len(arr)
	for i := 0; i < int(math.Pow(float64(arr_len), float64(L))); i++ {
		result_arr = append(result_arr, convertArrayList(arr, i, arr_len, L))
	}
	return result_arr
}

func main() {
	arr := []int{1, 2, 3, 4, 5}
	L := 2

	result_arr := [][]int{}
	result_arr = getAllPermutations(result_arr, arr, L)

	fmt.Println(result_arr)
}
