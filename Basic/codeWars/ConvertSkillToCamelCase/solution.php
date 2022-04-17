function toCamelCase($str){
    $str = str_replace("_", "-", $str);
    $words = explode("-",$str);
    
  for($i=1;$i<count($words); $i++){
    $words[$i] = ucfirst($words[$i]);
  }
  
  return join("", $words);
}