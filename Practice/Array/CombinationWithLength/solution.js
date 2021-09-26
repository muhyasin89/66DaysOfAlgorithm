arr = [1, 2, 3, 4, 5]
L = 2

const arrChopped =(arr, L) =>{
    result = []
    let temp;
    for(let i=0; i< arr.length; i++){
        temp = arr.slice(i, i+L);
        result.push.apply(result, [temp])
    }

    return result
}

const combinationUtils = (result, arr, data, start, end, index, L) =>{
    result =[]
    if(index == L){
        for(let i=0;i< L; i++){
            result.push(data[i]);
        }

        return result;
    }

    for (let j = start; (j <= end) && (end - j + 1 >= L - index); j++) {
        data[index] = arr[j];
        result.push(...combinationUtils(result, arr, data, j + 1, end, index + 1, L));
        
    }
    return result;

}

const getAllCombinations =(arr, L) =>{
    
    result_arr = []
    arr_len = arr.length
    data = []

    result_arr = combinationUtils(result_arr, arr, data, 0, arr_len-1, 0, L);

    return arrChopped(result_arr,L)
    
}

console.log(getAllCombinations(arr, L));