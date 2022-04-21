function rowSumOddNumbers($n) {
  // your code here
  $firstNumber = $n*$n -($n-1);
  $result = $firstNumber;
  $currentValue = $firstNumber;
  
  for($i=1; $i < $n; ++$i){
    $currentValue = $firstNumber + 2;
    $result = $result+$currentValue;
  }
  
  return $result;
  
}