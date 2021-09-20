<?php
$arr = array(1, 2, 3, 4, 5);
$size = count($arr);
$L = 2;


function combinationUtil($result, $arr, $data,  $start, $end, $index, $L)
{
    if ($index == $L) {
        for ($j = 0; $j < $L; $j++) {
            array_push($result, $data[$j]);
        }
    }

    for ($i = $start; $i <= $end && $end - $i + 1 >= $L - $index; $i++) {
        $data[$index] = $arr[$i];
        $result = combinationUtil($result, $arr, $data, $i + 1, $end, $index + 1, $L);
    }

    return $result;
}

function getCombinations($arr, $size, $L)
{
    $result = array();
    $data = array();
    $result = combinationUtil($result, $arr, $data, 0, $size - 1, 0, $L);
    return array_chunk($result, $L);
}

var_dump(getCombinations($arr, $size, $L));
