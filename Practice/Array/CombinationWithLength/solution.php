<?php
$arr = array(1, 2, 3, 4, 5);
$L = 2;


function combinationUtils($arr, $data,  $start, $end, $index, $L)
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

function flattenArray($result_arr)
{
    $result = array();
    $it = new RecursiveIteratorIterator(new RecursiveArrayIterator($result_arr));
    foreach ($it as $v) {
        array_push($result, $v);
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
