package main

import "fmt"

func arrChopped(arr []int, L int) [][]int {
	new_result := [][]int{}

	for i := 0; i < len(arr); i += L {
		new_result = append(new_result, arr[i:i+L])
	}
	return new_result
}

func combinationUtils(arr []int, data []int, start int, end int, index int, L int) []int {
	result := []int{}

	if index == L {
		for i := 0; i < L; i++ {
			result = append(result, data[i])
		}

		return result
	}

	for j := start; (j <= end) && (end-j+1 >= L-index); j++ {
		data[index] = arr[j]
		result = append(result, combinationUtils(arr, data, j+1, end, index+1, L)...)
	}

	return result
}

func getAllCombinations(arr []int, L int) [][]int {
	data := make([]int, 2)
	arr_len := len(arr)

	return arrChopped(combinationUtils(arr, data, 0, arr_len-1, 0, L), L)
}

func main() {
	arr := []int{1, 2, 3, 4, 5}
	L := 2
	result_arr := [][]int{}

	result_arr = getAllCombinations(arr, L)

	fmt.Println(result_arr)
}
