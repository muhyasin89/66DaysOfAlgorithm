arr = [ 1, 2, 3, 4, 5]
size = arr.length
L=2


const convertToLenTHBase = (n, arr, size, L) =>{
    a = []
    for(let i=0; i< L;i++){
        result.push(arr[n % size]);
        n = Math.round(n/size);
    }

    if(a.length > 0){
        return a;
    } else{
        return null;
    }
}

const getAllPermutations = (arr, size, L) =>{
    result = []
    temp = []
    for(let i=0; i< Math.pow(size, L); i++){
        a = convertToLenTHBase(i, arr, size, L)
        if(a){
            temp.push(a)
        }
        // console.log(convertToLenTHBase(i, arr, size, L));
    }

    return result
}

console.log(getAllPermutations(arr, size, L));