package main

import (
	"fmt"
	"math"
	"strconv"
	"strings"
)

func removeDuplicateValues(list_int []int) []int {
	keys := make(map[int]bool)
	list := []int{}

	for _, item := range list_int {
		if _, value := keys[item]; !value {
			keys[item] = true
			list = append(list, item)
		}
	}

	return list
}

func Contains(list_str []string, x string) bool {
	for _, n := range list_str {
		if x == n {
			return true
		}
	}
	return false
}

func Find(list_str []string, x string) int {
	for i, n := range list_str {
		if x == n {
			return i
		}
	}
	return -1
}

func removeValueinList(a []string, index int) []string {
	return append(a[:index], a[index+1:]...)
}

func ContainsKey(m map[int]string, key int) bool {
	if _, ok := m[key]; ok {
		if ok {
			return true
		}
	}

	return false
}

func ContainsValue(m map[int]string, v string) bool {
	for _, x := range m {
		if x == v {
			return true
		}
	}

	return false
}

func main() {

	// make string "Hello World" and string "11223344"
	str1 := "Hello World"
	int1 := "1122334455"

	fmt.Println("Str:", str1, "Int:", int1)
	// turn string into list

	chars := []rune(str1)
	list_str := []string{}

	for i := 0; i < len(chars); i++ {
		list_str = append(list_str, string(chars[i]))
	}

	fmt.Println(list_str)

	// turn list int into list
	chars = []rune(int1)
	arr_int := []string{}

	for i := 0; i < len(chars); i++ {
		arr_int = append(arr_int, string(chars[i]))
	}
	fmt.Println(arr_int)

	// turn list  string into int
	list_int := []int{}

	for _, item := range arr_int {
		j, err := strconv.Atoi(item)
		if err != nil {
			panic(err)
		}

		list_int = append(list_int, j)
	}
	// remove duplicate
	list_int = removeDuplicateValues(list_int)
	fmt.Println(list_int)

	// make another list
	list_int1 := []int{6, 7, 8, 9, 10}

	// merge 2 list with same type
	list_int = append(list_int, list_int1...)

	fmt.Println(list_int)

	//print list into string
	fmt.Println(strings.Join(list_str, ""))

	// check if 'space' inside list
	fmt.Println(Contains(list_str, " "))

	// check index space
	ind_space := Find(list_str, " ")
	fmt.Println(ind_space)

	// remove space in list
	list_str = removeValueinList(list_str, ind_space)
	fmt.Println(list_str)

	// swap list
	list_str[4], list_str[5] = list_str[5], list_str[4]
	fmt.Println(list_str)

	// cut list into 2 left and right
	mid := int(math.Floor(float64(len(list_str) / 2)))

	left, right := []string{}, []string{}

	left, right = append(left, list_str[0:mid]...), append(right, list_str[mid:]...)
	fmt.Println(left, right)

	// make hash map
	m := map[int]string{1: "first", 2: "second", 3: "third"}
	fmt.Println("Map:", m)

	// check if n in keys
	fmt.Println(ContainsKey(m, 1))

	//print hash[index]
	fmt.Println(m[1])
	// check if n in values
	fmt.Println(ContainsValue(m, "first"))

	// itterate

	for key, val := range m {
		fmt.Println("Key:", key, "value:", val)
	}
}
