package main

import "fmt"

func ContainsValue(str string, dict_map map[string]string) bool {
	for _, val := range dict_map {
		if val == str {
			return true
		}
	}

	return false
}

func ContainsKey(str string, dict_map map[string]string) bool {
	if _, ok := dict_map[str]; ok {
		if ok {
			return true
		}
	}

	return false
}

func ValidBracket(str string, dict_map map[string]string) bool {
	list_bracket := []string{}
	chars := []rune(str)
	list_str := []string{}

	for i := 0; i < len(str); i++ {
		list_str = append(list_str, string(chars[i]))
	}

	for i, val := range list_str {
		if ContainsValue(val, dict_map) && i < 1 {
			return false
		} else if ContainsKey(val, dict_map) {
			list_bracket = append(list_bracket, val)
		} else if ContainsValue(val, dict_map) {
			if dict_map[list_bracket[len(list_bracket)-1]] != val {
				return false
			} else {
				list_bracket = list_bracket[:len(list_bracket)-1]
			}
		}
	}

	if len(list_bracket) > 0 {
		return false
	}

	return true
}

func main() {
	inp_str := "[]"                     // expected True
	inp_str1 := "{([{}()[]])}"          // expected True
	inp_str2 := "{(][)}"                // expected False
	inp_str3 := "]["                    // expected False
	inp_str4 := "{<[adadas]@1234>#$%^}" // expected True
	inp_str5 := "{{{{{"                 // expected  False

	dict_map := map[string]string{"{": "}", "[": "]", "<": ">", "(": ")"}

	fmt.Println(ValidBracket(inp_str, dict_map))
	fmt.Println(ValidBracket(inp_str1, dict_map))
	fmt.Println(ValidBracket(inp_str2, dict_map))
	fmt.Println(ValidBracket(inp_str3, dict_map))
	fmt.Println(ValidBracket(inp_str4, dict_map))
	fmt.Println(ValidBracket(inp_str5, dict_map))

}
