
function digital_root(n) {
    if(n < 10){
        return n;
    }else{
        const arrayOfDigits  = Array.from(String(n), Number);
        let result = 0;
        for(let item of arrayOfDigits){
            result += item;
        }

        return digital_root(result);
    }
}

