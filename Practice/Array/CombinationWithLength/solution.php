<?php
$arr = array(1, 2, 3, 4, 5);
$L = 2;


function combinationUtils($result, $arr, $data,  $start, $end, $index, $L)
{
    if ($index == $L) {
        for ($i = 0; $i < $L; $i++) {
            array_push($result, $data[$i]);
        }
    }

    for ($j = $start; ($j <= $end) && ($end - $j + 1 >= $L - $index); $j++) {
        $data[$index] = $arr[$j];
        $result = combinationUtils($result, $arr, $data, $j + 1, $end, $index + 1, $L);
    }

    return $result;
}

function getAllCombinations($arr, $L)
{
    $result_arr = array();
    $data = array();
    $arr_len = count($arr);
    $result_arr = combinationUtils($result_arr, $arr, $data, 0, $arr_len - 1, 0, $L);
    return array_chunk($result_arr, $L);
}


var_dump(getAllCombinations($arr, $L));
