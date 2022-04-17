function toCamelCase($str){
  if(strpos($str, "-") !== false){
    $words = explode("-",$str);
  }else{
    $words = explode("_",$str);
  }
  
  for($i=1;$i<count($words); $i++){
    $words[$i] = ucfirst($words[$i]);
  }
  
  return join("", $words);
}