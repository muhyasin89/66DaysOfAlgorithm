

inp_str = "[]"  // expected True
inp_str1 = "{([{}()[]])}"  // expected True
inp_str2 = "{(][)}"  // expected False
inp_str3 = "]["  // expected False
inp_str4 = "{<[adadas]@1234>#$%^}"  // expected True

dict_map = new Map([
    ["{", "}"],
    ["[", "]"],
    ["(", ")"],
    ["<", ">"]
]);  



const ValidBracket = (str, map) => {
    let list_str = str.split("");
    let list_bracket = [];

    if(list_bracket.length == 1){
        return false;
    }

    for(var i=0; i < list_str.length; i++){
        if(Array.from(map.values()).includes(list_str[i]) && i< 1){
            return false
        }else if(map.has(list_str[i])){
            list_bracket.push(list_str[i])
        }else if(Array.from(map.values()).includes(list_str[i])){
            if(map.get(list_bracket[list_bracket.length-1]) != list_str[i]){
                return false;
            }else{
                list_bracket.pop();
            }
        }
    }

    return true;
}

console.log(ValidBracket(inp_str, dict_map));
console.log(ValidBracket(inp_str1, dict_map));
console.log(ValidBracket(inp_str2, dict_map));
console.log(ValidBracket(inp_str3, dict_map));
console.log(ValidBracket(inp_str4, dict_map));