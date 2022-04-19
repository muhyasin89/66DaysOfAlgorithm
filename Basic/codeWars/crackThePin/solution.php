<?php
//Don't echo anything, will take to much time
function crack($hash){
    //G00D LUCK
    $length = 5;
  
    for($i=0; $i < 100000; $i++){
  
        $password = substr(str_repeat(0, $length).$i, - $length);
        if(md5($password)==$hash){
            return $password;
        }
    }
  }