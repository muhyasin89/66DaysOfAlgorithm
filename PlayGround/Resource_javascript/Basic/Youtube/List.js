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
