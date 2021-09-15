package main

import (
	"fmt"
	"math"
)

func convertToLenTHBase(n int, arr []int, len int, r int) []int {
	result := []int{}

	for i := 0; i < r; i++ {
		result = append(result, arr[n%len])
		n /= len
	}

	return result
}

func getAllPermutations(result [][]int, arr []int, arr_len int, r int) [][]int {
	for i := 0; i < int(math.Pow(float64(arr_len), float64(r))); i++ {
		result = append(result, convertToLenTHBase(i, arr, arr_len, r))
	}

	return result
}

func main() {
	arr := []int{1, 2, 3, 4, 5}
	arr_len := len(arr)
	r := 2
	result := [][]int{}

	result = getAllPermutations(result, arr, arr_len, r)

	fmt.Println(result)
}
