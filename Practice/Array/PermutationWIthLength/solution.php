<?php
$arr = array(1, 2, 3, 4, 5);
$L = 2;


function convertArrayList($arr, $n, $arr_len, $L)
{
    $result = array();
    for ($i = 0; $i < $L; $i++) {
        array_push($result, $arr[$n % $arr_len]);
        $n = round($n / $arr_len);
    }

    return $result;
}


function getAllPermutations($arr, $L)
{
    $result_arr = array();
    $arr_len = count($arr);
    for ($i = 0; $i < (int)pow($arr_len, $L); $i++) {
        array_push($result_arr, convertArrayList($arr, $i, $arr_len, $L));
    }

    return $result_arr;
}

var_dump(getAllPermutations($arr, $L));
