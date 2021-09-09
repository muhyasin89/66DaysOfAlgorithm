// make string "Hello World" and string "11223344"
let str1 = "Hello World";
let int1 = "11223344";

console.log("Str:" +str1+ " Int:"+int1+"\n");

// turn string into list
let list_str1 = str1.split("");
let list_int1 = int1.split("");

console.log(list_str1);
console.log(list_int1);

// turn list string into list int
list_int1 = list_int1.map(Number);
console.log(list_int1);

// remove duplicate
list_int1 = [...new Set(list_int1)];
console.log(list_int1);

// turn list into string
console.log(list_str1.join(""));

// check index space
let ind_space = list_str1.indexOf(" ");
console.log(ind_space);

// remove space in list
list_str1.splice(ind_space, 1);
console.log(list_str1);

// swap list
[list_str1[4], list_str1[5]] = [list_str1[5], list_str1[4]]
console.log(list_str1);

// make another list
let list_int2 = [6,7,8,9,10];


// merge 2 list with same type
list_int1 = list_int1.concat(list_int2);
console.log(list_int1);

// check if 'k' inside list
console.log(list_int1.includes(9));

// cut list into 2 left and right
mid = list_str1.length/2
left = list_str1.splice(0, mid);
right =list_str1.splice(-mid);

console.log(left);
console.log(right);

// make hash map
let fistHashMap = new Map([
    [1, "first"],
    [2, "second"],
    [3, "third"]
])

// check if n in keys
console.log(fistHashMap.has(1));

// get second value
console.log(fistHashMap.get(1));

// check if n in values
console.log(Array.from(fistHashMap.values()).includes("second"));

for(let [key, value] of fistHashMap){
    console.log(key+" = "+value);
}
