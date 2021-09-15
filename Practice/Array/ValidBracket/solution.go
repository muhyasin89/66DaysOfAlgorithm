package main

import "fmt"

func containsKeys(m map[string]string, s string) bool {
	if _, ok := m[s]; ok {
		if ok {
			return true
		}
	}
	return false
}

func containsValue(m map[string]string, s string) bool {
	for _, val := range m {
		if val == s {
			return true
		}
	}
	return false
}

func ValidBracket(str string, m map[string]string) bool {
	list_bracket := []string{}
	chars := []rune(str)
	list_str := []string{}

	for i := 0; i < len(str); i++ {
		list_str = append(list_str, string(chars[i]))
	}

	for i, val := range list_str {
		if containsKeys(m, val) {
			list_bracket = append(list_bracket, val)
		} else if containsValue(m, val) && i < 1 {
			return false
		} else if containsValue(m, val) {
			if m[list_bracket[len(list_bracket)-1]] != val {
				// fmt.Println(m[list_bracket[len(list_bracket)-1]], val)
				return false
			} else {
				list_bracket = list_bracket[:len(list_bracket)-1]

			}
		} else {

		}
	}

	return true
}

func main() {
	inp_str := "[]"                     // expected True
	inp_str1 := "{([{}()[]])}"          // expected True
	inp_str2 := "{(][)}"                // expected False
	inp_str3 := "]["                    // expected False
	inp_str4 := "{<[adadas]@1234>#$%^}" // expected True

	m := map[string]string{"{": "}", "[": "]", "(": ")", "<": ">"}

	fmt.Println(ValidBracket(inp_str, m))
	fmt.Println(ValidBracket(inp_str1, m))
	fmt.Println(ValidBracket(inp_str2, m))
	fmt.Println(ValidBracket(inp_str3, m))
	fmt.Println(ValidBracket(inp_str4, m))
}
