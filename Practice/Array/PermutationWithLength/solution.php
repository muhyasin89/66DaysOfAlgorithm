<?php
$arr = array(1, 2, 3, 4, 5);
$size = count($arr);
$L = 2;


function convertToLenTHBase($n, $arr, $size, $L)
{
    $a = array();
    for ($i = 0; $i < $L; $i++) {
        // Print the ith element
        // of sequence
        array_push($a, $arr[$n % $size]);

        $n = round($n / $size);
    }


    return $a;
}

function getAllPermutations($arr, $size, $L)
{
    $result = array();
    for ($i = 0; $i < (int)pow($size, $L); $i++) {

        array_push($result, convertToLenTHBase($i, $arr, $size, $L));
    }

    return $result;
}

var_dump(getAllPermutations($arr, $size, $L));
