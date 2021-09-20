arr = [1, 2, 3, 4, 5 ];
L=2;
n = arr.length

const combinationUtil = (result,arr, data, start, end, index, L) =>{
    if(index == L){
        for(let j=0;j< L; j++){
            result.push(data[j]);
        }
    }

    for (let i = start; i <= end && end - i + 1 >= L - index; i++) {
        data[index] = arr[i];
        result = combinationUtil(result, arr, data, i + 1, end, index + 1, L);
        
    }
    return result;
}

const chopped = (arr, L) =>{
    new_result=[]
    let i,j, temporary;
    for (i = 0,j = result.length; i < j; i += L) {
        temporary = result.slice(i, i + L);
        // do whatever
        new_result.push.apply(new_result, [temporary])
    }
    
    return new_result;
}

const getCombination = (arr, n, L) =>{
    result = []
    data = []
    
    result = combinationUtil(result, arr, data, 0, n - 1, 0, L);

   return chopped(result, L);
}

console.log(getCombination(arr, n, L));