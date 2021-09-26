<?php
$arr = array(1, 2, 3, 4, 5);
$L = 2;

function flattenArray($return_arr)
{

    $result = array();
    $all = new RecursiveIteratorIterator(new RecursiveArrayIterator($return_arr));
    foreach ($all as $item) {
        array_push($result, $item);
    }

    return $result;
}

function combinationUtils($arr, $data, $start, $end, $index, $L)
{
    $result = array();
    if ($index == $L) {
        for ($i = 0; $i < $L; $i++) {
            array_push($result, $data[$i]);
        }
        return $result;
    }

    for ($j = $start; ($j <= $end) && ($end - $j + 1 >= $L - $index); $j++) {
        $data[$index] = $arr[$j];
        array_push($result, combinationUtils($arr, $data, $j + 1, $end, $index + 1, $L));
    }

    return $result;
}


function getAllCombinations($arr, $L)
{
    $result_arr = array();
    $data = array();
    $arr_len = count($arr);
    $result_arr = combinationUtils($arr, $data, 0, $arr_len - 1, 0, $L);
    return array_chunk(flattenArray($result_arr), $L);
}


var_dump(getAllCombinations($arr, $L));
