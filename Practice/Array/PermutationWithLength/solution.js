arr = [ 1, 2, 3, 4, 5]
size = arr.length
L=2


const convertToLenTHBase = (result,n, arr, size, L) =>{
    for(let i=0; i< L;i++){
        result.push(arr[n % size]);
        n = Math.round(n/size);
    }

    return result
}

const chopped = (result, L) => {

    new_result = []
    var i,j, temporary;
    for (i = 0,j = result.length; i < j; i += L) {
        temporary = result.slice(i, i + L);
        // do whatever
        new_result.push.apply(new_result, [temporary])
    }

    return new_result

}

const getAllPermutations = (arr, size, L) =>{
    result = []
    
    for(let i=0; i< Math.pow(size, L); i++){
        convertToLenTHBase(result,i, arr, size, L)
    }

    return chopped(result, L);
    
}

console.log(getAllPermutations(arr, size, L));