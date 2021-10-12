// make string "Hello World" and string "1122334455"
let str1 = "Hello World";
let int1 = "1122334455";

console.log("String :"+str1 + " Integer:"+int1);

// turn string into list
let list_str = str1.split("");
let list_int = int1.split("");

console.log("String :"+list_str + " Integer:"+list_int);

// turn list string into list int
list_int = list_int.map(Number)
console.log(list_int);

// remove duplicate
list_int = [...new Set(list_int)]
console.log(list_int);

// turn list into string
console.log(list_str.join(""))

// check if 'space' inside list
console.log(list_str.includes(" "));

// check index space
let ind_space = list_str.indexOf(" ")
console.log(ind_space)

// remove space in list
list_str.splice(ind_space,1);
console.log(list_str);

// swap list
[list_str[4], list_str[5]] = [list_str[5], list_str[4]];
console.log(list_str);

// make another list
let list_int1 = [6,7,8,9,10]


// merge 2 list with same type
list_int = list_int.concat(list_int1);
console.log(list_int);


// cut list into 2 left and right
mid = list_str.length/2
left = list_str.splice(0, mid);
right = list_str.splice(-mid);
console.log(left);
console.log(right);

// make hash map
let hash_map = new Map([
    [1, "first"],
    [2, "second"],
    [3, "third"],
])

// check if n in keys
console.log(hash_map.has(1));

// get second value
console.log(hash_map.get(2));

// check if n in values
console.log(Array.from(hash_map.values()).includes("third"));

//itterate hashmap
for(let [key, val] of hash_map){
    console.log(key+ " = "+ val);
}
