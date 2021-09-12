let arr = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5]
let hash_map = new Map([]);

const SumList = (arr, hash_map) =>{
    arr.forEach(item => {
        if(hash_map.has(item)){
            hash_map.set(item, hash_map.get(item)+1)
        }else{
            hash_map.set(item,1);
        }
        
    });

    return hash_map;
}

const printHashMap = (hash_map) =>{
    for(let [key,val] of hash_map){
        console.log("number "+ key +" = "+ val +" times");
    }
    
}

hash_map = SumList(arr, hash_map);

printHashMap(hash_map)