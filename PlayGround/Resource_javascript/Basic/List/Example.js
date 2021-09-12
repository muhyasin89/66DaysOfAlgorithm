// make string "Hello World" and string "11223344"
let str1 = "Hello World";
let int1 = "1122334455";


console.log(str1);
console.log(int1);

// turn string into list
let list_str1 = str1.split("");
let list_int1 = int1.split("");

console.log(list_str1);
console.log(list_int1);

// turn list string into list int
list_int1 = list_int1.map(Number);
console.log(list_int1);

// remove duplicate
list_int1 = [...new Set(list_int1)]
console.log(list_int1);

// turn list into string
console.log(list_str1.join(""));

// check index space
ind_space = list_str1.indexOf(" ")
console.log(ind_space);

// remove space in list
list_str1.splice(ind_space, 1);
console.log(list_str1);

// swap list
[list_str1[4], list_str1[5]] = [list_str1[5], list_str1[4]]
console.log(list_str1);

// make another list
let list_int2 = [5,6,7,8,9,10]

// merge 2 list with same type
list_int1 = list_int1.concat(list_int2);
console.log(list_int1);

// check if 'k' inside list
console.log(list_int1.includes(10));

// cut list into 2 left and right
let mid = Math.floor(list_str1.length/2);
let left = list_str1.splice(0, mid);
let right = list_str1.splice(-mid);

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
console.log(fistHashMap.get(2));

// check if n in values
console.log(Array.from(fistHashMap.values()).includes("second"));

for(let [key, value] of fistHashMap){
    console.log(key + " = " + value);
}

console.log("=============================");
console.log(fistHashMap["1"] !== undefined)

console.log(!("1" in fistHashMap));
console.log("=============================");



let first_string = "Hello World"
let first_int = 11223344

let list_str = first_string.split("");
// Array.from(first_int);
// Object.assign([], first_int);

let list_int = Array.from(first_int.toString());

const toNum =  (list_int) = list_int.map((i) => Number(i));

const set1 = new Set(list_int);

// let arraySet = Array.from(set1);
let arraySet = [...set1];

list_a = [2, 4, 3, 5, 1]


console.log(list_str);
list_str.splice(5, 1);
console.log(list_str);

console.log(list_int);
// console.log(toNum(list_int));

console.log(set1);

console.log(arraySet)

mid = Math.floor(arraySet.length/2);

left = arraySet.slice(0, mid);
right = arraySet.slice(mid, arraySet.length);

console.log(left);
console.log(right);


[left[0], left[1]] = [left[1], left[0]];

console.log(left);

const map1 = new Map();

map1.set('a', 1);
map1.set('b', 2);
map1.set('c', 3);

console.log(map1.get('a'));

console.log(map1.has('b'));


const findInMap = (map1, val) => {
    for(let [k, v] of map1){
        if (v == val){
            return true
        }
    }
    return false;
}
console.log(findInMap(map1, 4));

const itterateHashMap = (map1) =>{
    for(const [key, value] of map1.entries()){
        console.log(key +" =" + value);
    }
}

itterateHashMap(map1)
const object = {'a': 1, 'b': 2, 'c' : 3};
for (const [key, value] of Object.entries(object)) {
  console.log(key, value);
}
