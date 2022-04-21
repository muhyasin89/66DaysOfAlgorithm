def row_sum_odd_numbers(n):
    #your code here
    firstNumber = n*n -(n-1)
    currentNumber = firstNumber
    result = currentNumber
    
    for i in range(1, n):
        result= result + (currentNumber +2)
        
    return result