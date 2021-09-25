arr = [1,2,3,4,5]
L=2


const convertArrayList = (result_arr, n, arr, arr_len, L) => {
    for(let i=0; i< L;i++){
        result_arr.push(arr[n % arr_len])
        n = Math.round(n/arr_len)
    }

    return result_arr
}

const arr_chopped = (result_arr, L) =>{
    new_result = []
    var i, j, temp;
    for(i=0, j=result_arr.length; i<j; i+=L){
        temp = result_arr.slice(i, i+L);
        new_result.push.apply(new_result, [temp])
    }

    return new_result;
}

const getAllPermutations = (arr, L) =>{
    result_arr = [];
    arr_len = arr.length;arr_len

    for(let i=0; i<Math.pow(arr_len, L); i++){
        convertArrayList(result_arr, i, arr, arr_len, L);
    }

    return arr_chopped(result_arr, L);
}

console.log(getAllPermutations(arr, L));