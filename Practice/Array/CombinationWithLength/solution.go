package main

import "fmt"

func chopped(temp_result []int, r int) [][]int {
	list_arr := [][]int{}

	for i := 0; i < len(temp_result); i += r {
		list_arr = append(list_arr, temp_result[i:i+r])
	}
	return list_arr
}

func combinatioUtils(arr []int, data []int, start int, end int, index int, r int) []int {
	temp_result := []int{}
	if index == r {
		for j := 0; j < r; j++ {
			temp_result = append(temp_result, data[j])
		}

		return temp_result
	}

	for i := start; i <= end && end-i+1 >= r-index; i++ {
		data[index] = arr[i]
		// fmt.Println(arr, data, i+1, end, index+1, r)
		temp_result = append(temp_result, combinatioUtils(arr, data, i+1, end, index+1, r)...)

	}

	return temp_result
}

func getCombinations(arr []int, start int, end int, index int, r int) [][]int {
	data := make([]int, 2)
	return chopped(combinatioUtils(arr, data, start, end, index, r), r)

}

func main() {
	arr := []int{1, 2, 3, 4, 5}
	r := 2
	n := len(arr)

	fmt.Println(getCombinations(arr, 0, n-1, 0, r))
}
