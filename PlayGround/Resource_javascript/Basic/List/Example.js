list_a = [2, 4, 3, 5, 1]

mid = Math.floor(list_a.length /2);
left = list_a.slice(0, mid);
right = list_a.slice(mid, list_a.length-1);

console.log(mid);
console.log(left, right);

[left[0], left[1]] = [left[1], left[0]];

console.log(left, right);

let fistHashMap = new Map([
    [1, "first"],
    [2, "second"],
    [3, "third"],
]);

console.log(fistHashMap);
console.log(fistHashMap.has(1));
console.log(fistHashMap.get(1));

// add in list

console.log(fistHashMap["1"] !== undefined)

console.log(!("1" in fistHashMap));

