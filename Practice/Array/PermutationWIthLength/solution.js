arr = [1,2,3,4,5]
L=2

const convertArrayList = (result_arr, arr, n, arr_len, L) =>{
    for(let i=0; i< L;i++){
        result_arr.push(arr[n%arr_len]);
        n =Math.round(n/arr_len);
    }

    return result_arr

}

const arr_chopped = (result_arr) =>{
    new_result =[]
    var i, temp;
    for(i=0; i<result_arr.length; i+=L){
        temp = result_arr.slice(i, i+L);
        new_result.push.apply(new_result, [temp]);
    }

    return new_result;
}

const getAllPermutations = (arr, L) =>{
    result_arr = [];
    arr_len = arr.length;

    for(let i=0; i< Math.pow(arr_len, L); i++){
        convertArrayList(result_arr, arr, i, arr_len, L);
    }

    return arr_chopped(result_arr);
}

console.log(getAllPermutations(arr, L));