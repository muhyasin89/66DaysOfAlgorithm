package main

import (
	"fmt"
	"math"
	"strconv"
	"strings"
)

func removeDuplicateValues(intSlice []int) []int {
	keys := make(map[int]bool)
	list := []int{}

	for _, i := range intSlice {
		if _, value := keys[i]; !value {
			keys[i] = true
			list = append(list, i)
		}
	}

	return list
}

// Find returns the smallest index i at which x == a[i],
// or len(a) if there is no such index.
func Find(a []string, x string) int {
	for i, n := range a {
		if x == n {
			return i
		}
	}

	return -1
}

func Constains(a []string, x string) bool {
	for _, n := range a {
		if x == n {
			return true
		}
	}

	return false
}

func removeValueinList(a []string, index int) []string {
	return append(a[:index], a[index+1:]...)
}

func containsValue(m map[int]string, v string) bool {
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

	fmt.Println("String: ", str1)
	fmt.Println("Integer : ", int1)

	// turn string into list
	chars := []rune(str1)
	strArray := []string{}
	for i := 0; i < len(chars); i++ {
		strArray = append(strArray, string(chars[i]))
	}

	fmt.Println(strArray)

	chars = []rune(int1)
	intArray := []string{}
	for i := 0; i < len(chars); i++ {
		intArray = append(intArray, string(chars[i]))
	}

	fmt.Println(intArray)

	// turn list int into list
	var listInt = []int{}

	for _, i := range intArray {
		j, err := strconv.Atoi(i)
		if err != nil {
			panic(err)
		}

		listInt = append(listInt, j)
	}

	fmt.Println(listInt)

	// remove duplicate
	listInt = removeDuplicateValues(listInt)

	fmt.Println(listInt)
	// turn list into string
	fmt.Println(strings.Join(strArray, ""))

	// check if 'space' inside list
	fmt.Println(Constains(strArray, " "))

	// check index space
	ind_space := Find(strArray, " ")
	fmt.Println(ind_space)

	// remove space in list
	strArray = removeValueinList(strArray, ind_space)
	fmt.Println(strArray)

	// swap list
	strArray[4], strArray[5] = strArray[5], strArray[4]
	fmt.Println(strArray)

	// make another list
	listInt1 := []int{5, 6, 7, 8, 9, 10}
	fmt.Println(listInt1)
	// merge 2 list with same type
	listInt = append(listInt, listInt1...)
	fmt.Println(listInt)

	// cut list into 2 left and right
	mid := int(math.Floor(float64(len(strArray) / 2)))

	left, right := []string{}, []string{}
	left, right = append(left, strArray[0:mid]...), append(right, strArray[mid:]...)

	fmt.Println(left, right)

	// make hash map
	// m := make(map[int]string)
	// m[1] = "first"
	// m[2] = "second"
	// m[3] = "third"

	m := map[int]string{1: "first", 2: "second", 3: "third"}

	fmt.Println("map:", m)

	// check if n in keys
	if _, ok := m[1]; ok {
		if ok {
			fmt.Println("Key Found")
		} else {
			fmt.Println("Key Not Found")
		}
	}

	fmt.Println(containsValue(m, "first"))

	//itterate hashmap
	for key, val := range m {
		fmt.Println("Key:", key, "=>", "Value:", val)
	}

}
